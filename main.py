from bottle import route, run, template, get, post, request, static_file, os
import home, parser
from urllib.parse import quote

@route('/')
def index():
    #return template('<b>Helloo {{name}}</b>!', name=name)
    print("os")
    return template(home.temp(), search_results="", greet=True)


@route('/', method="POST")
def search():
    word = request.forms.get('keyword')
    #do search
    return template(home.temp(), search_results=parser.data(word), greet=False)


my_module = os.path.abspath(__file__)
parent_dir = os.path.dirname(my_module)
static_dir = os.path.join(parent_dir, 'static')

@route('/static/<filename:path>')
def static(filename):
    return static_file(filename, root=static_dir)


run(host='localhost', port=8080)

