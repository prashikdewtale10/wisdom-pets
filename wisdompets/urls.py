
from django.contrib import admin
from django.urls import path
from adaptions import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name="home"),
    path('pet_detail/<int:id>',views.pet_detail,name="pet_detail")
]
