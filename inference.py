import tensorflow as tf
import numpy as np

trained_model = tf.keras.models.load_model('./3_class_model_fp16')
class_names = ['blue', 'orange','empty']
def inference(input_frame):
    final_pred = {}
    input_im = input_frame/255.0
    # input_im = tf.cast(tf.expand_dims(input_im, 0),tf.float32)
    input_im = tf.cast(input_im,tf.float32)
    predictions = trained_model(input_im)
    score = tf.nn.softmax(predictions)
    # final_pred['class_id'] = tf.where(tf.reduce_max(score,axis=1)>=0.5,tf.argmax(score,axis=1),2)
    final_pred['class_id'] = tf.argmax(score,axis=1)
    final_pred['score'] = tf.cast(tf.argmax(score,axis=1)*100,tf.int8)
    return final_pred
