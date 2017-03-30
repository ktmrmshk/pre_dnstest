from flask import Flask, render_template, Markup, request

app=Flask(__name__)

@app.route('/', methods=['GET'])
@app.route('/index.html')
def index():
  pagedata={'zone':'example.com', 'authns':'a123.12.akamai.net', 'zonefile':'zonezone'}
  pagedata['console']='result is gone'
  pagedata['table']=[(True,2,3), (False,4,5)]
  pagedata['action'] = '/'
  return render_template('pre_dns_check.html', pd=pagedata)


@app.route('/', methods=['POST'])
def recv_post():
  pagedata={}
  pagedata['authns']=request.form['authns']
  pagedata['zone']=request.form['zone']
  pagedata['zonefile']=request.form['zonefile']

  pagedata['action'] = '/'
  pagedata['console']='postdata received'
  pagedata['table']=[(True,2,3), (False,4,5)]
  return render_template('pre_dns_check.html', pd=pagedata)
  

if __name__ == "__main__":
  app.run(debug = True)


