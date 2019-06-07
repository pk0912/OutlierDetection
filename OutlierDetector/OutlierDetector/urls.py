"""OutlierDetector URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from OutlierDetectorApp.views import GetOutlierView,GetOutlierView2
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^getOutlierMethod1/(?P<resource_id>\d+)[/]?$', GetOutlierView.as_view(), name='outlier_view1'),
    url(r'^getOutlierMethod1[/]?$', GetOutlierView.as_view(), name='my_rest_view'),
    url(r'^getOutlierMethod2/(?P<resource_id>\d+)[/]?$', GetOutlierView2.as_view(), name='outlier_view2'),
    url(r'^getOutlierMethod2[/]?$', GetOutlierView2.as_view(), name='outlier_view'),
]
