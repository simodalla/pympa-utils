from django.db.models import Q, Manager
from django.utils.timezone import now


class PublishedManager(Manager):

    def get_queryset(self):
        qs = super(PublishedManager, self).get_queryset().filter(
            Q(published_from__lte=now()),
            Q(published_to__isnull=True) | Q(published_to__gte=now()),
        )
        return qs
