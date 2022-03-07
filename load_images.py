import cv2
import tensorflow as tf
import pandas as pd
import numpy as np
    
def generate_masks(data, imgPath, label):
    masks=[]
    images = []
    for imageId in data['ImageId']:
        enc_pxl=data.loc[data['ImageId']==imageId,'EncodedPixels'].tolist()
        enc_px_lst=list(map(int, enc_pxl[0].split(' ')))
        pixel,pixel_count = [],[]
        [pixel.append(enc_px_lst[i]) if i%2==0 else pixel_count.append(enc_px_lst[i]) for i in range(0, len(enc_px_lst))]
        rle_pixels = [list(range(pixel[i],pixel[i]+pixel_count[i])) for i in range(0, len(pixel))]
        rle_mask_pixels = sum(rle_pixels,[])
        h=int(data.loc[data['ImageId']==imageId,'Height'].tolist()[0])
        w=int(data.loc[data['ImageId']==imageId,'Width'].tolist()[0])
        img=cv2.imread(imgPath + imageId + '.jpg')
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        mask_img = np.zeros((h*w,1), dtype=np.uint8)
        mask_img[rle_mask_pixels] = label
        mask = np.reshape(mask_img, (w, h)).T
        masks.append(tf.convert_to_tensor(mask))
        images.append(tf.convert_to_tensor(img))
    return images, masks
   
    
 
