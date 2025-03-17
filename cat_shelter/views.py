from django.shortcuts import render
from .models import Cat, Breed
from django.shortcuts import get_object_or_404
from django.views import generic
from django import forms
from datetime import datetime

def index(request):
 all_cats = Cat.objects.all().count()
     
 all_breeds = Breed.objects.all().count()

 free_cats = Cat.objects.filter(adopt_status__exact='a').count()

 cats_sex = Cat.objects.filter(adopt_status__exact='f').count()
 cats2_sex = Cat.objects.filter(adopt_status__exact='m').count() 
 cats = Cat.objects.all().order_by('add_date')
 context = {
  'all cats' : all_cats,
  'all breeds' : all_breeds,
  'free cats': free_cats,
  'cats_sex':cats_sex,
  'cats2_sex':cats2_sex,
  'cats': cats
 }
 return render(request, 'index.html', context=context) 

class CatListView(generic.ListView):
  model = Cat
  context_object_name = 'cat_list'
  queryset = Cat.objects.all() 
  template_name = 'cat_list.html' 

class CatDetailView(generic.DetailView):
    model = Cat
    template_name = 'cat_detail.html'

def cat_model_view(request, pk):
    cat = get_object_or_404(Cat, pk=pk)
    return render(request, 'cat_shelter/cat_detail.html', context={'cat': cat})

def index(request):
    return render(request, 'cat_shelter/index.html', {'timestamp': datetime.now().timestamp()})