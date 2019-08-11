from django.db import models
from django.contrib import auth
from django.template.defaultfilters import slugify
from django.urls import reverse
from django.utils import timezone
# Create your models here.


class UserProfile(models.Model):
    name = models.OneToOneField('auth.user',on_delete=models.CASCADE)
    college = models.CharField(max_length=700)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    dateOfBirth = models.DateTimeField(default=timezone.now)
    slug = models.SlugField(blank=True,null=True)
    image = models.ImageField(upload_to='proapp/images',default="hexapod_edr1JFH.jpg")

    def __str__(self):
        return self.name.username

    def save(self,*args,**kwargs):
        str = self.name.username
        str1 = str+self.college
        self.slug = slugify(str1)
        super(UserProfile,self).save(*args,**kwargs)

    def get_absolute_url(self):
        return reverse("usersdetail",kwargs={'slug':self.slug})
