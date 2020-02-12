"""weggcron URL Configuration

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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.documentation import include_docs_urls

API_TITLE = 'Egg Rest Scheduler'
API_DESCRIPTION = 'Egg Rest Scheduler'


urlpatterns = [
    path('admin/', admin.site.urls),
    path('egg/', include('uploadapp.urls')),
    path('cron/', include('cronapp.urls')),
    path('', include('viewerapp.urls')),
    path(r'docs/', include_docs_urls(title=API_TITLE, description=API_DESCRIPTION))
]

if settings.DEBUG:
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)