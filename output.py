from scipy import misc,ndimage
import matplotlib.pyplot as plt

img = misc.face()
rotate_img = ndimage.rotate(img, 90) # rotating the image

fig = plt.figure()
plt.imshow(img)
fig=plt.figure()
plt.imshow(rotate_img)
plt.show()