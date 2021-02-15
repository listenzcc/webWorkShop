'''
A collection of views object in django
Since there are a lot of projects in the workshop,
it is necessary to put an one-in-all views manager to manage them.
'''

import os
import time

from django.conf.urls import url
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import path
from django.views.generic.base import RedirectView

from . import url_patterns

SYNC_FOLDER = os.environ.get('SYNC', None)


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
        return url_patterns.append(p, 'Home Page', 'html')

    def route_page(self):
        '''
        The html of route table
        '''
        route = r'^route$'

        def view(request):
            return HttpResponse(url_patterns.df.to_html())

        p = url(route, view)
        return url_patterns.append(p, 'Route Table', 'html')


class FlowersPlotView(object):
    '''
    Page of Flowers Plot View
    '''

    def __init__(self):
        self.prefix = os.path.join(
            'flowersPlot')

        self.working_dir = os.path.join(
            os.path.dirname(__file__),
            '..',
            '..',
            'workshop',
            'flowersPlot'
        )

    def home_page(self):
        '''
        The html of Home page
        '''
        route = r'^flowersPlot$'

        def view(request):
            contents = dict(
                workingDir=self.prefix
            )
            return render(request, 'flowersPlot.html', contents)

        p = url(route, view)
        return url_patterns.append(p, 'Page of Flowers Plot', 'html')

    def js_file(self):
        '''
        The js file in the [self.working_dir]
        '''
        route = r'^flowersPlot/(.{1,20}\.js)$'

        def view(request, x):
            return HttpResponse(
                open(os.path.join(self.working_dir, x)).read(),
                'application/javascript')

        p = url(route, view)
        return url_patterns.append(p, 'JS File', 'json')


class ChoroplethMapsView(object):
    '''
    Response using geojson of choropleth maps
    '''

    def __init__(self, dir=None):
        '''
        Init the View

        Args:
        - @dir: Full path of the directory containing the required files.
        '''
        self.dir = dir
