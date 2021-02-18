- [WebWorkShop](#webworkshop)
  - [Choropleth Maps](#choropleth-maps)
    - [Sync Folder](#sync-folder)
    - [Stand Alone Development](#stand-alone-development)
    - [Implement in Django](#implement-in-django)
  - [Draft Space](#draft-space)
  - [Flowers Plot](#flowers-plot)
    - [Stand Alone Development](#stand-alone-development-1)
    - [Implement in Django](#implement-in-django-1)

# WebWorkShop

Workshop of self-entertainment web-support projects

A web server of [django](https://www.djangoproject.com/) is established to ship the works.

Wish me a good luck.

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

## Draft Space

The projects in the work shop need some coding draft to test something.
And I would like to track them down.
As a result, the space is to practice the notebook work,
accordingly, the jupyter notebook will be used.

To avoid the notebook files overflow the language statistics in github,
since the files are always of too-large size.
I have marked the folder as **linguist-vendored** in the **.gitattributes** file.

## Flowers Plot

Plot simulation flowers using closed curves in [D3.js](https://d3js.org/d3.v6.min.js).

The files in the folder of [flowersPlot](./workShop/flowersPlot).

### Stand Alone Development

One can enter the folder, and browse the [index.html](./workShop/flowersPlot/index.html).
It will automatically operates the .js scripts and plots the flowers.

### Implement in Django

- The Workshop Side

  The [index.html](./workShop/flowersPlot/index.html) file is modified and moved to the template file of [flowersPlot.html](./serverDjango/templates/flowersPlot.html).
  The '{{prefix}}' placeholder is added into the .js importing commands.

  ```html
  <script type="text/javascript" src="{{prefix}}/css-colors.js"></script>
  <script type="text/javascript" src="{{prefix}}/flower.js"></script>
  <script type="text/javascript" src="{{prefix}}/draw.js"></script>
  ```

- The Django Side

  - The Django render can use the [workshop folder](./workshop/flowersPlot) as the **workingDir** variable.
  - The route of the .js files are added into **url_patterns** to serve the calling of the .js files.

  ```python
  # Setup the working_dir
  working_dir = os.path.join(
      os.path.dirname(__file__),
      '..',
      '..',
      'workshop',
      'flowersPlot'
  )

  # Route path
  route = r'^flowersPlot/(.{1,20}\.js)$'

  # The working_dir is pre-allocated
  def view(request, x):
      return HttpResponse(
          open(os.path.join(working_dir, x)).read(),
          'application/javascript')

  # Setup routes
  url(route, view)
  ```

Then the Django can render the template of the flowers plot.
And the route path is **/flowersPlot**.
