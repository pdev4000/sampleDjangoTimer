"""TestTimer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static

from django.conf.urls import url
from django.views.static import serve

from timer.views import myHome, myTable, myTimer, myTimer1

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", myHome, name="home"),
    path("sections/<id>", myTable, name="sectionDetails"),
    path("sections/<testId>/<order>/timer", myTimer, name="sectionTimer"),
    path("sections/<sectionId>/timer", myTimer1, name="sectionTimer1"),
    # path('media/(<path>)', serve,{'document_root':       settings.MEDIA_ROOT}),
    # path('static/(<path>)', serve,{'document_root': settings.STATIC_ROOT}),
    url(r"^media/(?P<path>.*)$", serve, {"document_root": settings.MEDIA_ROOT}),
    url(r"^static/(?P<path>.*)$", serve, {"document_root": settings.STATIC_ROOT}),
]
+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)