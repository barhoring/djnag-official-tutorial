from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, Bar. You're at the polls index.")