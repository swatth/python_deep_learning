import keras
import tensorflow
import numpy as np
from keras.models import load_model
from keras.applications.mobilenet import preprocess_input
from keras.preprocessing import image

image_size = 224

model = load_model('meedthii13_ver2.hdf5')


#test prediction to compare the original model to the coreml model
img_path = 'testVol6.jpg'
img = keras.preprocessing.image.load_img(img_path, target_size=(image_size, image_size))
x = keras.preprocessing.image.img_to_array(img)
x = np.expand_dims(x, axis=0)
x = preprocess_input(x)

#the output from Keras model prediction
preds = model.predict(x)
print(preds)

#start converting
import coremltools

output_labels = ['Vol1', 'Vol2', 'Vol3', 'Vol4', 'Vol5', 'Vol6']

coreml_model = coremltools.converters.keras.convert(model, 
                                                    input_names=['image'], 
                                                    output_names=['output'], 
                                                    image_input_names = 'image',  
                                                    class_labels = output_labels, 
                                                    image_scale=2./255, 
                                                    red_bias=-1.0, 
                                                    green_bias=-1.0, 
                                                    blue_bias=-1.0, 
                                                    model_precision='float16')

#adding metadata to the model to export in .mlmodel format
coreml_model.author = 'Surasak Watthanayontkit'
coreml_model.license = 'the Apache License for initial pre-trained weights'
coreml_model.short_description = 'Marcus Knives recognizer v2'
coreml_model.input_description['image'] = 'image'
coreml_model.output_description['output'] = 'Confidence'
coreml_model.output_description['classLabel'] = 'Labels'

#test prediction on coreml model
from PIL import Image
image = Image.open(img_path)

#predict the same image after converted to .mlmodel to verify the result
#the values may not be exact match due to the loss of precision on conversion
coreml_model.predict({'image':image})

coreml_model_spec = coreml_model.get_spec()
coremltools.utils.visualize_spec(coreml_model.get_spec())

#save model
coreml_model.save('meedthii13ver2.mlmodel')
