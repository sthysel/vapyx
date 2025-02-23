from pprint import pformat

from loguru import logger


class APIItems:
    """map of API items"""
    def __init__(self, raw, request, path, item_cls) -> None:
        self._request = request
        self._path = path
        self._item_cls = item_cls
        self._items = {}
        self.process_raw(raw)

    def update(self, path=None) -> None:
        path = path or self._path
        raw = self._request('get', path)
        self.process_raw(raw)

    def process_raw(self, raw: dict) -> None:
        for id, raw_item in raw.items():
            obj = self._items.get(id)

            if obj is not None:
                obj.raw = raw_item
            else:
                self._items[id] = self._item_cls(id, raw_item, self._request)

    def values(self):
        return self._items.values()

    def __getitem__(self, obj_id: str):
        return self._items[obj_id]

    def __iter__(self):
        return iter(self._items)
