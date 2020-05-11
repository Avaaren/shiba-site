from django.views.generic import TemplateView, View
from django.http import JsonResponse
import requests

import os

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
        print('lol!')
        json_response = {}
        try:
            image_url = request.POST.get('image_url')
            filename = request.POST.get('filename')

            response = requests.get(image_url)
            home = os.path.expanduser('~')
            print(home)
            if os.path.exists(os.path.join(home, 'Downloads')):
                filename = os.path.join(os.path.join(home, 'Downloads'), filename)
            elif os.path.exists(os.path.join(home, 'Загрузки')):
                filename = os.path.join(os.path.join(home, 'Загрузки'), filename)
            print(filename)
            with open(filename, 'wb') as f:
                f.write(response.content)
            
            json_response['message'] = 'Success'
        except:
            json_response['message'] = 'Error'

        return JsonResponse(json_response)