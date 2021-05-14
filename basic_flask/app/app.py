from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
	return "Hello World! Changes RR - Destiny"

@app.route('/home')
def home():
	return "Destiny Awaits you!"


print("starting web server")
if __name__ == '__main__':
	app.run(host='0.0.0.0',debug=True)