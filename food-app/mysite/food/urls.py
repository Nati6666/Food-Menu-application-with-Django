from .import views
from django.urls import path

app_name = 'food'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:item_id>/', views.item_detail, name='item_detail'),
    path('item/', views.item, name='item'),

]
