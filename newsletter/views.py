from django.http import HttpResponseRedirect
from django.contrib import messages
from django.conf import settings

from .forms import EmailSubscribeForm
from .models import Subscribe

import json
import requests


MAILCHIMP_API_KEY = settings.MAILCHIMP_API_KEY
MAILCHIMP_DATA_CENTER = settings.MAILCHIMP_DATA_CENTER
MAILCHIMP_EMAIL_LIST_ID = settings.MAILCHIMP_EMAIL_LIST_ID

api_url = f'https://{MAILCHIMP_DATA_CENTER}.api.mailchimp.com/3.0/'
members_endpoint = f'{api_url}/lists/{MAILCHIMP_EMAIL_LIST_ID}/members'


def subscribe(email):
    data = {
        'email_address': email,
        'status': 'subscribed',
    }
    s = requests.post(
        members_endpoint,
        auth=("", MAILCHIMP_API_KEY),
        data=json.dumps(data)
    )
    return s.status_code, s.json()


def email_collect(request):

    form = EmailSubscribeForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            email_subscribe_qs = Subscribe.objects.filter(
                email=form.instance.email)
            if email_subscribe_qs.exists():
                messages.error(request, "Your are already subscribed!")
            else:
                subscribe(form.instance.email)
                form.save()
                messages.success(request, "Your are succesfully subscribed!")
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))