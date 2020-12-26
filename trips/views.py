from django.shortcuts import render, redirect
from django.http import HttpResponse
from trips.forms import InputForm
from django.contrib import messages
from trips.models import Trip

# Create your views here.
def index(request):
    return render(request, 'trips/index.html')



def book_trip(request):

    form = InputForm(request.POST)
    if request.method =='POST':
       
        if form.is_valid():
            event=form.save(commit=False)
            event.customer=request.user
            event.save()
            return redirect('trips:trips')    
        else:
            messages.error(request, "Error")
            
    return render(request, 'trips/book.html',{'form':form})
    
def trips(request):
    trips = Trip.objects.filter(customer=request.user)
    print(trips)
    context = {
        "trips_list": trips,
    }
    return render(request, 'trips/trips.html', context)

def delete_trip(request, id):
    delete = Trip.objects.get(id = id)
    delete.delete()
    
    return redirect ('trips:trips')

