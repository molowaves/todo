from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import UpdateView, DetailView, DeleteView
from django.core.paginator import Paginator

from .models import Todo
from .forms import TodoForm, SearchForm


def index(request):
	# retrives query strings
	qs = request.GET.get('todos')
	evd = request.GET.get('evd')

	# Filters todos by query string
	if qs:
		todos = Todo.objects.filter(note__icontains=qs).order_by('-time_stamp')
	elif evd:
		todos = Todo.objects.filter(event_date=evd).order_by('-time_stamp')
	else:
		todos = Todo.objects.order_by('-time_stamp')


	if request.method == 'POST':
		form = TodoForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, 'Data Saved!')
			return redirect('index')
	else:
		form = TodoForm()

	search_form =  SearchForm()
	paginator = Paginator(todos, 15)
	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)

	context = {'form':form, 'search_form':search_form, 'page_obj':page_obj}
	return render(request, 'core/index.html', context)



class TodoUpdateView(UpdateView):
	model = Todo
	form_class = TodoForm
	template_name = 'core/todo_update.html'
	success_url = reverse_lazy('index')



class TodoDetailView(DetailView):
	model =  Todo



class TodoDeleteView(DeleteView):
	model = Todo
	success_url = reverse_lazy('index')


