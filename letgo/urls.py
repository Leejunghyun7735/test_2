
from django.urls import path,include
from letgo import views

urlpatterns = [
    path('/', views.letgoAPI, name="index"),
    path('<int:id>/', views.letgodetailAPI, name="letgo_view"),
]