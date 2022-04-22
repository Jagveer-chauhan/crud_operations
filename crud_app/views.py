from django.shortcuts import render,redirect
from .models import*
# Create your views here.
def insertpageview(request):
    return render(request,"crud_app/insert.html")

def insertdata(request):
    fname = request.POST['fname']
    lname = request.POST['lname']
    email = request.POST['email']
    contact = request.POST['contact']
    #create object of model class
    #insert data in table
    newuser = Student.objects.create(Firstname=fname,Lastname=lname,Email=email,Contact=contact)
    # after insert render on show.html
    return redirect('showdata')
def showdata(request):
    #for fetching all data from table
    all_data = Student.objects.all()
    return render(request,"crud_app/show.html",{'key1':all_data})
#edit page view
def editpage(request, pk):
    #fetching data using perticular id
    get_data = Student.objects.get(id=pk)
    return render(request,"crud_app/edit.html",{'key2':get_data})

#update data view
def updatedata(request,pk):
    user_data = Student.objects.get(id=pk)
    user_data.Firstname= request.POST['fname']
    user_data.Lastname= request.POST['lname']
    user_data.Email= request.POST['email']
    user_data.Contact= request.POST['contact']
    # query for update
    user_data.save()
    #render to show page
    return redirect('showdata')
#delete data view
def deletedata(request,pk):
    delete_data=Student.objects.get(id=pk)
    delete_data.delete()
    return redirect('showdata')