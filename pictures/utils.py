import os
from django.http import HttpResponse, FileResponse

def write_file(filename, response):
    # try:
        # Get home directory
    home = os.path.expanduser('~')

    path = os.path.join(home, filename)
    # Open file in download folder
    with open(path, 'wb') as f:
        # And write binary file from response to it
        f.write(response.content)

    return filename


def download(filename):
    home = os.path.expanduser('~')

    filename = os.path.join(home, filename)

    with open(filename, "rb") as f:
        response = HttpResponse(f.read(), content_type="image/jpeg")
        response['Content-Disposition'] = f'attachment; filename={filename}'
        response['X-Sendfile'] = filename
    os.remove(filename)
    return response

