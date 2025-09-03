#!/usr/bin/env sh
set -e

# Run DB migrations
python manage.py migrate

# Idempotent superuser creation
python manage.py shell -c "
from django.contrib.auth import get_user_model
import os
User = get_user_model()
u = os.environ.get('DJANGO_SUPERUSER_USERNAME')
e = os.environ.get('DJANGO_SUPERUSER_EMAIL')
p = os.environ.get('DJANGO_SUPERUSER_PASSWORD')
if u and e and p:
    if not User.objects.filter(username=u).exists():
        User.objects.create_superuser(username=u, email=e, password=p)
        print('[entrypoint] Created superuser', u)
    else:
        print('[entrypoint] Superuser already exists:', u)
else:
    print('[entrypoint] Missing DJANGO_SUPERUSER_* env vars; skipping')
"

# Run dev server
exec python manage.py runserver 0.0.0.0:8000
