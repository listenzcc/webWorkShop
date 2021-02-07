'''
A collection of views object in django
Since there are a lot of projects in the workshop,
it is necessary to put an one-in-all views manager to manage them.
'''

import time

from django.conf.urls import url
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import path
from django.views.generic.base import RedirectView

from . import url_patterns


class DefaultView(object):
    '''
    Index view of the server.
    Generate index html and serve it.
    '''

    def __init__(self):
        pass

    def home_page(self):
        '''
        The html of Home page
        '''
        route = r'^$'

        def view(request):
            contents = dict(
                currentTime=time.ctime(),
            )
            return render(request, 'index.html', contents)

        p = url(route, view)
        return url_patterns.append(p, 'Home page', 'html')

    def route_page(self):
        '''
        The html of route table
        '''
        route = r'^route$'

        def view(request):
            return HttpResponse(url_patterns.df.to_html())

        p = url(route, view)
        return url_patterns.append(p, 'Route table', 'html')
