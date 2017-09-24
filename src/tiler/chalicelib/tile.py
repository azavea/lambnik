import mapnik
import mercantile

from io import BytesIO
from os import environ

from mapnik import PostGIS, Layer


def tile_bounds(z, x, y):
    return mercantile.bounds(x, y, z)


def render(app, z, x, y):
    b = tile_bounds(z, x, y)

    epsg3857 = '+proj=merc +a=6378137 +b=6378137 +lat_ts=0.0 +lon_0=0.0 +x_0=0.0 +y_0=0 +k=1.0 +units=m +nadgrids=@null +wktext  +no_defs'  # noqa
    proj = mapnik.Projection(epsg3857)

    m = mapnik.Map(256, 256)
    m.srs = epsg3857
    im = mapnik.Image(256, 256)

    s = mapnik.Style()
    r = mapnik.Rule()

    ptsym = mapnik.PointSymbolizer()
    r.symbols.append(ptsym)
    s.rules.append(r)

    m.append_style('My Style', s)

    lyr = Layer('PostGIS')
    postgis_ds = PostGIS(host=environ.get('POSTGRES_HOST'),
                         user=environ.get('POSTGRES_USER'),
                         password=environ.get('POSTGRES_PASSWORD'),
                         dbname=environ.get('POSTGRES_DB'),
                         table='pwd_inlets')

    lyr.datasource = postgis_ds
    lyr.styles.append('My Style')
    m.layers.append(lyr)

    mbox = mapnik.Box2d(b.east, b.south, b.west, b.north)
    bbox = proj.forward(mbox)
    try:
        m.zoom_to_box(bbox)
        m.buffer_size = 256
        mapnik.render(m, im)

        img = im.tostring('png')
        return BytesIO(img).getvalue()
    except Exception, e:
        app.log.error(e)
