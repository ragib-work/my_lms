from django.db import models
import my_helpers
from cloudinary.models import CloudinaryField
my_helpers.cloudinary_init()

class AccessRequired(models.TextChoices):
    ANYONE = "any", "Anyone"
    EMAIL_REQUIRED = "email","Email required"
    PURCHASE_REQUIRED = "purchase_required", "Purchase required"
    USER_REQUIRED = "user_required", "User required"
class PublishStatus(models.TextChoices):
    PUBLISHED = "pub", "Published"
    COMING_SOON = "soon", "Coming Soon"
    DRAFT = "draft", "Draft"

def handle_upload(instance, filename):
    return f"{filename}"

class Course(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)
    # image = models.ImageField(upload_to=handle_upload, blank=True, null=True)
    image = CloudinaryField("image", null=True)
    access = models.CharField(
        max_length=20,
        choices = AccessRequired.choices,
        default = AccessRequired.EMAIL_REQUIRED
    )
    status = models.CharField(
        max_length=10,
        choices=PublishStatus.choices,
        default=PublishStatus.DRAFT
    )

    @property
    def image_admin_url(self):
        if not self.image:
            return ""
        image_options = {
            "width":500
        }
        url = self.image.build_url(**image_options)
        return url

    def get_image_thumbnail(self, as_html=False, width=500):
        if not self.image:
            return ""
        image_options = {
            "width":width
        }
        if as_html:
            # CloudinaryImage(str(self.image)).image(**image_options)
            return self.image.image(**image_options)
        # CloudinaryImage(str(self.image)).build_url(**image_options)
        url = self.image.build_url(**image_options)
        return url