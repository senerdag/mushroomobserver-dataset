# mushroomobserver-dataset
Collection of mushroom pictures separated into types.   Collected from https://mushroomobserver.org/
# **Main description**
This repository is for downloading thousands of images of thousands of types from https://mushroomobserver.org which is well-established for classifying images with deep learning. You can easily use these codes and create your own CNN model. Below is a description of the two codes. Download path is where you download the code.

##NOTE* on full-resolution original image downloads 10/2024
As of 10/2024 Mushroom Observer discourages bulk downloads of original resolution images, as this bandwidth from google cloud cost their hosting large sums. <https://mushroomobserver.org/articles/41>.

As of 10/2024, original image paths as scraped in original scripts will fail to resolve.

 Mushroom Observer provides .tsv lists of paths for automated bulk download of images for ML model training. Scripts that include '640' have been updated to redirect to the 640p images preferred for bulk download. The original scripts can still be used (not anonymously), but likely will require altering the request to include an api key or pass a login cookie.

# Search and collect pictures by specie
Using 'search_and_collect_pictures_by_specie.py', Especially if you are going to deal with only a few species in your deep learning model, just write your specie name as I have shown in the part of this code below.(Just put one specie)


```
if __name__ == "__main__": 
  species_name = "Amanita muscaria"   # ======>  Please type here the specie of mushroom you want before running the code.
  main(species_name)
 ```

So you can scrape images of the species you are looking for. You can also view the species on this [site](https://mushroomobserver.org/names?with_observations=true)

#Batch Downloading Workflow for a subset of species
Download the and unzip the .tsv of observations for ML training here: <https://mushroomobserver.org/articles/20>.

Filter in any spreadsheet software to ID the species of interest and save the column of species as a .csv. 

The goal of this feature is to allow training a model for local use, based on reported distribution of species for forays in a particular locale. 

USGRIN, plantdb, local biodiversity databases and university extensions generally have this information. Academic sources for distribution of fungal population should allow correcting weights to reflect actual distribution of a species in an area in confidence values, to combat bias from frequency of observation overall (or training focus on particularly identifiable species), while still including all images in the data in the training set.

Filter for unique values (or use something like listmaker.sh) to prune the list, and point the -batch-640.py file to this list of species to download all images from identified species sorted into folders.

-640.py points at the 480x640p images preferred paths for ML training data, while -orig.py should allow batch downloading at the original paths if they are restored or login credentials are passed.


# Collecting all images according to their specie
This code file goes to https://mushroomobserver.org and starting from the first image, it creates a folder of that image type and downloads the image into it. It does this until it downloads all the images on the site. Of course, you can stop the code anywhere you want.

# Dataset 
I haven't downloaded the whole dataset yet. I'll give you dropbox link when I do. If you have questions and suggestions, please specify in the Issues section.

