from flask import Flask, render_template, Markup

app=Flask(__name__)

@app.route('/')
@app.route('/index.html')
def index():
  return 'about this page'

@app.route('/template/')
def from_temp():
  data = {'Goo':'0101', 'Foo':'masa', '123':6, 987: 'strstr'}
  msg = Markup('<i>%s</i>') % '<tag> is a tag'
  msg2 = '<h4>this is h4 line</h4>'
  plaintxt='''
Abc
egfdsafa
dsfaf\n124231
'''

  return render_template('tmp.html', name='hoge', name2='foobar', msg=msg, data=data, msg2=msg2, plaintxt=plaintxt)


if __name__ == "__main__":
  app.run(debug = True)


