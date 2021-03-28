from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
from .models import Abc
from .form import AbcForm


# Create your views here.
    
def index(request):
    form = AbcForm()
    data = Abc.objects.all()
    context = {
        'form':form,
        'data':data
    }
    return render(request, 'index.html',context)

def Add_data(request):
    if request.method =='POST':
        form = AbcForm(request.POST)
        if form.is_valid():
            id = request.POST.get('id')
            name = form.cleaned_data['name']
            age = form.cleaned_data['age']
            score =form.cleaned_data['score']
            if id == '':
                form.save()
            else:
                Abc.objects.filter(id=id).update(name=name,age=age,score=score)
            data = Abc.objects.values() 
            return JsonResponse({'status':'success','data':list(data)})
        else:
            return JsonResponse({'status':'failed'})

def edit_data(request):
    if request.method == 'POST':
        id = request.POST['id']
        d = Abc.objects.get(id=id) 
        data = {'id':d.id,'name':d.name,'age':d.age,'score':d.score}
        return JsonResponse({'status':'success','data':data})
    else:
        return JsonResponse({'status':'failed'})

def delete_data(request):
    if request.method =='POST':
        id = request.POST['id']
        data = Abc.objects.filter(id=id).delete()
        return JsonResponse({'status':'success'})
    else:
        return JsonResponse({'status':'failed'})
