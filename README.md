# mushroomobserver-dataset
Collection of mushroom pictures separated into types.   Collected from https://mushroomobserver.org/
# **Main description**
This repository is for downloading thousands of images of thousands of types from https://mushroomobserver.org which is well-established for classifying images with deep learning. You can easily use these codes and create your own CNN model. Below is a description of the two codes. Download path is where you download the code.

# Search and collect pictures by specie
Especially if you are going to deal with only a few species in your deep learning model, just write your specie name as I have shown in the part of this code below.(Just put one specie)


```
if __name__ == "__main__": 
  species_name = "Amanita muscaria"   # ======>  Please type here the specie of mushroom you want before running the code.
  main(species_name)
 ```

So you can scrape images of the species you are looking for. You can also view the species on this [site]([https://www.gooogle.com](https://mushroomobserver.org/names?with_observations=true)).

# Collecting all images according to their specie
This code file goes to https://mushroomobserver.org and starting from the first image, it creates a folder of that image type and downloads the image into it. It does this until it downloads all the images on the site. Of course, you can stop the code anywhere you want.

# Dataset 
I haven't downloaded the whole dataset yet. I'll give you dropbox link when I do. If you have questions and suggestions, please specify in the Issues section.

