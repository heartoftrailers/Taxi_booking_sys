from django import forms
from trips.models import Trip
import datetime
from django.forms import widgets
from django.contrib.admin import widgets  



class InputForm(forms.ModelForm): 
    PAYMENT_METHODS = (
            ('1', 'Card'),
            ('2', 'Cash'),
    )
    pick_up_time = forms.DateTimeField()
    pick_up_place = forms.CharField(max_length=100, label = 'Pick up place')
    payment_method  = forms.ChoiceField(widget=forms.RadioSelect,choices=PAYMENT_METHODS)
    drop_off_place = forms.CharField(max_length=80, label = 'Drop off place')
    
    class Meta:
        model = Trip
        fields = ('pick_up_place','drop_off_place','pick_up_time','payment_method','driver')






