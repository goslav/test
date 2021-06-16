from django.shortcuts import render, redirect
from .forms import CitizenForm
from django.contrib import messages
from datetime import date
from dateutil import relativedelta


today = date.today()


def age(date_of_birth):

    diff = relativedelta.relativedelta(today, date_of_birth)

    years = diff.years
    months = diff.months
    days = diff.days

    return ('{} years {} months {} days'.format(years, months, days))


def indexPage(request):
    if request.method == 'POST':
        form = CitizenForm(request.POST)
        if form.is_valid():
            id_number = form.cleaned_data.get('id_number')
            date_of_birth = form.cleaned_data.get('date_of_birth')
            if date_of_birth > today:
                messages.error(
                    request, 'Error. Date of birth cannot be \
                    greater than the current time!')
            else:
                messages.success(
                    request, f'the citizen with identification {id_number} \
                    and date of birth {date_of_birth} \
                    is {age(date_of_birth)} old!')

        return redirect('citizens:index')

    else:
        form = CitizenForm()
    return render(request, 'citizens/index.html', {'form': form})
