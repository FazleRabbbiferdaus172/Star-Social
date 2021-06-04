from django import template
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.http import Http404
from braces.views import generic
from . import models
from . import forms

from django.contrib.auth import get_user_model
# Create your views here.
User = get_user_model()


class PostList(SelectRelatedMixin, generic.ListView):
    model = models.Post
    select_related = ('user', 'group')


class UserPosts(generic.ListView):
    model = models.Post
    template_name = 'posts/user_post_list.html'

    def get_queryset(self):
        try:
            self.post.user = User.objects.prefetch_related('posts').get(
                username__iexact=self.kwargs.get('username'))
        except User.DoesNotExist:
            raise Http404
        else:
            return self.post_user.posts.all()
