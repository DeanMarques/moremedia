from django.conf.urls import url
from accounts_app import views


app_name = 'accounts_app'

urlpatterns = [
    url(r'^signup/', views.signup, name='signup'),
    url(r'^login/', views.loginview, name ='login'),
    url(r'^logout/', views.logoutview, name='logout'),
    
    
]