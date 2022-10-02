from django.urls import path
from . import views


#URL Conf
urlpatterns = [
    path('',views.customer_form, name= 'customer_insert'),
    path('<int:id>/',views.customer_form, name="customer_update"),
    path('list/',views.customer_list, name='customer_list')
]
  