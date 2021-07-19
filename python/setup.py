
import os
import tarfile
import urllib
import opendatasets as od

def fetch_crop_data():
    os.makedirs('data-raw', exist_ok = True)
    os.system('kaggle datasets download -d abhinand05/crop-production-in-india -p data-raw')
