## Instructions for porting Keras model to .mlmodel (iOS CoreML model) ##

The steps here are largely the consolidation of the following:

- The documentation given on [Apple GitHub](https://apple.github.io/coremltools/generated/coremltools.converters.keras.convert.html) 
- Apple also recommends the practice to create virtual environment with virtualenv package as detailed [here](https://github.com/apple/coremltools#installation) )
- Contents on `convert_keras_coreml.py` are mostly taken from [the original conversion file](https://github.com/freedomtan/coreml-mobilenet-models/blob/master/mobilenets.py) by [freedomtan](https://github.com/freedomtan) with substantial simplification.
- Specific to Keras' mobilenet model, there was an issue related to ReLu6 activation function [here](https://github.com/apple/coremltools/issues/85). The issue should have been resolved but to be confirmed with model saved from tensorflow 2.x

1. Open Terminal window and change the directory to the location where the virtualenv is intalled. Ex: if the directory name is `mlvirtualenv` then execute: 

    `$ source mlvirtualenv/bin/activate`

    The prompt should change to:

    `(mlvirtualenv)`
    
2. Change the directory to the location that stores file `convert_keras_coreml.py` , copy test image file to the location and then run:

    `(mlvirtualenv) python convert_keras_coreml.py`

