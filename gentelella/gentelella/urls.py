"""gentella URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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

#from django.conf.urls import handler404,handler500
#from app.views import Error404View, Error500View

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    # app/ -> Genetelella UI and resources
    url(r'^app/', include('app.urls')),
    url(r'^', include('app.urls')),

    #URL necesaria para el login
    url('accounts/', include('django.contrib.auth.urls')),
]

#handler404 = Error404View.as_view()
#handler500 = Error500View.as_view()

