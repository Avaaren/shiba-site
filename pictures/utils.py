import os
from django.http import HttpResponse, FileResponse

def write_file(filename, response):
    # Find home dir on server
    home = os.path.expanduser('~')
    # Make path to file, we getting from cdn
    path = os.path.join(home, filename)
    # Open file in home folder
    try:
        with open(path, 'wb') as f:
            # And write binary file from response to it
            f.write(response.content)
    except:
        return False

    return filename


def download(filename):
    # Find the file we saved
    home = os.path.expanduser('~')
    filename = os.path.join(home, filename)
    try:
        # Open file and add in to http response
        with open(filename, "rb") as f:
            response = HttpResponse(f.read(), content_type="image/jpeg")
            response['Content-Disposition'] = f'attachment; filename={filename}'
            response['X-Sendfile'] = filename
        # After it delete from server
        os.remove(filename)
    except:
        return False
    return response

