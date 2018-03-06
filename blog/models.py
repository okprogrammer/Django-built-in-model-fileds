from django.db import models
from django.utils import timezone
from django.utils.text import slugify
# Create your models here.
from .validators import validate_justin



PUBLISH_CHOICES = {
    ('draft','Draft'),
    ('publish','Publish'),
    ('private','Private'),
}
class PostModel(models.Model):
    id = models.BigAutoField(primary_key=True)
    active = models.BooleanField(default=True)
    title = models.CharField(max_length=240,verbose_name='Post Title',unique=True)
    slug = models.SlugField(null=True,blank=True)
    content = models.TextField(null=True, blank=True)
    publish = models.CharField(max_length=120,choices=PUBLISH_CHOICES,default='draft')
    view_count = models.IntegerField(default=0)
    publish_date = models.DateField(auto_now=False,auto_now_add=False,default=timezone.now)
    author_email = models.EmailField(max_length=240,validators=[validate_justin],blank=True,null=True)

    def save(self,*args,**kwargs):
        if not self.slug and self.title:
            self.slug and self.title
        super(PostModel, self).save(*args,**kwargs)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return self.title