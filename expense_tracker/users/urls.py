from django.urls import path
from .views import login_page, signup_page, logoutpage

urlpatterns = [
    path('login/', login_page, name='login'),
    path('signup/', signup_page, name='signup'),
    path('logout/', logoutpage, name='logout'),
]