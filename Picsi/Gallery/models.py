from django.db import models
from PIL import Image as PilImage, ImageOps
from django.core.files import File
from io import BytesIO
from django.contrib.auth.models import User
import os

IMAGE_SIZES = [
    ("pic-long", "LONG"),
    ("pic-wide", "WIDE")
]

class Pic(models.Model):
    title                = models.CharField(max_length=100, blank=True)
    image                = models.ImageField(upload_to="pics/", null=False)
    very_low_res_image   = models.ImageField(upload_to="pics/very_low_res/", null=True, blank=True)
    low_res_image        = models.ImageField(upload_to="pics/low_res/", null=True, blank=True)
    mid_res_image        = models.ImageField(upload_to="pics/mid_res/", null=True, blank=True)
    size                 = models.CharField(max_length=20, choices=IMAGE_SIZES, editable=False)
    author               = models.ForeignKey(User, on_delete=models.CASCADE, related_name="pics")

    def save(self, *args, **kwargs):
        # Open original and apply EXIF orientation
        img = PilImage.open(self.image)
        img = ImageOps.exif_transpose(img)

        # 1) determine portrait vs landscape
        if img.width == 0 or img.height == 0:
            raise ValueError("Image dimensions are invalid.")
        self.size = "pic-long" if (img.height / img.width) >= 1 else "pic-wide"

        # 2) ensure we have a PK so upload paths work
        if not self.pk:
            super().save(*args, **kwargs)

        # 3) for each “res” slot, skip if already set, else re-save original pixels with different compression
        compressions = [
            ("very_low_res_image", 10),  # very heavy compression
            ("low_res_image",      20),  # heavy compression
            ("mid_res_image",      40),  # medium compression
        ]

        for field_name, quality in compressions:
            if not getattr(self, field_name):
                img_io = BytesIO()

                # Preserve mode and format, just compress
                if img.format == "PNG":
                    # PNG: keep transparency & original dimensions
                    img.save(img_io, format="PNG", optimize=True)
                else:
                    # JPEG or others: convert to RGB & save with quality
                    rgb = img.convert("RGB")
                    rgb.save(img_io, format="JPEG", quality=quality, optimize=True)

                # Rewind buffer
                img_io.seek(0)

                filename = f"{field_name}_{os.path.basename(self.image.name)}"
                getattr(self, field_name).save(filename, File(img_io), save=False)

        # 4) final save (update new fields)
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        # Remove associated image files
        for field in ['image', 'very_low_res_image', 'low_res_image', 'mid_res_image']:
            file_field = getattr(self, field)
            if file_field and os.path.isfile(file_field.path):
                os.remove(file_field.path)

        # Call the parent class's delete method to remove the database record
        super().delete(*args, **kwargs)