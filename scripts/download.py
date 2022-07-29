# The following code is based from https://github.com/akiratwang/MAST30034_Python/tutorials/
# and modified by Haonan Zhong
from urllib.request import urlretrieve
import os

output_relative_dir = '../data/'

YEARS = range(2016, 2020)
MONTHS = range(1, 13)

# this is the URL template of the download destination
URL_TEMPLATE = "https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_"

# data output directory is `data/raw/`
raw_output_dir = output_relative_dir + 'raw/'
for year in YEARS:
    for month in MONTHS:
        month = str(month).zfill(2)
        print(f"Begin year {year} month {month}")
        # generate url
        url = f'{URL_TEMPLATE}{year}-{month}.parquet'
        # generate output location and filename
        output_dir = f"{raw_output_dir}/{year}-{month}.parquet"
        # download
        urlretrieve(url, output_dir) 
        
        print(f"Completed year {year} month {month}")