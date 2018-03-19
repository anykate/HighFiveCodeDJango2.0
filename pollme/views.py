from django.http import HttpResponse
from datetime import datetime


def current_datetime(request):
    now = datetime.now()
    html = '<html><body style="color:red;">It is now: <h3>%s</h3>.</body></html>' % now
    return HttpResponse(html)
