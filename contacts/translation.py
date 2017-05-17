from modeltranslation.translator import translator, TranslationOptions
from .models import Contact, Map, ContactInfo


class ContactInfoTranslationOptions(TranslationOptions):
	fields = ('title_form', 'description', 'title_map')


class ContactTranslationOptions(TranslationOptions):
	fields = ('name', 'value')


class MapTranslationOptions(TranslationOptions):
	fields = ('name',)


translator.register(ContactInfo, ContactInfoTranslationOptions)
translator.register(Contact, ContactTranslationOptions)
translator.register(Map, MapTranslationOptions)