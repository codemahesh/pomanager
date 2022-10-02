"""pomanager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from unicodedata import name
from django.contrib import admin
from django.urls import path, include
from po import views


admin.site.site_header = 'PO Management System Admin'
admin.site.index_title = 'Admin'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('__debug__/', include('debug_toolbar.urls')),
    path('customer/', include('po.urls')),
    path('', views.add_show, name="addandshow"),
    path('delete/<id>/', views.delete_data, name="deletedata"),
    path('update/<id>/', views.update_data, name="updatedata"),
    path('unit/',views.unit_add, name='addunit'),
    path('unit/update/<id>/',views.unit_update, name='updateunit'),
    path('unit/delete/<id>/',views.unit_delete, name='deleteunit'),
    path('customerpo/',views.customer_po_add, name='addcustomerpo'),
    path('customercode/', views.getCustomerCode, name='customercode'),
    path('fillcustomerdetail/',views.fillcustomercode, name='fillcustomerdetail'),

]
