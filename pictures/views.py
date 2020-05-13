from django.views.generic import TemplateView, View
from django.http import JsonResponse, HttpResponse
import requests
from django.shortcuts import reverse
import os

from .utils import write_file, download

class GetShibaImage(TemplateView):
    template_name = 'pictures/shibe.html'

    def get_context_data(self, **kwargs):
        response = requests.get('http://shibe.online/api/shibes?count=2&urls=true&httpsUrls=true')
        image_url = response.json()[0]
        data = super(GetShibaImage, self).get_context_data(**kwargs)
        data['image_url'] = image_url
        data['filename'] = image_url.split('/')[-1]
        return data


class DownloadClickHandle(View):

    def post(self, request):
        json_response = {}

        image_url = request.POST.get('image_url')
        filename = request.POST.get('filename')
        if image_url and filename:
            response = requests.get(image_url)
            filename = write_file(filename, response)
            if filename:
                json_response['message'] = 'Success'
                json_response['filename'] = filename
            else:
                json_response['message'] = 'File doesn`t download'
        else:
            json_response['message'] = 'Requests are empty'
            
        return JsonResponse(json_response)

class DownloadFileView(View):

    def get(self, request, **kwargs):

        filename = self.kwargs.get('filename')
        filename = f'{filename}.jpg'
        response = download(filename)
        if response:
            return response
        else:
            return False