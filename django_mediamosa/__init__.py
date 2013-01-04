__all__ = ('VERSION',)

try:
    VERSION = __import__('pkg_resources') \
        .get_distribution('django-mediamosa').version
except Exception, e:
    VERSION = 'unknown'
