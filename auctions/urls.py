from django.urls import path
from django.conf.urls import handler404

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("categories", views.categories, name="categories"),
    path("category/<int:category_id>", views.category, name="category"),
    path("watchlist", views.watchlist, name="watchlist"),
    path("create", views.create_list, name="create_list"),
    path("product/<int:product_id>", views.product, name="product"),
    path("bid", views.bid, name="bid"),
    path("close", views.close, name="close"),
    path("profile", views.profile, name="profile"),
    path("profile/bids", views.userBids, name="userBids"),
    path("profile/wins", views.userwins, name="userwins"),
    path("profile/products", views.userproducts, name="userproducts"),
    path("comment", views.comment, name="comment"),
    path("watchlistChange", views.watchlistChange, name="watchlistChange"),


]
