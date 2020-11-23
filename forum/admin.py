from django.contrib import admin
from .models import subject, post, replies, like, agree, informative
# Register your models here.

admin.site.register(subject)
admin.site.register(post)
admin.site.register(replies)
admin.site.register(like)
admin.site.register(agree)
admin.site.register(informative)