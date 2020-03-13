from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse

# Create your views here.
class Index(View):

    def get(self, request):
        return render(request, 'index.html')

    def post(self, request):
        html = '<html><body>'
        for key, value in request.POST.items():
            html += f'{key}: {value}<br>'
        html += '</html></body>'
        return HttpResponse(html)


class About(View):

    def get(self, request):
        return render(request, 'about.html')

    def post(self, request):
        html = '<html><body>'
        for key, value in request.POST.items():
            html += f'{key}: {value}<br>'
        html += '</html></body>'
        return HttpResponse(html)


class Speakers(View):

    def get(self, request):
        return render(request, 'speaker.html')

    def post(self, request):
        html = '<html><body>'
        for key, value in request.POST.items():
            html += f'{key}: {value}<br>'
        html += '</html></body>'
        return HttpResponse(html)


class Scedule(View):

    def get(self, request):
        return render(request, 'event-schedule.html')

    def post(self, request):
        html = '<html><body>'
        for key, value in request.POST.items():
            html += f'{key}: {value}<br>'
        html += '</html></body>'
        return HttpResponse(html)


class Gallery(View):

    def get(self, request):
        return render(request, 'event-gallery.html')

    def post(self, request):
        html = '<html><body>'
        for key, value in request.POST.items():
            html += f'{key}: {value}<br>'
        html += '</html></body>'
        return HttpResponse(html)


class Price(View):

    def get(self, request):
        return render(request, 'price.html')

    def post(self, request):
        html = '<html><body>'
        for key, value in request.POST.items():
            html += f'{key}: {value}<br>'
        html += '</html></body>'
        return HttpResponse(html)


class Blog_single(View):

    def get(self, request):
        return render(request, 'blog.html')

    def post(self, request):
        html = '<html><body>'
        for key, value in request.POST.items():
            html += f'{key}: {value}<br>'
        html += '</html></body>'
        return HttpResponse(html)


class Blog_details(View):

    def get(self, request):
        return render(request, 'blog-details.html')

    def post(self, request):
        html = '<html><body>'
        for key, value in request.POST.items():
            html += f'{key}: {value}<br>'
        html += '</html></body>'
        return HttpResponse(html)


class Contact(View):

    def get(self, request):
        return render(request, 'contact.html')

    def post(self, request):
        html = '<html><body>'
        for key, value in request.POST.items():
            html += f'{key}: {value}<br>'
        html += '</html></body>'
        return HttpResponse(html)

