from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

# from rest_framework.authtoken.views import ObtainAuthToken

# router = DefaultRouter()
# router.register('post', views.PostModelViewset, basename = 'post')
# router.register('category', views.CategoryModelViewset, basename = 'category')

app_name = 'api-v1'
urlpatterns = [
    #registration
    path('registration/',views.RegistrationApiView.as_view(), name="registration"),
    #change password
    #reset password
    #login token
    path('token/login/', views.CustomObtainAuthToken.as_view(), name="token-login"),
    path('token/logout/', views.CustomDiscardAuthToekn.as_view(), name="token-logout"),
    #login jwt
]
# urlpatterns += router.urls 