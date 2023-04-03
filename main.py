 
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

mydict = {"DEU": {"Metal": 3, "Death Metal":4, "Black Metal":2, "Folk Metal":1},
          "POL": {"Metal": 2, "Death Metal":1, "Black Metal":1, "Folk Metal":3},
          "DNK": {"Metal": 5, "Death Metal":3, "Black Metal":2, "Folk Metal":1},
          "NOR": {"Metal": 1, "Death Metal":4, "Black Metal":9, "Folk Metal":3},
          "GBR": {"Metal": 1, "Death Metal":4, "Black Metal":9, "Folk Metal":3},
          "UKR": {"Metal": 1, "Death Metal":4, "Black Metal":9, "Folk Metal":3},
          "ISL": {"Metal": 1, "Death Metal":4, "Black Metal":4, "Folk Metal":8}
          }

df = pd.DataFrame.from_dict(mydict)
mymap = MapPlot(place="Europe", style="dark", title="Finnish Metal Music Export")
mymap.add_country_network(country="FIN", dataframe=df, directed=True)
mymap.add_pie_charts(dataframe=df)
#mymap.save()