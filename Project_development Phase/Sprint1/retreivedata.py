import ibm_db
conn=ibm_db.connect("DATABASE=bludb;HOSTNAME=815fa4db-dc03-4c70-869a-a9cc13f33084.bs2io90l08kqb1od8lcg.databases.appdomain.cloud;PORT=30367;Security=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=bqh92776;PWD=7bYNfVhcyvVn6Hot;","","")


#To retrive all the records from DB2

sql = "SELECT * FROM user"
stmt = ibm_db.exec_immediate(conn, sql)
dictionary = ibm_db.fetch_both(stmt)
values=dictionary
while dictionary != False:
    #print(dictionary)
    print ("The Name is : ",  dictionary["NAME"])
    print ("The Email is : ", dictionary["EMAIL"])
    print ("The Phone is : ", dictionary["PHNUM"])
    print(" ******************* ")
    values.update(dictionary)
    dictionary = ibm_db.fetch_both(stmt)

print(values)