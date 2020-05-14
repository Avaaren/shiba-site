from django.views.generic import View
from django.http import JsonResponse

from .models import Liked


class ToggleLikeView(View):

    def post(self, request):
        json_response = {}

        image_url = request.POST.get('image_url', None)
        if image_url:
            image,created = Liked.objects.get_or_create(user=self.request.user, image_href=image_url)
            if not created:
                image.delete()
                json_response['message'] = 'unliked'
            else:
                json_response['message'] = 'liked'
        return JsonResponse(json_response)

            



