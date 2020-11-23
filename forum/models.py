import datetime

from django.db import models
from django.utils import timezone

# Create your models here.

class subject(models.Model):
    # ...
    def __str__(self):
        return self.question_text

class post(models.Model):
    # ...
    def __str__(self):
        return self.question_text

class replies(models.Model):
    # ...
    def __str__(self):
        return self.question_text

class like(models.Model):
    # ...
    def __str__(self):
        return self.choice_text

class agree(models.Model):
    # ...
    def __str__(self):
        return self.choice_text

class informative(models.Model):
    # ...
    def __str__(self):
        return self.choice_text