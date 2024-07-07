from django.db import models
from django.utils.text import slugify

class blog(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to="blogs")
    description = models.TextField()
    is_active= models.BooleanField(default=False)
    is_home = models.BooleanField(default=False)
    slug = models.SlugField(null=True,blank=True, unique=True, db_index=True,editable=False,)
    def __str__(self):
        return f"{self.title}"    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args,**kwargs)






class category(models.Model):
    name = models.CharField(max_length=1000)
    slug = models.SlugField(null=True,blank=True,unique=True, db_index=True,editable=False,)
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args,**kwargs)

    def __str__(self):
        return self.name
