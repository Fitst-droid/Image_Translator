from django.shortcuts import render
from django.urls import reverse_lazy

from django.views import  generic

from .forms import TextForm

class IndexView(generic.TemplateView):
  template_name = "index.html"
  form_class = TextForm

  def form_valid(self, form):
    data = form.cleaned_data
    choice1 = data["choice1"]
    choice2 = data["choice2"]

    new_text = text.replace(choice1, choice2)

    ctxt = self.get_context_data(new_text=new_text, form=form)
    return self.render_to_response(ctxt)


