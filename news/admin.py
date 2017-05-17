from django.contrib import admin
from news.models import News, CategoryNews, NewsInfo
from modeltranslation.admin import TranslationAdmin, TabbedTranslationAdmin


class NewsInfoAdmin(TranslationAdmin):
	pass


class CategoryNewsAdmin(TranslationAdmin):
	list_display = ('name', 'publish')
	list_filter = ('publish',)
	prepopulated_fields = {'slug': ('name',)}


class NewsAdmin(TabbedTranslationAdmin):
	list_display = ('title', 'counter', 'category', 'publish', 'publishing_date')
	list_filter = ('category', 'publish')
	prepopulated_fields = {'slug': ('title',)}
	# ordering = ('publishing_date',)
	search_fields = ['title']


admin.site.register(NewsInfo, NewsInfoAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(CategoryNews, CategoryNewsAdmin)
