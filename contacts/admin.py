from django.contrib import admin
from .models import Contact, Map, ContactInfo
from modeltranslation.admin import TranslationAdmin, TabbedTranslationAdmin


class ContactInfoAdmin(TranslationAdmin):
	pass


class ContactAdmin(TranslationAdmin):
	list_display = ('name', 'value', 'icon', 'pub_contact', 'pub_footer', 'ordering')
	list_filter = ('pub_contact', 'pub_footer')
	list_editable = ('pub_contact', 'pub_footer', 'ordering')
	ordering = ('ordering', 'name')


class MapAdmin(TranslationAdmin):
	list_display = ('name', 'lat', 'lng', 'scale', 'publish')
	list_editable = ('lat', 'lng', 'scale')


admin.site.register(ContactInfo, ContactInfoAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Map, MapAdmin)