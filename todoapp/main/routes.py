from flask import Blueprints , render_template , blueprints
# from gevent.pywsgi import WSGIServer

main = Blueprints('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

#from waitress import serve
#serve(main, host="0.0.0.0", port=8080)
# http_server = WSGIServer(("127.0.0.1", 8080), main)
# http_server.serve_forever()