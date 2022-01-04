import tensorflow as tf

params = tf.experimental.tensorrt.ConversionParams(precision_mode='FP16',maximum_cached_engines=100)
converter = tf.experimental.tensorrt.Converter(input_saved_model_dir='./3_class_model', conversion_params=params)
converter.convert()

def my_input_fn():
  for _ in range(100):
    inp1 = tf.random.normal((1,52,52,3),dtype=tf.float32)
    yield [inp1]

converter.build(input_fn=my_input_fn)
converter.save('./3_class_model_fp16')