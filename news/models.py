from django.db import models
from django.core.urlresolvers import reverse
from django.core.exceptions import ValidationError # validate_image
from django.utils.translation import ugettext_lazy as _
from cms.models import CMSPlugin
from ckeditor_uploader.fields import RichTextUploadingField


class NewsInfo(models.Model):
	title = models.CharField(_('Главный заголовок раздела'), max_length=64)
	description = models.CharField(_('Подзаголовок раздела'), max_length=512, blank=True, null=True)

	def __str__(self):
		return 'Заголовок раздела'

	class Meta:
		verbose_name = _('Заголовок раздела')
		verbose_name_plural = _('Заголовок раздела')


class CategoryNews(models.Model):
	name = models.CharField(_('Название категории'), max_length=64)
	slug = models.SlugField(_('URL'), max_length=90, db_index=True, unique=True,
		help_text=_('Cсылка для категории. Формируется автоматически. Не изменять'))
	publish = models.BooleanField(default=True, verbose_name='Опубликовано', 
		help_text=_('Категории желательно не удалять. Просто снимите отметку Опубликовано'))

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = _('Категория')
		verbose_name_plural = _('Категории')


class News(models.Model):
	def validate_image(fieldfile_obj):
		filesize = fieldfile_obj.file.size
		megabyte_limit = 0.5
		if filesize > megabyte_limit*1024*1024:
			raise ValidationError("Максимально допустимый размер %s MB" % str(megabyte_limit))

	title = models.CharField(_('Заглавие'), max_length=128)
	slug = models.SlugField(_('URL'), max_length=96, db_index=True, unique=True,
		help_text=_('Cсылка на новость. Формируется автоматически. Не изменять'))
	h1 = models.CharField(_('H1'), max_length=256, blank=True, null=True)
	meta_description = models.CharField(_('Meta description'), max_length=256, blank=True, null=True)
	text = RichTextUploadingField(_('Текст Новости'), blank=True, null=True)
	category = models.ForeignKey(CategoryNews, related_name='news_category', default='id=1')
	image = models.ImageField(_('Фото новости'), upload_to='news_fotos', blank=True, null=True, validators=[validate_image], 
		help_text=_('Допускаются изображения разрешением больше (ш*в) 600px*350px и размером меньше 0,5 Мб')) # /%Y/%m/%d
	# image = models.ImageField(_('Фото новости'), upload_to='news_fotos', blank=True, null=True)
	publishing_date = models.DateTimeField(_('Дата публикации'))
	publish = models.BooleanField(default=True, verbose_name='Опубликовано', 
		help_text=_('Для отображения на сайте, новость должна быть опубликована'))
	counter = models.IntegerField(_('Колличество просмотров'), default=0)

	def __str__(self):
		return self.title

	class Meta:
		verbose_name = _('Новость')
		verbose_name_plural = _('Новости')
		ordering = ['-publishing_date']

	def get_absolute_url(self):
		return reverse('news:news-details', kwargs={'slug': self.slug})