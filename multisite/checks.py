# -*- coding: utf-8 -*

from django.conf import settings
from django.core.checks import Error

from .threadlocals import SiteID


def check_site_id(app_configs, **kwargs):
    if (
        hasattr(settings, 'SITE_ID') and
        not isinstance(settings.SITE_ID, (type(None), int, SiteID))
    ):
        return [
            Error('The SITE_ID setting must be an integer', id='sites.E101'),
        ]
    return []