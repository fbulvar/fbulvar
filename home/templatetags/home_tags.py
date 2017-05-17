from django import template
from home.models import Home


register = template.Library()


@register.inclusion_tag('home/_home_slider.html')
def home_slider():
	return {'home_slider': Home.objects.filter(id=1)}

@register.inclusion_tag('home/_home_customer_adv.html')
def home_customer_adv():
	return {'home_customer_adv': Home.objects.all().prefetch_related('customer_adv_item').filter(id=1)}

@register.inclusion_tag('home/_home_facts.html')
def home_facts():
	return {'home_facts': Home.objects.all().prefetch_related('facts').filter(id=1)}

@register.inclusion_tag('home/_home_news.html')
def home_news():
	return {'home_news': Home.objects.filter(id=1)}