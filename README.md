# CrazyAliens generation script
# Intro
This is the repository for crazyAliens, which is a collection of programmatically generated NFTs. The repository is based on https://github.com/nft-fun/generate-bitbirds repository.

# Dependencies

- Python 3 (tested on Python 3.6  and Ubuntu 18.04)

- PIP - a command-line installation mechanism for python assets. 

- Pillow - python library for image processing

- NumPy - python library to work with arrays 

# Setting up
At first, for a clean Python environment run, open a command line (terminal for linux) and type:

    python3 -m venv ~/venv
    cd venv
    source bin/activate

Now you have created a virtual Python environment, so when you install Python modules / libraries with PIP, you don't affect the whole system but only the Python environment that exists in "venv" folder.

Then with the "venv" environment activated type:
    
    pip install Pillow
    pip install numpy
    
# How this script works

We are iterating through a 'loop' once for each alien. The loop starts with a 'seed number' that is used to deterministically generate pseudo-random numbers. I say 'deterministically' and 'pseudo-random' because from the same seed number the 'random' output will always be the same. It's not truly random in a security or mathematical sense. I used the most recent ETH block at the time as my seed number - 13280437.

There is then a 'chain' of additional random numbers generated that are used to define all of the various traits of the aliens. Many of the attributes generate a random number between 1-1000 and use that for some sort of logical statement (e.g. to decide for a coolAl look). 

This random-number chain results in some specific behavior and combinations because of the specific seed number for each iteration. If you run the script yourself (without changing the seed) you should see identical matches for each number.

The alien images are 31x31 arrays of variables, representing every pixel in the final image. I've used variables with two letters for each type of pixel (e.g. outline `bd`, body color ), so as to keep the 'matrix' of pixel variables easy to see and work with. If you zoom way out on the code you may even be able to see a rough picture of the aliens in the code, just from the slight differences in the variables.

Because I wanted crazyAliens to have specific colours and not random, I found some colours that I liked for their body and their eyes and I defined  them in lists. So in each iteration the random.choice() function (build-in function in Python) pick one of them at random. 

Also, beyond the basic 31 x 31 arrays that shape the whole image, I defined smaller arrays in order to add gear to the aliens like: hats, hair, mustache, e.t.c. So, I defined lists of arrays for each type of gear (e.g headgear: fedora, afro, crazy hair or facial hair: gentleman mustache, beard etc) and I used numpy to replace the corresponding parts of the 31 x 31 arrays with the randomly selected array for the headgear, tthe facial hair and the mouth.

From there, you're just about home free. The final bit of the loop re-sizes the generated alien from 31x31 pixels up to 512x512 pixels. It generates the image file path (dynamically, wherever you have the folder using the `os` library), and saves the image into the included folder `alien_images`.

Then it goes right back to the top of the loop, and does it again for the next alien, until the number of defined loops is completed. 

In each iteration, the algorithm checks if the image that has been composed, exists from an older iteration. If that is True, it skips that iteration and goes to the next iteration.

It's worth to mention that, after the generation of the images, you can run the file "unique.py" in order to check if the images that you created are unique. If not the doubled images are stored in a folder which is called "identical_images". This file ensures for a 100% that all the aliens from the collection is unique.

# Wrap up
I sincerely hope this inspires someone to learn a new skill, take up coding, or generally expand their horizons! 

If you feel absolutly compelled to send ETH or NFTs to me directly, please know that it is not necessary, but the crazyAliens project hardware wallet address is: 0x6f182b3566A0d98387A5A47A0CAfD512ff444417

Happy hacking !

