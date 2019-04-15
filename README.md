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

## Heroku
  - create heroku project. needs custom buildpack in order to reduce sludge:  
    `heroku create etrog-or-lemon --buildpack https://github.com/nyutal/heroku-buildpack-python-etrog-or-lemon.git`  
    (Actually it doesn't true, I overcome the sludge issue by changing the torch requirement to non-gpu smaller version, but it was a good practice...)
  - push the project:  
    `git push heroku master`
    Right now it doesn't work on free dyno (heroku container) due memory violation...
  