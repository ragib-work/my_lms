from email.policy import default

import cloudinary
from decouple import config



CLOUDINARY_CLOUD_NAME = config("CLOUDINARY_CLOUD_NAME",default="")
CLOUDINARY_PUBLIC_API_KEY = config("CLOUDINARY_PUBLIC_API_KEY", default="965791395726544")
CLOUDINARY_API_SECRET_KEY = config("CLOUDINARY_API_SECRET_KEY")


def cloudinary_init():
    cloudinary.config(
        cloud_name = CLOUDINARY_CLOUD_NAME,
        api_key = CLOUDINARY_PUBLIC_API_KEY,
        api_secret = CLOUDINARY_API_SECRET_KEY, # Click 'View API Keys' above to copy your API secret
        secure=True
    )