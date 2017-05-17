from django.views.generic import ListView, DetailView
from django.db.models import Prefetch
from collection.models import Wine, CategoryWine, CategoryWineInfo


class WineListView(ListView):
	# model = Wine
	queryset = CategoryWine.objects.filter(publish=True).prefetch_related(
		Prefetch('category_wine', queryset=Wine.objects.filter(publish=True), to_attr='some_wines'))
	template_name = 'collection/wine_list.html'
	context_object_name = 'category_wines'

	def get_context_data(self, **kwargs):
		context = super(WineListView, self).get_context_data(**kwargs)
		context["collection_wines_title"] = CategoryWineInfo.objects.filter(id=1)
		return context


class WineDetailView(DetailView):
	model = Wine
	template_name = 'collection/wine_detail.html'