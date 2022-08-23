# The following code is based from https://github.com/akiratwang/MAST30034_Python/tutorials/
# and modified by Un Leng Kam
from urllib.request import urlretrieve
import os
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

# data output directory is `data/raw/`
output_relative_dir = '../data/'

YEARS = range(2016, 2018)
MONTHS_2016 = range(1, 13)
MONTHS_2017 = range(1, 6)

# this is the URL template of the download destination
URL_TEMPLATE = "https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_"


if not os.path.exists(output_relative_dir):
    os.makedirs(output_relative_dir)

target_dir = output_relative_dir + 'raw'
if not os.path.exists(target_dir):
    os.makedirs(target_dir)


for month in MONTHS_2016:
    month = str(month).zfill(2)
    print(f"Begin year {2016} month {month}")
    # generate url
    url = f'{URL_TEMPLATE}{2016}-{month}.parquet'
    # generate output location and filename
    output_filename = f"{target_dir}/{2016}-{month}-yellow_taxi.parquet"
    # download
    urlretrieve(url, output_filename) 
    
    print(f"Completed year {2016} month {month}")

for month in MONTHS_2017:
    month = str(month).zfill(2)
    print(f"Begin year {2017} month {month}")
    # generate url
    url = f'{URL_TEMPLATE}{2017}-{month}.parquet'
    # generate output location and filename
    output_filename = f"{target_dir}/{2017}-{month}-yellow_taxi.parquet"
    # download
    urlretrieve(url, output_filename) 
    
    print(f"Completed year {2017} month {month}")