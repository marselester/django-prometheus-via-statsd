# [Instrumenting Django with Prometheus and StatsD](http://marselester.com/django-prometheus-via-statsd.html)

This repository is an example setup of Django application
that exposes its metrics for Prometheus monitoring toolkit using StatsD and statsd_exporter.
The application and Prometheus run on Kubernetes cluster.

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
