# -*- coding: utf-8 -*

from django.apps import AppConfig
from django.core.checks import register, Tags

from .checks import check_site_id


# https://docs.djangoproject.com/en/3.2/topics/checks/
class MultiSiteConfig(AppConfig):
    name = 'multisite'

    def ready(self):
        super(MultiSiteConfig, self).ready()
        register(check_site_id, Tags.sites)
