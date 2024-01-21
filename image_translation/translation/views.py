from django.shortcuts import render
from django.urls import reverse_lazy

from django.views import  generic

from .forms import ControlForm

class IndexView(generic.TemplateView):
  template_name = "index.html"
  form_class = ControlForm

  def get(self, request, *args, **kwargs):
    """GETリクエスト用のメソッド"""
    form = ControlForm
    return render(request, 'index.html', {"from": form})

  def post(self, request, *args, **kwargs):
    """POSTリクエスト用のメソッド"""
    form = ControlForm(request.POST, request.FILES)

    if not form.is_valid():
      return render(request, 'index.html', {"from": form})
  
    filename_save = form.save()

    context = {
      'form': form,
      'filename_save': filename_save,
    }
 
    return render(request, 'index.html', context)
   
  # def form_valid(self, form):
  #   data = form.cleaned_data
  #   choice1 = data["choice1"]
  #   choice2 = data["choice2"]

  #   new_text = text.replace(choice1, choice2)

  #   ctxt = self.get_context_data(new_text=new_text, form=form)
  #   return self.render_to_response(ctxt)


