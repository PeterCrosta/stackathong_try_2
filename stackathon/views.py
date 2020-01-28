from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView
from stackathon.forms import UserForm, AllergyForm, PrescriptionForm
from stackathon.models import User, Prescription, Allergy

# Create your views here.

# def home(request):
#     form = UserForm(request.GET or None)
#     user = form.save(commit=False)
#     user.save()
#     return render(request, 'stackathon/home.html')

class HomeUserView(ListView):
    """Renders the home page, with a list of all messages."""
    model = User

    def get_context_data(self, **kwargs):
        print('kwargs are: ', kwargs)
        print('all my users', User.objects.all())
        context = super(HomeUserView, self).get_context_data(**kwargs)
        return context

def login(request):
    return render(request, 'stackathon/login.html')

def allergies(request):
    form = AllergyForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            allergy = form.save(commit=False)
            allergy.save()
            return redirect("contraindications")

    else:
        return render(request, 'stackathon/allergies.html', {"form": form})

def contraindications(request):
    return render(request, 'stackathon/contraindications.html')

def create_account(request):
    print('request.post: ', request.POST)
    form = UserForm(request.POST or None)
    print('the create account form sent: ', form)
    
    if request.method == "POST":
        if form.is_valid():
            user = form.save()
            print('user is: ', request)
            user.save()
            request.session['id'] = request.POST.id
            print('session is: ', request.session)
            return redirect("home")

    else:
        return render(request, 'stackathon/create_account.html', {"form": form})

def prescriptions(request):
    form = PrescriptionForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            prescription = form.save(commit=False)
            prescription.save()
            return redirect('contraindications')

    else:
        return render(request, 'stackathon/prescriptions.html', {"form": form})