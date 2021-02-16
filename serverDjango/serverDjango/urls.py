"""serverDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from .views_collection import DefaultView
from .views_collection import FlowersPlotView
from .views_collection import ChoroplethMapsView
from . import url_patterns


# ----------------------------------------
# System Default
url_patterns.append(
    path('admin/', admin.site.urls),
    'Admin managing page'
)


# ----------------------------------------
# Project Default
default_view = DefaultView()
default_view.home_page()
default_view.route_page()


# ----------------------------------------
# View of flowers plot
flowers_plot_view = FlowersPlotView()
flowers_plot_view.home_page()
flowers_plot_view.js_file()


# ----------------------------------------
# View of choropleth maps
choropleth_maps_view = ChoroplethMapsView()
choropleth_maps_view.home_page()
choropleth_maps_view.js_file()
choropleth_maps_view.json_file()


# ----------------------------------------
# Show what we have
url_patterns.display()


# ----------------------------------------
# Generate urlpatterns list
urlpatterns = url_patterns.to_list()
