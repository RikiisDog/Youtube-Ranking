from django.shortcuts import render
from django.views.generic import View

# Create your views here.
class Test(View):
    template_name = 'index.html'
    def post(self, request):
        pass
    def get(self, request):
        return render(request, 'index.html', {'context':'test'})