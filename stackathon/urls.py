from django.urls import path
from stackathon import views
from stackathon.models import Allergy, Prescription, User

home_user_info = views.HomeUserView.as_view(
    queryset=User.first_name,
    context_object_name="user",
    template_name="stackathon/home.html",
)

urlpatterns = [
    path("", home_user_info, name="home"),
    path('login/', views.login, name='login'),
    path('prescriptions/', views.prescriptions, name='prescriptions'),
    path('allergies/', views.allergies, name='allergies'),
    path('contraindications/', views.contraindications, name='contraindications'),
    path('create_account/', views.create_account, name='create_account')
]