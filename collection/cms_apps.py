from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _


class CollectionApphook(CMSApp):
    app_name = 'collection'
    name = _('Collection Application')

    def get_urls(self, page=None, language=None, **kwargs):
        return ['collection.urls']


apphook_pool.register(CollectionApphook)