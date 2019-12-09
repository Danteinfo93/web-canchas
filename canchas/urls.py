from django.urls import path

from .views import CanchaDetailView, CanchaListView

canchas_patterns = ([
    path('', CanchaListView.as_view(), name='list'),
    path('<int:pk>/', CanchaDetailView.as_view(), name='detail'),
],'canchas')