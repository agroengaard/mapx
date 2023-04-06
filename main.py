 
from mapplot import MapPlot
#from country_codes import CountryCodes

#mymap.show_urban_areas()
#mymap.save("urban")
#mymap.show_ports()

#mymap.show_airports()

#mymap.highlight_countries(show_eu=True, show_cis=True)    


import pandas as pd

  
# =============================================================================
# df_list = pd.read_html("https://en.wikipedia.org/wiki/List_of_the_largest_trading_partners_of_United_Kingdom")
# df = df_list[1]
# df = df[df["Rank"] != "-"]
# CountryCodes.to_alpha3(df, "Country")
# df.reset_index(inplace=True)
# 
#  
# mymap = MapPlot(place="World", style="light")
# mymap.add_country_network(country="GBR", dataframe=df, value_col="Trade balance", scale=0.0005, directed=True)
# 
# 
# =============================================================================




from mapplot import MapPlot
import pandas as pd

mydict = {"BRA": {"Coffee": 3, "Cocoa":4, "Beef":2, "Rubber":1},
          "COL": {"Coffee": 2, "Cocoa":1, "Beef":1, "Rubber":3},
          "PER": {"Coffee": 5, "Cocoa":3, "Beef":2, "Rubber":1},
          "ARG": {"Coffee": 1, "Cocoa":4, "Beef":9, "Rubber":3},
          "VEN": {"Coffee": 1, "Cocoa":4, "Beef":9, "Rubber":3}
          }

df = pd.DataFrame.from_dict(mydict)

# =============================================================================
# # Example 1:
# barplot = MapPlot(place="South America", style="light", title="South America Exports")
# barplot.highlight_countries(country_codes=list(df.columns))    
# barplot.add_bar_plots(dataframe=df, width=0.25)
# barplot.save(filename="bar_example")
# 
# # Example 2:
# barplot = MapPlot(place="South America", style="light", title="South America Exports")
# barplot.highlight_countries(country_codes=list(df.columns))    
# barplot.add_pie_charts(dataframe=df)
# barplot.save(filename="pie_example")
# 
# =============================================================================
# Example 3:
    
barplot = MapPlot(place="South America", style="light", title="South America Exports")
barplot.highlight_countries(country_codes=list(df.columns))    
barplot.add_circle_plots(dataframe=df, scale=300, linewidth=2)
#barplot.save(filename="pie_example")



