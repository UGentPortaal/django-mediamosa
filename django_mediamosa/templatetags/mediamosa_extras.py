from django import template

register = template.Library()


@register.filter
def mimetype(value, mime_type):
    mediafiles = []
    for mediafile in value:
        if mediafile.metadata.get('mime_type') == mime_type:
            mediafiles.append(mediafile)
    return mediafiles
