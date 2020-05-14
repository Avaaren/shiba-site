from django.views.generic import TemplateView, View
from django.http import JsonResponse, HttpResponse
import requests
from django.shortcuts import reverse
import os

from .utils import write_file, download
from likes.models import Liked


class GetShibaImage(TemplateView):
    template_name = 'pictures/shibe.html'

    def get(self, request):
        # If there is no variable in session - get it as 0
        dogs_viewed = request.session.get('dogs_viewed', 0)
        # Set session variable as earlier + 1
        request.session['dogs_viewed'] = dogs_viewed + 1
        # Execute default get method
        return super(GetShibaImage, self).get(request)
    
    def get_context_data(self, **kwargs):
        # Make request to api
        response = requests.get('http://shibe.online/api/shibes?count=2&urls=true&httpsUrls=true')
        # Get response as JSON and take first element
        image_url = response.json()[0]
        # Get click count from session
        dogs_viewed = self.request.session.get('dogs_viewed', 0)
        # Execute original method and append it
        data = super(GetShibaImage, self).get_context_data(**kwargs)
        
        if self.request.user.is_authenticated:
            try:
                Liked.objects.get(user=self.request.user, image_href=image_url)
                data['liked'] = True
            except:
                data['liked'] = False
        
        data['image_url'] = image_url
        data['filename'] = image_url.split('/')[-1]
        data['dogs_viewed'] = dogs_viewed
        return data


class DownloadClickHandle(View):

    def post(self, request):
        json_response = {}
        # Get parameters from ajax
        image_url = request.POST.get('image_url')
        filename = request.POST.get('filename')
        # If all parameters got
        if image_url and filename:
            # Do request to image on cdn
            response = requests.get(image_url)
            # And writing file in home folder on server
            filename = write_file(filename, response)
            # If file written - make positive response
            if filename:
                json_response['message'] = 'Success'
                json_response['filename'] = filename
            else:
                # If not - negative
                json_response['message'] = 'File doesn`t download'
        else:
            json_response['message'] = 'Requests are empty'
            
        return JsonResponse(json_response)

class DownloadFileView(View):
    # This url called by ajax success function
    def get(self, request, **kwargs):
        # Reading name of written recently file from url 
        filename = self.kwargs.get('filename')
        filename = f'{filename}.jpg'
        # And make http response forcing download
        response = download(filename)
        if response:
            return response
        else:
            return False