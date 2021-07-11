from django.db import models

# Create your models here.

class Htmldata(models.Model):
    code_id = models.AutoField(primary_key=True)
    title = models.TextField(max_length=70)
    image = models.ImageField(upload_to="media/images", default="")
    html_code = models.TextField(max_length=999999999, default="")
    css_code = models.TextField(max_length=999999999, default="")
    js_code = models.TextField(max_length=999999999, default="")

    def __str__(self):
        return self.title

class Pythondata(models.Model):
    code_id = models.AutoField(primary_key=True)
    title = models.TextField(max_length=70)
    subtitle = models.TextField(max_length=150)
    desc = models.TextField(max_length=99999)
    image = models.ImageField(upload_to="media/images", default="")
    code = models.TextField(max_length=999999999, default="")

    def __str__(self):
        return self.title

class Pygamedata(models.Model):
    code_id = models.AutoField(primary_key=True)
    title = models.TextField(max_length=70)
    subtitle = models.TextField(max_length=150)
    desc = models.TextField(max_length=99999)
    image = models.ImageField(upload_to="media/images", default="")
    code = models.TextField(max_length=999999999, default="")

    def __str__(self):
        return self.title
