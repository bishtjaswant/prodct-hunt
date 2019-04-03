from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Product
import datetime
from django.shortcuts import redirect

# Create your views here.
def homepage(request):
    products = Product.objects
    return render(request, "products/home.html",{'products':products})


def detail(request, product_id):
    get_product = get_object_or_404(Product, pk=product_id)
    return render(request, 'products/detail.html', {'product': get_product})






# create products
@login_required
def create(request):
    if request.method == "POST":
        # CODE
        if request.POST['title'] and request.POST['body'] and request.POST['url'] and request.FILES['image'] and request.FILES['icon']:
              # add product
            product = Product()
            product.title =  request.POST['title']
            product.body =  request.POST['body']
            if request.POST['url'].startswith('http://') or request.POST['url'].startswith('https://'):
                product.url =  request.POST['url']
            else:
                product.url = "http://"+ request.POST['url']

            product.image =  request.FILES['image']
            product.icons =  request.FILES['icon']
            product.pub_date = datetime.datetime.now()
            product.hunter = request.user
            product.save()
            return redirect('/products/'+ str(product.id))
        else:
            return render(request, 'products/create.html',{'error':'please fill all the fields to proceed'})

    else:
        return render(request, 'products/create.html')


@login_required
def upvote(request, product_id):
    if request.method ==  "POST" :
        product = get_object_or_404(Product, pk=product_id)
        product.votes_total += 1
        product.save()
        return redirect('/products/'+str(product.id))
