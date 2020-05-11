from django.views.generic import TemplateView

import requests

class GetShibaImage(TemplateView):
    template_name = 'pictures/shibe.html'

    def get_context_data(self, **kwargs):
        response = requests.get('http://shibe.online/api/shibes?count=1&urls=true&httpsUrls=true')
        image_url = response.json()[0]
        data = super(GetShibaImage, self).get_context_data(**kwargs)
        data['image_url'] = image_url

        return data


