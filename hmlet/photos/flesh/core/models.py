from io import BytesIO

from PIL import Image
from django.contrib.auth.models import User
from django.db import models
from django.db.models import ImageField
from photos import settings


class Photo(models.Model):
    name = models.CharField(max_length=32, unique=True)
    draft = models.BooleanField(default=False)
    caption = models.CharField(max_length=32)
    image = ImageField(upload_to='.', max_length=10e6)  # Will be saved to s3 (minio) storage
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    publish_date = models.DateTimeField()
    thumbnail = ImageField(max_length=10e6)

    def save(self, *args, **kwargs):
        # TODO: optimise this
        image = Image.open(self.image)

        image_io = BytesIO()
        resized = image.resize(settings.IMAGE_SERVE_SIZE, Image.ANTIALIAS)
        resized.save(image_io, format=image.format, quality=100)
        self.thumbnail.save(f"{settings.MEDIA_ROOT}/thumb_{self.image.name}", image_io, save=False)

        super().save()
