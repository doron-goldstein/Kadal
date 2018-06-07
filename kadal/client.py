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
    def __init__(self, session=None, *, lib='asyncio', loop=None):
        if lib not in ('asyncio', 'multio'):
            raise ValueError("lib must be of type `str` and be either `asyncio` or `multio`, "
                             "not `{}`".format(lib if isinstance(lib, str) else lib.__class__.__name__))
        self._lib = lib
        if lib == 'asyncio':
            import asyncio
            loop = loop or asyncio.get_event_loop()
        self.session = session or self._make_session(lib, loop)

    @staticmethod
    def _make_session(lib, loop=None):
        if lib == 'asyncio':
            try:
                import aiohttp
            except ImportError:
                raise ImportError("To use Kadal in asyncio mode, it requires the `aiohttp` module.")
            return aiohttp.ClientSession(loop=loop)
        try:
            import asks
        except ImportError:
            raise ImportError("To use Kadal in curio/trio mode, it requires the `asks` module.")
        return asks.Session()

    async def _request(self, query, **variables):
        return await self.session.post(URL, json={"query": query, "variables": variables})

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
        if self._lib == 'asyncio':
            data = await r.json()
        else:
            data = r.json()
        if data.get('errors'):
            self.handle_error(data['errors'][0])
        return Media(data)

    async def get_manga(self, id):
        r = await self._request(BY_ID, id=id, type='MANGA')
        if self._lib == 'asyncio':
            data = await r.json()
        else:
            data = r.json()
        if data.get('errors'):
            self.handle_error(data['errors'][0])
        return Media(data)

    async def search_anime(self, query):
        r = await self._request(SEARCH, search=query, type='ANIME')
        if self._lib == 'asyncio':
            data = await r.json()
        else:
            data = r.json()
        if data.get('errors'):
            self.handle_error(data['errors'][0])
        return Media(data)

    async def search_manga(self, query):
        r = await self._request(SEARCH, search=query, type='MANGA')
        if self._lib == 'asyncio':
            data = await r.json()
        else:
            data = r.json()
        if data.get('errors'):
            self.handle_error(data['errors'][0])
        return Media(data)
