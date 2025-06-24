from django import forms
from .models import ContactMessage, Booking

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['first_name','last_name','email','message']

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['name','phone','email','start_date','end_date','need_insurance','extension_requested']
        widgets = {
            'start_date': forms.DateInput(attrs={'type':'date'}),
            'end_date':   forms.DateInput(attrs={'type':'date'}),
        }
