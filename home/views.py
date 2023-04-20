from django.shortcuts import render

def home(req):
    return render(req,"home/index.html",context={'name':'hamid reza'})

def about(req):
    return render(req,"home/about.html")

def contact(req):
    return render(req,"home/contact.html")

def blog(req):
    return render(req,"home/blog-home.html")

def blog_single(req):
    return render(req,"home/blog-single.html")

def test(req):
    return render(req,"home/test.html")




    


