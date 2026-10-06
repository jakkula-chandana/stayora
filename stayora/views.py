from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login
from .models import Hostel

def home(request):

    hostels = Hostel.objects.all()

    search = request.GET.get('search', '')
    hostel_type = request.GET.get('type', '')
    max_rent = request.GET.get('max_rent', '')
    food = request.GET.get('food', '')

    if search:
        hostels = hostels.filter(
            name__icontains=search
        ) | hostels.filter(
            location__icontains=search
        )

    if hostel_type:
        hostels = hostels.filter(
            hostel_type=hostel_type
        )

    if max_rent:
        hostels = hostels.filter(
            rent__lte=max_rent
        )

    if food == 'yes':
        hostels = hostels.filter(
            food_available=True
        )

    context = {
        'hostels': hostels,
        'search': search,
        'selected_type': hostel_type,
        'selected_rent': max_rent,
        'selected_food': food,
    }

    return render(
        request,
        'stayora/home.html',
        context
    )
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = User.objects.create_user(
            username=username,
            password=password
        )

        login(request, user)

        return redirect('home')

    return render(request, 'stayora/register.html')