from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
import osdef load_images_from_folder(folder):
images = []
for filename in os.listdir(folder):
img = load_img(os.path.join(folder,filename), target_size (224, 224)) 
img = img_to_array(img)
img = img.reshape((1,) + img.shape)
if img is not None:
images.append(img)
return images