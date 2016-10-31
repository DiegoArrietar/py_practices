try:
    from setuptools import setup
except ImportError:
    from distutils.core import setuptools

config  = {
    'description':'My project',
    'author':'Diego Arrieta',
    'url':'myproject.com',
    'download_url':'Where to download it.',
    'author_email':'diego.arrieta.r@gmail.com',
    'version':'0.1',
    'install_requires':['nose'],
    'packages':['EX47'],
    'scripts':[],
    'name':'projectname'
}

setup(**config)
