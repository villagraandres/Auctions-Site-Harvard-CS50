from django.contrib import admin
from . models import User,List,Category,Watchlist,Bid,Comment
# Register your models here.





def delete_selected(modeladmin, request, queryset):
    queryset.delete()
delete_selected.short_description = "Delete selected"

class ListAdmin(admin.ModelAdmin):

    list_display=("id","title");
    actions = [delete_selected]

class BidAdmin(admin.ModelAdmin):
    actions = [delete_selected]

admin.site.register(User);
admin.site.register(Category);
admin.site.register(List,ListAdmin);
admin.site.register(Watchlist);
admin.site.register(Bid,BidAdmin);
admin.site.register(Comment);