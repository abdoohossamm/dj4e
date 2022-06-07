from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def myview(request):
    counter = request.session.get('counter', 0) +1
    request.session['counter'] = counter
    resp = HttpResponse(f'view count={str(counter)}')
    resp.set_cookie('dj4e_cookie', 'cb804af6', max_age=1000)
    return resp