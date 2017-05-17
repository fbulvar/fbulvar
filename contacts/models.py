from django.db import models
from django.utils.translation import ugettext_lazy as _


class ContactInfo(models.Model):
	title_form = models.CharField(_('Заголовок контактной формы'), max_length=64)
	description = models.CharField(_('Подзаголовок контактной формы'), max_length=256, blank=True, null=True)
	title_map = models.CharField(_('Заголовок контактов и карты'), max_length=64)

	def __str__(self):
		return 'Заголовки раздела'

	class Meta:
		verbose_name = _('Заголовок раздела')
		verbose_name_plural = _('Заголовки раздела')


class Contact(models.Model):
	name = models.CharField(_('Название'), max_length=64, help_text=_('Например: Телефон'))
	icon = models.CharField(_('Иконка для контакта'), max_length=64, 
		help_text=_('Например fa-phone  Примеры иконок http://fontawesome.io/icons/'))
	value = models.CharField(_('Контакт'), max_length=64, help_text=_('Например: +38 (048) 722-17-74'))
	pub_contact = models.BooleanField(default=True, verbose_name='Опубликовать в контактах', 
		help_text=_('Опубликовать на странице контактов'))
	pub_footer = models.BooleanField(default=True, verbose_name='Опубликовать в footer', 
		help_text=_('Опубликовать в footer (внизу страницы)'))
	ordering = models.IntegerField(_('Очередность вывода'), default=99) 

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = _('Контакт')
		verbose_name_plural = _('Контакты')
		ordering = ['ordering']


class Map(models.Model):
	name = models.CharField(_('Название карты'), max_length=64, help_text=_('Например: Главный офис'))
	lat = models.CharField(_('Latitude'), help_text=_('Например 48.8569878'), max_length=12, blank=True, null=True)
	lng = models.CharField(_('Longitude'), help_text=_('Например 2.2956073'), max_length=12, blank=True, null=True)
	scale = models.PositiveSmallIntegerField(_('Масштабирование карты'), default=12)
	publish = models.BooleanField(default=True, verbose_name='Опубликовать карту')

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = _('Карта')
		verbose_name_plural = _('Карты')
		ordering = ['name']