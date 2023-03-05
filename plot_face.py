"""
Displaying a Racoon Face
========================

Small example to plot a racoon face.


"""
from scipy import misc,ndimage
import imageio
img = misc.face()
img_2 = misc.face(gray=True).astype(float)
imageio.imsave('face.png', img)
import matplotlib.pyplot as plt

# use filter
blur_G = ndimage.gaussian_filter(img_2,sigma=7)
rotate_face = ndimage.rotate(img, 45)
blur = ndimage.gaussian_filter(img, 5)

# one filter
plt.subplot(131)
plt.imshow(blur_G, cmap=plt.cm.gray)

# two filter

plt.subplot(132)
plt.imshow(rotate_face, cmap=plt.cm.gray, vmin=30, vmax=200)

# three filter
blur_G = ndimage.gaussian_filter(blur, 1)
alpha = 30
plt.subplot(133)
sharp = blur+alpha*(blur-blur_G)

plt.imshow(sharp) # sharpening the image with NumPy and SciPy
plt.show()