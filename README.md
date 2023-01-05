# bionic_hand
A bionic hand controlled by a Raspberry Pi 4 connected to an ultrasonic sensor and camera. Uses TensorFlow Lite to detect objects and determine how to control the five connected servos.


pros_hand.py is the main code. I run it in a virtual environment on the Raspberry Pi 4, and it performs the full functionality described above. It requires the detection_model folder contents to perform object detection with Tensorflow Lite. Much of the object detection code was originally based on this sample code:
https://github.com/AnteZovko23/Machine_Learning-RaspberryPI_ObjectDetection_TensorFlow_OpenCV/blob/master/ObjectDetection2.py


detection_model contains the trained model, along with a text document, gripinfo.txt, that contains important information for pros_hand.py. The first column in the document contains labels for each possible classification, which is referenced by the index outputted by the trained model. The next five columns contain finger positions for their respective object so that pros_hand.py can specialize the grip to the targeted object.


solidworks_parts contains the parts I used to design the hand in solidworks. I recommend using the assembly to navigate between parts. Almost everything in the folder was designed by myself, with these exceptions:

Raspberry Pi Camera: https://grabcad.com/library/raspberry-pi-camera-v2-1

MG996R Servo: https://grabcad.com/library/servo-mg-996r-2

Ultrasonic Sensor: https://grabcad.com/library/ultrasonic-sensor-hc-sr04-5


printable_stl_parts contains stl parts exported from solidworks for printing, and everything in it is my original design.
