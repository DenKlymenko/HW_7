from setuptools import setup, find_namespace_packages

setup(name='clean_folder',
      version='0.0.1',
      description='Our first Package',
      #packages=find_namespace_packages(),
      packages=['clean_folder'],
      entry_points={'console_scripts': ['clean_folder=clean_folder.clean:start']}
      #entry_points={'console_scripts': ['helloworld = useful.some_code:hello_world']}
      )