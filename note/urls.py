from django.urls import path
from . import views

urlpatterns = [
    path("", views.home_page, name="home_page"),
    path("rename/<str:note_content>/", views.rename, name="rename")
]