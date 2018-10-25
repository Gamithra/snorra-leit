from bottle import route, run, template, get, post, request, static_file, os
import home, parser
from urllib.parse import quote

@route('/')
def index():
    return template(home.temp(), search_results="", greet=True)


@route('/', method="POST")
def search():
    word = request.forms.get('keyword')
    myndir = parser.word(word)
    results = parser.data(word)
    if results == []: success = False
    else: success = True
    return template(home.temp(), success=success, search_results=results, words=myndir, greet=False, keyword=word)


my_module = os.path.abspath(__file__)
parent_dir = os.path.dirname(my_module)
static_dir = os.path.join(parent_dir, 'static')

@route('/static/<filename:path>')
def static(filename):
    return static_file(filename, root=static_dir)



if os.environ.get('APP_LOCATION') == 'heroku':
    run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
else:
    run(host='localhost', port=8080, debug=True)
