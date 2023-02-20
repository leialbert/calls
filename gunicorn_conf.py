bind = '127.0.0.1:8000'
backlog = 2048
workers = 1
worker_class = 'sync'
worker_connections = 1000
timeout = 30
keepalive = 2
spew = False
user = None
group = None
errorlog = '/var/log/gunicorn/calls.error.log'
accesslog = '/var/log/gunicorn/calls.access.log'
loglevel = 'info'
access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"'
proc_name = 'calls'

