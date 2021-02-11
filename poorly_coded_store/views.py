from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
from .models import Order, Product
from django.db.models import Sum,Max,Min,Avg
from django.contrib import messages

def index(request):
    context = {
        "all_products": Product.objects.all()
    }
    return render(request, "store/index.html", context)

def checkout(request):
    return render(request, "store/checkout.html",context={
        #"some_order":Order.objects.last(), ###
        "some_order":Order.objects.get(id=len(Order.objects.all())),
        "total_spent":Order.objects.all().aggregate(total_spent=(Sum('total_price'))),
        "total_ordered":Order.objects.aggregate(total_ordered=Sum('quantity_ordered'))
        })
    
def order_process(request):
    if request.method=="POST":
        id_from_form = request.POST["price"]
        quantity_from_form = int(request.POST["quantity"])
        price_from_form = float(Product.objects.get(id = id_from_form).price)
        total_charge = quantity_from_form * price_from_form
        print("Charging credit card...")
        some_order=Order.objects.create(quantity_ordered=quantity_from_form, total_price=total_charge)
        print(some_order.id)
        return redirect("/checkout")
    return redirect("/")
