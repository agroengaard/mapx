 
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



# =============================================================================
# 
# from mapplot import MapPlot
# import pandas as pd
# 
# mydict = {"BRA": {"Metal": 3, "Death Metal":4, "Black Metal":2, "Folk Metal":1},
#           "COL": {"Metal": 2, "Death Metal":1, "Black Metal":1, "Folk Metal":3},
#           "PER": {"Metal": 5, "Death Metal":3, "Black Metal":2, "Folk Metal":1},
#           "ARG": {"Metal": 1, "Death Metal":4, "Black Metal":9, "Folk Metal":3},
#           "VEN": {"Metal": 1, "Death Metal":4, "Black Metal":9, "Folk Metal":3}
#           }
# 
# df = pd.DataFrame.from_dict(mydict)
# mymap = MapPlot(place="South America", style="dark", title="Coffee Production")
# mymap.highlight_countries(country_codes=list(df.columns))    
# mymap.add_bar_plots(dataframe=df, width=0.25)
# #mymap.save()
# =============================================================================

mymap2 = MapPlot(place="North America", style="light", title="Coffee Production")