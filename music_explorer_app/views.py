# music_explorer_app/views.py - definitions of views of music_explorer_app
#
# Copyright 2015 kharts (https://github.com/kharts)
#
# This software may be used and distributed according to the terms of the
# GNU General Public License version 2 or any later version.

__author__ = 'kharts'

from django.shortcuts import render

def index(request):
    """
    Main view
    :param request: - django HttpRequest object
    :return: HttpResponse
    """

    context = {}
    return render(request,
                  "music_explorer_app/index.html",
                  context)
