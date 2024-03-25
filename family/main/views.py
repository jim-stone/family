from django.shortcuts import render
from django.views import View
from .helpers import cre_sup

# Create your views here.


class IndexView(View):
    def get(self, request):
        return render(request, 'index.html')


class FamiliesView(View):
    def get(self, request):
        cre_sup()
        return render(request, 'families.html')


class OpinionsView(View):
    def get(self, request, pk=None):
        return render(request, 'opinions.html')


class WishesView(View):
    def get(self, request, pk=None):
        return render(request, 'wishes.html')
