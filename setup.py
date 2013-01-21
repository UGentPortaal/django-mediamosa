from setuptools import setup

with open('README.rst', 'r') as file:
    long_desc = file.read()

version = __import__('django_mediamosa').get_version()

setup(
    name='django-mediamosa',
    version=version,
    author='UGent Portaal Team',
    author_email='portaal-tech@ugent.be',
    packages=['django_mediamosa', 'tests'],
    scripts=[],
    url='https://github.com/UGentPortaal/django-mediamosa',
    license='BSD',
    description='Django integration support for the mediamosa api.',
    long_description=long_desc,
    install_requires=(
        'mediamosa>=0.0.2'
    ),
    classifiers=[
          'Development Status :: 3 - Alpha',
          'Environment :: Web Environment',
          'Framework :: Django',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: BSD License',
          'Operating System :: MacOS :: MacOS X',
          'Operating System :: Microsoft :: Windows',
          'Operating System :: POSIX',
          'Programming Language :: Python',
          'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
          'Topic :: Multimedia :: Video',
          'Topic :: Software Development :: Libraries',
          'Topic :: Utilities'
    ],
)
