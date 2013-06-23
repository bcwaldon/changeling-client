import json
import urlparse

import requests

import warlock


class Service(object):
    def __init__(self, endpoint):
        self.endpoint = endpoint
        self._model = None

    def _request(self, method, rel_path, body=None):
        full_path = urlparse.urljoin(self.endpoint, rel_path)
        kwargs = {'headers': {}}

        if body is not None:
            kwargs['data'] = json.dumps(body)
            kwargs['headers']['content-type'] = \
                    'application/vnd.changeling.v0+json'

        return requests.request(method, full_path, **kwargs)

    @property
    def model(self):
        if self._model is None:
            schema = self.get_schema()
            self._model = warlock.model_factory(schema)
        return self._model

    def get_schema(self):
        response = self._request('GET', '/schemas/change')
        return response.json()

    def list_changes(self):
        response = self._request('GET', '/changes')
        return [self.model(change) for change in response.json()]

    def get_change(self, change_id):
        response = self._request('GET', '/changes/%s' % change_id)
        return self.model(response.json())

    def delete_change(self, change):
        self._request('DELETE', '/changes/%s' % change.id)

    def create_change(self, change):
        response = self._request('POST', '/changes', dict(change))
        return self.model(response.json())
