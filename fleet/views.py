from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, FormView
from .models import Category, Vehicle, Testimonial
from .forms import ContactForm, BookingForm

class HomeView(TemplateView):
    template_name = 'fleet/home.html'
    def get_context_data(self, **kw):
        ctx = super().get_context_data(**kw)
        ctx['featured']   = Vehicle.objects.all()[:4]
        ctx['categories'] = Category.objects.all()
        return ctx

class ServicesView(TemplateView):
    template_name = 'fleet/services.html'

class TestimonialsView(ListView):
    model               = Testimonial
    template_name       = 'fleet/testimonials.html'
    context_object_name = 'testimonials'

class ContactView(FormView):
    template_name = 'fleet/contact.html'
    form_class    = ContactForm
    success_url   = reverse_lazy('contact')
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class CategoryView(ListView):
    model               = Vehicle
    template_name       = 'fleet/category.html'
    context_object_name = 'vehicles'
    def get_queryset(self):
        return Vehicle.objects.filter(category__slug=self.kwargs['slug'])
    def get_context_data(self, **kw):
        ctx = super().get_context_data(**kw)
        ctx['category'] = Category.objects.get(slug=self.kwargs['slug'])
        return ctx

class VehicleDetailView(FormView, DetailView):
    model               = Vehicle
    template_name       = 'fleet/vehicle_detail.html'
    form_class          = BookingForm
    context_object_name = 'vehicle'
    def form_valid(self, form):
        booking = form.save(commit=False)
        booking.vehicle = self.get_object()
        booking.save()
        return super().form_valid(form)
    def get_success_url(self):
        return self.request.path
