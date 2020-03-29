from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('introduction/', views.IntroductionPageView.as_view(), name='introduction'),
    path('product/', views.ProductPageView.as_view(), name='product'),
    path('contact/', views.ContactPageView.as_view(), name='contact'),
]