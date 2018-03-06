from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.db.models.signals import pre_save,post_save


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
    title = models.CharField(
        max_length=240,
        verbose_name='Post Title',
        unique=True,
        error_messages={"unique":"This title is not unique,please try again?",
        "blank":"This field is required!"},
        help_text='Must be a unique title.')
    slug = models.SlugField(null=True,blank=True)
    content = models.TextField(null=True, blank=True)
    publish = models.CharField(max_length=120,choices=PUBLISH_CHOICES,default='draft')
    view_count = models.IntegerField(default=0)
    publish_date = models.DateField(auto_now=False,auto_now_add=False,default=timezone.now)
    author_email = models.EmailField(max_length=240,validators=[validate_justin],blank=True,null=True)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def save(self,*args,**kwargs):
        #if not self.slug and self.title:
           # self.slug = slugify(self.title)
        super(PostModel, self).save(*args,**kwargs)
        

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return self.title

def blog_post_model_pre_save_receiver(sender,instance,*args,**kwargs):
    print('before save')
    if not instance.slug  and instance.title:
        instance.slug = slugify(instance.title)

pre_save.connect(blog_post_model_pre_save_receiver,sender=PostModel)

def blog_post_model_post_save_receiver(sender,instance,created,*args,**kwargs):
    print("after save")
    print(created)
    if created:
        if not instance.slug  and instance.title:
            instance.slug = slugify(instance.title)
            instance.save()

post_save.connect(blog_post_model_post_save_receiver,sender=PostModel)