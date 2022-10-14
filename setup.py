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
    download_url = 'https://github.com/AldimGeldi/reponame/archive/v_01.tar.gz',   
    keywords = ['serverless', 'cache', 'serverless-db','serverless-cache'],   
    install_requires=[            
        'simplejson',
        'boto3',
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',      
        'Intended Audience :: Developers',      
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',   
        'Programming Language :: Python :: 3',      

    ],
)
