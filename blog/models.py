from django.db import models
from django.utils import timezone
# Create your models here.

PUBLISH_CHOICES = {
    ('draft','Draft'),
    ('publish','Publish'),
    ('private','Private'),
}
class PostModel(models.Model):
    id = models.BigAutoField(primary_key=True)
    active = models.BooleanField(default=True)
    title = models.CharField(max_length=240,verbose_name='Post Title',unique=True)
    content = models.TextField(null=True, blank=True)
    publish = models.CharField(max_length=120,choices=PUBLISH_CHOICES,default='draft')
    view_count = models.IntegerField(default=0)
    publish_date = models.DateField(auto_now=False,auto_now_add=False,default=timezone.now)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return self.title