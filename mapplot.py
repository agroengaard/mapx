"""
===============================================================================
|| Script for creating various map plots
===============================================================================

    Tested with:
        Basemap 1.3.6
        

    Written in Python 3.9
    by agroengaard    


  Country shapefiles downloaded from:
      https://public.opendatasoft.com/explore/dataset/world-administrative-boundaries/export/


  Roads downloaded from:
      https://www.naturalearthdata.com/downloads/10m-cultural-vectors/

  Urban shapes downloaded from:     
     https://www.oecd.org/cfe/regionaldevelopment/functional-urban-areas.htm

===============================================================================
"""

import aulibrary as au 


import os
import json
import numpy as np
import networkx as nx

import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
from matplotlib.collections import PatchCollection
from matplotlib.patches import Polygon

from mpl_toolkits.axes_grid1.inset_locator import inset_axes

# =============================================================================
# 
# =============================================================================

 
 

class MapPlot:
    """
    ===========================================================================
    || CLASS FOR CREATING VARIOUS PLOTS WITH MAPS, COUNTRIES AND POSSIBLY    ||
    || COMBINED WITH OTHER THINGS LIKE NETWORKS, BAR PLOTS ETC.              ||
    ===========================================================================
    """
    def __init__(self, **kwargs):
        
        self.place = kwargs.get("place", "World")
        self.draw_lines = kwargs.get("draw_lines", False)
        self.style = kwargs.get("style", "light")
        self.resolution = kwargs.get("resolution", None)
        self._figsize = kwargs.get("figsize", None)
        
        self._define_themes()
        self._define_mapmode()
        
        if self.resolution == None:
            self._res = self.mapmode["resolution"]
        else:
            self._res = self.resolution
            
        if self._figsize == None:
            self._figsize = self.mapmode.get("figsize", (6,6))
            
        self.fig = plt.figure(figsize=self._figsize)
        self.ax = self.fig.add_subplot(111)
        
        if self.mapmode["definition"] == "edge_to_edge":    
            self.m = Basemap(llcrnrlat=self.mapmode['llcrnrlat'],
                             urcrnrlat=self.mapmode['urcrnrlat'],
                             llcrnrlon=self.mapmode['llcrnrlon'],
                             urcrnrlon=self.mapmode['urcrnrlon'],
                             resolution = self._res,                           # Possible values are:  c (crude), l (low), i (intermediate), h (high), f (full) 
                             projection = self.mapmode['projection'],          # Possible values: 'merc', 'laea'
                             lat_ts= self.mapmode['lat_ts'],
                             ax = self.ax)
        else:
            self.m = Basemap(width = self.mapmode['width'], 
                             height = self.mapmode['height'], 
                             lat_ts = self.mapmode['lat_ts'], 
                             lat_0 = self.mapmode['lat_0'],
                             lon_0 = self.mapmode['lon_0'],
                             resolution = self._res,                           # Possible values are:  c (crude), l (low), i (intermediate), h (high), f (full) 
                             projection = self.mapmode['projection'],          # Possible values: 'merc', 'laea'                  
                             ax = self.ax)     
        
        if self.draw_lines:
            parallels = np.arange(0.,81,10.)
            self.m.drawparallels(parallels,labels=[False,True,True,False])
            meridians = np.arange(10.,351.,20.)
            self.m.drawmeridians(meridians,labels=[True,False,False,True])
        
        self.m.drawmapboundary(fill_color = self.theme[self.style]["ocean"],
                               zorder=0, ax=self.ax)
        self.m.fillcontinents(color=self.theme[self.style]["continents"],
                              alpha=0.5, zorder=0.1, ax=self.ax)
        self.m.drawcountries(color=self.theme[self.style]["borders"], 
                             linewidth=0.6, zorder=3, ax=self.ax)
                
        self.ax.spines["top"].set_visible(False)
        self.ax.spines["right"].set_visible(False)
        self.ax.spines["left"].set_visible(False)
        self.ax.spines["bottom"].set_visible(False)
        plt.tight_layout()
        
        
    def save(self, filename):
        """
        -----------------------------------------------------------------------
        | Method for saving the plot                                          |
        -----------------------------------------------------------------------
        """
        self.output_folder = "./saved_plots/"
        self.output_path = os.path.join(self.output_folder, filename+".png")
        plt.savefig(self.output_path, bbox_inches='tight', pad_inches=-0.1)
        
        
        
    def _define_mapmode(self):
        """
        -----------------------------------------------------------------------
        | Method for defining the map layout, projection amd limits           |
        -----------------------------------------------------------------------
        """
        if self.place == "Europe":
            self.mapmode = {'definition': 'center_and_height_width',
                            'figsize': (12,12),
                            'width': 4000000,
                            'height': 4000000,
                            'lat_0': 54,
                            'lon_0':12,
                            'lat_ts': 45,
                            'projection': 'laea',
                            'resolution': 'l'
                            }
      
        elif self.place == "Norway":
            self.mapmode = {'definition': 'center_and_height_width',
                            'width': 1400000,
                            'height': 1400000,
                            'lat_0': 56,
                            'lon_0':6,
                            'lat_ts': 45,
                            'projection': 'laea'
                            }
              
        elif self.place == "Sweden":
            self.mapmode = {'definition': 'center_and_height_width',
                            'width': 1500000,
                            'height': 1500000,
                            'lat_0': 57,
                            'lon_0':15,
                            'lat_ts': 45,
                            'projection': 'laea'
                            }
            
        elif self.place == "Denmark":
            self.mapmode = {'definition': 'center_and_height_width',
                            'width': 400000,
                            'height': 400000,
                            'lat_0': 56,
                            'lon_0':11,
                            'lat_ts': 45,
                            'projection': 'laea',
                            'resolution': 'i'
                            }
        else:
            self.mapmode = {   
                'figsize': (16,9),
                'definition': 'edge_to_edge',
                'llcrnrlat':-60,
                'urcrnrlat':80,
                'llcrnrlon':-170,
                'urcrnrlon':190,
                'lat_ts':20,
                'projection': 'merc',
                'resolution': 'c'
                }
 
            
    def _define_themes(self):
        """
        -----------------------------------------------------------------------
        | Method for defining available map color themes                      |
        -----------------------------------------------------------------------
        """
        self.theme = {
                'light': {
                    'continents': au.grey,
                    'borders': 'w',
                    'ocean': 'w'
                    },
                'dark':{
                    'continents': au.AUverydarkgrey,
                    'borders': au.AUverydarkgrey,
                    'ocean': au.AUdarkgrey
                    },
                'cyberpunk':{
                    'continents':'#212946',
                    'borders': '#3a487c',
                   # 'borders': '#08F7FE',
                    'ocean':'#2A3459'               
                    } 
                }
 
    def _define_eu(self):
        """
        -----------------------------------------------------------------------
        |  Method for loading in a list of European Union (EU) and EFTA      
        |  countries in the ISO-3 code format                                 |
        -----------------------------------------------------------------------
        """
        self.eu = {"EU":[
                    'AUT', 'BEL', 'CZE', 'DEU', 'DNK', 'ESP',
                    'EST', 'FIN', 'FIN', 'FRA', 'GRC',  
                    'HUN', 'ITA', 'LTU', 'LUX', 'LVA', 'NLD', 
                    'POL', 'POL', 'PRT', 'SVK', 'SVN', 'SWE'
                       ],
                   "EU, Non-Schengen": [
                     'BGR', 'CYP', 'HRV', 'IRL', 'ROU'
                       ],
                   "EFTA": ['ISL', 'NOR', 'CHE'] 
                   }
 
    def _plot_eu(self):
        self._define_eu()

        for k, v in self.eu.items():
            _patches = []
            for i, s in zip(self.m.countries_info, self.m.countries):
                if i['iso3'] in v:
                    _patches.append(Polygon(np.array(s), True))
            self.ax.add_collection(
                PatchCollection(_patches, 
                                facecolor=au.AUblue2, 
                                edgecolor='None',
                                alpha=0.4, 
                                linewidths=1, 
                                zorder=1))  
 
    def _define_cis(self):
        """
        -----------------------------------------------------------------------
        |  Method for loading in a list of the                                |
        |  Commonwealth of Independent States (CIS)                           |   
        |  countries in the ISO-3 code format                                 |
        -----------------------------------------------------------------------
        """
        self.cis_core = ["RUS", "ARM", "AZE", "BLR", 
                         "KAZ", "KGZ", "MDA", "TJK", 
                         "UZB"]
        self.cis_associated = ["TKM"]
        
        
    def _plot_cis(self):
        self._define_cis()
        
        self._cis = []
        self._cis_associated = []
        for i, s in zip(self.m.countries_info, self.m.countries):
            if i['iso3'] in self.cis_core:
                self._cis.append(Polygon(np.array(s), True))
            elif i['iso3'] in self.cis_associated:
                self._cis_associated.append(Polygon(np.array(s), True))    
                          
        self.ax.add_collection(
            PatchCollection(self._cis, facecolor=au.AUpink, 
                            edgecolor='None', alpha=0.4, 
                            linewidths=1, zorder=1))               
        self.ax.add_collection(
            PatchCollection(self._cis_associated, facecolor=au.AUpink3, 
                            edgecolor='None', alpha=0.4, 
                            linewidths=1, zorder=1))      
 
 

    def _load_country_shapefiles(self):
        self.m.readshapefile("./shapefiles/boundaries/world-administrative-boundaries",
                             'countries', drawbounds=False)
        
    def _load_urban_shapefiles(self):
        print("Loading urban shapefiles...")
        self.m.readshapefile("./shapefiles/ne_10m_urban_areas/ne_10m_urban_areas",
                             'urban', drawbounds=False)
        print("Urban shapefiles loaded")
   
 
    def _load_ports(self):
        print("Loading port shapefiles...")
        self.m.readshapefile("./shapefiles/ne_10m_ports/ne_10m_ports",
                             'ports', drawbounds=False)
        print("Urban port loaded")
        
    def _load_airports(self):
        print("Loading airport shapefiles...")
        self.m.readshapefile("./shapefiles/ne_10m_airports/ne_10m_airports",
                             'airports', drawbounds=False)
        print("Airports loaded")
           
    def show_ports(self):
        """
        -----------------------------------------------------------------------
        | Method for adding urban areas to the plot                           |
        -----------------------------------------------------------------------
        """
        self._load_ports()
 
        scale = 0.05
        for info, port in zip(self.m.ports_info, self.m.ports):
            self.m.plot(port[0], port[1], marker="o", color=au.AUlightblue, 
                        markersize=info["natlscale"]*scale, markeredgewidth=0)
 
    
    def show_airports(self):
        """
        -----------------------------------------------------------------------
        | Method for adding urban areas to the plot                           |
        -----------------------------------------------------------------------
        """
        self._load_airports()

        scale = 0.05
        for info, airport in zip(self.m.airports_info, self.m.airports):
            self.m.plot(airport[0], airport[1], marker="o", color=au.AUpink2, 
                        markersize=info["natlscale"]*scale, markeredgewidth=0)
    
 
    def show_urban_areas(self):
        """
        -----------------------------------------------------------------------
        | Method for adding urban areas to the plot                           |
        -----------------------------------------------------------------------
        """
        self._load_urban_shapefiles()

        self.polygon_shapes = []
        for i, s in zip(self.m.urban_info, self.m.urban):
        
            self.polygon_shapes.append(Polygon(np.array(s), True))
    
        self.ax.add_collection(
            PatchCollection(self.polygon_shapes, facecolor="#F3E600", 
                            edgecolor='None', alpha=0.75, 
                            linewidths=1, zorder=2))
        
        
    def highlight_countries(self, **kwargs):
        """
        -----------------------------------------------------------------------
        | Method for coloring / highlight the countries supplied in the list  |
        | "country_codes"                                                     |
        -----------------------------------------------------------------------
        |  OPTIONAL INPUT:                                                    |
        |                                                                     |
        |     show_eu (bool) : True or False for whether or not to highlight  |
        |                      EU countries on the map                        |
        |                                                                     |
        |     show_cis (bool) : True or False for whether or not to highlight |
        |                       Commonwealth of Inpendent States (CIS)        |
        |                       countries.                                    |
        |                                                                     |
        |     country_codes (list of str) : A list of strings, each with      |
        |                                   3 characters containing the       |
        |                                   country codes of the countries    |
        |                                   that you would like to highlight, | 
        |                                   for example:                      |
        |                                   ["DNK", "NOR", "SWE"]             |  
        |                                                                     |
        |     continents (str or list of str):                                |
        |                      Possible values are:                           |
        |                       'Europe', 'Asia', 'Africa',                   |
        |                       'Americas', 'Oceania', 'Antarctica'           |
        |                                                                     |
        |     region (str or list of str):                                    |
        |                      Possible values are:                           |
        |                        'Australia and New Zealand',                 |
        |                        'Caribbean',                                 |
        |                        'Central America',                           |
        |                        'Central Asia',                              |
        |                        'Eastern Africa',                            |
        |                        'Eastern Asia',                              |
        |                        'Eastern Europe',                            |
        |                        'Melanesia',                                 |  
        |                        'Micronesia',                                |
        |                        'Middle Africa',                             |
        |                        'Northern Africa',                           |
        |                        'Northern America',                          |
        |                        'Northern Europe',                           |
        |                        'Polynesia',                                 |
        |                        'South America',                             | 
        |                        'South-Eastern Asia',                        |
        |                        'Southern Africa',                           |
        |                        'Southern Asia',                             |
        |                        'Southern Europe',                           |
        |                        'Western Africa',                            |
        |                        'Western Asia',                              |
        |                        'Western Europe'                             |
        |                                                                     |
        -----------------------------------------------------------------------
        """
        
        self._load_country_shapefiles()
    
        country_codes = kwargs.get("country_codes", None)
        continent = kwargs.get("continent", None)
        region = kwargs.get("region", None)
        show_eu = kwargs.get("show_eu", False)
        show_cis = kwargs.get("show_cis", False)
        
        self.polygon_shapes = []
        
        if country_codes != None:
            for i, s in zip(self.m.countries_info, self.m.countries):
                if i['iso3'] in country_codes:
                    self.polygon_shapes.append(Polygon(np.array(s), True))
    
        if continent != None:
            for i, s in zip(self.m.countries_info, self.m.countries):
                if i['continent'] == continent:
                    self.polygon_shapes.append(Polygon(np.array(s), True))
    
        if region != None:
            for i, s in zip(self.m.countries_info, self.m.countries):
                if i['region'] in region:
                    self.polygon_shapes.append(Polygon(np.array(s), True))
    
        if show_eu:
            self._plot_eu()
        if show_cis:
            self._plot_cis()              
                    
        self.ax.add_collection(
            PatchCollection(self.polygon_shapes, facecolor=au.AUblue4, 
                            edgecolor='None', alpha=0.7, 
                            linewidths=1, zorder=1))


    def _load_country_centroids(self):
        
        with open('./data/country_centroids.json') as json_file:
            self._country_o = json.load(json_file)
 
        
 
# =============================================================================
#     def _i_make_piesss(self, n_pie):
#         x_y = n_centroids.loc[n_pie].values
#         x1, y1 = self.m(x_y[0], x_y[1])
#         axins = inset_axes(self.ax, width=0.5, height=0.5, bbox_to_anchor=(x1, y1), loc='center',
#                            bbox_transform=self.ax.transData, borderpad=0)
#         pie_scale=2
#         patches, texts = axins.pie(tech[n_pie], radius=(np.sqrt((data[n_pie]*pie_scale)/(np.pi*100))),
#                                                 colors=[color_cat.get(x, '#333333') for x in tech.index],
#                                                 wedgeprops={'alpha': 0.9} )
#         return patches, texts
#     
#     def add_node_pie_charts(self, n):
#     
#         for n_pie in n:
#             pie_slices, texts = self._i_make_piesss(n_pie)   
#  
# =============================================================================
    
 
    def add_country_network(self, country_links):
        """
        -----------------------------------------------------------------------
        | Method for drawing a network of countries onto the map plot         |
        -----------------------------------------------------------------------
        | INPUT:                                                              |
        |    country_links (list): List of country links as a list of tuples  |
        |                          containing iso3 codes, for example:        |
        |                          [("DEU", "FRA"), ("FRA", "ESP")]           |
        -----------------------------------------------------------------------
        """
        self._load_country_centroids()
        
   
        def flatten(l):
            return [item for sublist in l for item in sublist]
        
        nx_countries = list(set(flatten(country_links)))
        nx_country_centroids = [self._country_o[i] for i in nx_countries]
        print(nx_country_centroids)
        
        nx_ctry_o_x = [o[0] for o in nx_country_centroids]
        nx_ctry_o_y = [o[1] for o in nx_country_centroids]
        [MX, MY] = self.m(nx_ctry_o_x, nx_ctry_o_y)
        posm = dict(zip(nx_countries, list(map(list, zip(MX, MY)))))
        
 
        G = nx.DiGraph()
 
        [G.add_node(n) for n in nx_countries]
        
        nx.draw_networkx_nodes(G, posm, node_color=au.AUlightblue, 
                               node_size=200, alpha=1, ax=self.ax)
 
        for j in range(len(country_links)):
            G.add_edge(country_links[j][0], country_links[j][1], weight=2)
      
        weights = [G[u][v]['weight'] for u, v in G.edges()]
 
        nx.draw_networkx_edges(G, posm, edge_color=au.AUlightblue, 
                               width=weights, alpha=1.0, arrows=False,
                                ax=self.ax)
 
if __name__ == "__main__":

    

    
    mymap = MapPlot(place="Europe", style="light")
    
    country_links = [("DEU", "FRA"), 
                     ("FRA", "ESP"),
                     ("DEU", "DNK"),
                     ("DNK", "SWE"),
                     ("DNK", "NOR"),
                     ("DEU", "POL"),
                     ("NOR", "SWE"),
                     ("POL", "LTU"),
                     ("LTU", "LVA"),
                     ("LVA", "EST"),
                     ("EST", "FIN"),
                     ("SWE", "FIN"),
                     ("DEU", "CZE"),
                     ("POL", "CZE"),
                     ("DEU", "AUT"),
                     ("AUT", "CZE"),
                     ("ESP", "PRT"),
                     ("CZE", "SVK"),
                     ("HUN", "AUT"),
                     ("GBR", "IRL"),
                     ("FRA", "BEL"),
                     ("NLD", "BEL"),
                     ("NLD", "DEU"),
                     ("BEL", "DEU"),
                     ("LUX", "DEU"),
                     ("CHE", "DEU"),
                     ("CHE", "FRA"),
                     ("CHE", "AUT"),
                     ("CHE", "ITA"),
                     ("FRA", "ITA"),
                     ("AUT", "ITA"),
                     ("AUT", "SVN"),
                     ("HRV", "SVN"),
                     ("HRV", "SRB"),
                     ("GRC", "ITA"),
                     ("HUN", "ROU"),
                     ("HRV", "HUN"),
                     ("BGR", "ROU"),
                     ("SRB", "ROU"),
                     ("SRB", "BGR"),
                     ("BGR", "GRC"),
                     ("POL", "SVK"),
                     ("HUN", "SVK"),
                     ("HUN", "SRB"),
                     ("POL", "SWE"),
                     ("SWE", "LTU"),
                     ("FRA", "GBR")]   
    
    mymap.highlight_countries(show_eu=True)
    mymap.add_country_network(country_links)
  #  test = [[i]+[v] for i, v in country_links]
 #   test2 = list(set(flatten(country_links)))
    
    
  #  mymap.show_ports()
   # mymap.show_airports()
   # mymap.save("cyberpunk_ports")
    #mymap.highlight_countries(country_codes=["DNK", "NOR", "SWE"])
  #  mymap.highlight_countries(region=["Northern Europe"])       
  #  mymap.highlight_countries(show_eu=True, show_cis=True)       
     

#
  #  mymap2 = MapPlot(place="Europe", style="dark")
 #   mymap2.show_urban_areas()
    
  #  mymap3 = MapPlot(place="Denmark")
  #  mymap3.show_urban_areas()
    
    
 #   mymap2.show_DNK_urban_areas()
   # mymap2.highlight_countries(region=["Western Europe"])     
 #   mymap2.highlight_countries(show_eu=True)