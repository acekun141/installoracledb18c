from cx_Oracle

con = cx_Oracle.connect()
print(con.version)