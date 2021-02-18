## Choropleth Maps

Draw interactive maps using geoData of choropleth map.

The geoData of choropleth map is stored in the **sync** folder.

### Sync Folder

The sync folder setting is an experimental method.
It allows programmers accessing to their **large-in-size** files easily across different machines or even platforms.
The aim of the setting is to keep the files in the same structure and being easily transformed and synchronized.

The current state is crude,

- The folder is some folder on the disk, whose full path is saved in environ variable named as **sync**.
- The transform is performed by archiving and saving in cloud space of QQ **manually**.

### Stand Alone Development

The project is to draw choropleth maps using d3-geo library.

- The [data.js](./workShop/choroplethMaps/data.js) is the example of loading **geojson** file to the variable of **geoJson**.
- The [rewind.js](./workShop/choroplethMaps/rewind.js) is a tool from [https://github.com/mapbox/geojson-rewind].
  The aim is to rewind the order of the vertex of the multi-polygon to **CLOCK-WISE**,
  which is actually the points in **features** option of the geojson object.
  The reason is as below
  > The GeoJSON specification is picky about winding order.
  >
  > This helps you generate compliant Polygon and MultiPolygon geometries. Furthermore it lets you use Canvas and other drawing libraries's default behavior to color the interior rings of Polygon and MultiPolygon features.

### Implement in Django

The [choroplethMaps.html](./serverDjango/templates/choroplethMaps.html) is generated to show the project.
The '{{prefix}}' placeholder is added to locate the .js files in the workShop folder.

In the Django view,
the class of **ChoroplethMapsView** is used to maintain the service.
The view file is [view_collection.py](./serverDjango/serverDjango/views_collection.py).

```python

    def __init__(self, dir=None):
        '''
        Init the View

        Args:
        - @dir: Full path of the directory containing the required files.
        '''
        if dir is not None:
            self.dir = dir
        else:
            self.dir = os.path.join(os.environ.get(
                'SYNC', None), 'GeoData', 'json-files')

        self.prefix = 'choroplethMaps'

        self.working_dir = os.path.join(
            os.path.dirname(__file__),
            '..',
            '..',
            'workshop',
            'choroplethMaps'
        )

```

As a result, the user should make sure the directory of **SYNC** is in the environ variables,
and the folder has the correct files.
