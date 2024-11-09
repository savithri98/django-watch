from django.contrib import admin
from .models import Watches,WatchesUploads,Wishlist,Cart,CartItem,WatchReview
# Register your models here.
admin.site.register(Watches)

#wishlist part to display data in admin page
#class WishlistAdmin(admin.ModelAdmin):
#   list_display=('user','products')   
#   list_filter=('user','products') 
admin.site.register(Wishlist)

#cart part to display data in admin page
#class CartAdmin(admin.ModelAdmin):
 #   list_display=('user','products')   
 #   list_filter=('user','products')
admin.site.register(Cart)
admin.site.register(CartItem)

#WatchesUploads part to display data in admin page
class WatchesUploadsAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'price', 'description', 'image')
    list_filter = ('name', 'price')
    search_fields = ['name', 'description']
admin.site.register(WatchesUploads, WatchesUploadsAdmin)

#watchreview part to display data in admin page
class WatchReviewAdmin(admin.ModelAdmin):
    list_display=('user','product','review_text','rating')   
    list_filter=('rating','product') 
admin.site.register(WatchReview,WatchReviewAdmin)