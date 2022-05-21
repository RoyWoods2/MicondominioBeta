from django.shortcuts import get_object_or_404, render

from .forms import ProductForm
from .models import Category, Product, ProductImage


def product_all(request):
    products = Product.objects.prefetch_related("product_image").filter(is_active=True)
    return render(request, "store/index.html", {"products": products})


def category_list(request, category_slug=None):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(
        category__in=Category.objects.get(name=category_slug).get_descendants(include_self=True)
    )
    return render(request, "store/category.html", {"category": category, "products": products})


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, is_active=True)
    return render(request, "store/single.html", {"product": product})


def agregar_producto (request):
    data = {
        'form': ProductForm(),
    
    }
    if request.method == 'POST':
        formulario = ProductForm(data=request.POST , files= request.FILES)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "guardado correctamente"
        else:
            data  ["form"] = formulario
    return render (request, 'store/agregar_producto.html', data)
