from django.db import models
from PIL import Image as PilImage
from django.core.files import File
from io import BytesIO

IMAGE_SIZES = [
    ("pic-long", "LONG"),
    ("pic-wide", "WIDE")
]

# Create your models here.
class Pic(models.Model):
    title = models.CharField(max_length=100, blank=True)
    image = models.ImageField(upload_to="pics/", null=False)
    size = models.CharField(max_length=20, choices=IMAGE_SIZES)

    def save(self, *args, **kwargs):
        img = PilImage.open(self.image)

        if (img.height / img.width) >= 1:
            self.size = "pic-long"
        else:
            self.size = "pic-wide"

        img_io = BytesIO()
        img.save(img_io, format='JPEG') 
        img_file = File(img_io, name=self.image.name)
        self.image = img_file

        super().save(*args, **kwargs)