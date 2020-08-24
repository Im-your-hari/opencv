import cv2

a=cv2.VideoCapture(0)
a.set(3,400)
a.set(4,400)

while True:
    s,v=a.read()
    cv2.imshow("Video",v)
    cv2.waitKey(0)

'''
Oru key click cheyyunnath vare camera stuck aayirikkum...after clicking...Current captured image show cheyyum...
'''
    
