from setuptools import setup, find_packages

setup(
    name='seiryu',
    version='0.2',
    packages=find_packages(),
    description='The Pinnacle of Advanced Hash Generation and Cryptographic Precision',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Veilwr4ith',
    author_email='hidetheveil@gmail.com',
    url='https://github.com/veilwr4ith/seiryu',
    license='GNU General Public license',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: GNU General Public License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.10',
    install_requires=[
        'numpy', 'argon2', 'argon2-cffi', 'bcrypt', 'passlib', 'siphashc', 'spookyhash', 'uuid', 'xxhash', 'argon2-cffi-bindings', 'cffi'
    ],
)

