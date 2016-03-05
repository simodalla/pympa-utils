# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.timezone import now

from .managers import PublishedManager


class Published(models.Model):
    published_from = models.DateTimeField(_('published from'), default=now)
    published_to = models.DateTimeField(_('published from'), blank=True,
                                        null=True)

    objects = models.Manager()
    published = PublishedManager()

    class Meta:
        abstract = True
