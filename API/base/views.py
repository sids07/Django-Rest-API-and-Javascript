from django.shortcuts import render

def home(request):
    print('inside home view')
    return render(request, 'home.html')
def login(request):
    print('inside home view')
    return render(request, 'new_url.html')

def signup(request):
    print('inside home view')
    return render(request, 'signup.html')

def donate(request):
    print("Donation")
    return render(request,'donate.html')

def profile(request):
    print("Profile")
    return render(request,'profile.html')

def donation_form(request):
    return render(request,'create.html')

def donation(request):
    return render(request,'donation_form.html')

def form(request):
    return render(request,'form.html')

def search(request):
    return render(request,'search.html')
