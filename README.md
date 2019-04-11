# Etrog Or Lemon

## Dataset Creation  
  - Downloaded with googleimagesdownload (chromedriver, selenium needed as well).  
  - Filtered incorrect images
  - Download logs under `dataset_download_logs`
  - New dataset can be generated with:  
    `source scripts/download_dataset.sh`
 
 ## Training
  - Done with resnet34 model. (fastai)
  - details under `nbs/etrog_or_lemon.ipynb`

## Web app
  - Starlette application.
  - Install python packages:  
    `pip install .` 
  - Run server:  
    `python src/server.py serve`
