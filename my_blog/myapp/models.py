from django.db import models
from django.itils.text import slugify
from django.contrib.auth.models import User

# Create your models here.

Class Category[models.Model]:
name = models.CharField{max_length=50, unique=True}
slug = models.SlugField{max_length=50, unique=True}

    def _ _str_ _(self):
        return self.name

    def save(self,'args, ''kwargs):
        self.slug = slugify(self.name)
        super{}.save('args, ''kwargs)

Class Post(models.Model):
title = models.CharField(max_length=100)
slug = models.SlugField(max_length=100, unique=True)
author = models.ForeignKey(User)

