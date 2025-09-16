from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.home_page),
    path('about', views.about_page),
    path('contacts', views.contacts_page),
    path('categories', views.categories_page),
    path('category/<str:pk>', views.category_page),
    path('new/<int:pk>', views.new_page),
    path('add_new', views.add_new, name='add_news'),
    path('add_category', views.add_category, name='add_categories'),
    path('register', views.register_user),
    path('login', views.auth_user),
    path('profile', views.profile, name='profile'),
    path('logout/', views.logout_view, name='logout'),
    path("profile/change-avatar/", views.change_avatar, name="change_avatar"),

]