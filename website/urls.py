from django.urls import path
from .views import home_view,objective_view,contact_view,signup,galleryView,deletePicture
from django.contrib.auth.views import LoginView,LogoutView


urlpatterns = [
    path('',home_view,name='home'),
    path('objectives/',objective_view,name='objectives'),
    path('contact/',contact_view,name='contacts'),
    path('gallery/',galleryView,name='gallery'),
    path('blog/',contact_view,name='blog'),
    path('delete_picture/<int:id>',deletePicture,name='pic_delete'),
    path('signup/',signup,name='signup'),
    path('login/',LoginView.as_view(template_name='login.html'),name='login'),
    path('logout/',LogoutView.as_view()),
]