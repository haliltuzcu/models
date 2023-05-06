from django.contrib import admin
from django.urls import path,include
from django.http import HttpResponse

def home(request):
    return HttpResponse('''
        <h1>
        Welcome to Home.
        </h1>
    ''')

urlpatterns = [
    # path('url/path/', view_func_name, 'redirection_name'),
    path('', home),
    path('admin/', admin.site.urls),
    path('fscohort/',include('fscohort.urls'))
]