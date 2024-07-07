from django.urls import path, include

from api.spectacular.urls import urlpatterns as doc_urls
from blog.urls import urlpatterns as posts_urls

app_name = 'api'

urlpatterns = [
    path('auth/', include('djoser.urls.base')),
    path('auth/', include('djoser.urls.jwt')),
]
urlpatterns += doc_urls
urlpatterns += posts_urls