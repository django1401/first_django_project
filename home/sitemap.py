from django.urls import reverse
from django.contrib import sitemaps




class StaticSiteMaps(sitemaps.Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items(self):
        return ['home:home', 'home:about', 'home:contact', 'blog:blog_home']
    
    def location(self, item):
        return reverse(item)


