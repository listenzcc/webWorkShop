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
