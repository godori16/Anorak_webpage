from django.urls import path

from . import views

urlpatterns = [
    path('', views.DataListView.as_view(), name='data'),
    path('<int:pk>/', views.DataDetailView.as_view(), name='data_detail'),
]