from django.shortcuts import render
from  django.http import HttpResponse
from django.template import loader

from .models import Product


def product_detail_view(request, my_id):
    obj = Product.objects.get(id=my_id)

    context = dict(object=obj)

    return render(request, "products/product_details.html", context)
def product_list_view(request, self, my_id):
    queryset = Product.objects.all(id=my_id)
    template = loader.get_template('index.html')
    context = {
        "object_list": self.queryset
    }
    return HttpResponse(template.render(request, context))
