from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "Your cart is still empty. Keep shopping!")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51JGi0hESJDhTJKBGJZVL3EX1cyFR6OrnLrt0ftyYNM5LWpFYUROpjRcvv5Cj8EpAS3OQ1g1eWDF0e9acJhPimYb00088iipmUE',
    }

    return render(request, template, context)
