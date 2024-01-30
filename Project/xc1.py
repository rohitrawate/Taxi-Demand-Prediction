import tensorflow as tf, sys
print(tf.__version__)
import cv2

import time
import numpy as np
import cv2

##cap = cv2.VideoCapture(0)
##while True:
##    
##       
##        ret, frame = cap.read()
##
##       
##
##        cv2.imshow('frame',frame)
##        if cv2.waitKey(1) & 0xFF == ord('q'):
##               cv2.imwrite('1.jpeg',frame) 
##               break
image_path = '45.png'

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
     mild_s = predictions[0][0]
     print('%s (score = %.5f)' % (human_string, mild_s))
     
     
     human_string = label_lines[1]
     moderate_s = predictions[0][1]
     print('%s (score = %.5f)' % (human_string, moderate_s))
     
     human_string = label_lines[2]
     normal_s = predictions[0][2]
     print('%s (score = %.5f)' % (human_string, normal_s))
     human_string = label_lines[3]
     pdr_s = predictions[0][3]
     print('%s (score = %.5f)' % (human_string, pdr_s))
     human_string = label_lines[4]
     severe_s = predictions[0][4]
     print('%s (score = %.5f)' % (human_string, severe_s))
     if mild_s>moderate_s and mild_s>normal_s and mild_s>pdr_s and mild_s>severe_s:
             print ('Mild')
     if moderate_s>mild_s and moderate_s>normal_s and moderate_s>pdr_s and moderate_s>severe_s:
             print ('Moderate')
    
     if normal_s>moderate_s and normal_s>mild_s and normal_s>pdr_s and normal_s>severe_s:
             print ('Normal')
     if pdr_s>moderate_s and pdr_s>normal_s and pdr_s>mild_s and pdr_s>severe_s:
             print ('PDR')
     if severe_s>moderate_s and severe_s>normal_s and severe_s>pdr_s and severe_s>mild_s:
             print ('Mild')
    







