from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages

from products.models import Product


def view_cart(request):
    """ A view to return the cart page """
    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """ Add one or more of the selected plant in the cart """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):
        cart[item_id] += quantity
        messages.success(request, f'Great! You now have {cart[item_id]} {product.name} plants in your cart!')
    else:
        cart[item_id] = quantity
        messages.success(request, f'{product.name} is been successfully added to your cart!')

    request.session['cart'] = cart
    return redirect(redirect_url)


def adjust_cart(request, item_id):
    """Adjust the quantity of the products"""

    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})
    product = get_object_or_404(Product, pk=item_id)

    if quantity > 0:
        cart[item_id] = quantity
        messages.success(request, f'Great! You now have {cart[item_id]} {product.name} plants in your cart!')
    else:
        cart.pop(item_id)
        messages.error(request, f'Why did you remove {product.name} from the cart? You made it cry!')

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))


def remove_from_cart(request, item_id):
    """Remove a product from the cart"""

    cart = request.session.get('cart', {})
    product = get_object_or_404(Product, pk=item_id)
    try:
        cart.pop(item_id)
        messages.error(request, f'Why did you remove {product.name} from the cart? You made it cry!')

        request.session['cart'] = cart
        return HttpResponse(status=200)

    except Exception as e:
        messages.warning(request, f'There was an error in removing {product.name} from your cart')
        return HttpResponse(status=500)
