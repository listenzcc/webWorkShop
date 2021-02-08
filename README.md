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

- The folder is some folder in the disk, whose full path is saved in environ variable of **sync**.
- The transform is performed by archiving and saving in cloud space of QQ **manually**.

### Mapping

The choropleth maps part is not done yet.

## Flowers Plot

Plot simulation flowers using closed curves in [D3.js](https://d3js.org/d3.v6.min.js).

The files in the folder of [flowersPlot](./workShop/flowersPlot).

### Stand Alone Development

One can enter the folder, and browse the [index.html](./workShop/flowersPlot/index.html).
It will automatically operates the .js scripts and plots the flowers.

### Implement in Django

- The Workshop Side

  The [index.html](./workShop/flowersPlot/index.html) file is modified and moved to the template file of [flowersPlot.html](./serverDjango/templates/flowersPlot.html).
  The '{{workingDir}}' placeholder is added into the .js importing commands.

  ```html
  <script type="text/javascript" src="{{workingDir}}/css-colors.js"></script>
  <script type="text/javascript" src="{{workingDir}}/flower.js"></script>
  <script type="text/javascript" src="{{workingDir}}/draw.js"></script>
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
