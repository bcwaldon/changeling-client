import urlparse
import requests

import warlock


class Service(object):
    def __init__(self, endpoint):
        self.endpoint = endpoint
        self._model = None

    def _request(self, method, rel_path):
        full_path = urlparse.urljoin(self.endpoint, rel_path)
        return requests.request(method, full_path)

    @property
    def model(self):
        if self._model is None:
            schema = self.get_schema()
            self._model = warlock.model_factory(schema)
        return self._model

    def get_schema(self):
        request = self._request('GET', '/schemas/change')
        return request.json()

    def list_changes(self):
        request = self._request('GET', '/changes')
        return [self.model(change) for change in request.json()]

    def get_change(self, change_id):
        request = self._request('GET', '/changes/%s' % change_id)
        return self.model(request.json())

    def delete_change(self, change):
        self._request('DELETE', '/changes/%s' % change.id)
