center_pos = 0
maxx = 0
maxy= 0

#last rectangle details
def last_obj_pos(x,y,w,h):
	global center_pos
	center_pos = [ (x+(w/2)), (y+(h/2))]


def set_frame(mx,my):
	global maxx
	maxx = mx
	global maxy
	maxy = my

def set_side():
	if (0,0) <= center_pos < (maxx/3,maxy/3):
		edge = 'UL'
	elif (maxx/3,0) <= center_pos < (2*maxx/3,maxy/3):
		edge = 'U'
	elif (2*maxx/3,0) <= center_pos <= (maxx,maxy):
		edge = 'UR'
	elif (maxx/3,maxy/3) <= center_pos < (2*maxx/3,2*maxy/3):
		edge = 'L'
	elif (maxx/3,maxy/3) <= center_pos < (2*maxx/3,2*maxy/3):
		edge = 'R'
	elif (maxx/3,maxy/3) <= center_pos < (2*maxx/3,2*maxy/3):
		edge = 'DL'
	elif (maxx/3,maxy/3) <= center_pos < (2*maxx/3,2*maxy/3):
		edge = 'D'
	elif (maxx/3,maxy/3) <= center_pos < (2*maxx/3,2*maxy/3):
		edge = 'DR'
	return edge