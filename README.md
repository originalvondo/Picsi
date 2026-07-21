# Picsi

A Pinterest-style image sharing website built for users to upload, discover, and download images.

## Features

- **User Authentication**: Secure login and logout functionality
- **Image Upload**: Upload your image
- **Image Download**: Download images shared by other users

## Getting Started

### Prerequisites
- You need to have **Python** installed

### Installation

1. Clone the repository
```bash
git clone https://github.com/originalvondo/Picsi.git
cd Picsi
```
2. Create a virtual environment
```bash
python -m venv .venv
.venv\Scripts\activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Run the application
```bash
cd Picsi
python manage.py runserver
```

## Usage

1. **Sign Up / Login**: Create an account or log in with your credentials
2. **Upload Images**: Click the upload button and select images to share
3. **Download & Delete Images**: If an image is uploaded by you, there'll be a cross button on the top right of the image, click it to delete the image. And hover on an image and click **download** to download the image. 

## License

See [LICENSE](./LICENSE) for more info. 