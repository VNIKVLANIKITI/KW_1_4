from django.shortcuts import render
from letters.models import Mailing, Customer
from django.db.models import Count


def health_check(request):
    customer_count = Customer.objects.count
    mailings_count = Mailing.objects.count
    mailings_active_count = Mailing.objects.annotate(attempts_count=Count('attemtps')).filter(attempts_count__gt=0).count
    context = {
        'mailings_count': mailings_count,
        'customer_count': customer_count,
        'mailings_active_count': mailings_active_count,
    }
    return render(request, 'letters/general_page.html', context)
