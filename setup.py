from setuptools import setup, find_packages


setup(
    name='color-temp',
    version='0.1.0',
    description=('Convert color from RGB to Kelvin and back'),
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    keywords='color temperature',
    author='Jon Robison',
    author_email='narfman0@gmail.com',
    url='https://github.com/narfman0/color-temp',
    license='LICENSE',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=True,
    install_requires=[
        'colour-science',
        'numpy',
    ],
    test_suite='tests',
)
