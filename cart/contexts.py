from decimal import Decimal
from django.conf import settings


def cart_contents(request):

    cart_items = []
    total = 0
    product_count = 0

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE/100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total  # This will inform about how much more the user have to spend to get free delivery
    else:
        delivery = 0
        free_delivery_delta = 0

    grand_total = delivery + total

    if total < settings.FREE_GIFT_THRESHOLD:
        free_gift_delta = settings.FREE_GIFT_THRESHOLD - total  # This will inform about how much more the user have to spend to get the free baby plant
    else:
        free_gift_delta = 0

    context = {
        'cart_items': cart_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'free_gift_delta': free_gift_delta,
        'free_gift_threshold': settings.FREE_GIFT_THRESHOLD,
        'grand_total': grand_total,
    }

    return context
