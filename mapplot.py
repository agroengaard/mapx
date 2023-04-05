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
import matplotlib.patches as mpatches
import matplotlib.font_manager as fm
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
        
        self.title = kwargs.get("title", None)
        
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
        
        if self.title != None:
          # self.ax.set_title(self.title, #fontproperties=au.AUb, 
          #                    fontsize=18, color=au.AUblue)
        
            self.ax.text(.5,.95,self.title,
                             horizontalalignment='center',
                             fontsize=18, 
                             fontproperties=au.AUb,
                             color=self.theme[self.style]["title_color"],
                             transform=self.ax.transAxes) 
        
        plt.tight_layout()
        
        
    def save(self, **kwargs):
        """
        -----------------------------------------------------------------------
        | Method for saving the plot                                          |
        -----------------------------------------------------------------------
        | OPTIONAL INPUT:                                                     |
        |     filename (str): Name of the output file, fx "myplot"            |
        |     output_folder (str): Path to the output folder, fx: "C:\\fld\\" |
        |_____________________________________________________________________|
        """
        self.filename = kwargs.get("filename", "myplot")
        self.output_folder = kwargs.get("output_folder", "./saved_plots/")
        self.output_path = os.path.join(self.output_folder, 
                                        self.filename+".png")
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
                            'figsize': (12,12),
                            'width': 1400000,
                            'height': 1400000,
                            'lat_0': 56,
                            'lon_0':6,
                            'lat_ts': 45,
                            'projection': 'laea'
                            }
              
        elif self.place == "Sweden":
            self.mapmode = {'definition': 'center_and_height_width',
                            'figsize': (12,12),
                            'width': 1500000,
                            'height': 1500000,
                            'lat_0': 57,
                            'lon_0':15,
                            'lat_ts': 45,
                            'projection': 'laea'
                            }
            
        elif self.place == "Denmark":
            self.mapmode = {'definition': 'center_and_height_width',
                            'figsize': (12,12),
                            'width': 400000,
                            'height': 400000,
                            'lat_0': 56,
                            'lon_0':11,
                            'lat_ts': 45,
                            'projection': 'laea',
                            'resolution': 'i'
                            }
        
        elif self.place == "South America":
            self.mapmode = {'definition': 'center_and_height_width',
                            'figsize': (12,12),
                            'width': 8000000,
                            'height': 9000000,
                            'lat_0': -19,
                            'lon_0':-62,
                            'lat_ts': -19,
                            'projection': 'laea',
                            'resolution': 'i'
                            }
                    
        elif self.place == "North America":
            self.mapmode = {'definition': 'center_and_height_width',
                            'figsize': (12,12),
                            'width': 8000000,
                            'height': 9000000,
                            'lat_0': 45,
                            'lon_0':-102,
                            'lat_ts': 45,
                            'projection': 'laea',
                            'resolution': 'i'
                            }
        elif self.place == "Africa":
            self.mapmode = {'definition': 'center_and_height_width',
                            'figsize': (12,12),
                            'width': 9000000,
                            'height':9000000,
                            'lat_0': 2,
                            'lon_0':17,
                            'lat_ts': 2,
                            'projection': 'laea',
                            'resolution': 'i'
                            }
        elif self.place == "Middle East":
            self.mapmode = {'definition': 'center_and_height_width',
                            'figsize': (12,12),
                            'width':  4000000,
                            'height': 4000000,
                            'lat_0': 26,
                            'lon_0':45,
                            'lat_ts': 26,
                            'projection': 'laea',
                            'resolution': 'l'
                            }
        elif self.place == "Asia":
            self.mapmode = {'definition': 'center_and_height_width',
                            'figsize': (12,12),
                            'width':  9000000,
                            'height': 9000000,
                            'lat_0': 45,
                            'lon_0':90,
                            'lat_ts': 45,
                            'projection': 'laea',
                            'resolution': 'l'
                            }
        elif self.place == "Eurasia":
            self.mapmode = {'definition': 'center_and_height_width',
                            'figsize': (12,12),
                            'width':  11000000,
                            'height': 11000000,
                            'lat_0': 55,
                            'lon_0':70,
                            'lat_ts': 55,
                            'projection': 'laea',
                            'resolution': 'l'
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
                    'ocean': 'w',
                    'node_colour':au.AUblue2,
                    'node_font_colour': au.AUblue,
                    'highlight_country': au.AUblue4,
                    'highlight_country_edge':'None',
                    'pie_colormap':plt.cm.viridis,
                    'title_color':au.AUblue,
                    'legend_facecolor': au.AUmapgrey,
                    'legend_edgecolor':au.AUmapgrey,
                    'legend_fontcolor': 'black'
                    },
                'dark':{
                    'continents': au.AUverydarkgrey,
                    'borders': au.AUverydarkgrey,
                    'ocean': au.AUdarkgrey,
                    'node_colour':au.AUblue2,
                    'node_font_colour': au.AUblue,
                    'highlight_country': '#08304A',
                    'highlight_country_edge':'#1688A1',
                    'pie_colormap':plt.cm.cividis,
                    'title_color':au.AUblue4,
                    'legend_facecolor': au.AUdarkgrey,
                    'legend_edgecolor':au.AUmapgrey,
                    'legend_fontcolor': 'white'
                    },
                'cyberpunk':{
                    'continents':'#212946',
                    'borders': '#3a487c',
                    'ocean':'#2A3459',
                    'node_colour':au.AUblue3,
                    'node_font_colour': au.AUblue4,
                    'highlight_country': '#08304A',
                    'highlight_country_edge':'#1688A1',
                    'pie_colormap':plt.cm.cool,
                    'title_color':au.AUblue4,
                    'legend_facecolor': "#0A3645",
                    'legend_edgecolor': "#136D8A",
                    'legend_fontcolor': au.AUblue4
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
            PatchCollection(self.polygon_shapes, 
                            facecolor=self.theme[self.style]["highlight_country"], 
                            edgecolor=self.theme[self.style]["highlight_country_edge"],
                            alpha=0.7, 
                            linewidths=1, zorder=1))


    def _load_country_centroids(self):
        
        with open('./data/country_centroids.json') as json_file:
            self._country_o = json.load(json_file)
 
        
 

 
   # class Network:
# =============================================================================
#     def country_trade(country, df, countries_col, value_col):
#         """
#         -------------------------------------------------------------------
#         | Method for drawing a network of directed links with values      |
#         -------------------------------------------------------------------
#         | INPUT:                                                          |
#         |    country: For example "GBR"                                   |
#         |    df: dataframe with alpha3 value country codes in one column  |
#         |    countries_col: Name of the column with the alpha3 country    |
#         |                   codes.                                        |
#         |    value_col: Name of the column that contains the link values, |
#         |               and thus determine the displayed width of the     |
#         |               links                                             |
#         |_________________________________________________________________|
#         """
# =============================================================================
         
            
    def add_country_network(self, **kwargs):
        """
        -----------------------------------------------------------------------
        | Method for drawing a network of countries onto the map plot         |
        |                                                                     |
        | Method 1: Supply a list of tuples with alpha3 code countries to     |
        |           create a simple country network plot.                     |
        -----------------------------------------------------------------------
        | OPTINAL INPUT:                                                      |
        |    country_links (list): List of country links as a list of tuples  |
        |                          containing iso3 codes, for example:        |
        |                          [("DEU", "FRA"), ("FRA", "ESP")]           |
        |    df : Dataframe                                                   |
        |    link_values (list): List of link values. Should have the         |
        -----------------------------------------------------------------------
        """
        self._load_country_centroids()
        
   
        def flatten(l):
            return [item for sublist in l for item in sublist]
        
        
        self.country_links = kwargs.get("country_links", None)
        self.df = kwargs.get("dataframe", None)
        country = kwargs.get("country", None)
        value_col = kwargs.get("value_col", None)
        link_values = kwargs.get("link_values", None)
        directed = kwargs.get("directed", False)
        scale = kwargs.get("scale", 1)
        color_countries = kwargs.get("color_countries", True)
        
 
        if self.df is not None:
            if "from" in self.df.columns and "to" in self.df.columns:
                self.country_links = list(zip(self.df["from"] , self.df["to"]))
            elif "Country" in self.df.columns:            
                self.country_links = [(country, itm) for itm in self.df["Country"].values]
            elif all([len(col) == 3 for col in self.df.columns]) and country != None:
                self.country_links = [(country, itm) for itm in self.df.columns]
              
        if self.country_links != None:                                              
            nx_countries = list(set(flatten(self.country_links)))
        
        if color_countries:
            self.highlight_countries(country_codes=nx_countries)
    
   
        self.nx_country_centroids = [self._country_o[i] for i in nx_countries]
  
        
        nx_ctry_o_x = [o[0] for o in self.nx_country_centroids]
        nx_ctry_o_y = [o[1] for o in self.nx_country_centroids]
        [MX, MY] = self.m(nx_ctry_o_x, nx_ctry_o_y)
        posm = dict(zip(nx_countries, list(map(list, zip(MX, MY)))))
        
        # ------------------------ Draw the network ---------------------------
        G = nx.DiGraph()
 
        [G.add_node(n) for n in nx_countries]
        
        nx.draw_networkx_nodes(G, posm, node_color=self.theme[self.style]["node_colour"], 
                               node_size=260, alpha=0.5, ax=self.ax )
        
        nx.draw_networkx_labels(G, posm, font_size=9, 
                                font_color=self.theme[self.style]["node_font_colour"])
        
        def add_simple_edges(self):
            for j in range(len(self.country_links)):
                    G.add_edge(self.country_links[j][0], 
                               self.country_links[j][1], 
                               weight=2 * scale)
        
        def add_edges_with_widths(self):
            for j in range(len(self.country_links)):
                link_value = self.df[value_col][j]
                if link_value > 0:
                    G.add_edge(self.country_links[j][0], self.country_links[j][1], 
                               weight=abs(link_value) * scale)
                else:
                    G.add_edge(self.country_links[j][1], self.country_links[j][0], 
                               weight=abs(link_value) * scale)               
      
        
        add_simple_edges(self)
        
        weights = [G[u][v]['weight'] for u, v in G.edges()]
 
        nx.draw_networkx_edges(G, posm, edge_color=au.AUlightblue, 
                               width=weights, alpha=0.5, 
                               arrows=directed,
                               connectionstyle="arc3,rad=0.1",
                               ax=self.ax)
 
    
    # =========================================================================
    #      Pie Chart code
    # =========================================================================

    def _add_country_pie(self, n_pie, **kwargs):
        """
        -----------------------------------------------------------------------
        | Method for adding a pie chart in the center of a country            |
        -----------------------------------------------------------------------
        """
        
        self.pie_origo = self._country_o[n_pie]
        
        
        x1, y1 = self.m(self.pie_origo[0], self.pie_origo[1])
        axins = inset_axes(self.ax, width=0.5, height=0.5, 
                           bbox_to_anchor=(x1, y1), loc='center',
                           bbox_transform=self.ax.transData, borderpad=0)
        pie_scale=1
        
        
        pie_cmap = kwargs.get("pie_cmap", self.theme[self.style]["pie_colormap"])
        
        pie_colors = [*pie_cmap(np.linspace(0, 1, self.pie_df[n_pie].shape[0]))]
        
        patches, texts = axins.pie(self.pie_df[n_pie], 
                                 radius=pie_scale,
                                 colors=pie_colors,
                                 wedgeprops={'alpha': 1.0} )
        return patches, texts
    
    def add_pie_charts(self, **kwargs):
        """
        -----------------------------------------------------------------------
        | Method for adding pie charts on each country node based on a        |
        | dataframe.                                                          |
        -----------------------------------------------------------------------
        | POSSIBLE INPUT:                                                     |
        |     dataframe : the pandas dataframe to plot piechart data for.     |
        |                 Must have the the folloing structure;               |
        |                      - country alpha-3 codes as columns             |
        |                      - data categories as indices                   |
        |     legend (bool): True or False for whether or not to plot a       |  
        |                    legend.                                          |
        |     pie_cmap : Pie plot color map to use for the coloring.          |
        |_____________________________________________________________________|
        """
        self._load_country_centroids()
        
        self.pie_df = kwargs.get("dataframe", None)
        self._legend = kwargs.get("legend", True)   
        self.pie_cmap = kwargs.get("pie_cmap", self.theme[self.style]["pie_colormap"])
        
        if self.pie_df is not None:
            if all([len(col) == 3 for col in self.pie_df.columns]):
                self.pie_countries = self.pie_df.columns    
                
            for n_pie in self.pie_countries:
                pie_slices, texts = self._add_country_pie(n_pie, 
                                                          pie_cmap=self.pie_cmap)   
                
            if self._legend == True:
                self.legend_font = fm.FontProperties(family='AU Passata', 
                                                     weight="regular", 
                                                     size=12)
                pie_legend = self.ax.legend(pie_slices, self.pie_df.index, 
                                            facecolor=self.theme[self.style]["legend_facecolor"], 
                                            edgecolor=self.theme[self.style]["legend_edgecolor"],
                                            labelcolor=self.theme[self.style]["legend_fontcolor"],
                                            framealpha=1,
                                            prop=self.legend_font
                                 #      bbox_to_anchor=(0.00, -0.15), 
                               #        loc="upper left",# ncol=6, 
                                      
                                       )                        
                self.ax.add_artist(pie_legend)

        else:
            print("no dataframe supplied")
    
    # =========================================================================
    #  Bar chart code
    # =========================================================================
    
    def _add_country_bar(self, country, **kwargs):
        """
        -----------------------------------------------------------------------
        |  Method for adding a single bar plot to a single country            | 
        -----------------------------------------------------------------------
        """
        width = kwargs.get("width", 1)
        self.pie_origo = self._country_o[country]
        x1, y1 = self.m(self.pie_origo[0], self.pie_origo[1])
   
        ax_h = inset_axes(self.ax, width=width, height= 1, loc='lower center',
                          bbox_to_anchor=(x1, y1),
                          bbox_transform=self.ax.transData, borderpad=0, 
                          axes_kwargs={'alpha': 0.35, 'visible': True})
        
        bar_cmap = kwargs.get("pie_cmap", self.theme[self.style]["pie_colormap"])
        
        bar_colors = [*bar_cmap(np.linspace(0, 1, self.bar_df[country].shape[0]))]
        
        for i in range(len(self.bar_df.index)):
       
            ax_h.bar(self.bar_df.index[i], 
                     self.bar_df[country].values[i], 
                     label=self.bar_df.index[i],
                     fc=bar_colors[i]
                     )
       # ax_h.set_ylim([0, 85])
        ax_h.axis('off')
        return ax_h
    
    
    def add_bar_plots(self, **kwargs):
        """
        -----------------------------------------------------------------------
        | Method for adding bar plots from a dataframe onto individual        |
        | countries.                                                          |
        -----------------------------------------------------------------------
        """
        self._load_country_centroids()
        
        self.bar_df = kwargs.get("dataframe", None)
        self._legend = kwargs.get("legend", True)   
        self.bar_cmap = kwargs.get("pie_cmap", 
                                   self.theme[self.style]["pie_colormap"])
        width = kwargs.get("width", 1)
        
        if self.bar_df is not None:
            if all([len(col) == 3 for col in self.bar_df.columns]):
                self.pie_countries = self.bar_df.columns    
                
            for n_pie in self.pie_countries:
                ax_h = self._add_country_bar(n_pie, 
                                             bar_cmap=self.bar_cmap, 
                                             width=width)   
        bar_cmap = kwargs.get("pie_cmap", self.theme[self.style]["pie_colormap"])
        
        if self._legend == True:
            bar_colors = [*bar_cmap(np.linspace(0, 1, len(self.bar_df.index)))]
            patches = [mpatches.Patch(color=bar_colors[i], label=self.bar_df.index[i]) for i in range(len(self.bar_df.index))]
            self.legend_font = fm.FontProperties(family='AU Passata', 
                                                 weight="regular", 
                                                 size=12)
            self.ax.legend(handles=patches, loc=1,
                           facecolor=self.theme[self.style]["legend_facecolor"], 
                           edgecolor=self.theme[self.style]["legend_edgecolor"],
                           labelcolor=self.theme[self.style]["legend_fontcolor"],
                           framealpha=1,
                           prop=self.legend_font
                           
                           )
        
    
    
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