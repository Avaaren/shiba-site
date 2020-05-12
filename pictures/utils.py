import os

def save_file(filename, response):
    try:
        # Get home directory
        home = os.path.expanduser('~')
        # If Downloads folder is in home directory
        if os.path.exists(os.path.join(home, 'Downloads')):
            # Set path to file home/downloads/filename
            filename = os.path.join(os.path.join(home, 'Downloads'), filename)
        # Elif Загрузки folder in home directory
        elif os.path.exists(os.path.join(home, 'Загрузки')):
            # Set path to file home/загрузки/filename
            filename = os.path.join(os.path.join(home, 'Загрузки'), filename)
        else:
            # Set path to file home/filename
            filename = os.path.join(home, filename)
        # Open file in download folder
        print(filename)
        with open(filename, 'wb') as f:
            # And write binary file from response to it
            f.write(response.content)
        return True
    except:
        return False