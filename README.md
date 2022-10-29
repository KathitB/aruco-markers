This project is for generation and detection of aruco markers

generation.py is the program for creation of Aruco markers 
detection.py is the program to detect the aruco markers, the aruco markers that can be tetected till 1000 id,the program moreover displays auco marker's unique ID
calibration images.py captures various images to calibragte the camera . Estimating the parameters of a camera, parameters about the camera are required to determine an accurate relationship between a 3D point in the real world and its corresponding 2D projection (pixel) in the image captured by that calibrated camera. 
camera calibration.py uses the photos taken in calibration images.py to connect the 3D to 2D images and also calculates parameters like distance coefficient , rotational vector and translational vector
pose.py gives the 3D pose of the aruco marhers giving the distance of the marker from the camera and also gives the position of the marker
