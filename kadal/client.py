import asks

from kadal.query import SEARCH, BY_ID
from kadal.media import Media

URL = 'https://graphql.anilist.co'


class KadalError(Exception):
    def __init__(self, message, status):
        self.message = message
        self.status = status


class MediaNotFound(KadalError):
    pass


class Client:
    def __init__(self):
        self.lib = asks

    async def _request(self, query, **variables):
        return await self.lib.post(URL, json={"query": query, "variables": variables})

    @staticmethod
    def handle_error(error):
        msg = error['message']
        status = error['status']
        if status == 404:
            raise MediaNotFound(msg, status)
        else:
            raise KadalError(msg, status)

    async def get_anime(self, id):
        r = await self._request(BY_ID, id=id, type='ANIME')
        data = r.json()
        if data.get('errors'):
            self.handle_error(data['errors'][0])
        return Media(data)

    async def get_manga(self, id):
        r = await self._request(BY_ID, id=id, type='MANGA')
        data = r.json()
        if data.get('errors'):
            self.handle_error(data['errors'][0])
        return Media(data)

    async def search_anime(self, query):
        r = await self._request(SEARCH, search=query, type='ANIME')
        data = r.json()
        if data.get('errors'):
            self.handle_error(data['errors'][0])
        return Media(data)

    async def search_manga(self, query):
        r = await self._request(SEARCH, search=query, type='MANGA')
        data = r.json()
        if data.get('errors'):
            self.handle_error(data['errors'][0])
        return Media(data)
