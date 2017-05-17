from django.contrib import admin
from .models import Home, CustomerAdvItem, FactItem
from modeltranslation.admin import TranslationAdmin, TabbedTranslationAdmin, TranslationTabularInline


class CustomerAdvItemInline(TranslationTabularInline):
	model = CustomerAdvItem
	extra = 0


class FactItemInline(TranslationTabularInline):
	model = FactItem
	extra = 0


class HomeAdmin(TabbedTranslationAdmin):
	# list_display = ('h1',)
	inlines = [CustomerAdvItemInline, FactItemInline]


admin.site.register(Home, HomeAdmin)