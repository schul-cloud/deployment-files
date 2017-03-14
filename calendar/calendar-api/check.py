import psycopg2
import subprocess
conn = None
i = 0
while i < 10:
	try:
			conn = psycopg2.connect("dbname='schulcloud_calendar' user='node' host='postgres'")
			print("Successfully connected to postgres")
			break
	except:
			print("Will retry connecting to postgres")
	i = i +1
cur = conn.cursor()
cur.execute("select exists(select 1 from information_schema.tables where table_name='events')")
exists = bool(cur.rowcount)
if exists:
	subprocess.call("./start.sh")
else:
	subprocess.call("./database.sh")
	subprocess.call("./start.sh")
