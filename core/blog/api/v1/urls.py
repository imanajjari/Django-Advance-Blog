from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('post', views.PostModelViewset, basename = 'post')
router.register('category', views.CategoryModelViewset, basename = 'category')

app_name = 'api-v1'
urlpatterns = [
    # path('post/',views.postList,name="post-list"),
    # path('post/',views.PostList.as_view(),name="post-list"),
    # path('post/',views.PostViewset.as_view({'get':'list'}),name="post-list"),
    # path('post/<int:id>/',views.postDetail,name="post-detail"),
    # path('post/<int:id>/',views.PostDetail.as_view(),name="post-detail"),
]
urlpatterns += router.urls 