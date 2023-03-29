from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django import forms
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

from django.views.defaults import page_not_found
from .models import User,List,Category,Watchlist,Bid,Comment

class ListForm(forms.Form):
   categories=Category.objects.all();
   category_choices = [(category.id, category.name) for category in categories]
   category_choices.insert(0, ("", "Select a category"))

   title = forms.CharField()
   description=forms.CharField(widget=forms.Textarea)   
   price=forms.IntegerField()
   image = forms.URLField()
   select = forms.ChoiceField(choices=category_choices, initial="default")


class CommentForm(forms.Form):
    comment=forms.Textarea()
 

def index(request):
    articles=List.objects.exclude(closed=True).order_by('-id');

    return render(request, "auctions/index.html",{
        "articles":articles,
        "title":"Active Listings"
       
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")




def categories(request):
    categories=Category.objects.all();
    return render(request,"auctions/categories.html",{
        "categories": categories
    });

def category(request, category_id):
    try:
        category = Category.objects.get(id=category_id)
    except Category.DoesNotExist:
        return render(request, "auctions/error.html", {"message": "Category does not exist."})

    products = category.products.all().exclude(closed=True).order_by('-id');
    return render(request, "auctions/index.html", {"articles": products,"title":""})

@login_required
def watchlist(request):


    try:
      watchlist=Watchlist.objects.get(user=request.user);
    except Watchlist.DoesNotExist:
        return render(request,"auctions/watchlist.html",{"message":"There are no articles in your Watchlist "});

    products=watchlist.products.all();
      
    return render(request,"auctions/watchlist.html",{
        "articles":products
    });

@login_required
def create_list(request):
   

   if request.method=="POST":
     f= ListForm(request.POST);
     if f.is_valid():
      
        article=List(title=f.cleaned_data['title'],description=f.cleaned_data['description'],price=f.cleaned_data['price'],image=f.cleaned_data['image'],user=request.user,closed=False);
        article.save();
        category=Category.objects.get(pk=f.cleaned_data['select'])
        article.categories.add(category);
        return HttpResponseRedirect(reverse("index"))
      
     else:
            errors = f.errors
            return render(request, "auctions/create.html",{
            "form":f,
            "error":errors
        })
       
   else:
        return render(request, "auctions/create.html",{
            "form":ListForm()
        })
  

def product(request,product_id):
    try:

        product=List.objects.get(id=product_id);
        added=Watchlist.objects.filter(products=product);
        comments=Comment.objects.filter(product=product).order_by('-date');
        add='';
        if len(added)==0:
            add=True
        else:
            add=False;
        
    except List.DoesNotExist:
        return render(request, "auctions/error.html", {"message": "Product does not exist."})
    
    if product.user == request.user:
        return render(request, "auctions/product.html",{
        "admin":True,
        "article":product,
        "add":add,
        "comments":comments
        
    })
        
    return render(request, "auctions/product.html",{
        "article":product,
        "add":add,
        "comments":comments
     
    })


@login_required
def watchlistChange(request):

    product=List.objects.get(id=request.POST.get('product_id'));
    added=Watchlist.objects.filter(products=product);
    comments=Comment.objects.filter(product=product).order_by('-date');

    add='';
    if len(added)==0:
        add=True
    else:
        add=False;
    url = reverse('product', args=[product.id])
    if request.method=="POST":
        exists=Watchlist.objects.filter(user=request.user);     
        if add==True:
            #Creamos una nueva wachlist si el usuario no tiene una 
            if len(exists)==0:
                new=Watchlist(user=request.user);
                new.save();
                new.products.add(product)
                
                return redirect(url)
            else:
                #el arreglo trae valores, entonces seleccionamos su watchlist y agregamos el elemento
                current=Watchlist.objects.get(user=request.user);
                current.products.add(product);
                return redirect(url)
        else:
            #Si el producto ya esta agregado, lo eliminamos de la watchlist
            current=Watchlist.objects.get(user=request.user);
            current.products.remove(product);
            return redirect(url)


@login_required
def bid(request):
    if request.method == "POST":
        try:
            product_id = request.POST.get('product')
            bid_amount = request.POST.get('bid')
            product=List.objects.get(id=product_id);
            added=Watchlist.objects.filter(products=product);

            add=None;
            if len(added)==0:
                add=True
            else:
                add=False;

            if  product.bidsProduct.all().last() and float(bid_amount) <= product.bidsProduct.all().last().bid:
                return render(request, "auctions/product.html",{
                    "article":product,
                    "message":"Your bid must be higher than the current bid.",
                    "class":"danger",
                    "add":add
                })
            
            newBid=Bid(product=product,user=request.user,bid=float(bid_amount));
            newBid.save()
           
            return render(request, "auctions/product.html",{
                    "article":product,
                    "message":"Your bid was successfully submitted",
                    "class":"success",
                    "add":add
                })
        
        except ValueError:
            return HttpResponseRedirect(reverse('login'))
    else:
              pass;

@login_required
def close(request):
 if request.method == "POST":
        try:
            product_id = request.POST.get('product_id')
            product=List.objects.get(id=product_id);
            highest_bid = Bid.objects.filter(product=product).order_by('-bid').first()

            product.closed=True;
            product.comments.all().delete();
            product.winner=highest_bid.user
            product.save()
            return render(request, "auctions/product.html",{
                    "article":product,
                    "message":"The article has been closed",
                    "class":"success"
                })
        except ValueError:
            return HttpResponseRedirect(reverse('login'))
 else:
       pass;

@login_required
def profile(request):
    return render(request,"auctions/profile.html")


def userBids(request):
     
    product_ids = Bid.objects.filter(user=request.user).values_list('product_id', flat=True);
    products = List.objects.filter(id__in=product_ids).exclude(closed=True);
    
    return render(request,"auctions/userBids.html",{"products":products})


@login_required
def userwins(request):

    products=List.objects.filter(winner=request.user);
    return render(request,"auctions/index.html",{"articles":products,"title":"Wins"})


@login_required
def userproducts(request):
    activeArticles=List.objects.filter(user=request.user).filter(closed=False);
    closedArticles=List.objects.filter(user=request.user).filter(closed=True);
    return render(request,"auctions/userProducts.html",{"activeArticles":activeArticles,"closedArticles":closedArticles})

@login_required
def comment(request):
    
        try:
            product_id = request.POST.get('product_id')
            product=List.objects.get(id=product_id);
            text=request.POST.get('text');

            c=Comment(product=product,user=request.user,content=text)
            c.save();
            return render(request, "auctions/product.html",{
                    "article":product,
                    "message":"Thank you for your comment",
                    "class":"success"
                })
        except ValueError:
            return HttpResponseRedirect(reverse('login'))
    
