import mapnik
from mapnik import PostGIS, Layer
from io import BytesIO


def render():
    m = mapnik.Map(256, 256)
    im = mapnik.Image(256, 256)

    s = mapnik.Style()
    r = mapnik.Rule()

    ptsym = mapnik.PointSymbolizer()
    r.symbols.append(ptsym)
    s.rules.append(r)

    m.append_style('My Style', s)

    lyr = Layer('PostGIS')
    ds = PostGIS(host='database.lambnik.azavea.com',
                 user='lamb', password='lamb',
                 dbname='lambnik-test', table='pwd_inlets')

    lyr.datasource = ds
    lyr.styles.append('My Style')
    m.layers.append(lyr)
    m.zoom_all()

    mapnik.render(m, im)

    return BytesIO(im.tostring('png')).getvalue()
