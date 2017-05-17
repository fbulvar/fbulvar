from django.views.generic import ListView, DetailView
from news.models import News, NewsInfo


class NewsListView(ListView):
	# model = News
	queryset = News.objects.filter(publish=True).filter(category__publish=True)
	template_name = 'news/news_list.html'
	context_object_name = 'news'
	paginate_by = 10

	def get_context_data(self, **kwargs):
		context = super(NewsListView, self).get_context_data(**kwargs)
		context["news_title"] = NewsInfo.objects.filter(id=1)
		return context


class NewsDetailView(DetailView):
	model = News
	template_name = 'news/news_detail.html'

	# counter view news
	def get_object(self):
		object = super(NewsDetailView, self).get_object()
		object.counter += 1
		object.save(update_fields=['counter'])
		return object