 
<div align="center">

 <br/> 
 
 <h1 align="center">  MapZ </h1>
 
 <br/> 
 
 
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
![Size](https://img.shields.io/github/repo-size/agroengaard/mapz)
![GitHub top language](https://img.shields.io/github/languages/top/agroengaard/mapz)
![GitHub last commit](https://img.shields.io/github/last-commit/agroengaard/mapz)
 
 
 
 
 
 
 
 
 
 <br/>
<i> A repository for containing python code for creating various map plots </i>
 
</div>

<br/><br/>

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



<br/><br/>

Or to plot all the worlds airports:

```python
from mapplot import MapPlot

mymap = MapPlot(style="cyberpunk")
mymap.show_airports()
 
```

<div align="center">
<img src="./docs/cyberpunk_airports.png" width="1000">
</div>


<br/><br/>

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



<br/><br/>


### Plots with networks


Another example, could be combining a map plot with a networks plot, and also pie plots for each country. See for the following example with some made up data for finnish metal "exports":


```python
from mapplot import MapPlot
import pandas as pd

mydict = {"DEU": {"Metal": 3, "Death Metal":4, "Black Metal":2, "Folk Metal":1},
          "POL": {"Metal": 2, "Death Metal":1, "Black Metal":1, "Folk Metal":3},
          "DNK": {"Metal": 5, "Death Metal":3, "Black Metal":2, "Folk Metal":1},
          "NOR": {"Metal": 1, "Death Metal":4, "Black Metal":9, "Folk Metal":3},
          "ISL": {"Metal": 1, "Death Metal":4, "Black Metal":4, "Folk Metal":8}
          }

df = pd.DataFrame.from_dict(mydict)
mymap = MapPlot(place="Europe", style="cyberpunk", title="Finnish Metal Music Export")
mymap.add_country_network(country="FIN", dataframe=df, directed=True)
mymap.add_pie_charts(dataframe=df)
mymap.save()
 
```

From which you should be able to produce the folloing plot:

<div align="center">
<img src="./docs/pie_plot_example.png" width="700">
</div>

You should be able to replacate this example with any data you like and for any countries you would like, as long as you follow the dataframe structure in the example.




<br/><br/>

## Notes

Available regions that you can specify in the the "place" parameter when calling "MapPlot" are:
- Africa
- Asia
- Europe
- North America
- South America
- Oeania
- Norway
- Sweden
- Denmark

I can add more if anyone requests them.


Available styles that you can specify under the "style" parameter when calling "MapPlot", in the time of writing are:
- light
- dark
- cyberpunk

Some of the geometric country centroids that define the placement of country network nodes have been manually edited for aesthetic reasons (for example, the geometric centroid of Norway is inside Sweden, or the geometric centroid of Portugal is in the Atlantic Ocean) or to better represent the population density (For example, Swedens and Great Britain's node has been moved south). The centroids that have been edited are:
- Norway
- Sweden
- Portugal
- Great Britain
- Finland
- USA

## Acknowledgements


Country shapefiles obtained from: https://public.opendatasoft.com/explore/dataset/world-administrative-boundaries/export/

Shapefiles for airports, ports and urban areas were obtained from: https://www.naturalearthdata.com/downloads/
