from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField()
    technology = models.CharField(max_length=256)
    image = models.FileField(upload_to='project_images/', blank=True)
    githublink = models.CharField(max_length=256, null=True, blank=True)
    replitlink = models.CharField(max_length=256, null=True, blank=True)
    anotherlink = models.CharField(max_length=256, null=True, blank=True)

    def __str__(self):
        return(self.title)