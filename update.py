#!/usr/bin/python

def update1(date_input, testcaseid,  status, category):

	import MySQLdb
	# Open database connection
	db = MySQLdb.connect("localhost","priyank","yo","priyank" )

	# prepare a cursor object using cursor() method
	cursor = db.cursor()

	# Prepare SQL query to INSERT a record into the database.
	sql = """INSERT INTO try1_log1(date, testcase_name  , status , project , testcase_category) VALUES (  '%s', '%s' ,  '%s', '%s' , 'null' )""" %(date_input, testcaseid ,status, category)



	try:
	   
	   cursor.execute(sql)
	   db.commit()
	   print "Database updated"
	except:
	   db.rollback()
	   print "database failed to update"
	# disconnect from server
	db.close()

    
