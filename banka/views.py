from django.shortcuts import render
from banka.models import Deposit
from banka.Deposit import Deposit_class
from django.views.generic import View, ListView, FormView, DetailView

def add_deposit(request):
    if request.method == "POST":

        deposit = Deposit(
            deposit=request.POST['deposit'],
            term=request.POST['term'],
            rate=request.POST['rate'],
        )



        # interest=request.POST['interest'],
        dep_function = Deposit_class(float(deposit.deposit), int(deposit.term), float(deposit.rate))
        interest = dep_function.interest()

        deposit = Deposit(
            deposit=deposit.deposit,
            term=deposit.term,
            rate=deposit.rate,
            interest=interest,
        )

        deposit.save()

        deposits = Deposit.objects.all()
        context = {
            'deposits': deposits,
        }
        return render(
            template_name="deposit_list.html",
            request=request,
            context=context,
        )

    return render(
        template_name="add_deposit.html",
        request=request,
    )


def index(request):
    deposits = Deposit.objects.all()

    context = {
        'deposits': deposits,
    }

    return render(
        template_name='deposit_list.html',
        request=request,
        context=context,
    )

class DepoDetailView(DetailView):

	model = Deposit
	template_name = 'deposit_detail.html'


