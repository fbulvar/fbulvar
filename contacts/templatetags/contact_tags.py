from django import template
from contacts.models import Contact, Map, ContactInfo


register = template.Library()


@register.inclusion_tag('contacts/_contact_form_title.html')
def contact_form_title():
	return {'contact_form_title': ContactInfo.objects.filter(id=1)}


@register.inclusion_tag('contacts/_contact_map_title.html')
def contact_map_title():
	return {'contact_map_title': ContactInfo.objects.filter(id=1)}


@register.inclusion_tag('contacts/_contacts.html')
def contacts():
	return {'contacts': Contact.objects.filter(pub_contact=True)}


@register.inclusion_tag('contacts/_contacts_footer.html')
def contacts_footer():
	return {'contacts_footer': Contact.objects.filter(pub_footer=True)}


@register.inclusion_tag('contacts/_contact_map.html')
def contact_map():
	return {'contact_map': Map.objects.filter(publish=True)}