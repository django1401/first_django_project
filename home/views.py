from django.shortcuts import render

def home(req):
    return render(req,"home/index.html")


def about(req):
    return render(req,"home/about.html")



    


