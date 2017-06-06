# Instrumenting Django with Prometheus and StatsD

Get the Olympus application running to emit StatsD metrics.

```sh
$ git clone https://github.com/marselester/django-prometheus-via-statsd.git
$ cd ./django-prometheus-via-statsd/olympus-app
$ virtualenv venv
$ source ./venv/bin/activate
$ pip install -r requirements.txt
$ python manage.py runserver
$ curl http://localhost:8000/hello
Hello, World!
```
