from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    p1 = Product_mst.objects.get(name = 'vivo')
    filtered_Product = Product_category.objects.all()
    try:
        
        return render(request,'products.html', {'Products': filtered_Product})
    except:
        return render(request,'products.html')

def add_product(request):
    return render(request,'add_product.html')

def edit_product(request, pid):
    productdata = Product_category.objects.get(id = pid)
    if request.method == 'GET':
        return render(request,'edit_product.html', {'productdata': productdata})
    else:
        productdata.product_model = request.POST['model']
        productdata.product_price = request.POST['price']
        productdata.product_ram = request.POST['ram']
        try:
            productdata.product_image = request.FILES['pic']
            productdata.save()
            return render(request, 'edit_product.html', {'productdata':productdata})
        except:
            productdata.save()
            return render(request, 'edit_product.html', {'productdata':productdata})