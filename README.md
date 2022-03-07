# fashionPedia
Segmentation of fashionPedia datset
This is not the full fashionPedia dataset. I have selected 200 images from 2 classes (100 from each classes). image data have different sizes of images and corresponding annotations are in csv format and this csv file have size of 1.33GB. Since this file can't be uploaded due to big size. I created two small size csv files for 2 classes having 250 images in each. processing these files to create corresponding masks require a lot of time and memory, keepig this in mind I have randomly selected 100 images from each images and used generate_maks function to create masks and generate two lists of images and masks data. in this same function, masks are encoded with different labels(1 & 2) for both classes respectively. 

After this, I have resized images and masks to size 256x256 and 128x128.


