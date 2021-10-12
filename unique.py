import numpy as np
import glob
from PIL import Image
import os

if os.path.isdir('identicalImages')==False:
    os.mkdir('identicalImages')

imList = glob.glob('alien_images/*.png')

x = np.array([np.array(Image.open(fname)) for fname in imList])

for i in range(len(x)):
    for j in range(len(x)):
        if i != j:
            b = np.array_equal(x[i], x[j])
            if (b == True):
                print('Idectical images found')
                new_image = Image.fromarray(x[i])
                new_image = new_image.resize((512, 512), resample=0)
                imgname = 'identicalImages/identicalImage_' + str(i) + '.png'
                new_image.save(imgname)
