from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()

setup(name='UTide',
      version='v1p0',
      description='Python distribution of the MatLab package UTide.',
      long_description=readme(),
      url='https://github.com/wesleybowman/UTide',
      author='Wesley Bowman',
      author_email='wesley.bowman23@gmail.com',
      maintainer='Wesley Bowman',
      license='MIT',
      packages=['utide'],
      package_data={'utide': ['data/*.mat']},
      zip_safe=False)
