## Cycle GAN implementation ##

This one is an exercise as part of Deep Learning Nanodegree program offered by Udacity. 
I find the provided solution looks a little strange and does not reflect the description bundled with the notebook so I modified the code a bit. 

The notebook can run on Google Colab (enable GPU to accerlerate the training) 
but the helpers.py needs to be put in the working directory of the workspace.
In addition, the helper functions written The helpers.py needs to be modified since method scipy.misc.imsave() is deprecated and 
needs to switch to imageio.imwrite() instead.

The original version can be found at [Udacity GitHub repo](https://github.com/udacity/deep-learning-v2-pytorch/tree/master/cycle-gan)

The sameple dataset can also be downloaded from my own Google Drive [here](https://drive.google.com/open?id=1SzuwBlCC7xgfRspgrLz8fOI0oYxN8e31).
The zip file is meant to be put at the same location as the notebook (assuming working directory is there)
