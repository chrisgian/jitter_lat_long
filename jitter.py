import numpy as np
# calcualte length of degree
def lod(deg, kind):
    length_at_equator = 110.5742727
    if kind == 'lon':
        out = np.cos(deg * (2 * np.pi) / 360) * length_at_equator
    elif kind == 'lat':
        out = length_at_equator
    return out
        
def jitter(lon, lat, km):
    lon_km_per_degree = lod(lat,'lon')
    lon_degree_per_km = 1/lon_km_per_degree
    lon_rand = np.random.uniform(-1,1,1)
    lon_j = lon + lon_rand*lon_degree_per_km*km
    
    lat_km_per_degree = lod(lat,'lat')
    lat_degree_per_km = 1/lat_km_per_degree
    lat_rand = np.random.uniform(-1,1,1)
    lat_j = lat + lat_rand*(lat_degree_per_km)*km
    
    return [lat_j[0],lon_j[0]]



jitter(
        lat = 45.512794, 
        lon = -122.679565, 
        km = 1)