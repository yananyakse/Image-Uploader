from django.db import models

# Create your models here.
class Upload(models.Model):
      user = models.CharField(max_length=100)
      image = models.ImageField(upload_to='profiles')
      caption = models.TextField(max_length=300)

      def __str__(self):
        return self.user