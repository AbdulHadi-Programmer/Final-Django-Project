ALLOWED_HOSTS = []
ALLOWED_HOSTS = ['127.0.0.1', 'localhost']
DEBUG = False

ALLOWED_HOSTS = ['"GET /expenses/ HTTP/1.1" 500 59', '127.0.0.1', 'localhost']


INSTALLED_APPS = [
    # Other apps...
    'expenses',
]
DEBUG = False

from django.shortcuts import render
from django.http import HttpResponseServerError

def some_view(request):
    try:
        # Your code logic here
        pass
    except Exception as e:
        return HttpResponseServerError("An error occurred: " + str(e))
