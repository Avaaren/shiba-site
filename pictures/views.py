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


class DownloadImage(View):

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

# def download(request):
#     file_name = #get the filename of desired excel file
#     path_to_file = #get the path of desired excel file
#     response = HttpResponse(mimetype='application/force-download')
#     response['Content-Disposition'] = f'attachment; filename={filename}
#     response['X-Sendfile'] = filename
#     return response


def save_file(request, filename):
    # try:
        # Get home directory
    filename = f'{filename}.jpg'
    response = download(filename)
    # Open file in download folder
    return response