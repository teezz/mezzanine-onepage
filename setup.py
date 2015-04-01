from setuptools import setup

setup(name='mezzanine-onepage',
      version='0.0.2',
      description='one-page design helper for Mezzanine',
      url='http://github.com/lucmilland/mezzanine-onepage',
      author='Luc Milland',
      author_email='luc@hekenet.com',
      license='BSD',
      packages=['onepage'],
      install_requires=['mezzanine'],
      zip_safe=False,
      package_data={'onepage' : ['templates/pages/*.html']},
      )