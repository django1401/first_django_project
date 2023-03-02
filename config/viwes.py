from django.http import HttpResponse


def home(req):
    return HttpResponse("hello first page")

def contact(req):
    return HttpResponse("contact_Us")