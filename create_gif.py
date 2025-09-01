# import imageio 
import imageio.v3 as iio

# access the files needed
filenames = ['nyan-cat1.png', 'nyan-cat2.png', 'nyan-cat3.png']
images = [ ]

# load images
for filename in filenames:
  images.append(iio.imread(filename))

# create the gif
iio.imwrite('nyan-cat.gif', images, duration = 500, loop = 0)