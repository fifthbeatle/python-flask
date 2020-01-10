from flask import Flask, redirect, url_for, request 

app = Flask(__name__)

@app.route('/')
def hello_world():
  print('HTTP Request has been received')
  print(request)
  return('''<h1>This is our first Flask app</h1>
            <p>We will learn how to deploy this to Openshift''')

if __name__ == '__main__':
  app.run()