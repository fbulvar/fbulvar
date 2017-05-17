from django.db import models
from django.utils.translation import ugettext_lazy as _
from ckeditor_uploader.fields import RichTextUploadingField


class Home(models.Model):
	title = models.CharField(_('Заглавие'), max_length=64, blank=True, null=True)
	h1 = models.CharField(_('H1'), max_length=64, help_text=_('Самый важный текст (для SEO)'))
	button  = models.CharField(_('Надпись на кнопке'), max_length=32)
	button_url  = models.CharField(_('URL на страницу'), max_length=64, help_text=_('Указать URL для каждой языковой версии'))
	# image = models.ImageField(_('Картинка-заставка'), upload_to='page')

	customer_adv_title = models.CharField(_('Преимущества для клиентов - Заглавие'), max_length=64)
	customer_adv_desc = models.CharField(_('Преимущества для клиентов - Подзаголовок'), max_length=256, blank=True, null=True)
	customer_adv_text = RichTextUploadingField(_('Преимущества для клиентов - Текст'), blank=True)

	facts_title = models.CharField(_('Факты о нас - Заглавие'), max_length=64)
	facts_desc = models.CharField(_('Факты о нас - Подзаголовок'), max_length=256, blank=True, null=True)

	news_title = models.CharField(_('Новости - Заглавие'), max_length=64)
	news_desc = models.CharField(_('Новости - Подзаголовок'), max_length=256, blank=True, null=True)

	def __str__(self):
		return 'Главная страница'

	class Meta:
		verbose_name = _('Главная страница')
		verbose_name_plural = _('Главная страница')


class CustomerAdvItem(models.Model):
	image = models.ImageField(_('Картинка преимущества'), upload_to='page')
	title = models.CharField(_('Заглавие преимущества'), max_length=32, blank=True, null=True)
	description = models.CharField(_('Краткое описание преимущества'), max_length=64, blank=True, null=True)
	publish = models.BooleanField(_('Опубликовано'), default=True)
	ordering = models.PositiveSmallIntegerField(_('Порядок показа'), default=99)
	page = models.ForeignKey(Home, related_name='customer_adv_item')

	def __str__(self):
		return self.title

	class Meta:
		verbose_name = _('Преимущество для клиентов')
		verbose_name_plural = _('Преимущества для клиентов')
		ordering = ['ordering']


class FactItem(models.Model):
	icon = models.CharField(_('Иконка'), max_length=32, blank=True, null=True,
		help_text=_('Например fa-history  Примеры иконок http://fontawesome.io/icons/'))
	value = models.CharField(_('Значение'), max_length=8)
	value_end = models.CharField(_('Единица измерения'), max_length=8, blank=True, null=True)
	description = models.CharField(_('Краткий подзаголовок'), max_length=36, blank=True, null=True)
	publish = models.BooleanField(_('Опубликовано'), default=True)
	ordering = models.PositiveSmallIntegerField(_('Порядок показа'), default=99)
	page = models.ForeignKey(Home, related_name='facts')

	def __str__(self):
		return self.description

	class Meta:
		verbose_name = _('Факт о нас')
		verbose_name_plural = _('Факты о нас')
		ordering = ['ordering']