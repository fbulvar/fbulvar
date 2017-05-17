from modeltranslation.translator import translator, TranslationOptions
from .models import CategoryWine, Wine, CategoryWineInfo


class CategoryWineInfoTranslationOptions(TranslationOptions):
	fields = ('title', 'description')


class CategoryWineTranslationOptions(TranslationOptions):
	fields = ('name', 'slug', 'meta_description')
	empty_values = {'slug': None} 


class WineTranslationOptions(TranslationOptions):
	fields = ('title', 'slug', 'h1', 'meta_description', 'text')
	empty_values = {'slug': None} 


translator.register(CategoryWineInfo, CategoryWineInfoTranslationOptions)
translator.register(CategoryWine, CategoryWineTranslationOptions)
translator.register(Wine, WineTranslationOptions)