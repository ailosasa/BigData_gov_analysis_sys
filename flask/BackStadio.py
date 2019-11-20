#coding:utf-8
from flask import Flask, redirect, url_for, request, jsonify
from flask_cors import CORS
# from login_verify import check

app = Flask(__name__)
CORS(app, resources=r'/*')

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/success/<name>')
def success(name):
  return 'welcome %s' % name

@app.route('/false/<name>')
def false(name):
  return 'welcome %s' % name
   
# @app.route('/authentication', methods=['GET', 'POST'])
# def home():
#   login_form = request.json if request.method == "POST" else request.args
#   name = login_form["name"]
#   password = login_form["password"]
#   print(name)
#   print(password)
#   status = check(1, name, password)
#   if(status == 1):
#     response = {
#         'Authentication': 'Yes'
#     }
#     return jsonify(response)
#   else:
#     response = {
#         'AuAuthentic': 'No'
#     }
#     return jsonify(response)

@app.route('/authentication_test', methods=['GET', 'POST'])
def home_test():
  login_form = request.json if request.method == "POST" else request.args
  name = login_form["name"]
  password = login_form["password"]
  print(name)
  print(password)
  # status = check(1, name, password)

  if(name == 'hty'): # 测试用
    status = 1

  if(status == 1):
    response = {
        'Authentication': 'Yes'
    }
    return jsonify(response)
  else:
    response = {
        'AuAuthentic': 'No'
    }
    return jsonify(response)

@app.route('/hello/<name>')
def hello_name(name):
   return 'Hello %s!' % name

# 启动运行
if __name__ == '__main__':
    app.run()   # 这样子会直接运行在本地服务器，也即是 localhost:5000
   # app.run(host='your_ip_address') # 这里可通过 host 指定在公网IP上运行
   # app.run(host, port, debug, options)