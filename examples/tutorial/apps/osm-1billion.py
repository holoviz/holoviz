import holoviews as hv, geoviews as gv, param, dask.dataframe as dd, panel as pn
from holoviews.operation.datashader import datashade, rasterize, shade
from holoviews.streams import RangeXY
from colorcet import cm

hv.extension('bokeh', logo=False)

df = dd.read_parquet('../../data/osm-1billion.snappy.parq').persist()

cmaps = ['fire','bgy','bgyw','bmy','gray','kbc']
topts = dict(width=900,height=600,xaxis=None,yaxis=None,bgcolor='black',show_grid=False)

class OSM(param.Parameterized):
    alpha = param.Magnitude(default=0.75, doc="Map tile opacity")
    cmap  = param.ObjectSelector(cm['fire'], objects={c:cm[c] for c in cmaps})
    
    @param.depends('alpha')
    def tiles(self):
        return gv.tile_sources.EsriImagery.options(alpha=self.alpha, **topts)

    @param.depends()
    def view(self):
        points = hv.DynamicMap(hv.Points(df, kdims=['x', 'y']))
        raster = rasterize(points, x_sampling=1, y_sampling=1, width=900, height=600)
        return hv.DynamicMap(self.tiles) * shade(raster, streams=[hv.streams.Params(self, ['cmap'])])

osm = OSM(name="Open Street Map GPS")
pn.Row(osm.param, osm.view).servable()
