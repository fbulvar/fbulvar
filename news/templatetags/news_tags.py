from django import template
from news.models import News, CategoryNews


register = template.Library()


@register.inclusion_tag('news/_home_news_list.html')
def home_news_list():
    return {'home_news': News.objects.filter(publish=True).filter(category__publish=True).order_by('-publishing_date')[:2]}