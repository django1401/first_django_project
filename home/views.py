from django.shortcuts import render
from .models import *
from blog.models import Post

def home(req):
    last_six_posts = Post.objects.filter(status=True)[:6]
    cheap = CheapPackage.objects.all()
    luxuray = LuxuryPackage.objects.all()
    camp = CampingPackage.objects.all()

    context = {'cheap':cheap,'luxuray':luxuray,'camp':camp, 'last':last_six_posts}
    return render(req,"home/index.html",context=context)

def about(req):
    return render(req,"home/about.html")

def contact(req):
    return render(req,"home/contact.html")






    


