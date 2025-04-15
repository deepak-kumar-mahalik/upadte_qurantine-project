from flask_mysqldb import MySQL
from flask import Flask, render_template,request

app=Flask(__name__)

app.config['MYSQL_USER']='root'
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_PASSWORD']='chiku@123'
app.config['MYSQL_DB']='mine'

dp=MySQL(app)

@app.route('/')
def dub():
    return render_template('Q_Home.html')

@app.route('/a')
def dy():
    return render_template('QHOM.html')

@app.route('/b')
def sya():
    return render_template('Availability.html')

@app.route('/c')
def so():
    return render_template('Book_now.html')

@app.route('/d')
def ji():
    return render_template('Facilities.html')

@app.route('/e')
def sun():
    return render_template('FAQ.html')

@app.route('/f')
def aj():
    return render_template('CON.html')

@app.route('/g')
def au():
    return render_template('Introduction.html')

@app.route('/h')
def gu():
    return render_template('Servicess.html')

@app.route('/i')
def wt():
    return render_template('Announ.html')

@app.route('/j')
def jk():
    return render_template('Facility.html')

@app.route('/k')
def bj():
    return render_template('Update.html')

@app.route('/l')
def duch():
    return render_template('Meal.html')

@app.route('/m')
def gok():
    return render_template('Health.html')

@app.route('/n')
def al():
    return render_template('Facilityy.html')

@app.route('/o')
def ad():
    return render_template('q_login.html')

@app.route('/register')
def xc():
    return render_template('q_regi.html')

@app.route('/cann')
def ch():
    return render_template('cancel.html')

@app.route('/t')
def ki():
    return render_template('admin.html')

@app.route('/v')
def dv():
    return render_template('payment.html')

@app.route('/ab',methods=['post'])
def fu():
    na  = request.form['name']
    em  = request.form['email']
    msg = request.form['message']
    faq = request.form['FAQ']
    nam = request.form['name_book']
    con = request.form['contact_book']
    id  = request.form['idNumber']
    rom = request.form['roomType']
    chi = request.form['checkIn']
    cho = request.form['checkOut']
    req = request.form['requests']
    pay = request.form['paymentMethod']
    naa = request.form['room']
    loc = request.form['location']
    fas = request.form['facilities']
    emw = request.form['q_lem']
    pas = request.form['q_lpa']
    ful = request.form['q_rna']
    emd = request.form['q_rem']
    pae = request.form['q_rpa']
    pss = request.form['q_rcp']
    gsd = request.form['cancel_id']
    khd = request.form['cancel_msg']
    conn = dp.connection.cursor()
    conn.execute('insert into student(name,email,message,FAQ,name_book,contact_book,idNumber,roomType,checkIn,checkOut,requests,paymentMethod,room,location,facilities,q_lem,q_lpa,q_rna,q_rem,q_rpa,q_rcp,cancel_id,cancel_msg) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(na,em,msg,faq,nam,con,id,rom,chi,cho,req,pay,naa,loc,fas,emw,pas,ful,emd,pae,pss,gsd,khd))
    dp.connection.commit()
    conn.close()
    return render_template('Thanks.html')

app.run(debug=True,port=36780)