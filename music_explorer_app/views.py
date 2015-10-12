# music_explorer_app/views.py - definitions of views of music_explorer_app
#
# Copyright 2015 kharts (https://github.com/kharts)
#
# This software may be used and distributed according to the terms of the
# GNU General Public License version 2 or any later version.

__author__ = 'kharts'

from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world!")
