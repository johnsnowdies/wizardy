command = '/usr/bin/gunicorn'
pythonpath = '/app/apps'
bind = "0.0.0.0:80"
workers = 3
limit_request_fields = 32000
limit_request_field_size = 0
raw_env = 'DJANGO_SETTINGS_MODULE=apps.wizardy.settings'