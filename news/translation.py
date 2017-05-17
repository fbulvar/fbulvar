from modeltranslation.translator import translator, TranslationOptions
from .models import News, CategoryNews, NewsInfo


class NewsInfoTranslationOptions(TranslationOptions):
	fields = ('title', 'description')


class CategoryNewsTranslationOptions(TranslationOptions):
	fields = ('name', 'slug')
	empty_values = {'slug': None} # на випадок, коли в базі обнуляться slug, вони стануть None щоб не порушити унікальність 


class NewsTranslationOptions(TranslationOptions):
	fields = ('title', 'slug', 'h1', 'meta_description', 'text')
	empty_values = {'slug': None} 


translator.register(NewsInfo, NewsInfoTranslationOptions)
translator.register(CategoryNews, CategoryNewsTranslationOptions)
translator.register(News, NewsTranslationOptions)