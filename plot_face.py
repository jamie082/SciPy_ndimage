"""
Displaying a Racoon Face
========================

Small example to plot a racoon face.


"""
from scipy import misc,ndimage
import imageio
img = misc.face()
imageio.imsave('face.png', img)
import matplotlib.pyplot as plt

# use filter
blur_G = ndimage.gaussian_filter(img,sigma=7)
rotate_face = ndimage.rotate(img, 45)

plt.subplot(131)
plt.imshow(blur_G, cmap=plt.cm.gray)

plt.subplot(132)
plt.imshow(rotate_face, cmap=plt.cm.gray, vmin=30, vmax=200)
plt.show()