# -*- coding: utf-8 -*-
from django.contrib import admin
#from django.core.urlresolvers import reverse
from vkontakte_api.admin import VkontakteModelAdmin
from . models import Comment


class CommentAdmin(VkontakteModelAdmin):
    list_display = ('remote_id', 'instance_id', 'author_id', 'text', 'date')
    list_filter = ('instance_id',)


admin.site.register(Comment, CommentAdmin)
