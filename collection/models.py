from django.db import models
from django.core.urlresolvers import reverse
from django.core.exceptions import ValidationError # validate_image
from django.utils.translation import ugettext_lazy as _
from cms.models import CMSPlugin
from ckeditor_uploader.fields import RichTextUploadingField


class CategoryWineInfo(models.Model):
	title = models.CharField(_('Главный заголовок раздела'), max_length=64)
	description = models.CharField(_('Подзаголовок раздела'), max_length=512, blank=True, null=True)

	def __str__(self):
		return 'Заголовок раздела'

	class Meta:
		verbose_name = _('Заголовок раздела')
		verbose_name_plural = _('Заголовок раздела')


class CategoryWine(models.Model):
	name = models.CharField(_('Название категории'), max_length=64)
	slug = models.SlugField(_('URL'), max_length=90, db_index=True, unique=True,
		help_text=_('Cсылка для категории. Формируется автоматически. Не изменять'))
	meta_description = models.CharField(_('Meta description'), max_length=512, blank=True, null=True)
	publish = models.BooleanField(default=True, verbose_name='Опубликовано', 
		help_text=_('Чтобы категорию отображать на сайте, она должна быть опубликована'))
	ordering = models.IntegerField(_('Очередность вывода'), default=99) 

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = _('Категория вин')
		verbose_name_plural = _('Категории вин')
		ordering = ['ordering']


class Wine(models.Model):
	def validate_image(fieldfile_obj):
		filesize = fieldfile_obj.file.size
		megabyte_limit = 1.0
		if filesize > megabyte_limit*1024*1024:
			raise ValidationError("Максимально допустимый размер %s MB" % str(megabyte_limit))

	title = models.CharField(_('Название (title)'), max_length=256)
	slug = models.SlugField(_('URL'), max_length=96, db_index=True, unique=True,
		help_text=_('Cсылка на продукцию. Формируется автоматически. Не изменять'))
	h1 = models.CharField(_('H1'), max_length=256, blank=True, null=True)
	meta_description = models.CharField(_('Meta description'), max_length=512, blank=True, null=True)
	text = RichTextUploadingField(_('Описание'), blank=True)
	category = models.ForeignKey(CategoryWine, related_name='category_wine')
	image = models.ImageField(_('Фото продукции'), upload_to='collection_fotos', blank=True, null=True, validators=[validate_image], 
		help_text=_('Допускаются изображения разрешением больше 700px высотой и размером меньше 1,0 Мб'))
	publish = models.BooleanField(default=True, verbose_name='Опубликовано', 
		help_text=_('Для отображения на сайте, продукция должна быть опубликована'))
	ordering = models.IntegerField(_('Очередность вывода'), default=99) 

	def __str__(self):
		return self.title

	class Meta:
		verbose_name = _('Продукция')
		verbose_name_plural = _('Продукция')
		ordering = ['ordering']

	def get_absolute_url(self):
		return reverse('collection:collection-details', kwargs={'slug': self.slug})

# class WineFooterPlugin(CMSPlugin):

# 	def get_article_title(self):
# 		return Wine.objects.filter(publish=True).filter(category=1).order_by('?')[:1]