from flask.ext.lesscss import lesscss
from app import app
lesscss(app)
app.run(host='0.0.0.0' ,debug = True)
