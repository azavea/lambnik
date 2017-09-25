from chalice import Chalice, Response, ChaliceViewError
from chalicelib import tile

import logging
import traceback

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
        inlet = get_filter(app.current_request)
        grd = tile.grid(int(z), int(x), int(y), inlet)

        return grd
    except Exception, e:
        return handle_exception(e)


@app.route('/tile/{z}/{x}/{y}')
def render_tile(z, x, y):
    app.log.debug('tile')
    try:
        inlet = get_filter(app.current_request)
        img = tile.image(int(z), int(x), int(y), inlet)

        return Response(body=img, status_code=200,
                        headers={
                            'Content-Type': 'image/png'
                        })
    except Exception, e:
        return handle_exception(e)


@app.route('/favicon.ico')
def favicon():
    pass


def get_filter(req):
    if req.query_params:
        return req.query_params.get('type', None)
    else:
        return None

def handle_exception(e):
    app.log.error(e)
    app.log.error(traceback.format_exc())
    return ChaliceViewError(e.message)

