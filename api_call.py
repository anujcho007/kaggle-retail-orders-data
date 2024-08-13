import kaggle

kaggle.api.authenticate()
kaggle.api.dataset_download_files(
    'ankitbansal06/retail-orders', path='.', unzip=True)
