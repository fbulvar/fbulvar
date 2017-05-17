from modeltranslation.translator import translator, TranslationOptions
from .models import Home, CustomerAdvItem, FactItem


class HomeTranslationOptions(TranslationOptions):
	fields = ('title', 'h1', 'button', 'button_url', 'customer_adv_title', 'customer_adv_desc', 'customer_adv_text', 'facts_title', 'facts_desc', 'news_title', 'news_desc')


class CustomerAdvItemTranslationOptions(TranslationOptions):
	fields = ('title', 'description')


class FactItemTranslationOptions(TranslationOptions):
	fields = ('value_end', 'description')


translator.register(Home, HomeTranslationOptions)
translator.register(CustomerAdvItem, CustomerAdvItemTranslationOptions)
translator.register(FactItem, FactItemTranslationOptions)