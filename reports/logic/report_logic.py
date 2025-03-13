from ..models import Report

def get_reports():
    queryset = Report.objects.all().order_by('-dateTime')[:10]
    return (queryset)

def create_report(form):
    report = form.save()
    report.save()
    return ()