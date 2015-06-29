import sys
sys.path.append("D:\Rushil\Workspace\Semester Project\Face detection")
from Sql import sqldb

def lplm(lat,lon):
	next_cam_id = 0
	ch = False
	cam_id = sqldb.lplm(lat,lon)
	ch = det(cam_id)
	if ch == False:
		cam_id = sqldb.lslm(lat,lon)
		ch = det(cam_id)
		if ch == True:
			next_cam_id = cam_id
		else:
			cam_id = sqldb.lpls(lat,lon)
			ch = det(cam_id)
			if ch == True:
				next_cam_id = cam_id
	else:
		next_cam_id = cam_id
	return next_cam_id

def lplp(lat,lon):
	next_cam_id = 0
	ch = False
	cam_id = sqldb.lplp(lat,lon)
	ch = det(cam_id)
	if ch == False:
		cam_id = sqldb.lpls(lat,lon)
		ch = det(cam_id)
		if ch == True:
			next_cam_id = cam_id
		else:
			cam_id = sqldb.lslp(lat,lon)
			ch = det(cam_id)
			if ch == True:
				next_cam_id = cam_id
	else:
		next_cam_id = cam_id
	return next_cam_id

def lmlm(lat,lon):
	next_cam_id = 0
	ch = False
	cam_id = sqldb.lmlm(lat,lon)
	ch = det(cam_id)
	if ch == False:
		cam_id = sqldb.lslm(lat,lon)
		ch = det(cam_id)
		if ch == True:
			next_cam_id = cam_id
		else:
			cam_id = sqldb.lmls(lat,lon)
			ch = det(cam_id)
			if ch == True:
				next_cam_id = cam_id
	else:
		next_cam_id = cam_id
	return next_cam_id

def lmlp(lat,lon):
	next_cam_id = 0
	ch = False
	cam_id = sqldb.lmlp(lat,lon)
	ch = det(cam_id)
	if ch == False:
		cam_id = sqldb.lmls(lat,lon)
		ch = det(cam_id)
		if ch == True:
			next_cam_id = cam_id
		else:
			cam_id = sqldb.lslp(lat,lon)
			ch = det(cam_id)
			if ch == True:
				next_cam_id = cam_id
	else:
		next_cam_id = cam_id
	return next_cam_id

def lslm(lat,lon):
	next_cam_id = 0
	ch = False
	cam_id = sqldb.lslm(lat,lon)
	ch = det(cam_id)
	if ch == False:
		cam_id = sqldb.lplm(lat,lon)
		ch = det(cam_id)
		if ch == True:
			next_cam_id = cam_id
		else:
			cam_id = sqldb.lmlm(lat,lon)
			ch = det(cam_id)
			if ch == True:
				next_cam_id = cam_id
	else:
		next_cam_id = cam_id
	return next_cam_id

def lslp(lat,lon):
	next_cam_id = 0
	ch = False
	cam_id = sqldb.lslp(lat,lon)
	ch = det(cam_id)
	if ch == False:
		cam_id = sqldb.lplp(lat,lon)
		ch = det(cam_id)
		if ch == True:
			next_cam_id = cam_id
		else:
			cam_id = sqldb.lmlp(lat,lon)
			ch = det(cam_id)
			if ch == True:
				next_cam_id = cam_id
	else:
		next_cam_id = cam_id
	return next_cam_id

def lmls(lat,lon):
	next_cam_id = 0
	ch = False
	cam_id = sqldb.lmls(lat,lon)
	ch = det(cam_id)
	if ch == False:
		cam_id = sqldb.lmlm(lat,lon)
		ch = det(cam_id)
		if ch == True:
			next_cam_id = cam_id
		else:
			cam_id = sqldb.lmlp(lat,lon)
			ch = det(cam_id)
			if ch == True:
				next_cam_id = cam_id
	else:
		next_cam_id = cam_id
	return next_cam_id

def lpls(lat,lon):
	next_cam_id = 0
	ch = False
	cam_id = sqldb.lpls(lat,lon)
	ch = det(cam_id)
	if ch == False:
		cam_id = sqldb.lplm(lat,lon)
		ch = det(cam_id)
		if ch == True:
			next_cam_id = cam_id
		else:
			cam_id = sqldb.lplp(lat,lon)
			ch = det(cam_id)
			if ch == True:
				next_cam_id = cam_id
	else:
		next_cam_id = cam_id
	return next_cam_id