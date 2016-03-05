from django.contrib.sites.models import Site

from django_auth_ldap.backend import LDAPBackend

from mezzanine.utils.sites import current_site_id
from mezzanine.core.models import SitePermission


class MezzanineLDAPBackend(LDAPBackend):

    def get_or_create_user(self, username, ldap_user):
        user, create = super(MezzanineLDAPBackend, self).get_or_create_user(
            username, ldap_user)
        if create:
            sp, _ = SitePermission.objects.get_or_create(user=user)
            try:
                sp.sites.add(Site.objects.get(pk=current_site_id()))
            except Site.DoesNotExist:
                pass
        return user, create
