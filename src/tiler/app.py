from chalice import Chalice, Response, ChaliceViewError
import logging
from chalicelib import tile

app = Chalice(app_name='lambnik-tiler')
app.log.setLevel(logging.DEBUG)


@app.route('/')
def index():
    app.log.debug('ghose mouse')
    return "ghost mouse"


@app.route('/grid/{z}/{x}/{y}', cors=True)
def render_grid(z, x, y):
    app.log.debug('grid')
    try:
        grd = tile.grid(int(z), int(x), int(y))
        return grd
    except Exception, e:
        app.log.error(e)
        return ChaliceViewError(e.message)


@app.route('/tile/{z}/{x}/{y}')
def render_tile(z, x, y):
    app.log.debug('tile')
    try:
        img = tile.image(int(z), int(x), int(y))
        return Response(body=img, status_code=200,
                        headers={
                            'Content-Type': 'image/png'
                        })
    except Exception, e:
        app.log.error(e)
        return ChaliceViewError(e.message)


@app.route('/favicon.ico')
def favicon():
    pass
