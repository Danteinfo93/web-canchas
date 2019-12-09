from django.urls import path

from .views import ReservaDetailView, ReservaListView, ReservaCreate, ReservaUpdate, ReservaDelete

reservas_patterns = ([
    path('', ReservaListView.as_view(), name='list'),
    path('<int:pk>/', ReservaDetailView.as_view(), name='detail'),
    path('create/', ReservaCreate.as_view(), name='create'),
    path('update/<int:pk>/', ReservaUpdate.as_view(), name='update'), 
    path('delate/<int:pk>/', ReservaDelete.as_view(), name='delete'),
], 'reservas')