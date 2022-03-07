import cv2
import tensorflow as tf
images = []
 for i in range(500):
     url = './data/train/%04d.jpg'%(i)
     img = cv2.imread(url)
     img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
     images.append(tf.convert_to_tensor(img)) 
