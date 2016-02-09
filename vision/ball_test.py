from tracker import *
from camera import Camera

c = Camera()

frame = c.get_frame()

t = BallTracker('red')

'''while True:
	frame = c.get_frame()
	center, radius = t.get_ball_coordinates(frame)
	print center
	frame = cv2.circle(frame, center, 8, (0,0,0), 2)
	cv2.imshow('frame', frame)
	k = cv2.waitKey(5) & 0xFF
	if k == 27:
		break
'''

r = RobotTracker('bright_blue', 1)

while True:
	frame = c.get_frame()
	center = r.our_defender_coordinates(frame)
	#print center

	p, v1 = r.getRobotOrientation(frame, 'us', 'defender')
	print p

	print 80 * '='

	frame = cv2.circle(frame, ( int(center[0]), int(center[1])), 20, (0,0,0), 2)
	print "center: " + str(center)
	x, y = Tracker.transformCoordstoDecartes(center)
	vector1 = (x+v1[0] * 50, y+v1[1] * 50)
	#vector2 = (x+v2[0]* 5, y+v2[1] * 5)
	x1, y1 = Tracker.transformCoordstoCV(vector1)
	#x2, y2 = Tracker.transformCoordstoCV(vector2)
	#print x,y
	cv2.line(frame, (int(center[0]),int(center[1])), (int(x1),int(y1)), (0,255,122), 2)
	#cv2.line(frame, (int(center[0]),int(center[1])), (int(x2),int(y2)), (199,21,133), 2)
	cv2.imshow('frame', frame)
	k = cv2.waitKey(5) & 0xFF
	if k == 27:
		break

c.close()
cv2.destroyAllWindows()		