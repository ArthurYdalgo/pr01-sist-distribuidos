
import uuid
import hashlib


class CRUD():
    def __init__(self):
        self.users = {}

    def store(self, data):
        new_user_uuid = int(hashlib.sha1(
            (str(uuid.uuid4())).encode("utf-8")).hexdigest(), 16) % (10 ** 4)
        data['uuid'] = new_user_uuid
        self.users[new_user_uuid] = data
        return {'data': data}

    def update(self, user_uuid, data):
        user_uuid = int(user_uuid)
        if(user_uuid in self.users):
            self.users[user_uuid] = data
            return {'data': user_uuid}

        return {'data': 'none'}

    def destroy(self, user_uuid):
        user_uuid = int(user_uuid)
        if(user_uuid in self.users):
            del self.users[user_uuid]
            return {'data': user_uuid}
        return {'data': 'none'}

    def get(self, user_uuid):
        user_uuid = int(user_uuid)
        if(user_uuid in self.users):
            return {'data': self.users[user_uuid]}
        return {'data': 'none'}
