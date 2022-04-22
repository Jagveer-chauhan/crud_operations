from django.urls import path, include
from . import views
urlpatterns = [
 path("",views.insertpageview,name="insertpage"),
 path("insert/",views.insertdata,name="insert"),  
 path("showdata/",views.showdata,name="showdata"),
 path("editpage/<int:pk>",views.editpage,name="editpage"),
 path("update/<int:pk>",views.updatedata,name="update"),
 path("delete/<int:pk>",views.deletedata,name="delete"),
]