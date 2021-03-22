from hashlib import md5
import mistune
from django.contrib.auth.models import User
from django.db import models


class Qauser(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    first_name = models.CharField(max_length=35, null=True, default=None,
                                  blank=True)
    last_name = models.CharField(max_length=35, null=True, default=None,
                                 blank=True)
    email = models.EmailField(null=True, blank=True, default=None)

    about_text = models.TextField(blank=True, null=True, max_length=500,
                                  default=None)

    profile_pic = models.ImageField(default="logo.png", null=True)

    date_created = models.DateTimeField(auto_now_add=True, null=True)

    website = models.URLField(null=True, blank=True, default=None)
    twitter = models.URLField(null=True, blank=True, max_length=50,
                               default=None)
    facebook = models.URLField(null=True, blank=True, max_length=50,
                               default=None)
    github = models.URLField(null=True, blank=True, max_length=39,
                              default=None)


    def __str__(self): 
         return self.first_name

    def __unicode__(self):
        return "<Qauser:{}>".format(self.user.first_name)

    def update_profile_data(self):
        self.about_html = mistune.markdown(self.about_text)
        


