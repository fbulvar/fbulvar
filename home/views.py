from django.views.generic import ListView, DetailView
from .models import Home


# class WineListView(ListView):
# 	# model = Wine
# 	queryset = CategoryWine.objects.all().prefetch_related('category_wine').filter(publish=True).filter(category_wine__publish=True)
# 	template_name = 'collection/wine_list.html'
# 	context_object_name = 'category_wines'

	# def get_context_data(self, **kwargs):
	# 	context = super(WineListView, self).get_context_data(**kwargs)
	# 	# context["category_wines"] = CategoryWine.objects.filter(publish=True) #.select_related('wine') #.filter(building_function_id=context['building'].id)
	# 	context["category_wines"] = Wine.objects.select_related('category').filter(publish=True) #.select_related('wine') #.filter(building_function_id=context['building'].id)
	# 	# context["category_wines"] = Wine.objects.all().prefetch_related('category').filter(publish=True) #.select_related('wine') #.filter(building_function_id=context['building'].id)
	# 	# prefetch_related Pizza.objects.all().prefetch_related('toppings')
	# 	return context


# class HomeDetailView(DetailView):
# 	model = Home
# 	# queryset = Home.objects.all()[:0]
# 	template_name = 'fbulvar/templates/home.html'

#     def get_context_data(self, **kwargs):
#         context = super(HomeDetailView, self).get_context_data(**kwargs)
#         context['home'] = Home.objects.all()
#         return context