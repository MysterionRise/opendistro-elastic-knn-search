# How to use KNN search for efficient similarity search in Open Distro Elastic?

Instead of full vectors search (linear time) we are going to use k-NN which is a type of instance-based learning, or lazy learning, where the function is only approximated locally and all computation is deferred until function evaluation. Since this algorithm relies on distance for classification, if the features represent different physical units or come in vastly different scales then normalizing the training data can improve its accuracy dramatically

## How to run the demo:

1. `pip install -r requirements.txt`
2. Run Elastic OpenDistro cluster by doing `docker-compose -f opendistro-docker/docker-compose.yml up`
3. Create KNN index by using `scripts/create_index.sh`
4. Index Game Of Thrones data set by running `python index_data.py`
5. Do the KNN search for similarity in vectors by `python search_data.py`. Replace test message with anything you want