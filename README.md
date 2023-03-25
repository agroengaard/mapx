 
<div align="center">
 
 <h1 align="center">  MapX </h1>
 
  <a href="https://github.com/AndersGroengaard/mapx/issues/new?assignees=&labels=bug&template=01_BUG_REPORT.md&title=bug%3A+">Report a Bug</a>
  ·
  <a href="https://github.com/AndersGroengaard/mapx/issues/new?assignees=&labels=enhancement&template=02_FEATURE_REQUEST.md&title=feat%3A+">Request a Feature</a>
  .
  <a href="https://github.com/AndersGroengaard/mapx/discussions">Ask a Question</a>
</div>

<br/>


<div align="center">

[![Generic badge](https://img.shields.io/badge/Python-3.9-blue)]()
[![Generic badge](https://img.shields.io/badge/version-0.1.0_a-green)]()
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
 
 
 <br/>
<i> A repository for containing python code for creating various map plots </i>
 
</div>



## Examples

For example, to plot all the worlds harbors/ports:
```python
from mapplot import MapPlot

mymap = MapPlot(style="cyberpunk")
mymap.show_ports()
 
```


<div align="center">
<img src="./docs/cyberpunk_ports.png" width="1000">
</div>

Or to plot all the worlds airports:

```python
from mapplot import MapPlot

mymap = MapPlot(style="cyberpunk")
mymap.show_airports()
 
```

<div align="center">
<img src="./docs/cyberpunk_airports.png" width="1000">
</div>


Or to plot all the worlds urban areas on a dark theme and save the image as a png in the "saved_plots" folder:

```python
from mapplot import MapPlot

mymap = MapPlot(place="Europe", style="dark")
mymap.show_urban_areas()
mymap.save("urban")
 
```

<div align="center">
<img src="./docs/dark_urban.png" width="700">
</div>



## Acknowledgements


Country shapefiles obtained from: https://public.opendatasoft.com/explore/dataset/world-administrative-boundaries/export/

Shapefiles for airports, ports and urban areas were obtained from: https://www.naturalearthdata.com/downloads/
