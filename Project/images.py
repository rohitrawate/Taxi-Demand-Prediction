import tensorflow as tf, sys
print(tf.__version__)
import cv2

import time
import numpy as np
import cv2

image_path = 'WIN_20191117_10_21_55_Pro.jpg'

# Read in the image_data
image_data = tf.gfile.FastGFile(image_path, 'rb').read()

# Loads label file, strips off carriage return
label_lines = [line.rstrip() for line
    in tf.gfile.GFile("retrained_labels.txt")]
# Unpersists graph from file

with tf.gfile.FastGFile("retrained_graph.pb", 'rb') as f:
    graph_def = tf.GraphDef()
    graph_def.ParseFromString(f.read())
    _ = tf.import_graph_def(graph_def, name='')
# Feed the image_data as input to the graph and get first prediction

with tf.Session() as sess:
     softmax_tensor = sess.graph.get_tensor_by_name('final_result:0')
     
     predictions = sess.run(softmax_tensor, 
     {'DecodeJpeg/contents:0': image_data})
     # Sort to show labels of first prediction in order of confidence
     print ('k')
     top_k = predictions[0].argsort()[-len(predictions[0]):][::-1]
     #for node_id in top_k:
     human_string = label_lines[0]
     score = predictions[0][0]
    
     print('%s (score = %.5f)' % (human_string, score))
     if score>0.6:
             print ('apple')
     
     human_string = label_lines[1]
     score = predictions[0][1]
     print('%s (score = %.5f)' % (human_string, score))
     if score>0.4:
             print ('banana')
    
     human_string = label_lines[2]
     score = predictions[0][2]
     print('%s (score = %.5f)' % (human_string, score))
     if score>0.6:
             print ('mango')
     human_string = label_lines[3]
     score = predictions[0][3]
     print('%s (score = %.5f)' % (human_string, score))
     if score>0.6:
             print ('mango')
    
    







