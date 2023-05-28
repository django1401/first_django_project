from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import *
from blog.models import Post
from .forms import NewsLetterForm, ContactUsForm

def home(req):
    if req.method == 'GET':
        last_six_posts = Post.objects.filter(status=True)[:6]
        cheap = CheapPackage.objects.all()
        luxuray = LuxuryPackage.objects.all()
        camp = CampingPackage.objects.all()

        context = {'cheap':cheap,'luxuray':luxuray,'camp':camp, 'last':last_six_posts}
        return render(req,"home/index.html",context=context)
    elif req.method == 'POST':
        form = NewsLetterForm(req.POST)
        if form.is_valid():
            form.save()   
        return redirect('/')

def about(req):
    return render(req,"home/about.html")

def contact(req):
    if req.method == 'GET':
        return render(req,"home/contact.html")
    
    elif req.method == 'POST':
        form = ContactUsForm(req.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(req.path_info)
        









    


