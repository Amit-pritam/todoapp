from django.shortcuts import render,redirect
from .models import TodoModel




def index(request):                                      #index view function.             
	obj = TodoModel.objects.all()                        #query used to show all the data.
	context = {"obj": obj}                               #context written in dictioary.
	return render(request,"frontend/index.html",context) #render index.html(index page).

def addtask(request):                                    #add task view function.
	mytask = request.POST["task"]                        #POST method used for add task.(variable mytask)
	TodoModel(task = mytask).save()                      #query written to save the task.
	return redirect(request.META["HTTP_REFERER"])        #redirect to same page.


def deletetask(request , idpk):                          #view function of delete task(idpk is primary key id (from url))
	TodoModel.objects.filter(id = idpk).delete()         #query for delete tha task
	return redirect(request.META["HTTP_REFERER"])        # redirect to same page.


def edittaskview(request , idpk):                        #edit task view function on edit page.                       
	context = {"idname": idpk}
	return render(request,"frontend/edit.html",context)  #render to edit task page


def edittask(request, idpk):                             #edit task function view.                              
	mytask = request.POST["task"]                        #Post method used.
	update = TodoModel.objects.filter(id = idpk)[0]      #query to update task.
	update.task = mytask                                 #update the task to mytask.
	update.save()                                        #save the task.
	return redirect('index')                             #redirect to index page






	