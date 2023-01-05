# bionic_hand
A bionic hand controlled by a Raspberry Pi 4 connected to an ultrasonic sensor and camera. Uses TensorFlow Lite to detect objects and determine how to control the five connected servos.

pros_hand.py is the main code. I run it in a virtual environment on the Raspberry Pi 4, and it performs the full functionality described above. It requires the detection_model folder contents to perform object detection with Tensorflow Lite.

detection_model contains the trained model, along with a text document, gripingo.txt, that contains important information for pros_hand.py. The first column in the document contains labels for each possible classification, which is referenced by the index outputted by the trained model. The next five columns contain finger positions for each object so that pros_hand.py can specialize the grip to the targeted object.
