#Created by Abhimanyu Singh 
#Contact abhimanyus1997@gmail.com
#All rights reserved © 2019 Abhimanyu Singh

import socket, psutil, os

from flask import Flask, redirect, request, url_for, render_template

app = Flask(__name__)

#Variable to store CPU usage Data of Raspberry pi
cpu_usage = psutil.cpu_percent(interval=1, percpu=True)
cpu_count = psutil.cpu_count()
cpu_freq = psutil.cpu_freq()
virtual_mem = psutil.virtual_memory()
swap_mem = psutil.swap_memory()
disk_part = psutil.disk_partitions()
disk_usage = psutil.disk_usage('/')
cpu_temp = psutil.sensors_temperatures(fahrenheit=False)

@app.route('/')
def dashboard():
      return render_template('dash.html')


@app.route('/rpi')
def raspberry():
      return render_template('rpi.html',cpu_usage=cpu_usage,cpu_count=cpu_count,cpu_freq=cpu_freq,virtual_mem=virtual_mem,swap_mem=swap_mem,disk_part=disk_part,disk_usage=disk_usage,cpu_temp=cpu_temp)

@app.route('/welcome')
def welcome():
      return render_template('welcome.html')

@app.route('/sensor')
def sensor_data():
   return render_template('sensor.html')

@app.route('/myconsole')
def myconsole():
      return render_template('myconsole.html')

#======LOGIN PAGES====
@app.route('/login',methods = ['POST', 'GET'])
def login():
   return render_template('login.html')

@app.route('/admin')
def hello_admin():
   return 'Hello Admin'

@app.route('/guest/<guest>')
def hello_guest(guest):
   return 'Hello %s as Guest' % guest

@app.route('/user/<name>')
def hello_user(name):
   if name =='admin':
      return redirect(url_for('hello_admin'))
   else:
      return redirect(url_for('hello_guest',guest = name))

if __name__ == '__main__':
   app.run(
      host = "0.0.0.0",
      port = 80,
      debug = True
      )
