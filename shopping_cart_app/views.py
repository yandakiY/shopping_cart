from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.views import generic
from .models import Category , Product
from django.utils.html import escape
from django.urls import reverse

# Create your views here.

# class Index(generic.ListView):
#     template_name = ""
#     context_object_name = ""
    
#     return 

# Index Page
def Index(request):
    # send categories in index page
    categories = Category.objects.all()
    products = Product.objects.all()
    return render(request , "shopping_cart/index.html" , {"categories":categories , "products":products})

# Add a category
class AddCategory(generic.CreateView):
    model = Category
    fields = ["name"]
    template_name = "shopping_cart/create_cat.html"
    
# save category
def SaveCategory(request):
    # initizialition category
    cat = Category(name=escape(request.POST.get("name")))
    # save category
    cat.save()
    # redirection
    return render(request , "shopping_cart/create_cat.html")

# Add a product
def AddProduct(request):
    # model = Product
    # fields = ["name" , "description" , "price" , "image" , "category"]
    # send categories on lists for display in a checkbox
    categories = Category.objects.all()
     
    return render(request, "shopping_cart/create_product.html" , {"categories":categories})
    
def SaveProduct(request):
    # print("Name",escape(request.POST.get('name')))
    # print("Description",escape(request.POST.get('description')))
    # print("Price",escape(request.POST.get('price')))
    # print("Image",request.FILES['image'])
    
    model , created = Product.objects.get_or_create(name=escape(request.POST.get('name')) , description=escape(request.POST.get('description')),price=escape(float(request.POST.get('price'))) , image=request.FILES['image'])
    
    if model:
        categories = request.POST.getlist('categories')
        # add categories
        # for category in categories:
        for cat in categories :
            model.category.add(Category.objects.get(name=cat))
    
        # product.save()
            
        # print("Categories",request.POST.get('categories'))
        # print(cats)
    
        return HttpResponseRedirect(reverse('shopCart:Index' , args=()))
    
    return render(request , 'shoppin_cart/create_product.html',{"error":"Error"})


def DetailsProduct(request , prod_id):
    # product which correspond to id product
    product = Product.objects.get(id = prod_id)
    
    return render(request , "shopping_cart/details_product.html",{"product":product , "categories":Category.objects.all()})

def SearchByCategory(request):
    cat = request.POST.get("categories")
    
    category = Category.objects.get(name=cat)
    # products which correspond to category selected
    products_res = category.product_set.all()
    print(products_res)
    
    return render(request , "shopping_cart/results_search.html" , {"products":products_res , "query":cat, "categories":Category.objects.all()})