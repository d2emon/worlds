import uuid


class Database:
    def __init__(self, items):
        self.items = [self.sanitize(item) for item in items]

    @classmethod
    def sanitize(cls, data):
        # return {
        #     'id': uuid.uuid4().hex,
        #     'title': data.get('title'),
        #     'author': data.get('author'),
        #     'read': data.get('read')
        # }
        item = {
            'id': uuid.uuid4().hex,
        }
        item.update(data)
        return item

    def by_item_id(self, item_id):
        # return next((item for item in self.items if item.get('slug') == slug), None)
        return next((item for item in self.items if item.get('id') == item_id), None)

    def delete(self, item_id):
        item = next((item for item in self.items if item['id'] == item_id), None)
        if item is None:
            return False

        self.items.remove(item)
        return True

    def add(self, data):
        self.items.append(self.sanitize(data))
        return True

    def edit(self, item_id, data):
        self.delete(item_id)
        self.add(data)
        return True

    def all(self):
        return self.items
