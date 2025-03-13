from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import ReportForm
from .logic.report_logic import get_reports, create_report

def report_list(request):
    reports = get_reports()
    context = {
        'report_list': reports
    }
    return render(request, 'Report/reports.html', context)

def report_create(request):
    if request.method == 'POST':
        form = ReportForm(request.POST)
        if form.is_valid():
            create_report(form)
            messages.add_message(request, messages.SUCCESS, 'Successfully created report')
            return HttpResponseRedirect(reverse('reportCreate'))
        else:
            print(form.errors)
    else:
        form = ReportForm()

    context = {
        'form': form,
    }
    return render(request, 'Report/reportCreate.html', context)