import os
import urllib.request
import sys
import tarfile


def extract_files(data_files):
    
    if os.path.isdir(data_files.split('.')[0]):
        print("Skipping %s already present" % data_files.split('.')[0])
        return
    if (data_files.endswith("tar.gz")):
        print("Extracting %s ..." % data_files)
        tar = tarfile.open(data_files, "r:gz")
        tar.extractall()
        tar.close()

def load_file(datasets):

    #URL to access the files
    url="http://ufldl.stanford.edu/housenumbers/"
    
    # Making directory to store data files
    if not os.path.exists('data'):
        print("Making Directory-data to store the datasets...")
        os.makedirs('data')
        
    # Loading tar files
    for dataset in datasets:
        print("Loading %s tar file...." %dataset)
        urllib.request.urlretrieve("http://ufldl.stanford.edu/housenumbers/"+dataset+".tar.gz", "data/"+dataset+".tar.gz")
        print("%s tar file loaded!" %dataset)
    
    
    # Get list of all tar.gz files for the dataset folder
    list_data = [files for files in os.listdir("data") if 'tar.gz' in files]


    #getting into the data directory  
    os.chdir("data")
    for data_files in list_data:
        extract_files(data_files)
    #moving to parent directory
    os.chdir(os.path.pardir)