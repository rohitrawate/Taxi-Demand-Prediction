import tensorflow as tf, sys
import cv2
import RPi.GPIO as GPIO
import time
import serial
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)       # Use BCM GPIO numbers
pir=21
GPIO.setup(pir, GPIO.IN) 
print 'k'
import time



import MySQLdb as mdb


def push(item):

        
        con = mdb.connect('localhost', \
                          'root', \
                          'root', \
                          'tms' );
        cur = con.cursor()
        cur.execute("TRUNCATE TABLE `record`")
        cur.execute("""INSERT INTO record(it,rec) \
                   VALUES(%s,%s)""", (item,'g'))
        
        con.commit()
             
def push1(item):

        
        con = mdb.connect('localhost', \
                          'root', \
                          'root', \
                          'tms' );
        cur = con.cursor()
        #cur.execute("TRUNCATE TABLE `record`")
        cur.execute("""INSERT INTO record(re,rec) \
                   VALUES(%s,%s)""", (item,'g'))
        
        con.commit()
                
def push3(data):

        
        con = mdb.connect('localhost', \
                          'root', \
                          'root', \
                          'tms' );
        cur = con.cursor()
        #cur.execute("TRUNCATE TABLE `record`")
        cur.execute("""INSERT INTO record(recom,rec) \
                   VALUES(%s,%s)""", (data,'g'))
        
        con.commit()

var1=0
def upd(item1):
        c=0
##        item1=str(raw_input("Enter the item"))
##        print item1
        push(item1)
        for i in range(0,5):
            
            db = mdb.connect('localhost', \
                              'root', \
                              'root', \
                              'tms' );

           
            cursor = db.cursor()

            
            sql = "SELECT %s FROM `item`"%item1
           # sql = "SELECT  FROM `item`"
                
          
            cursor.execute(sql)
               
            wheat = cursor.fetchall()[i]              
            var2= str(wheat[0])
            print var2
            push1(var2)
            
        try:
                for i in range(0,5):
                    
                    db = mdb.connect('localhost', \
                                      'root', \
                                      'root', \
                                      'tms' );

                   
                    cursor = db.cursor()

                    
                    sql = "SELECT %s FROM `points`"%item1
                   # sql = "SELECT  FROM `item`"
                        
                  
                    cursor.execute(sql)
                       
                    wheat = cursor.fetchall()[i]              
                    var= int(wheat[0])
                    if var>var1:
                            var1=var
                            c=i
                    print var
        except:
                print ''
        print c
        
        db = mdb.connect('localhost', \
                              'root', \
                              'root', \
                              'tms' );

           
        cursor = db.cursor()

            
        sql = "SELECT %s FROM `item`"%item1
           # sql = "SELECT  FROM `item`"
                
          
        cursor.execute(sql)
               
        wheat = cursor.fetchall()[c]              
        var1= str(wheat[0])
        print var1
        push3(var1)
       
n=0
# Camera 0 is the integrated web cam on my netbook
camera_port = 0
 
#Number of frames to throw away while the camera adjusts to light levels
ramp_frames = 30
while True:
    if (GPIO.input(pir)) and n==0:
        n=1
        print "capture"
        camera = cv2.VideoCapture(camera_port)
 
        # Captures a single image from the camera and returns it in PIL format
        def get_image():
         # read is the easiest way to get a full image out of a VideoCapture object.
         retval, im = camera.read()
         return im
         
       
        for i in xrange(ramp_frames):
         temp = get_image()
        print("Taking image...")
        
        camera_capture = get_image()
       
       
      
         
        # You'll want to release the camera, otherwise you won't be able to create a new
        # capture object until your script exits
        del(camera)

        out = cv2.imwrite('x.jpg', camera_capture)
        image_path = 'x.jpg'
        print 'image save'
        # Read in the image_data
        image_data = tf.gfile.FastGFile(image_path, 'rb').read()
        print image_data
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
             top_k = predictions[0].argsort()[-len(predictions[0]):][::-1]
             human_string = label_lines[0]
             score = predictions[0][0]
             print('%s (score = %.5f)' % (human_string, score))
             if score>0.90:
                 print 'flower'
                 upd('cauliflower')
                 it1='cauliflower'
             human_string = label_lines[1]
             score = predictions[0][1]
             print('%s (score = %.5f)' % (human_string, score))
             if score>0.90:
                 print 'matar'
                 upd('matar')
                 it1='matar'
             human_string = label_lines[2]
             score = predictions[0][2]
             print('%s (score = %.5f)' % (human_string, score))
             if score>0.90:
                 print 'potato'
                 it1='potato'
                 upd('potato')
             human_string = label_lines[3]
             score = predictions[0][3]
             print('%s (score = %.5f)' % (human_string, score))
             if score>0.90:
                 print 'tomato'
                 it1='tomato'
                 upd('tomato')
             human_string = label_lines[4]
             score = predictions[0][4]
             print('%s (score = %.5f)' % (human_string, score))
             if score>0.90:
                 print 'onion'
                 it1='onion'
                 upd('onion')
             human_string = label_lines[5]
             score = predictions[0][5]
             print('%s (score = %.5f)' % (human_string, score))
             if score>0.90:
                 print 'apple'
                 it1='apple'
                 upd('apple')
             human_string = label_lines[6]
             score = predictions[0][6]
             print('%s (score = %.5f)' % (human_string, score))
             if score>0.90:
                 print 'paneer'
                 it1='paneer'
                 upd('paneer')
             human_string = label_lines[7]
             score = predictions[0][7]
             print('%s (score = %.5f)' % (human_string, score))
             if score>0.90:
                 print 'palak'
                 it1='palak'
                 upd('palak')
            
    elif (GPIO.input(pir)) and n==1:
                n=0
                print "capture"
                
                camera = cv2.VideoCapture(camera_port)
 
                # Captures a single image from the camera and returns it in PIL format
                def get_image():
                 # read is the easiest way to get a full image out of a VideoCapture object.
                 retval, im = camera.read()
                 return im
                 
               
                for i in xrange(ramp_frames):
                 temp = get_image()
                print("Taking image...")
                
                camera_capture = get_image()
               
               
              
                 
               
                del(camera)

                out = cv2.imwrite('x1.jpg', camera_capture)
                image_path = 'x1.jpg'
                print 'image save'
                # Read in the image_data
                image_data = tf.gfile.FastGFile(image_path, 'rb').read()
                print image_data
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
                     top_k = predictions[0].argsort()[-len(predictions[0]):][::-1]
                     human_string = label_lines[0]
                     score = predictions[0][0]
                     print('%s (score = %.5f)' % (human_string, score))
                     if score>0.90:
                         print 'flower'
                         upd('cauliflower')
                         it2='cauliflower'
                     human_string = label_lines[1]
                     score = predictions[0][1]
                     print('%s (score = %.5f)' % (human_string, score))
                     if score>0.90:
                         print 'matar'
                         upd('matar')
                         it2='matar'
                     human_string = label_lines[2]
                     score = predictions[0][2]
                     print('%s (score = %.5f)' % (human_string, score))
                     if score>0.90:
                         print 'potato'
                         it2='potato'
                         upd('potato')
                     human_string = label_lines[3]
                     score = predictions[0][3]
                     print('%s (score = %.5f)' % (human_string, score))
                     if score>0.90:
                         print 'tomato'
                         it2='tomato'
                         upd('tomato')
                     human_string = label_lines[4]
                     score = predictions[0][4]
                     print('%s (score = %.5f)' % (human_string, score))
                     if score>0.90:
                         print 'onion'
                         it2='onion'
                         upd('onion')
                     human_string = label_lines[5]
                     score = predictions[0][5]
                     print('%s (score = %.5f)' % (human_string, score))
                     if score>0.90:
                         print 'apple'
                         it2='apple'
                         upd('apple')
                     human_string = label_lines[6]
                     score = predictions[0][6]
                     print('%s (score = %.5f)' % (human_string, score))
                     if score>0.90:
                         print 'paneer'
                         it2='paneer'
                         upd('paneer')
                     human_string = label_lines[7]
                     score = predictions[0][7]
                     print('%s (score = %.5f)' % (human_string, score))
                     if score>0.90:
                         print 'palak'
                         it2='palak'
                         upd('palak')
                     time.sleep(1)
                     it3=it1+it2
                     upd(it3)

              

