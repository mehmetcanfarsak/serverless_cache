from distutils.core import setup
setup(
    name = 'serverless_cache',
    packages = ['serverless_cache'],
    version = '1.1',
    license='MIT',
    description = 'Using DigitalOcean s3 spaces service just 5$ unlimited cache service package',
    author = 'AldimGeldi',
    author_email = 'teknik@aldimgeldi.com',
    url = 'https://github.com/AldimGeldi/serverless_cache',
    download_url = 'https://github.com/AldimGeldi/reponame/archive/v_01.tar.gz',    # I explain this later on
    keywords = ['serverless', 'cache', 'serverless-db','serverless-cache'],   # Keywords that define your package best
    install_requires=[            # I get to this in a second
        'simplejson',
        'boto3',
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        'Intended Audience :: Developers',      # Define that your audience are developers
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',   # Again, pick a license
        'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)