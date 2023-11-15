from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.conf import settings
from .forms import CreditProfileForm
from .models import CreditProfile
from main import rf_model


# request handler

def say_hello(request):
    return render(request, 'hello.html')

def credit(request):
    return render(request, 'credit.html')

def credit_profile(request):
    if request.method == 'POST':
        form = CreditProfileForm(request.POST)
        if form.is_valid():
            # Extract data from form
            annual_income = form.cleaned_data.get('annual_income')

            # Define your custom condition
            if annual_income < 10000:  # Example condition
                # Add a non-field error
                form.add_error(None, "Annual income must be at least 10,000.")
            else:
                # If the condition is not met, save the form
                form.save()
                return redirect('/main/process')  # Redirect to a success URL
    else:
        form = CreditProfileForm()

    return render(request, 'credit_profile_form.html', {'form': form})

def Credit_Profile_Request(request, id=id):
    record_id = request.GET.get('id', None)
    if record_id and record_id.isdigit():
        record_id = int(record_id)
        record = get_object_or_404(CreditProfile, id=record_id)
    else:
        record = 1

    return render(request, 'credit_profile_detail.html', {'record': record})


def process(request):
    return render(request, 'process.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def credit_profile_form(request):
    if request.method == 'POST':
        # Create a new CreditProfile instance from the form data
        credit_profile = CreditProfile(
            no_of_dependents=request.POST.get('no_of_dependents'),
            education=request.POST.get('education'),
            self_employed=request.POST.get('self_employed'),
            annual_income=request.POST.get('annual_income'),
            loan_amount=request.POST.get('loan_amount'),
            credit_score=request.POST.get('credit_score'),
            res_assets=request.POST.get('res_assets'),
            com_assets=request.POST.get('com_assets'),
            bank_assets=request.POST.get('bank_assets'),
            total_assets=request.POST.get('total_assets')
        )
        credit_profile.save()

        # Call a Python script function using the last entry
        y, message = rf_model.process_data(credit_profile)

        # Redirect or show a success message
        # return redirect('success_page')
        return render(request, 'process.html', {'message': message, 'score':y})

    return render(request, 'credit_profile_form.html', {})

def my_view(request):
    context = {
        'firebase_config': settings.FIREBASE_CONFIG,
    }
    return render(request, 'my_template.html', context)