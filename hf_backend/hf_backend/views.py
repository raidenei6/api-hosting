# hf_backend/views.py
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hugging Face API is running!")
