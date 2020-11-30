from django.urls import reverse 
from django.contrib.sitemaps import Sitemap 


class StaticViewSitemap(Sitemap): 
    priority = 0.64
    changefreq = 'weekly' 

    def items(self): 
        return [ 
            #shop
            'shop:serviceintroduce',
            'shop:envigoods',

            #Account
            'Account:tos_seller_use',
            'Account:tos_seller_private',
            'Account:tos_user_use',
            'Account:tos_user_private',
            'Account:signupcustomer',
            'Account:signupseller',
            'Account:signup',
            'Account:login',
            'Account:customerPage',

            #order
            'order:create',
            'order:payment',
            'order:cart_needs'
    ] 

    def location(self, item): 
        return reverse(item)

