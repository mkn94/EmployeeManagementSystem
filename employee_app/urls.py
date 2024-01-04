
from django.urls import path,include
from .import views

urlpatterns = [
    path('',views.home1,name='home1'),
    path('admin_login',views.admin_login,name="admin_login"),
    path('login1',views.login1,name='login1'),
    path('index',views.index,name='index'),
    path('all_emp',views.all_emp,name='all_emp'),
    path('add_emp',views.add_emp,name='add_emp'),
    path('remove_emp',views.remove_emp,name='remove_emp'),
    path('remove_emp/<int:emp_id>',views.remove_emp,name='remove_emp'),
    path('filter_emp',views.filter_emp,name='filter_emp'),
    path('user_logout/',views.user_logout, name='logout'),
]