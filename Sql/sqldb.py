import MySQLdb

#Start database
db = MySQLdb.connect("localhost","root","root","recognition")

#Create DB
def create_sqldb():
    cursor = db.cursor()
    cursor.execute("DROP TABLE IF EXISTS cam_location")
    cursor.execute("DROP VIEW IF EXISTS latsort")
    cursor.execute("DROP VIEW IF EXISTS longsort")
    
    sql = "CREATE TABLE cam_location (cam_id INT PRIMARY KEY AUTO_INCREMENT,\
    latitude DECIMAL(11,8) NOT NULL, \
    longitude DECIMAL(11,8) NOT NULL,\
    face VARCHAR(2) NOT NULL);"
    cursor.execute(sql)

    sql1 = "CREATE VIEW latsort AS\
    SELECT * FROM cam_location\
    ORDER BY latitude, longitude;"
    cursor.execute(sql1)

    sql2 = "CREATE VIEW longsort AS\
    SELECT * FROM cam_location\
    ORDER BY longitude, latitude;"
    cursor.execute(sql2)
    
#Add DB
def add_cam(lat,lon,face):    
    cursor = db.cursor()
    try:
        cursor.execute("INSERT INTO cam_location(latitude,longitude,face)\
                      VALUES (%s,%s,%s);",(lat,lon,face))
        db.commit()
    except:
        db.rollback()

#View database
def view_sqldb():
    pass


#get the latitude of given cam_id
def lat(cam_id):
    cursor = db.cursor()
    try:
        cursor.execute("SELECT latitude WHERE cam_id = %s", (cam_id))
        row = cursor.fetchone()
        lat = row[1]
    except:
        lat = None
    return lat

#get the longitude of given cam_id
def lon(cam_id):
    cursor = db.cursor()
    try:
        cursor.execute("SELECT longitude WHERE cam_id = %s", (cam_id))
        row = cursor.fetchone()
        lon = row[1]
    except:
        lon = None
    return lon

def face(cam_id):
    cursor = db.cursor()
    try:
        cursor.execute("SELECT face WHERE cam_id = %s", (cam_id))
        row = cursor.fetchone()
        face = row[1]
    except:
        face = None
    return face

def lplm(lat,lon):
    cursor = db.cursor()
    sql("SELECT cam_id FROM \
    (SELECT cam_id FROM latsort WHERE latitude > %s )\
    WHERE longitude < %s ORDER BY longitude DESC LIMIT 1", (lat,lon))
    cursor.execute(sql)
    cam_id = cursor.fetchone()
    return cam_id

def lplp(lat,lon):
    cursor = db.cursor()
    sql("SELECT cam_id FROM \
    (SELECT cam_id FROM latsort WHERE latitude > %s )\
    WHERE longitude > %s ORDER BY longitude LIMIT 1", (lat,lon))
    cursor.execute(sql)
    cam_id = cursor.fetchone()
    return cam_id

def lmlm(lat,lon):
    cursor = db.cursor()
    sql("SELECT cam_id FROM \
    (SELECT cam_id FROM latsort WHERE latitude < %s ORDER BY latitude DESC )\
    WHERE longitude < %s ORDER BY longitude DESC LIMIT 1", (lat,lon))
    cursor.execute(sql)
    cam_id = cursor.fetchone()
    return cam_id

def lmlp(lat,lon):
    cursor = db.cursor()
    sql("SELECT cam_id FROM \
    (SELECT cam_id FROM latsort WHERE latitude < %s ORDER BY latitude DESC )\
    WHERE longitude > %s ORDER BY longitude LIMIT 1", (lat,lon))
    cursor.execute(sql)
    cam_id = cursor.fetchone()
    return cam_id

def lslm(lat,lon):
    cursor = db.cursor()
    sql("SELECT cam_id FROM \
    (SELECT cam_id FROM latsort WHERE latitude = %s)\
    WHERE longitude < %s ORDER BY longitude DESC LIMIT 1", (lat,lon))
    cursor.execute(sql)
    cam_id = cursor.fetchone()
    return cam_id

def lslp(lat,lon):
    cursor = db.cursor()
    sql("SELECT cam_id FROM \
    (SELECT cam_id FROM latsort WHERE latitude = %s )\
    WHERE longitude > %s ORDER BY longitude LIMIT 1", (lat,lon))
    cursor.execute(sql)
    cam_id = cursor.fetchone()
    return cam_id

def lmls(lat,lon):
    cursor = db.cursor()
    sql("SELECT cam_id FROM \
    (SELECT cam_id FROM latsort WHERE latitude < %s ORDER BY latitude DESC )\
    WHERE longitude = %s LIMIT 1", (lat,lon))
    cursor.execute(sql)
    cam_id = cursor.fetchone()
    return cam_id

def lpls(lat,lon):
    cursor = db.cursor()
    sql("SELECT cam_id FROM \
    (SELECT cam_id FROM latsort WHERE latitude > %s ORDER BY latitude ASC )\
    WHERE longitude = %s LIMIT 1", (lat,lon))
    cursor.execute(sql)
    cam_id = cursor.fetchone()
    return cam_id

def close():
    if db:
        db.close()
