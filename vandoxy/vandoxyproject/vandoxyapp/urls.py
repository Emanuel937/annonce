from django.urls import path
from . import views
from django.conf.urls import url
urlpatterns = [
    url('signup/',    views.signup,          name='signup'),
    url('login/',     views.login,           name='login' ),
    url('logout/',    views.logout_function, name='logout'),
    url('search/',    views.search_page,     name='search'),
    url('depot/',     views.depot_page,      name='depot'),
    url('messager/',  views.menssage_page,   name='msg'),
    url('fv/',        views.favorite_page,   name="favorite"),
    url('',           views.homepage,        name='home'  ),
   
  
]
SOCIAL_AUTH_URL_NAMESPACE = 'social'