from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from store.models import Product, Variation

from .models import Cart, CartItem


def _cart_id(request):
    cart_id = request.session.session_key
    if not cart_id:
        cart_id = request.session.create()
    return cart

def add_cart(request, product_id):
    current_user = request.user
    if current_user.is_authenticated:
        product = Product.objects.get(id=product_id)
        product_variation =[]
        if request.method == 'POST':
            for item in request.POST:
                key = item
                value = request.POST[key]
                
                try:
                    variation = Variation.objects.get(product=product, variation_category_iexact=key,variation_value_iexact=value)
                    product_variation.append(variation)
                except Variation.DoesNotExist:
                    pass

            
    

        is_cart_item_exists = CartItem.objects.filter(product=product, user = current_user).exists()
        
        if is_cart_item_exists:
            cart_item = CartItem.objects.filter(product=product, user = current_user)

            ex_var_list=[]
            id = []
            for item in cart_item:
                existing_variation = item.variations.all()
                ex_var_list.append(list(existing_variation))
                id.append(item.id)
            if product_variation in ex_var_list:
                item_id = id[ex_var_list.index(product_variation)]
                item = CartItem.objects.get(id=item_id,product=product)
                item.quantity += 1
                item.save()
            else:
                item = CartItem.objects.create(product=product,user = current_user, quantity=1)
                if len(product_variation)>0:
                    item.variations.clear()
                    item.variations.add(*product_variation)

                item.save()
        else:
            cart_item = CartItem.objects.create(product=product, user = current_user, quantity=1)
            if len(product_variation)>0:
                cart_item.variations.clear()
                
                cart_item.variations.add(*product_variation)

            cart_item.save()
            
        return redirect('cart')
    else:
        product = Product.objects.get(id=product_id)
        product_variation =[]
        if request.method == 'POST':
            for item in request.POST:
                key = item
                value = request.POST[key]
                
                try:
                    variation = Variation.objects.get(product=product, variation_category_iexact=key,variation_value_iexact=value)
                    product_variation.append(variation)
                except Variation.DoesNotExist:
                    pass

            
    
        try:
            cart = Cart.objects.get(cart_id=_cart_id(request))
        except Cart.DoesNotExist:
            cart = Cart.objects.create(cart_id=_cart_id(request))

        cart.save()
        is_cart_item_exists = CartItem.objects.filter(product=product, cart=cart).exists()
        
        if is_cart_item_exists:
            cart_item = CartItem.objects.filter(product=product,  cart=cart)
            ex_var_list=[]
            id = []
            for item in cart_item:
                existing_variation = item.variations.all()
                ex_var_list.append(existing_variation)
                id.append(item.id)
            if product_variation in ex_var_list:
                item_id = id[ex_var_list.index(product_variation)]
                item = CartItem.objects.get(id=item_id,product=product)
                item.quantity += 1
                item.save()
            else:
                item = CartItem.objects.create(product=product,cart=cart, quantity=1)
                if len(product_variation)>0:
                    item.variations.clear()
                    item.variations.add(*product_variation)

                item.save()
        else:
            cart_item = CartItem.objects.create(product=product, cart=cart, quantity=1)
            if len(product_variation)>0:
                cart_item.variations.clear()
                
                cart_item.variations.add(*product_variation)

            cart_item.save()
            
        return redirect('cart')
 
def remove_cart(request, product_id,cart_item_id):
    cart = Cart.objects.get(cart_id=_cart_id(request))
    product = get_object_or_404(Product,id=product_id)
    try:
        if request.user.is_authenticated:
             cart_item = CartItem.objects.get(product=product, user= request.user,id=cart_item_id)
        
        else:
            cart = Cart.objects.get(cart_id=_cart_id(request))
            cart_item = CartItem.objects.get(product=product, cart=cart,id=cart_item_id)
            

            


        if cart_item.quantity > 1:
            cart_item -= 1
            cart_item.save()
        else:
            cart_item.delete()
    except CartItem.DoesNotExist:
        pass

    return redirect('cart')

def remove_cart_item(request, product_id,cart_item_id):
    
    product = get_object_or_404(Product,id=product_id)
    if request.user.is_authenticated:
        cart_item = CartItem.objects.get(product=product, user= request.user,id=cart_item_id)
    else:
        cart = Cart.objects.get(cart_id=_cart_id(request))
        cart_item = CartItem.objects.get(product=product, cart=cart,id=cart_item_id)
    cart_item.delete()
    return redirect('cart')

def cart(request,total=0,quantity=0,cart_items=None):
    try:
       tax = 0
       grand_total = 0
       if request.user.is_authenticated:
           cart_items = CartItem.objects.filter(user=request.user,is_active=True)
       else:   
            cart = Cart.objects.get(cart_id=_cart_id(request))
            cart_items = CartItem.objects.filter(cart=cart,is_active=True)
       for cart_item in cart_items:
           total += (cart_item.product.price * cart_item.quantity)
           quantity += cart_item.quantity
       tax =(2*total)/100
       grand_total = total + tax
    except Cart.DoesNotExist:
        pass
    context = {
        'total':total,
        'quantity':quantity,
        'cart_items':cart_items,
        'tax':tax,
        'grand_total':grand_total,}
    return render(request,'store/cart.html',context) 
@login_required(login_url='login',redirect_field_name='next')
def checkout(request,total=0,quantity=0,cart_items=None):
    try:
       tax = 0
       grand_total = 0
       if request.user.is_authenticated:
           cart_items = CartItem.objects.filter(user=request.user,is_active=True)
       else:   
            cart = Cart.objects.get(cart_id=_cart_id(request))
            cart_items = CartItem.objects.filter(cart=cart,is_active=True)
       for cart_item in cart_items:
           total += (cart_item.product.price * cart_item.quantity)
           quantity += cart_item.quantity
       tax =(2*total)/100
       grand_total = total + tax
    except Cart.DoesNotExist:
        pass
    context = {
        'total':total,
        'quantity':quantity,
        'cart_items':cart_items,
        'tax':tax,
        'grand_total':grand_total,}
    return render(request,'store/checkout.html',context) 
