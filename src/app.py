from chalice import Chalice, Response
import logging
import test

app = Chalice(app_name='tiler')
app.log.setLevel(logging.DEBUG)


@app.route('/')
def index():
    return "ghost mouse"


@app.route('/tile.png')
def tile():
    app.log.debug('test')
    return Response(body=test.render(),
                    status_code=200,
                    headers={
                        'Content-Type': 'image/png'
                        })


@app.route('/favicon.ico')
def favicon():
    pass
