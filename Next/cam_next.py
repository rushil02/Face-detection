import sys
sys.path.append("D:\Rushil\Workspace\Semester Project\Face detection")
#from GUI import GUI_layout
from Sql import sqldb
#import cam_adj

#Camera Switch algorithm    
def cam_next(curr_cam_id, cam_edge):
    #access db for current camera's latitude and longitudes
    curr_lat = sqldb.lat(curr_cam_id)
    curr_long = sqldb.lon(curr_cam_id)
    curr_face = sqldb.face(curr_cam_id)
    #Algorithm for next camera
    if curr_face == 'N':
        next_cam_id = algo_N(cam_lat,cam_long,cam_edge)
    elif curr_face == 'E':
        next_cam_id = algo_E(cam_lat,cam_long,cam_edge)
    elif curr_face == 'W':
        next_cam_id = algo_W(cam_lat,cam_long,cam_edge)
    elif curr_face == 'S':
        next_cam_id = algo_S(cam_lat,cam_long,cam_edge)
    elif curr_face == 'NE':
        next_cam_id = algo_NE(cam_lat,cam_long,cam_edge)
    elif curr_face == 'NW':
        next_cam_id = algo_NW(cam_lat,cam_long,cam_edge)
    elif curr_face == 'SE':
        next_cam_id = algo_SE(cam_lat,cam_long,cam_edge)
    elif curr_face == 'SW':
        next_cam_id = algo_SW(cam_lat,cam_long,cam_edge)
    return next_cam_id

#default function array in case of no match
def all_search(lat,lon):
    next_cam_id = 0
    ch = False
    all_func = [sqldb.lpls, sqldb.lplm, sqldb.lmls, sqldb.lmlp, sqldb.lslm, sqldb.lslp, sqldb.lplp, sqldb.lmlm]
    for f in all_func:
        cam_id = f(lat,lon)
        ch = det(cam_id) #returns boolean value
        if ch == True:
            next_cam_id == cam_id
        else:
            break
    return next_cam_id 

#For camera facing north
def algo_N(lat,lon,edge):
    ch = False
    next_cam_id = 0
    if edge == 'U':
        cam_id = cam_adj.lpls(lat,lon)
        ch = det(cam_id)
        if ch == True:
            next_cam_id = cam_id
    elif edge == 'D':
        cam_id = cam_adj.lmls(lat,lon)        
        ch = det(cam_id)
        if ch == True:
            next_cam_id = cam_id
    elif edge == 'L':
        cam_id = cam_adj.lslm(lat,lon) 
        ch = det(cam_id)
        if ch == True:
            next_cam_id = cam_id
    elif edge == 'R':
        cam_id = cam_adj.lslp(lat,lon)
        ch = det(cam_id)
        if ch == True:
            next_cam_id = cam_id
    elif edge == 'UL':
        cam_id = cam_adj.lplm(lat,lon)
        ch = det(cam_id)
        if ch == True:
            next_cam_id = cam_id
    elif edge == 'DL':
        cam_id = cam_adj.lmlm(lat,lon)
        ch = det(cam_id)
        if ch == True:
            next_cam_id = cam_id
    elif edge == 'UR':
        cam_id = cam_adj.lplp(lat,lon)
        ch = det(cam_id)
        if ch == True:
            next_cam_id = cam_id
    elif edge == 'DR':
        cam_id = cam_adj.lmlp(lat,lon)
        ch = det(cam_id)
        if ch == True:
            next_cam_id = cam_id
    elif next_cam_id == 0:
        next_cam_id = all_search(lat,lon)
    return next_cam_id
        
#For camera facing east
def algo_E(lat,lon,edge):
    ch = False
    next_cam_id = 0
    if edge == 'U':
        cam_id = cam_adj.lslp(lat,lon)
        ch = det(cam_id)
        if ch == True:
            next_cam_id = cam_id
    elif edge == 'D':
        cam_id = cam_adj.lslm(lat,lon)
        ch = det(cam_id)
        if ch == True:
            next_cam_id = cam_id
    elif edge == 'L':
        cam_id = cam_adj.lpls(lat,lon)
        ch = det(cam_id)
        if ch == True:
            next_cam_id = cam_id
    elif edge == 'R':
        cam_id = cam_adj.lmls(lat,lon)
        ch = det(cam_id)
        if ch == True:
            next_cam_id = cam_id
    elif edge == 'UL':
        cam_id = cam_adj.lplp(lat,lon)
        ch = det(cam_id)
        if ch == True:
            next_cam_id = cam_id
    elif edge == 'DL':
        cam_id = cam_adj.lplm(lat,lon)
        ch = det(cam_id)
        if ch == True:
            next_cam_id = cam_id
    elif edge == 'UR':
        cam_id = cam_adj.lmlp(lat,lon)
        ch = det(cam_id)
        if ch == True:
            next_cam_id = cam_id
    elif edge == 'DR':
        cam_id = cam_adj.lmlm(lat,lon)
        ch = det(cam_id)
        if ch == True:
            next_cam_id = cam_id
    elif next_cam_id == 0:
        next_cam_id = all_search(lat,lon)
    return next_cam_id

#For camera facing west
def algo_W(lat,lon,edge):
    ch = False
    next_cam_id = 0
    if edge == 'U':
        cam_id = cam_adj.lslm(lat,lon)
        ch = det(cam_id)
        if ch == True:
            next_cam_id = cam_id
    elif edge == 'D':
        cam_id = cam_adj.lslp(lat,lon)
        ch = det(cam_id)
        if ch == True:
            next_cam_id = cam_id
    elif edge == 'L':
        cam_id = cam_adj.lmls(lat,lon)
        ch = det(cam_id)
        if ch == True:
            next_cam_id = cam_id
    elif edge == 'R':
        cam_id = cam_adj.lpls(lat,lon)
        ch = det(cam_id)
        if ch == True:
            next_cam_id = cam_id
    elif edge == 'UL':
        cam_id = cam_adj.lmlm(lat,lon)
        ch = det(cam_id)
        if ch == True:
            next_cam_id = cam_id
    elif edge == 'DL':
        cam_id = cam_adj.lmlp(lat,lon)
        ch = det(cam_id)
        if ch == True:
            next_cam_id = cam_id
    elif edge == 'UR':
        cam_id = cam_adj.lplm(lat,lon)
        ch = det(cam_id)
        if ch == True:
            next_cam_id = cam_id
    elif edge == 'DR':
        cam_id = cam_adj.lplp(lat,lon)
        ch = det(cam_id)
        if ch == True:
            next_cam_id = cam_id
    elif next_cam_id == 0:
        next_cam_id = all_search(lat,lon)
    return next_cam_id

#For camera facing south
def algo_S(lat,lon,edge):
    ch = False
    next_cam_id = 0
    if edge == 'U':
        cam_id = cam_adj.lmls(lat,lon)
        ch = det(cam_id)
        if ch == True:
            next_cam_id = cam_id
    elif edge == 'D':
        cam_id = cam_adj.lpls(lat,lon)
        ch = det(cam_id)
        if ch == True:
            next_cam_id = cam_id
    elif edge == 'L':
        cam_id = cam_adj.lslp(lat,lon)
        ch = det(cam_id)
        if ch == True:
            next_cam_id = cam_id
    elif edge == 'R':
        cam_id = cam_adj.lslm(lat,lon)
        ch = det(cam_id)
        if ch == True:
            next_cam_id = cam_id
    elif edge == 'UL':
        cam_id = cam_adj.lmlp(lat,lon)
        ch = det(cam_id)
        if ch == True:
            next_cam_id = cam_id
    elif edge == 'DL':
        cam_id = cam_adj.lplp(lat,lon)
        ch = det(cam_id)
        if ch == True:
            next_cam_id = cam_id
    elif edge == 'UR':
        cam_id = cam_adj.lmlm(lat,lon)
        ch = det(cam_id)
        if ch == True:
            next_cam_id = cam_id
    elif edge == 'DR':
        cam_id = cam_adj.lplm(lat,lon)
        ch = det(cam_id)
        if ch == True:
            next_cam_id = cam_id
    elif next_cam_id == 0:
        next_cam_id = all_search(lat,lon)
    return next_cam_id

#For camera facing northwest
def algo_NE(lat,lon,edge):
    ch = False
    next_cam_id = 0
    if edge == 'U':
        cam_id = cam_adj.lplp(lat,lon)
        ch = det(cam_id)
        if ch == True:
            next_cam_id = cam_id
    elif edge == 'D':
        cam_id = cam_adj.lmlm(lat,lon)
        ch = det(cam_id)
        if ch == True:
            next_cam_id = cam_id
    elif edge == 'L':
        cam_id = cam_adj.lplm(lat,lon)
        ch = det(cam_id)
        if ch == True:
            next_cam_id = cam_id
    elif edge == 'R':
        cam_id = cam_adj.lmlp(lat,lon)
        ch = det(cam_id)
        if ch == True:
            next_cam_id = cam_id
    elif edge == 'UL':
        cam_id = cam_adj.lpls(lat,lon)
        ch = det(cam_id)
        if ch == True:
            next_cam_id = cam_id
    elif edge == 'DL':
        cam_id = cam_adj.lslm(lat,lon)
        ch = det(cam_id)
        if ch == True:
            next_cam_id = cam_id
    elif edge == 'UR':
        cam_id = cam_adj.lslp(lat,lon)
        ch = det(cam_id)
        if ch == True:
            next_cam_id = cam_id
    elif edge == 'DR':
        cam_id = cam_adj.lmls(lat,lon)
        ch = det(cam_id)
        if ch == True:
            next_cam_id = cam_id
    elif next_cam_id == 0:
        next_cam_id = all_search(lat,lon)
    return next_cam_id

#For camera facing northeast
def algo_NW(lat,lon,edge):
    ch = False
    next_cam_id = 0
    if edge == 'U':
        cam_id = cam_adj.lplm(lat,lon)
        ch = det(cam_id)
        if ch == True:
            next_cam_id = cam_id
    elif edge == 'D':
        cam_id = cam_adj.lmlp(lat,lon)
        ch = det(cam_id)
        if ch == True:
            next_cam_id = cam_id
    elif edge == 'L':
        cam_id = cam_adj.lmlm(lat,lon)
        ch = det(cam_id)
        if ch == True:
            next_cam_id = cam_id
    elif edge == 'R':
        cam_id = cam_adj.lplp(lat,lon)
        ch = det(cam_id)
        if ch == True:
            next_cam_id = cam_id
    elif edge == 'UL':
        cam_id = cam_adj.lslm(lat,lon)
        ch = det(cam_id)
        if ch == True:
            next_cam_id = cam_id
    elif edge == 'DL':
        cam_id = cam_adj.lmls(lat,lon)
        ch = det(cam_id)
        if ch == True:
            next_cam_id = cam_id
    elif edge == 'UR':
        cam_id = cam_adj.lpls(lat,lon)
        ch = det(cam_id)
        if ch == True:
            next_cam_id = cam_id
    elif edge == 'DR':
        cam_id = cam_adj.lslp(lat,lon)
        ch = det(cam_id)
        if ch == True:
            next_cam_id = cam_id
    elif next_cam_id == 0:
        next_cam_id = all_search(lat,lon)
    return next_cam_id

#For camera facing southeast
def algo_SE(lat,lon,edge):
    ch = False
    next_cam_id = 0
    if edge == 'U':
        cam_id = cam_adj.lmlp(lat,lon)
        ch = det(cam_id)
        if ch == True:
            next_cam_id = cam_id
    elif edge == 'D':
        cam_id = cam_adj.lplm(lat,lon)
        ch = det(cam_id)
        if ch == True:
            next_cam_id = cam_id
    elif edge == 'L':
        cam_id = cam_adj.lplp(lat,lon)
        ch = det(cam_id)
        if ch == True:
            next_cam_id = cam_id
    elif edge == 'R':
        cam_id = cam_adj.lmlm(lat,lon)
        ch = det(cam_id)
        if ch == True:
            next_cam_id = cam_id
    elif edge == 'UL':
        cam_id = cam_adj.lslp(lat,lon)
        ch = det(cam_id)
        if ch == True:
            next_cam_id = cam_id
    elif edge == 'DL':
        cam_id = cam_adj.lpls(lat,lon)
        ch = det(cam_id)
        if ch == True:
            next_cam_id = cam_id
    elif edge == 'UR':
        cam_id = cam_adj.lmls(lat,lon)
        ch = det(cam_id)
        if ch == True:
            next_cam_id = cam_id
    elif edge == 'DR':
        cam_id = cam_adj.lslm(lat,lon)
        ch = det(cam_id)
        if ch == True:
            next_cam_id = cam_id
    elif next_cam_id == 0:
        next_cam_id = all_search(lat,lon)
    return next_cam_id

#For camera facing southwest
def algo_SW(lat,lon,edge):
    ch = False
    next_cam_id = 0
    if edge == 'U':
        cam_id = cam_adj.lmlm(lat,lon)
        ch = det(cam_id)
        if ch == True:
            next_cam_id = cam_id
    elif edge == 'D':
        cam_id = cam_adj.lplp(lat,lon)
        ch = det(cam_id)
        if ch == True:
            next_cam_id = cam_id
    elif edge == 'L':
        cam_id = cam_adj.lmlp(lat,lon)
        ch = det(cam_id)
        if ch == True:
            next_cam_id = cam_id
    elif edge == 'R':
        cam_id = cam_adj.lplm(lat,lon)
        ch = det(cam_id)
        if ch == True:
            next_cam_id = cam_id
    elif edge == 'UL':
        cam_id = cam_adj.lmls(lat,lon)
        ch = det(cam_id)
        if ch == True:
            next_cam_id = cam_id
    elif edge == 'DL':
        cam_id = cam_adj.lslp(lat,lon)
        ch = det(cam_id)
        if ch == True:
            next_cam_id = cam_id
    elif edge == 'UR':
        cam_id = cam_adj.lslm(lat,lon)
        ch = det(cam_id)
        if ch == True:
            next_cam_id = cam_id
    elif edge == 'DR':
        cam_id = cam_adj.lpls(lat,lon)
        ch = det(cam_id)
        if ch == True:
            next_cam_id = cam_id
    elif next_cam_id == 0:
        next_cam_id = all_search(lat,lon)
    return next_cam_id



