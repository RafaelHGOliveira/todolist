
from django.urls import path

from core.views import IndexView, DeleteTodoView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('delete/<int:pk>', DeleteTodoView.as_view(), name='del_todo')
]
