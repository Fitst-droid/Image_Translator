from django.urls import path

from . import views

# path('空欄は全て対象', as_view = ビューの関数化, URLを逆引きする時の名前)
# path('第1関数', 第2関数, 第3関数)
app_name = 'translation'
urlpatterns = [
  path('', views.IndexView.as_view(), name="index"),
  path('inquiry/', views.InquiryView.as_view(), name="inquiry"),
]
