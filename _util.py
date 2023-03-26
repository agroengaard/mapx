 
import geopandas as gpd
from shapely import wkt
import json


def _calculate_country_centroids():
    shapefile = gpd.read_file("./shapefiles/boundaries/world-administrative-boundaries.shp")
    
    result = {}
    for i in range(shapefile.shape[0]):
        iso3 = shapefile["iso3"].iloc[i]
        polygon = shapefile["geometry"].iloc[i]
        centroid = polygon.centroid
        result[iso3] = (centroid.x, centroid.y)
        
    with open('./data/country_centroids.json', 'w') as fp:
        json.dump(result, fp, indent=4)    
        
_calculate_country_centroids()
    
 