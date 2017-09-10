from chalice import Chalice, Response
import logging
from chalicelib import tile

app = Chalice(app_name='lambnik-tiler')
app.log.setLevel(logging.DEBUG)


@app.route('/')
def index():
    app.log.debug('ghose mouse')
    return "ghost mouse"


@app.route('/tile/{z}/{x}/{y}')
def render(z, x, y):
    app.log.debug('zxy')
    try:
        img = tile.render(app, int(z), int(x), int(y))
        return Response(body=img, status_code=200,
                        headers={
                            'Content-Type': 'image/png'
                            }
                        )
    except Exception, e:
        app.log.error(e)


@app.route('/favicon.ico')
def favicon():
    pass
