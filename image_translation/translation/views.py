from django.shortcuts import render
from .forms import ControlForm
from django.views.generic import View

class IndexView(View):
  def get(self, request, *args, **kwargs):
    """GETリクエスト用のメソッド"""
    form = ControlForm
    return render(request, 'index.html', {"form": form})

  def post(self, request, *args, **kwargs):
    """POSTリクエスト用のメソッド"""
    form = ControlForm(request.POST, request.FILES)
    context = {
      'form': form
    }

    if not form.is_valid():
      return render(request, 'index.html', {"form": form})
  
    filename_save = form.save()

    context = {
      'form': form,
      'filename_save': filename_save,
    }
 
    return render(request, 'index.html', context)
  
index = IndexView.as_view()    


