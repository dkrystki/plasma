from datetime import datetime
from typing import Dict, Any, Optional, List

from furl import furl
from requests import Session, Response
from requests.adapters import HTTPAdapter

from dataclasses import dataclass
from requests.auth import AuthBase


@dataclass
class Photo:
    name: str
    draft: bool
    caption: str
    image: str
    id: Optional[int] = None
    publish_date: Optional[datetime] = None
    username: Optional[str] = None

    def get_paylaod(self) -> Dict[str, Any]:
        payload = {
            "data": {
                "name": self.name,
                "draft": self.draft,
                "caption": self.caption,
            },
            'files': {
                "image": open(self.image, 'rb')
            }
        }
        return payload


class BearerAuth(AuthBase):
    def __init__(self, token) -> None:
        self.token = token

    def __call__(self, r):
        r.headers["authorization"] = "Bearer " + self.token
        return r


class Photos:
    def __init__(self, api_client: 'PhotosApiClient') -> None:
        self._api_client = api_client
        self._base_url = furl("photos/")

    def create(self, photo: Photo) -> None:
        payload = photo.get_paylaod()
        self._api_client.post(self._base_url, data=payload['data'], files=payload['files'])

    def list(self) -> List[Photo]:
        response = self._api_client.get(self._base_url)

        ret: List[Photo] = []
        for payload in response:
            payload["image"] = payload["thumbnail"]
            del payload["thumbnail"]
            ret.append(Photo(**payload))
        return ret

    def delete(self, photo: Photo) -> None:
        url = furl(self._base_url).add(path=str(photo.id))
        self._api_client.delete(url)


class PhotosApiClient:
    def __init__(self, username: str, password: str, api_url: str) -> None:
        self.photos = Photos(api_client=self)

        self.username = username
        self.password = password

        self._access_token: Optional[str] = None
        self._refresh_token: Optional[str] = None

        self._base_url = furl(api_url)
        self._auth_url = furl("token/")

        self._session = Session()

        adapter = HTTPAdapter(max_retries=3)
        self._session.mount("http://", adapter)
        self._session.mount("https://", adapter)

        self._authenticate()

    def _authenticate(self) -> None:
        if not self._access_token:
            response = self.post(self._auth_url, {
                "username": self.username,
                "password": self.password
            }, auth=False)

            self._access_token = response["access"]
            self._refresh_token = response["refresh"]

    def post(self, endpoint: furl, data: Dict[str, Any], files: Dict[str, Any] = None,
             auth: bool = True) -> Dict[str, Any]:
        # TODO: implement refreshing
        url = furl(self._base_url)
        url.add(path=str(endpoint))

        kwargs = {}
        if auth:
            kwargs.update({
                "auth": BearerAuth(self._access_token)
            })

        if files:
            kwargs.update({"data": data, "files": files})
        else:
            kwargs.update({"json": data})

        response: Response = self._session.post(str(url), **kwargs)
        response.raise_for_status()

        return response.json()

    def get(self, endpoint: furl) -> Dict[str, Any]:
        # TODO: implement refreshing

        url = furl(self._base_url)
        url.add(path=str(endpoint))
        response: Response = self._session.get(str(url), auth=BearerAuth(self._access_token))
        response.raise_for_status()
        return response.json()

    def delete(self, endpoint: furl) -> None:
        url = furl(self._base_url)
        url.add(path=str(endpoint))
        response: Response = self._session.delete(str(url), auth=BearerAuth(self._access_token))
        response.raise_for_status()
