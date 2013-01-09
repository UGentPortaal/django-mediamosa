from distutils.core import setup

long_desc = open('README.md').read()

setup(
    name='django-mediamosa',
    version='0.0.1',
    author='UGent Portaal Team',
    author_email='portaal-tech@ugent.be',
    packages=['django_mediamosa', 'tests'],
    scripts=[],
    url='http://www.mediamosa.org',
    license='LICENSE.txt',
    description='Django integration support for MediaMosa.',
    long_description=long_desc
)