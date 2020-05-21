from django.shortcuts import render
from django.utils import timezone
from .models import Payment
from .forms import PaymentForm


def payments_list(request):
    payments = Payment.objects.all().order_by('date')
    return render(request, 'payments/payments.html', {'payments': payments})


def new_payment(request):
    form = PaymentForm(request.POST)
    if form.is_valid():
        payment = form.save(commit=False)
        payment.save()
    return render(request, 'payments/payment_form.html', {'form': form})