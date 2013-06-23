import urlparse
import requests

#import warlock


class Service(object):
    def __init__(self, endpoint):
        self.endpoint = endpoint
        self._connection = None

    def _request(self, method, rel_path):
        full_path = urlparse.urljoin(self.endpoint, rel_path)
        return requests.request(method, full_path)

    def list_changes(self):
        request = self._request('GET', '/changes')
        return request.json()
