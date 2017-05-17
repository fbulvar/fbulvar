import os
gettext = lambda s: s
DATA_DIR = os.path.dirname(os.path.dirname(__file__))
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ROOT_URLCONF = 'fbulvar.urls'
# WSGI_APPLICATION = 'fbulvar.wsgi.application'

LANGUAGE_CODE = 'ru'

TIME_ZONE = 'Europe/Kiev'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale'),
]

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(DATA_DIR, 'media')
STATIC_ROOT = os.path.join(DATA_DIR, 'static')

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'fbulvar', 'static'),
)
SITE_ID = 1


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'fbulvar', 'templates'),],
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
    'django.contrib.messages.context_processors.messages',
    'django.template.context_processors.i18n',
    'django.template.context_processors.debug',
    'django.template.context_processors.request',
    'django.template.context_processors.media',
    'django.template.context_processors.csrf',
    'django.template.context_processors.tz',
    'sekizai.context_processors.sekizai',
    'django.template.context_processors.static',
    'cms.context_processors.cms_settings'
            ],
            'loaders': [
                'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    'django.template.loaders.eggs.Loader'
            ],
        },
    },
]


MIDDLEWARE = (
    'cms.middleware.utils.ApphookReloadMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware',
)

INSTALLED_APPS = (
    'modeltranslation',
    'djangocms_admin_style',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.admin',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'django.contrib.staticfiles',
    'django.contrib.messages',
    'cms',
    'menus',
    'sekizai',
    'treebeard',
    'djangocms_text_ckeditor',
    'filer',
    'easy_thumbnails',
    'djangocms_column',
    'djangocms_link',
    'cmsplugin_filer_file',
    'cmsplugin_filer_folder',
    'cmsplugin_filer_image',
    'cmsplugin_filer_utils',
    'djangocms_googlemap',
    'djangocms_video',

    'ckeditor',
    'ckeditor_uploader',
    'aldryn_bootstrap3',
    'aldryn_style',
    'djangocms_forms',

    'home',
    'collection',
    'contacts',
    'news',
    'fbulvar'
)

LANGUAGES = (
    ('ru', gettext('ru')),
    ('uk', gettext('uk')),
    ('en', gettext('en')),
)
# MODELTRANSLATION_DEFAULT_LANGUAGE = 'ru'         # по замовчування така ж як і перша в LANGUAGES
# MODELTRANSLATION_LANGUAGES = ('ru', 'uk', 'en')  # по замовчування такі ж як і в LANGUAGES
# MODELTRANSLATION_PREPOPULATE_LANGUAGE = 'ru'       # версія мови для slug


CMS_LANGUAGES = {
    1: [
        {
            'public': True,
            'hide_untranslated': False,
            'name': gettext('ru'),
            'code': 'ru',
            'redirect_on_fallback': True,
        },
        {
            'public': True,
            'hide_untranslated': False,
            'name': gettext('uk'),
            'code': 'uk',
            'redirect_on_fallback': True,
        },
        {
            'public': True,
            'hide_untranslated': False,
            'name': gettext('en'),
            'code': 'en',
            'redirect_on_fallback': True,
        },
    ],
    'default': {
        'public': True,
        'hide_untranslated': False,
        'redirect_on_fallback': True,
    },
}

CMS_TEMPLATES = (
    ('home.html', 'HomePage'),
    ('about.html', 'AboutPage'),
    ('news.html', 'NewsPage'),
    ('vinogradniki.html', 'VinogradnikiPage'),
    ('collection_wine.html', 'CollectionWinePage'),
    ('advantages.html', 'AdvantagesPage'),
    ('technology.html', 'TechnologyPage'),
    ('boutiques.html', 'BoutiquesPage'),
    ('contacts.html', 'ContactsPage'),
)

CMS_PERMISSION = True

CMS_PLACEHOLDER_CONF = {}

CKEDITOR_UPLOAD_PATH = 'uploads/' # Django CKEditor

DJANGOCMS_FORMS_WIDGET_CSS_CLASSES = {'__all__': ('form-control', ) }
DJANGOCMS_FORMS_TEMPLATES = (
    ('djangocms_forms/form_template/default.html', 'Default'),
    ('contactform.html', 'Contactform'),
)

MIGRATION_MODULES = {
    
}

THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters'
)
THUMBNAIL_QUALITY = 85

try:
    from .local_settings import *
except ImportError:
    pass

if DEBUG:
    # debug_toolbar settings
    INTERNAL_IPS = ('127.0.0.1',)
    MIDDLEWARE += ('debug_toolbar.middleware.DebugToolbarMiddleware',)
    INSTALLED_APPS += ('debug_toolbar',)
    DEBUG_TOOLBAR_PANELS = [
        'debug_toolbar.panels.versions.VersionsPanel',
        'debug_toolbar.panels.timer.TimerPanel',
        'debug_toolbar.panels.settings.SettingsPanel',
        'debug_toolbar.panels.headers.HeadersPanel',
        'debug_toolbar.panels.request.RequestPanel',
        'debug_toolbar.panels.sql.SQLPanel',
        'debug_toolbar.panels.staticfiles.StaticFilesPanel',
        'debug_toolbar.panels.templates.TemplatesPanel',
        'debug_toolbar.panels.cache.CachePanel',
        'debug_toolbar.panels.signals.SignalsPanel',
        'debug_toolbar.panels.logging.LoggingPanel',
        'debug_toolbar.panels.redirects.RedirectsPanel',
    ]
    DEBUG_TOOLBAR_CONFIG = {'INTERCEPT_REDIRECTS': False,}

