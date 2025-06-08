release: python manage.py collectstatic --noinput
web: gunicorn pd_proj.wsgi:application --log-file -
