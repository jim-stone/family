from django.contrib.auth.models import User


def cre_sup():
    superusers = User.objects.filter(is_superuser=True)
    if not superusers:
        User.objects.create_superuser(
            username='kuba', email=None, password='kubakuba'
        )
