from distutils.core import setup
setup(
  name = 'waPy', 
  packages = ['waPy'],   
  version = '0.1',      
  license='MIT',       
  description = 'A module that interfaces Python functions to Whatsapp', 
  author = 'Braitenberg',                  
  author_email = 'braitenberg@gmail.com',      
  url = 'https://github.com/Braitenberg/waPy',   
  download_url = 'https://github.com/user/reponame/archive/v_01.tar.gz',    # I explain this later on
  keywords = ['whatsapp', 'web', 'bot', 'chatbot'],  
  install_requires=[         
          'selenium',
          'beautifulsoup4',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',   
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',  
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)