import json

from mediamosa.resources import MediaMosaResource


class MediaMosaResourceEncoder(json.JSONEncoder):

    def default(self, obj):
        if isinstance(obj, MediaMosaResource):
            return obj.__dict__.get('data')
        else:
            return super(MediaMosaResourceEncoder, self).default(obj)


