import requests
from requests.auth import HTTPDigestAuth

URL = '{http}://{host}:{port}'


class Configuration:
    """Device configuration"""
    def __init__(
        self,
        *,
        loop,
        host:str,
        username:str,
        password:str,
        port:str=80,
        web_proto:str='http',
        verify_ssl:bool=False,
    ):
        """All config params available to the device."""
        self.loop = loop
        self.web_proto = web_proto
        self.host = host
        self.port = port
        self.username = username
        self.password = password

        self.session = requests.Session()
        self.session.auth = HTTPDigestAuth(self.username, self.password)
        self.session.verify = verify_ssl

    @property
    def url(self):
        """Represent device base url."""
        return URL.format(http=self.web_proto, host=self.host, port=self.port)
