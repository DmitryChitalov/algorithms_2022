from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest, HttpResponse
import datetime
from .models import Category, Product
from basketapp.models import Basket
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.

def undex(request: HttpRequest):
    products = Product.objects.all()

    return render(request, 'mainapp/index.html', {
        'products': products,
    })


def contact(request: HttpRequest):
    title = 'о нас'
    visit_date = datetime.datetime.now()

    locations = [
        {
            'city': 'Москва',
            'phone': '+7-888-888-8888',
            'email': 'info@geekshop.ru',
            'address': 'В пределах МКАД',
        },
        {
            'city': 'Екатеринбург',
            'phone': '+7-777-777-7777',
            'email': 'info_yekaterinburg@geekshop.ru',
            'address': 'Близко к центру',
        },
        {
            'city': 'Владивосток',
            'phone': '+7-999-999-9999',
            'email': 'info_vladivostok@geekshop.ru',
            'address': 'Близко к океану',
        },
    ]

    return render(request, 'mainapp/contact.html', {
        'title': title,
        'visit_date': visit_date,
        'locations': locations
    })


# def get_current_basket(current_user):
#     basket = Basket.objects.filter(user=current_user) if current_user.is_authenticated else None
#
#     return basket


def products(request, category_slug=None, page=1):
    title = 'продукты'
    links_menu = Category.objects.filter(is_valid=True)
    products = Product.objects.filter(category__slug=category_slug,
                                      available=True) if category_slug else Product.objects.filter(available=True,
                                                                                                   category__is_valid=True)
    category = get_object_or_404(Category, slug=category_slug,is_valid=True) if category_slug else None

    provider = Paginator(products, 1)

    try:
        products_provider = provider.page(page)
    except PageNotAnInteger:
        products_provider = provider.page(1)
    except EmptyPage:
        products_provider = provider.page(provider.num_pages)


    return render(request,
                  'mainapp/products.html',
                  {'title':title,
                   'category': category,
                   'links_menu': links_menu,
                   'provider': products_provider,
                   })


def product_detail(request, slug=None):
    links_menu = Category.objects.filter(is_valid=True)
    product = get_object_or_404(Product, slug=slug, available=True, category__is_valid=True, )
    products = Product.objects.exclude(slug=slug).filter(category__slug=product.category.slug, available=True,
                                                         category__is_valid=True, )
    return render(request, 'mainapp/product.html', {'product': product,
                                                    'links_menu': links_menu,
                                                    'title': f'Товар: {product.name}',
                                                    'products': products,
                                                    })

# def get_referer_view(request, default=None):
#     '''
#     Return the referer view of the current request
#
#     Example:
#
#         def some_view(request):
#             ...
#             referer_view = get_referer_view(request)
#             return HttpResponseRedirect(referer_view, '/accounts/login/')
#     '''
#
#     # if the user typed the url directly in the browser's address bar
#     referer = request.META.get('HTTP_REFERER')
#     if not referer:
#         return default
