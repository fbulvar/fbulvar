from django.contrib import admin
from collection.models import Wine, CategoryWine, CategoryWineInfo
from modeltranslation.admin import TranslationAdmin, TabbedTranslationAdmin


class CategoryWineInfoAdmin(TranslationAdmin):
	pass


class CategoryWineAdmin(TranslationAdmin):
	list_display = ('name', 'publish', 'ordering')
	list_editable = ('ordering',)
	list_filter = ('publish',)
	prepopulated_fields = {'slug': ('name',)}


class WineAdmin(TabbedTranslationAdmin):
	list_display = ('title', 'category', 'ordering', 'publish')
	list_filter = ('category', 'publish')
	prepopulated_fields = {'slug': ('title',)}
	list_editable = ('ordering',)
	ordering = ('category', 'ordering')
	search_fields = ['title']


admin.site.register(CategoryWineInfo, CategoryWineInfoAdmin)
admin.site.register(CategoryWine, CategoryWineAdmin)
admin.site.register(Wine, WineAdmin)