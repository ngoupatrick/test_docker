import os

class Mid_Factor():
    """
    A class representing urls access.

    Attributes:
        FAVICON_PATH (str): The favicon path on system.
        APP_NAME (str): The application name.
    """
    def __init__(self):
        """
        Initializes a bunch of parameters.

        Parameters:
        """
        ov = os.environ
        self.PORT = int(ov['PORT'])
        self.BACKEND_SERVER=str(ov['SERVER'])
        self.BACKEND_PORT=int(ov['PORT'])
        self.BACKEND_API_BASE=str(ov['API_BASE']).strip()
        self.APP_NAME = str(ov['APP_NAME'])
        self.VERSION_APP = str(ov['VERSION_APP'])
        self.DEVNAME=str(ov['DEVNAME'])
        self.GITHUB_URL = str(ov['GITHUB_URL'])
        self.EMAIL = str(ov['EMAIL'])
        self.FAVICON_ICON ="🚀"
        self.FAVICON_PATH =str(ov['FAVICO_PATH'])
