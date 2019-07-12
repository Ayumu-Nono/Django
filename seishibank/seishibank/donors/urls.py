from django.urls import path,include
from . import views
from .views import DonorListView ,DonorCreateView


app_name='donors'

urlpatterns = [
    path('',DonorListView.as_view(),name='donors.list'),
    path('donor_create/',views.DonorCreateView.as_view(),name='create'),
    # path('donor_search/',views.SearchFormView.as_view(),name='search'),
    
    ]
