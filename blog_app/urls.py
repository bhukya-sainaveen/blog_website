from django.urls import path
from blog_app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.get_all_posts, name='get_all_posts'),
    path('<int:blog_id>/', views.details, name='details')
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
