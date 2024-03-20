from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers

from blog_app import views

urlpatterns = [
    path('', views.get_all_posts, name='get_all_posts'),
    path('<int:blog_id>/', views.details, name='details'),
    path('hello', views.helloWorldView.as_view(), name='hello'),
    path('api-auth/', include('rest_framework.urls'))
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

router = routers.SimpleRouter()
router.register('post', views.PostView)
urlpatterns += router.urls
