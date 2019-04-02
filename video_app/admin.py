from django.contrib import admin
from .models import Group, Video, Comment
# Register your models here.
admin.site.register(Group)
admin.site.register(Video)
admin.site.register(Comment)