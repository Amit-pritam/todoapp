from django.urls import path,include
from. views import *



urlpatterns = [
    path('',index,name="index"),                           #url of index view.
    path('addtask/',addtask,name="add"),                   #url of addtask view.
    path('delete/<int:idpk>/',deletetask,name="delete"),   #url of delete task with (idpk(id primarykey)).
    path('edit/<int:idpk>/',edittaskview,name="editview"), #url of edit task view with (idpk(id primarykey)).
    path('edit/<int:idpk>/update/',edittask,name="edit"),  #url of edit task with (idpk(id primarykey)).
]
