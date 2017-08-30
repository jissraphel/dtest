from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView




def restaurant_listview(request):
	template_name='restaurants/restaurants_list.html'

	context={abc:[2,3,4]
		}
	return render(request,template_name,context)


# Create your views here.


# class HomeView(TemplateView):
# 	template_name="home.html"

# 	def get_context_data(self,*args,**kwargs):
# 		context=super(HomeView,self).get_context_data(*args,**kwargs)
		
# 		context={"cray":"check it out"}

# 		return context




