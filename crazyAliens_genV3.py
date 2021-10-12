# Built with python 3, dependencies installed with pip 
# library to generate images - Pillow 
# https://pillow.readthedocs.io/en/stable/installation.html
from PIL import Image

# library to work with arrays 
# https://numpy.org/
import numpy as np

# library to interact with the operating system
import os

# library to generate random integer values
from random import seed
from random import randint
from random import choice

# gets path to be used in image creation mechanism, using os.
dirname = os.path.dirname(__file__)
# dirname = os.path.dirname('~/nftCol/crazyAliens/alien_images')

# sets final image dimensions as 480x480 pixels
# the original 24x24 pixel image will be expanded to these dimensions
dimensions = 512, 512

# ram is the list that is stored all the unique combinations (e.g hat, eyes etc)
# of the image
ram = []

# Colors
# background (grey)
bg = (220, 220, 220)

# body
# olive green
bd_green = (50,205,50)
# sea blue
bd_sea_blue = (30,144,255)
# dark blue
bd_dark_blue = (0,0,139)
# orange color
bd_orange  = (255,101,0)
# yellow
#bd_yellow = (254, 222, 0)
bd_yellow = (204,204,0)

bd_colors = [bd_green, bd_sea_blue, bd_dark_blue, bd_orange, bd_yellow]

# boots and fingers
bt = (91, 39, 125)
fg = (91, 39, 125)

# mouth color
# mt = (145, 31, 31) 
mt = (0, 0, 0)
# teeth
th = (255, 255, 215)
#vglasses
gl = (0, 0, 0)
# tounge
to = (227, 11, 92)

# hats
# standard colors
ha = (0, 0, 0)
# red and green
rh_colors = [(241, 13, 12), (50,205,50)]
# grey
gr = (153, 153, 153)
# dark red
dr = (81, 3, 7)

# lips color
lp = (178,34,34)
# hands color
hd = (128,128,128)
# feet color
ft = (128,128,128)
# mustache color
mu = (0, 0, 0)

# beard color
be = (0, 0, 0)

# pupils colors
pu_black = (0, 0, 0)
# green pupils
pu_green = (43, 81, 26)
# brown pupils
pu_brown = (103, 54, 4)
# red pupils
pu_red = (241, 13 ,12)
# blue pupils
pu_blue = (41, 121, 255)

i = 0
j = 0 # a counter only for iterations
iterations = 750
while(i < iterations):
    # In each iteration iterRam must be empty in order
    # to store the random combination of the image
    iterRam = []

    # Using ETH block number as starting number for seed
    b = 13280437
    seed(i + b) # different seed in each iteration
 
    pu_colors = [pu_black, pu_green, pu_brown, pu_blue, pu_red]
    
    # use random.choice to pick an item from bd_colors list randomly
    bd = choice(bd_colors)
    
    # neck
    # Here I add brightness with the formula below
    nk = (min(255, 1.5* bd[0]),  min(255, 1.5*bd[1]), min(255, 1.5*bd[2]))

    # nose
    # Here I remove brightness with the formula below
    ns = (min(255,  bd[0])/1.5,  min(255, bd[1])/1.5, min(255, bd[2])/1.5)
    
    
    # choose between white and red eyes
    c = randint(0,1000)
    seed(c)

    if c < 900:
         # white colors
         ey = (255,255,215)
         pu = choice(pu_colors)
    else:
        # red eyes
        ey = (186, 19, 26)
       # if the eyes are red, then remove the red pupil because is quite evil
        pu_colors.pop(4)
        pu = choice(pu_colors)

    # baseball hat color
    d = randint(0, 1000)
    seed(d)
    rh = choice(rh_colors)
    

    basic = [
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, ey, ey, ey, ey, ey, bg, bg, bg, ey, ey, ey, ey, ey, bg, bg, bg, ey, ey, ey, ey, ey, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, ey, ey, ey, ey, ey, bg, bg, bg, ey, ey, ey, ey, ey, bg, bg, bg, ey, ey, ey, ey, ey, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, ey, ey, ey, ey, ey, bg, bg, bg, ey, ey, ey, ey, ey, bg, bg, bg, ey, ey, ey, ey, ey, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, pu, pu, ey, ey, ey, bg, bg, bg, pu, pu, ey, ey, ey, bg, bg, bg, pu, pu, ey, ey, ey, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, pu, pu, ey, ey, ey, bg, bg, bg, pu, pu, ey, ey, ey, bg, bg, bg, pu, pu, ey, ey, ey, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bd, bg, bg, bg, bg, bg, nk, bg, bg, bg, bg, bg, bd, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bd, bd, bg, bg, bg, bg, nk, bg, bg, bg, bg, bd, bd, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, fg, hd, bg, bg, bg, bg, bg, bd, bg, bg, bg, bg, nk, bg, bg, bg, bg, bd, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],      
        [bg, bg, bg, bg, hd, bg, bg, bg, bg, bg, bd, bg, bd, bd, bg, nk, bg, bd, bd, bg, bd, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, hd, hd, hd, hd, bd, bd, bd, bd, bd, bd, ns, nk, ns, bd, bd, bd, bd, bd, bd, hd, hd, hd, hd, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bg, bg, bg, hd, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bg, bg, hd, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bg, bg, fg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ft, bg, bg, bg, bg, bg, ft, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ft, bg, bg, bg, bg, bg, ft, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bt, bg, bg, bg, bg, bg, bt, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bt, bt, bg, bg, bg, bg, bg, bt, bt, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg]
        ]
    
    evil = [
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bd, bd, bd, bd, bd, bg, bg, bg, bd, bd, bd, bd, bd, bg, bg, bg, bd, bd, bd, bd, bd, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bd, bd, bd, bd, bd, bg, bg, bg, bd, bd, bd, bd, bd, bg, bg, bg, bd, bd, bd, bd, bd, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bd, bd, bd, bd, bd, bg, bg, bg, bd, bd, bd, bd, bd, bg, bg, bg, bd, bd, bd, bd, bd, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, pu, pu, ey, ey, ey, bg, bg, bg, pu, pu, ey, ey, ey, bg, bg, bg, pu, pu, ey, ey, ey, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, pu, pu, ey, ey, ey, bg, bg, bg, pu, pu, ey, ey, ey, bg, bg, bg, pu, pu, ey, ey, ey, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bd, bg, bg, bg, bg, bg, nk, bg, bg, bg, bg, bg, bd, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bd, bd, bg, bg, bg, bg, nk, bg, bg, bg, bg, bd, bd, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, fg, hd, bg, bg, bg, bg, bg, bd, bg, bg, bg, bg, nk, bg, bg, bg, bg, bd, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],      
        [bg, bg, bg, bg, hd, bg, bg, bg, bg, bg, bd, bg, bd, bd, bg, nk, bg, bd, bd, bg, bd, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, hd, hd, hd, hd, bd, bd, bd, bd, bd, bd, ns, nk, ns, bd, bd, bd, bd, bd, bd, hd, hd, hd, hd, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bg, bg, bg, hd, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bg, bg, hd, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bg, bg, fg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ft, bg, bg, bg, bg, bg, ft, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ft, bg, bg, bg, bg, bg, ft, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bt, bg, bg, bg, bg, bg, bt, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bt, bt, bg, bg, bg, bg, bg, bt, bt, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg]
        ]

    cool = [
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, gl, gl, gl, gl, gl, bg, bg, bg, gl, gl, gl, gl, gl, bg, bg, bg, gl, gl, gl, gl, gl, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, gl, gl, gl, gl, gl, gl, gl, gl, gl, gl, gl, gl, gl, gl, gl, gl, gl, gl, gl, gl, gl, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, gl, gl, gl, gl, gl, bg, bg, bg, gl, gl, gl, gl, gl, bg, bg, bg, gl, gl, gl, gl, gl, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, gl, gl, gl, gl, gl, bg, bg, bg, gl, gl, gl, gl, gl, bg, bg, bg, gl, gl, gl, gl, gl, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, gl, gl, gl, gl, gl, bg, bg, bg, gl, gl, gl, gl, gl, bg, bg, bg, gl, gl, gl, gl, gl, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bd, bg, bg, bg, bg, bg, nk, bg, bg, bg, bg, bg, bd, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bd, bd, bg, bg, bg, bg, nk, bg, bg, bg, bg, bd, bd, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bd, bg, bg, bg, bg, nk, bg, bg, bg, bg, bd, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],      
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bd, bg, bd, bd, bg, nk, bg, bd, bd, bg, bd, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, hd, hd, bd, bd, bd, bd, bd, bd, ns, nk, ns, bd, bd, bd, bd, bd, bd, hd, hd, bg, bg, bg, bg, bg, bg],        
        [bg, bg, bg, bg, bg, hd, bg, bg, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bg, bg, hd, bg, bg, bg, bg, bg],        
        [bg, bg, bg, bg, hd, bg, bg, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bg, bg, hd, bg, bg, bg, bg],        
        [bg, bg, bg, hd, bg, bg, bg, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bg, bg, bg, hd, bg, bg, bg],       
        [bg, bg, bg, bg, hd, fg, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, fg, hd, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ft, bg, bg, bg, bg, bg, ft, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ft, bg, bg, bg, bg, bg, ft, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bt, bg, bg, bg, bg, bg, bt, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bt, bt, bg, bg, bg, bg, bg, bt, bt, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg]
        ]
    
    classic_hat = [
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ha, ha, ha, ha, ha, ha, ha, ha, ha, ha, ha, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ha, ha, ha, ha, ha, ha, ha, ha, ha, ha, ha, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ha, ha, ha, ha, ha, ha, ha, ha, ha, ha, ha, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, ha, ha, ha, ha, ha, ha, ha, ha, ha, ha, ha, ha, ha, ha, ha, ha, ha, ha, ha, ha, ha, ha, ha, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg]
        ]

    tall_hat_with_red = [
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ha, ha, ha, ha, ha, ha, ha, ha, ha, ha, ha, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ha, ha, ha, ha, ha, ha, ha, ha, ha, ha, ha, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ha, ha, ha, ha, ha, ha, ha, ha, ha, ha, ha, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ha, ha, ha, ha, ha, ha, ha, ha, ha, ha, ha, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, rh, rh, rh, rh, rh, rh, rh, rh, rh, rh, rh, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ha, ha, ha, ha, ha, ha, ha, ha, ha, ha, ha, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, ha, ha, ha, ha, ha, ha, ha, ha, ha, ha, ha, ha, ha, ha, ha, ha, ha, ha, ha, ha, ha, ha, ha, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg]
        ]
        
    cowboy_hat_with_grey = [
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ha, ha, ha, ha, ha, ha, ha, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ha, ha, ha, ha, ha, ha, ha, ha, ha, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ha, ha, ha, ha, ha, ha, ha, ha, ha, ha, ha, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ha, ha, ha, ha, ha, ha, ha, ha, ha, ha, ha, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, ha, bg, bg, bg, bg, bg, gr, gr, gr, gr, gr, gr, gr, gr, gr, gr, gr, bg, bg, bg, bg, bg, ha, bg, bg, bg, bg],
        [bg, bg, bg, bg, ha, ha, bg, bg, bg, bg, ha, ha, ha, ha, ha, ha, ha, ha, ha, ha, ha, bg, bg, bg, bg, ha, ha, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, ha, ha, ha, ha, ha, ha, ha, ha, ha, ha, ha, ha, ha, ha, ha, ha, ha, ha, ha, ha, ha, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg]
        ]
        
    small_hat = [
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ha, ha, ha, ha, ha, ha, ha, ha, ha, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ha, ha, ha, ha, ha, ha, ha, ha, ha, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ha, ha, ha, ha, ha, ha, ha, ha, ha, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ha, ha, ha, ha, ha, ha, ha, ha, ha, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, dr, dr, dr, dr, dr, dr, dr, dr, dr, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ha, ha, ha, ha, ha, ha, ha, ha, ha, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, ha, ha, ha, ha, ha, ha, ha, ha, ha, ha, ha, ha, ha, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg]
        ]
        
    baseball_hat = [
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, ha, ha, ha, ha, ha, ha, ha, ha, ha, ha, ha, ha, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, ha, rh, rh, rh, rh, rh, rh, rh, rh, rh, rh, rh, rh, ha, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, ha, rh, rh, rh, rh, rh, rh, rh, rh, rh, rh, rh, rh, rh, rh, ha, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, ha, rh, rh, rh, rh, rh, rh, rh, rh, rh, rh, rh, rh, rh, rh, rh, rh, ha, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, ha, rh, rh, rh, rh, rh, rh, rh, rh, rh, rh, rh, rh, rh, rh, rh, rh, rh, rh, ha, ha, ha, ha, ha, ha, bg, bg],
        [bg, bg, bg, bg, ha, rh, rh, rh, rh, rh, rh, rh, rh, rh, rh, rh, rh, rh, rh, rh, rh, rh, rh, rh, rh, rh, rh, rh, ha, bg, bg],
        [bg, bg, bg, bg, ha, ha, ha, ha, ha, ha, ha, ha, ha, ha, ha, ha, ha, ha, ha, ha, ha, ha, ha, ha, ha, ha, ha, ha, ha, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg]
        ]
        
    afro_look = [
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, ha, ha, ha, ha, ha, ha, ha, ha, ha, ha, ha, ha, ha, ha, ha, ha, ha, ha, ha, ha, ha, ha, ha, ha, ha, ha, ha, ha, ha, bg],
        [bg, bg, ha, ha, ha, ha, ha, ha, ha, ha, ha, ha, ha, ha, ha, ha, ha, ha, ha, ha, ha, ha, ha, ha, ha, ha, ha, ha, ha, bg, bg],
        [bg, bg, bg, ha, ha, ha, ha, ha, ha, ha, ha, ha, ha, ha, ha, ha, ha, ha, ha, ha, ha, ha, ha, ha, ha, ha, ha, ha, bg, bg, bg],
        [bg, bg, bg, bg, ha, ha, ha, ha, ha, ha, ha, ha, ha, ha, ha, ha, ha, ha, ha, ha, ha, ha, ha, ha, ha, ha, ha, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, ha, ha, ha, ha, ha, ha, ha, ha, ha, ha, ha, ha, ha, ha, ha, ha, ha, ha, ha, ha, ha, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, ha, ha, ha, ha, ha, ha, ha, ha, ha, ha, ha, ha, ha, ha, ha, ha, ha, ha, ha, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, ha, ha, ha, ha, ha, ha, ha, ha, ha, ha, ha, ha, ha, ha, ha, ha, ha, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg]
        ]
        
    simple_hair = [
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, ha, bg, bg, ha, bg, bg, bg, ha, bg, bg, ha, bg, ha, bg, ha, bg, bg, ha, bg, bg, bg, ha, bg, bg, ha, bg, bg, bg],
        [bg, bg, bg, ha, ha, bg, ha, ha, bg, bg, ha, ha, bg, ha, bg, ha, bg, ha, bg, ha, ha, bg, bg, ha, ha, bg, ha, ha, bg, bg, bg],
        [bg, bg, bg, bg, ha, ha, bg, ha, ha, bg, bg, ha, bg, ha, bg, ha, bg, ha, bg, ha, bg, bg, ha, ha, bg, ha, ha, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, ha, ha, bg, ha, ha, bg, bg, bg, ha, bg, ha, bg, ha, bg, bg, bg, ha, ha, bg, ha, ha, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, ha, ha, bg, ha, ha, bg, bg, ha, bg, ha, bg, ha, bg, bg, ha, ha, bg, ha, ha, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, ha, bg, bg, ha, bg, bg, ha, bg, ha, bg, ha, bg, bg, ha, bg, bg, ha, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg]
        ]
        
    # mouth - mustache (middle piece of the image)
    # location in the basic frame: 
    # 19:27, 6:25

    close_mouth = [
        [bg, bg, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bg, bg],
        [bg, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bg],
        [bg, bd, bd, bd, bd, bd, lp, lp, lp, lp, lp, lp, lp, bd, bd, bd, bd, bd, bg],
        [bd, bd, bd, bd, bd, lp, th, th, th, th, th, th, th, lp, bd, bd, bd, bd, bd],
        [bd, bd, bd, bd, bd, lp, th, th, th, th, th, th, th, lp, bd, bd, bd, bd, bd],
        [bd, bd, bd, bd, bd, bd, lp, lp, lp, lp, lp, lp, lp, bd, bd, bd, bd, bd, bd],
        [bg, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bg],
        [bg, bg, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bg, bg]
        ]

    close_mouth_mustache = [
        [bg, bg, mu, bd, bd, bd, bd, mu, mu, mu, mu, mu, bd, bd, bd, bd, mu, bg, bg],
        [bg, bd, mu, mu, mu, mu, mu, mu, mu, mu, mu, mu, mu, mu, mu, mu, mu, bd, bg],
        [bg, bd, bd, mu, mu, mu, mu, mu, mu, mu, mu, mu, mu, mu, mu, mu, bd, bd, bg],
        [bd, bd, bd, bd, bd, bd, lp, lp, lp, lp, lp, lp, lp, bd, bd, bd, bd, bd, bd],
        [bd, bd, bd, bd, bd, lp, th, th, th, th, th, th, th, lp, bd, bd, bd, bd, bd],
        [bd, bd, bd, bd, bd, lp, th, th, th, th, th, th, th, lp, bd, bd, bd, bd, bd],
        [bg, bd, bd, bd, bd, bd, lp, lp, lp, lp, lp, lp, lp, bd, bd, bd, bd, bd, bg],
        [bg, bg, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bg, bg]
        ]

    close_mouth_beard = [
        [bg, bg, be, be, be, bd, bd, bd, bd, bd, bd, bd, bd, bd, be, be, be, bg, bg],
        [bg, be, be, be, be, be, be, be, be, be, be, be, be, be, be, be, be, be, bg],
        [bg, be, be, be, be, be, lp, lp, lp, lp, lp, lp, lp, be, be, be, be, be, bg],
        [be, be, be, be, be, lp, th, th, th, th, th, th, th, lp, be, be, be, be, be],
        [be, be, be, be, be, lp, th, th, th, th, th, th, th, lp, be, be, be, be, be],
        [be, be, be, be, be, be, lp, lp, lp, lp, lp, lp, lp, be, be, be, be, be, be],
        [bg, be, be, be, be, be, be, be, be, be, be, be, be, be, be, be, be, be, bg],
        [bg, bg, be, be, be, be, be, be, be, be, be, be, be, be, be, be, be, bg, bg]
        ]

    close_mouth_sideburns = [
        [bg, bg, be, be, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, be, be, bg, bg],
        [bg, bd, be, be, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, be, be, bd, bg],
        [bg, bd, be, be, bd, bd, lp, lp, lp, lp, lp, lp, lp, bd, bd, be, be, bd, bg],
        [bd, bd, be, be, bd, lp, th, th, th, th, th, th, th, lp, bd, be, be, bd, bd],
        [bd, bd, bd, be, bd, lp, th, th, th, th, th, th, th, lp, bd, be, bd, bd, bd],
        [bd, bd, bd, be, bd, bd, lp, lp, lp, lp, lp, lp, lp, bd, bd, be, bd, bd, bd],
        [bg, bd, bd, bd, bd, bd, bd, be, be, be, be, be, bd, bd, bd, bd, bd, bd, bg],
        [bg, bg, bd, bd, bd, bd, bd, be, be, be, be, be, bd, bd, bd, bd, bd, bg, bg]
        ]

    very_happy_mouth = [
        [bg, bg, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bg, bg],
        [bg, bd, bd, lp, lp, lp, lp, lp, lp, lp, lp, lp, lp, lp, lp, lp, bd, bd, bg],
        [bg, bd, bd, lp, mt, th, th, th, th, th, th, th, th, th, mt, lp, bd, bd, bg],
        [bd, bd, bd, lp, lp, mt, mt, mt, mt, mt, mt, mt, mt, mt, lp, lp, bd, bd, bd],
        [bd, bd, bd, bd, lp, lp, mt, to, to, to, to, to, mt, lp, lp, bd, bd, bd, bd],
        [bd, bd, bd, bd, bd, lp, mt, mt, mt, mt, mt, mt, mt, lp, bd, bd, bd, bd, bd],
        [bg, bd, bd, bd, bd, lp, lp, lp, lp, lp, lp, lp, lp, lp, bd, bd, bd, bd, bg],
        [bg, bg, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bg, bg]
        ]

    happy_mustache = [
        [bg, bg, bd, bd, bd, mu, mu, mu, mu, mu, mu, mu, mu, mu, bd, bd, bd, bg, bg],
        [bg, bd, bd, mu, mu, mu, mu, mu, mu, mu, mu, mu, mu, mu, mu, mu, bd, bd, bg],
        [bg, bd, mu, mu, bd, lp, lp, lp, lp, lp, lp, lp, lp, lp, bd, mu, mu, bd, bg],
        [bd, bd, mu, bd, lp, mt, mt, th, mt, th, mt, th, mt, mt, lp, bd, mu, bd, bd],
        [bd, bd, mu, bd, lp, mt, mt, mt, mt, mt, mt, mt, mt, mt, lp, bd, mu, bd, bd],
        [bd, bd, bd, bd, bd, lp, th, mt, mt, mt, mt, mt, th, lp, bd, bd, bd, bd, bd],
        [bg, bd, bd, bd, bd, bd, lp, mt, th, mt, th, mt, lp, bd, bd, bd, bd, bd, bg],
        [bg, bg, bd, bd, bd, bd, bd, lp, lp, lp, lp, lp, bd, bd, bd, bd, bd, bg, bg]
        ]

    happy_double_teeth = [
        [bg, bg, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bg, bg],
        [bg, bd, bd, lp, lp, lp, lp, lp, lp, lp, lp, lp, lp, lp, lp, lp, bd, bd, bg],
        [bg, bd, bd, lp, mt, th, th, th, th, th, th, th, th, th, mt, lp, bd, bd, bg],
        [bd, bd, bd, lp, lp, mt, mt, mt, mt, mt, mt, mt, mt, mt, lp, lp, bd, bd, bd],
        [bd, bd, bd, bd, lp, lp, mt, mt, mt, mt, mt, mt, mt, lp, lp, bd, bd, bd, bd],
        [bd, bd, bd, bd, bd, lp, mt, th, th, th, th, th, mt, lp, bd, bd, bd, bd, bd],
        [bg, bd, bd, bd, bd, lp, lp, lp, lp, lp, lp, lp, lp, lp, bd, bd, bd, bd, bg],
        [bg, bg, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bg, bg]
        ]

    scary_mouth = [
        [bg, bg, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bg, bg],
        [bg, bd, bd, bd, bd, lp, lp, lp, lp, lp, lp, lp, lp, lp, bd, bd, bd, bd, bg],
        [bg, bd, bd, bd, lp, th, th, mt, th, th, th, th, th, th, lp, bd, bd, bd, bg],
        [bd, bd, bd, bd, lp, mt, mt, mt, mt, mt, mt, mt, mt, mt, lp, bd, bd, bd, bd],
        [bd, bd, bd, bd, lp, mt, mt, mt, mt, mt, mt, mt, mt, mt, lp, bd, bd, bd, bd],
        [bd, bd, bd, bd, bd, lp, lp, lp, lp, lp, lp, lp, lp, lp, bd, bd, bd, bd, bd],
        [bg, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bg],
        [bg, bg, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bg, bg]
        ]

    # list of hats / hair
    hats = [classic_hat, 
            tall_hat_with_red, 
            cowboy_hat_with_grey, 
            small_hat , 
            baseball_hat, 
            afro_look, 
            simple_hair
           ]

    # list of mouth
    mouth = [close_mouth, 
             close_mouth_mustache, 
             close_mouth_beard, 
             close_mouth_sideburns, 
             very_happy_mouth, 
             happy_mustache,
             happy_double_teeth,
             scary_mouth
             ]

    e = randint(0, 1000)
    seed(e)
             
    random_hat = choice(hats)

    f = randint(0, 1000)
    seed(f)
    
    random_mouth = choice(mouth)
    
 
    # choose which alien character to use
    g = randint(0,1000)
    seed(g)

    if f < 450:
        pixels = basic
        p = "basic"
    elif 450 <= f < 900:
        pixels = evil
        p = "evil"
    else:
        pixels = cool
        p = "cool"

    # check for dublicate combinations
    if pixels == cool:
        iterRam = [bd, random_hat, random_mouth, pixels]
    else:
        iterRam = [bd, pu, random_hat, random_mouth, pixels]
    if iterRam in ram:
        # add one to the iterations in order to generate the same number
        # of images as the iterations. 
        iterations += 1
        i += 1
        continue
    else:
        ram.append(iterRam)
        i +=1

    # convert the pixels into an array using numpy
    array = np.array(pixels, dtype=np.uint8)

    array[0:9, :] = random_hat
    array[19:27, 6:25] = random_mouth

    j += 1

    # use PIL to create an image from the new array of pixels
    new_image = Image.fromarray(array)
    new_image = new_image.resize(dimensions, resample=0)
    imgname = dirname + '/alien_images/crazyAlien ' + (str(j)) + '.png'
    new_image.save(imgname)
