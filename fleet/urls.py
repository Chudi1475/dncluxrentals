from django.urls import path
from . import views

urlpatterns = [
    path('',                views.HomeView.as_view(),        name='home'),
    path('services/',       views.ServicesView.as_view(),    name='services'),
    path('testimonials/',   views.TestimonialsView.as_view(),name='testimonials'),
    path('contact/',        views.ContactView.as_view(),     name='contact'),
    path('category/<slug:slug>/', views.CategoryView.as_view(),      name='category'),
    path('vehicle/<slug:slug>/',  views.VehicleDetailView.as_view(), name='vehicle_detail'),
]
