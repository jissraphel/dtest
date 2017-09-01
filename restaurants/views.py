from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,get_object_or_404
from django.views import View
from django.views.generic import CreateView,DetailView,ListView 

from .forms import RestaurantLocationCreateForm
from .models import RestaurantLocation


@login_required(login_url='/login/')
def restaurant_createview(request):


	form=RestaurantLocationCreateForm(request.POST or None)

	if form.is_valid():
		if request.user.is_authenticated():
			instance=form.save(commit=False)
			instance.owner=request.user 

			instance.save()
			return HttpResponseRedirect("/restaurants/")
		else:
			return HttpResponseRedirect("/login/")

	if form.errors:
		errors=form.errors
	else:
		errors=None

		
	template_name='restaurants/form.html'
	context={"form":form,"errors":errors}


	return render(request,template_name,context)


def restaurant_listview(request):
	template_name='restaurants/restaurants_list.html'
	queryset=RestaurantLocation.objects.all()

	context={"abc":queryset
		}
	return render(request,template_name,context)

class RestaurantListView(ListView):
	
	template_name='restaurants/restaurants_list.html'
	def get_queryset(self):
		slug=self.kwargs.get("slug")
		if slug:
			queryset=RestaurantLocation.objects.filter(category__iexact=slug)
		else:
			queryset=RestaurantLocation.objects.all()
		return queryset


class RestaurantCreateView(LoginRequiredMixin,CreateView):
	form_class=RestaurantLocationCreateForm
	login_url='/login/'
	template_name='restaurants/form.html'
	# success_url="/restaurants/"

	def form_valid(self,form): 
		instance=form.save(commit=False)
		instance.owner=self.request.user
		return super(RestaurantCreateView,self).form_valid(form)



class RestaurantDetailView(DetailView):
	#model=RestaurantLocation

	queryset=RestaurantLocation.objects.all()


	# def get_context_data(self,*args,**kwargs):
	# 	print(self.kwargs)
	# 	print(self.args)
	# 	context=super(RestaurantDetailView,self).get_context_data(*args,**kwargs)
	# 	return context

	# def get_object(self,*args,**kwargs):
		
	# 	rest_id=self.kwargs.get('rest_id')
	# 	print(rest_id)
	# 	obj=get_object_or_404(RestaurantLocation,id=rest_id)
	# 	return obj


# Create your views here.


# class HomeView(TemplateView):
# 	template_name="ome.html"

# 	def get_context_data(self,*args,**kwargs):
# 		context=super(HomeView,self).get_context_data(*args,**kwargs)
		
# 		context={"cray":"check it out"}

# 		return context




