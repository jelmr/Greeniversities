from app import app as frontend
from backend import app as backend
from werkzeug.serving import run_simple
from werkzeug.wsgi import DispatcherMiddleware

app = DispatcherMiddleware(frontend, {
        '/api':     backend
        })

