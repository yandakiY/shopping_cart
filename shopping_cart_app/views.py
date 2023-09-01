from django.shortcuts import render, HttpResponse, HttpResponseRedirect , get_object_or_404
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

def SettingsViews(request):
    return render(request , "shopping_cart/settings.html");

def SettingsCategoriesViews(request):
    categories = Category.objects.all()
    return render(request , "shopping_cart/settings_categories.html" , {"categories":categories})

def DeleteCategory(request , cat_id):
    
    category = Category.objects.get(id = cat_id)
    category.delete()
    
    return HttpResponseRedirect(reverse('shopCart:settings_categories' , args=()))

def RemoveCategory(request , cat_id):
    
    category = Category.objects.get(id = cat_id)
    category.views = False
    
    category.save()
    
    return HttpResponseRedirect(reverse('shopCart:settings_categories' , args=()))

# Update a category
def UpdateCategory(request , cat_id):
    
    category = Category.objects.get(id=cat_id)
    return render(request , "shopping_cart/update_cat.html" , {"category":category})

# save update category
def SaveUpdateCategory(request , cat_id):
    category = Category.objects.get(id=cat_id)
    
    category.name = escape(request.POST.get("name"))
    category.save()
    
    return HttpResponseRedirect(reverse('shopCart:settings_categories' , args=()))


# SETTINGS PRODUCTS 

def SettingsProductsViews(request):
    products = Product.objects.all()
    return render(request , "shopping_cart/settings_products.html" , {"products":products})

def DeleteProduct(request , prod_id):
    
    product = Product.objects.get(id = prod_id)
    product.delete()
    
    return HttpResponseRedirect(reverse('shopCart:settings_products' , args=()))

def RemoveProduct(request , prod_id):
    
    product = Product.objects.get(id = prod_id)
    product.views = False
    
    product.save()
    
    return HttpResponseRedirect(reverse('shopCart:settings_products' , args=()))

# Update a category
def UpdateProduct(request , prod_id):
    product = Product.objects.get(id=prod_id)
    
    categories = Category.objects.all()
    return render(request , "shopping_cart/update_product.html" , {"product":product , "categories":categories})

# save update category
def SaveUpdateProduct(request , prod_id):
    product = get_object_or_404(Product, id=prod_id)
    
    # change value with new values
    product.name = escape(request.POST.get('name'))
    product.description = escape(request.POST.get('description'))
    product.price = escape(request.POST.get('price'))
    # set image product to None and change after that
    # product.image = None
    product.image = request.FILES['image']
    
    # delete all categories for product
    product.category.clear()
    
    # attribute new values to product.categories
    new_categories = request.POST.getlist('categories')
    for k in new_categories:
        cat = Category.objects.get(name = k)
        product.category.add(cat)
        
        
    product.save()
    # product.name = escape(request.POST.get("name"))
    # print(request.POST.get('name'))
    # print(request.POST.get('image'))
    # print(request.POST.get('description'))
    # print(request.POST.get('price'))
    # print(request.POST.getlist('categories'))
    
    # print("Id",prod_id)
    # product.save()
    
    return HttpResponseRedirect(reverse('shopCart:settings_products' , args=()))