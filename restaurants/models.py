from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import models
from django.db.models.signals import pre_save,post_save
# Create your models here.
 
from .utils import unique_slug_generator

User=settings.AUTH_USER_MODEL


class RestaurantLocation(models.Model):
	owner  		=models.ForeignKey(User)#klassinstance.model_set.all() 
	name		=models.CharField(max_length=120)
	location	=models.CharField(max_length=120,null=True,blank=True)
	category	=models.CharField(max_length=120,null=True,blank=True)
	timestamp	=models.DateTimeField(auto_now_add=True)
	updated		=models.DateTimeField(auto_now=True)
	slug		=models.SlugField(null=True,blank=True)

	def get_absolute_url(self):
	 	return reverse('restaurants:detail',kwargs={'slug':self.slug})

	def __str__(self):
		return self.name

	@property
	def title(self):
	    return self.name
	
def rl_pre_save_reciever(sender,instance,*args,**kwargs):
	print('saving..')
	print(instance.timestamp)
	if not instance.slug:

		instance.slug=unique_slug_generator(instance)



# def rl_post_save_reciever(sender,instance,*args,**kwargs):
# 	print('saved.')
# 	print(instance.timestamp)
# 	instance.save()
	

pre_save.connect(rl_pre_save_reciever,sender=RestaurantLocation)

# post_save.connect(rl_post_save_reciever,sender=RestaurantLocation)


