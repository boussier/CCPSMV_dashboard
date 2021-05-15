# users/urls.py
from django.urls import path
from .views import (
    RemoteworkEvalDetailView,
    RemoteworkEvalListView
)

urlpatterns = [
    path('', RemoteworkEvalListView.as_view()),
    path('<int:pk>/', RemoteworkEvalDetailView.as_view())
]
