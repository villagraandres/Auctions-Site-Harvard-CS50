from.models import Watchlist

def watchlist_count(request):
    if request.user.is_authenticated:

         try:
               watchlist_count = Watchlist.objects.get(user=request.user).products.count()
         except Watchlist.DoesNotExist:
            return {'watchlist_count': 0}

      
        
    else:
        watchlist_count = 0
    return {'watchlist_count': watchlist_count}