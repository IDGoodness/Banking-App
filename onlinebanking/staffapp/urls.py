from django.contrib import admin
from django.urls import path, re_path, include
from django.views.generic import TemplateView
from onlinebanking.staffapp import views as staff_view


urlpatterns = [
    re_path(r'^staff_profile/(?P<user_id>\d+)/', staff_view.staff_profile, name="staff_profile"),
    re_path(r'^manage_staff/', staff_view.manage_staff, name="manage_staff"),
    re_path(r'^manage_customer/', staff_view.manage_customer, name="manage_customer"),
    re_path(r'^edit_profile/(?P<user_id>\d+)/', staff_view.edit_profile, name="edit_profile"),
    re_path(r'^deactivate/(?P<user_id>\d+)/', staff_view.deactivate_staff, name="deactivate"),
    re_path(r'^create_account/(?P<user_id>\d+)/', staff_view.create_user_account, name="create_account"),
]