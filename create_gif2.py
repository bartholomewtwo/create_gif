# import imageio 
import imageio.v3 as iio

# access the files needed
filenames = ['dog1.png', 'dog2.png']
images = [ ]

# load images
for filename in filenames:
  images.append(iio.imread(filename))

# create the gif
iio.imwrite('dog.gif', images, duration = 500, loop = 0)