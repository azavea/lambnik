import mapnik
import mercantile

from io import BytesIO
from os import environ

from mapnik import PostGIS, Layer

postgis_ds = PostGIS(host=environ.get('POSTGRES_HOST'),
                     user=environ.get('POSTGRES_USER'),
                     password=environ.get('POSTGRES_PASSWORD'),
                     dbname=environ.get('POSTGRES_DB'),
                     table='pwd_inlets')


def tile_bounds(z, x, y):
    return mercantile.bounds(x, y, z)


def grid(z, x, y):
    grd = mapnik.Grid(256, 256)
    m = create_map(z, x, y)

    mapnik.render_layer(m, grd, layer=0, fields=['inlettype'])
    utfgrid = grd.encode('utf', resolution=4)

    return utfgrid


def image(z, x, y):
    img = mapnik.Image(256, 256)

    m = create_map(z, x, y)
    mapnik.render(m, img)
    png = img.tostring('png')

    return BytesIO(png).getvalue()


def create_map(z, x, y):
    # Get the lat/lng bounds for this ZXY tile
    b = tile_bounds(z, x, y)

    # Create a web mercator map
    epsg3857 = '+proj=merc +a=6378137 +b=6378137 +lat_ts=0.0 +lon_0=0.0 +x_0=0.0 +y_0=0 +k=1.0 +units=m +nadgrids=@null +wktext  +no_defs'  # noqa
    proj = mapnik.Projection(epsg3857)
    m = mapnik.Map(256, 256)
    m.srs = epsg3857

    # Specify symobolgy for the tile features
    style = mapnik.Style()
    rule = mapnik.Rule()

    ptsym = mapnik.PointSymbolizer()
    rule.symbols.append(ptsym)
    style.rules.append(rule)
    m.append_style('My Style', style)

    # Create a postgis layer
    lyr = Layer('PostGIS')
    lyr.datasource = postgis_ds
    lyr.styles.append('My Style')
    m.layers.append(lyr)

    # Clip map just to the tile bounds
    wg84_bbox = mapnik.Box2d(b.east, b.south, b.west, b.north)
    wm_bbox = proj.forward(wg84_bbox)
    m.zoom_to_box(wm_bbox)

    m.buffer_size = 256

    return m
