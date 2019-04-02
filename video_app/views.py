from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Group, Video,Comment
# Create your views here.

@login_required
def index(request):
    all_groups = Group.objects.all()
    context = {'all_groups':all_groups}
    return render(request, 'video_app/index.html', context)

def detail(request, group_id):
    group = Group.objects.get(pk=group_id)
    videos = Video.objects.filter(group=group_id)
    return render(request, 'video_app/detail.html', {'group': group,'videos':videos})

