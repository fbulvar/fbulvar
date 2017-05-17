from django import template
from collection.models import Wine, CategoryWine


register = template.Library()


@register.inclusion_tag('collection/_collection_list.html')
def collection_list_01():
	return {'collection_wines': Wine.objects.filter(publish=True).filter(category=1)}

@register.inclusion_tag('collection/_collection_list.html')
def collection_list_02():
	return {'collection_wines': Wine.objects.filter(publish=True).filter(category=2)}

@register.inclusion_tag('collection/_collection_list.html')
def collection_list_03():
	return {'collection_wines': Wine.objects.filter(publish=True).filter(category=3)}