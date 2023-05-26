import httpx


class Service:
    def __init__(self):
        self.client = httpx.Client()

    # async def request(self, method: str, url: str, **kwargs):
    #     return await self.client.request(method, url, **kwargs)
