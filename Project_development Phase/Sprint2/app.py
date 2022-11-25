from flask import Flask, render_template, request
import ibm_db

conn=ibm_db.connect("DATABASE=bludb;HOSTNAME=815fa4db-dc03-4c70-869a-a9cc13f33084.bs2io90l08kqb1od8lcg.databases.appdomain.cloud;PORT=30367;Security=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=bqh92776;PWD=7bYNfVhcyvVn6Hot;","","")

app = Flask(__name__)
@app.route('/')
def student():
    return render_template('Home.html')
    

@app.route('/userreg',methods = ['POST', 'GET'])
def userreg():
  if request.method == 'POST':
    email = request.form['mail']
    name = request.form['name']
    phnum = request.form['phnum']
    pas = request.form['pas']
    sql = "SELECT * FROM user WHERE name =?"
    stmt = ibm_db.prepare(conn, sql)
    ibm_db.bind_param(stmt,1,name)
    ibm_db.execute(stmt)
    account = ibm_db.fetch_assoc(stmt)

    if account:
      return render_template('index.html', msg="You are already a member, please login using your details")
    else:
      insert_sql = "INSERT INTO user VALUES (?,?,?,?)"
      prep_stmt = ibm_db.prepare(conn, insert_sql)
    
      ibm_db.bind_param(prep_stmt, 1, email)
      ibm_db.bind_param(prep_stmt, 2, name)
      ibm_db.bind_param(prep_stmt, 3, phnum)
      ibm_db.bind_param(prep_stmt, 4, pas)
    
      ibm_db.execute(prep_stmt)
  return render_template('userhome.html')
  

@app.route('/adminreg',methods = ['POST', 'GET'])
def adminreg():
  if request.method == 'POST':
    name = request.form['name']
    email = request.form['mail']
    phnum = request.form['phnum']
    pas = request.form['pas']
   

    sql = "SELECT * FROM admin WHERE name =?"
    stmt = ibm_db.prepare(conn, sql)
    ibm_db.bind_param(stmt,1,name)
    ibm_db.execute(stmt)
    account = ibm_db.fetch_assoc(stmt)

    if account:
      return render_template('adminlogin.html', msg="You are already a member, please login using your details")
    else:
      insert_sql = "INSERT INTO admin VALUES (?,?,?,?)"
      prep_stmt = ibm_db.prepare(conn, insert_sql)
      ibm_db.bind_param(prep_stmt, 1, name)
      ibm_db.bind_param(prep_stmt, 2, email)
      ibm_db.bind_param(prep_stmt, 3, phnum)
      ibm_db.bind_param(prep_stmt, 4, pas)
    
      ibm_db.execute(prep_stmt)
  return render_template('admin.html')
    
@app.route('/agentreg',methods = ['POST', 'GET'])
def agentreg():
  if request.method == 'POST':
    email = request.form['mail']
    name = request.form['name']
    phnum = request.form['phnum']
    pas = request.form['pas']
   

    sql = "SELECT * FROM agent WHERE name =?"
    stmt = ibm_db.prepare(conn, sql)
    ibm_db.bind_param(stmt,1,name)
    ibm_db.execute(stmt)
    account = ibm_db.fetch_assoc(stmt)

    if account:
      return render_template('agentlogin.html', msg="You are already a member, please login using your details")
    else:
      insert_sql = "INSERT INTO agent VALUES (?,?,?,?)"
      prep_stmt = ibm_db.prepare(conn, insert_sql)
      ibm_db.bind_param(prep_stmt, 1, email)
      ibm_db.bind_param(prep_stmt, 2, name)
      ibm_db.bind_param(prep_stmt, 3, phnum)
      ibm_db.bind_param(prep_stmt, 4, pas)
    
      ibm_db.execute(prep_stmt)
  return render_template('solution.html')
   
@app.route('/loginpage',methods=['POST'])

def loginpage():
 
  user = request.form['user']
  passw = request.form['passw']
  sql = "SELECT * FROM user WHERE email =? AND pas=?"
  stmt = ibm_db.prepare(conn, sql)
  ibm_db.bind_param(stmt,1,user)
  ibm_db.bind_param(stmt,2,passw)
  ibm_db.execute(stmt)
  account = ibm_db.fetch_assoc(stmt)
  if account:
    
    return render_template('home.html')
  else:
    
    return render_template('login.html') 

@app.route('/adminlogin',methods=['POST'])

def adminlogin():
 
  user = request.form['user']
  passw = request.form['passw']
  sql = "SELECT * FROM admin WHERE email =? AND pas=?"
  stmt = ibm_db.prepare(conn, sql)
  ibm_db.bind_param(stmt,1,user)
  ibm_db.bind_param(stmt,2,passw)
  ibm_db.execute(stmt)
  account = ibm_db.fetch_assoc(stmt)
  if account:
    
    return render_template('home.html')
  else:
    
    return render_template('login.html') 

@app.route('/agentlogin',methods=['POST'])

def agentlogin():
 
  user = request.form['user']
  passw = request.form['passw']
  sql = "SELECT * FROM agent WHERE email =? AND pas=?"
  stmt = ibm_db.prepare(conn, sql)
  ibm_db.bind_param(stmt,1,user)
  ibm_db.bind_param(stmt,2,passw)
  ibm_db.execute(stmt)
  account = ibm_db.fetch_assoc(stmt)
  if account:
    
    return render_template('home.html')
  else:
    
    return render_template('login.html') 




if __name__ == '__main__':
    app.run(debug = True)
