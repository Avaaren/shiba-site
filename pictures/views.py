from django.views.generic import TemplateView, View
from django.http import JsonResponse
import requests

import os

from .utils import save_file

class GetShibaImage(TemplateView):
    template_name = 'pictures/shibe.html'

    def get_context_data(self, **kwargs):
        response = requests.get('http://shibe.online/api/shibes?count=2&urls=true&httpsUrls=true')
        image_url = response.json()[0]
        data = super(GetShibaImage, self).get_context_data(**kwargs)
        data['image_url'] = image_url
        data['filename'] = image_url.split('/')[-1]
        return data


class DownloadImage(View):

    def post(self, request):
        json_response = {}

        image_url = request.POST.get('image_url')
        filename = request.POST.get('filename')
        if image_url and filename:
            response = requests.get(image_url)
            is_downloaded = save_file(filename)
            if is_downloaded:
                json_response['message'] = 'Success'
            else:
                json_response['message'] = 'File doesn`t download'
        else:
            json_response['message'] = 'Requests are empty'
            
        return JsonResponse(json_response)