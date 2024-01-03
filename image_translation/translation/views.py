from django.shortcuts import render
from django.urls import reverse_lazy

from django.views import  generic
from .forms import InquiryForm

# Create your views here.
class IndexView(generic.TemplateView):
  template_name = "index.html"

# 問い合わせ先
class InquiryView(generic.FormView):
  template_name = "inquiry.html"
  form_class = InquiryForm
