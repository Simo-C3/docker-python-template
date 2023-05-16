import tensorflow as tf

tf.test.is_gpu_available()

from tensorflow.python.client import device_lib
device_lib.list_local_devices()
