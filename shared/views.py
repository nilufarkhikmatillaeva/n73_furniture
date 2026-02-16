from django.shortcuts import render

# Functions for each HTML template
def page_404(request):
    return render(request, '404.html')

def about_us(request):
    return render(request, 'about-us.html')

def account(request):
    return render(request, 'account.html')

def blog_detail(request):
    return render(request, 'blog-detail.html')

def blog_list(request):
    return render(request, 'blog-list.html')

def cart(request):
    return render(request, 'cart.html')

def checkout(request):
    return render(request, 'checkout.html')

def contact(request):
    return render(request, 'contact.html')

def home(request):
    return render(request, 'home.html')

def index_2(request):
    return render(request, 'index-2.html')

def login(request):
    return render(request, 'login.html')

def product_detail(request):
    return render(request, 'product-detail.html')

def product_list(request):
    return render(request, 'product-list.html')

def register(request):
    return render(request, 'register.html')

def reset_password(request):
    return render(request, 'reset-password.html')

def wishlist(request):
    return render(request, 'wishlist.html')
