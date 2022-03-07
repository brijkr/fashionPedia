images = []
 for i in range(1,1001):
     url = './clothing-co-parsing/photos/%04d.jpg'%(i)
     img = cv2.imread(url)
     img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
     images.append(tf.convert_to_tensor(img)) 
