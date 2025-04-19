from scgt import GeoTiff, Tile
from forest_identification import get_forest_cover

def get_logged_area(tif1: GeoTiff, tif2: GeoTiff):
    '''
    Returns a GeoTiff representing the area logged between tif1 and tif2
    Logging is calculated as the delta loss of tree-cover

    TODO: define specs of input data
    tif1 (GeoTiff): baseline sattelite imagery of a certain area
    tif2 (GeoTiff): sattelite imagery of a certain area after suspected logging
    '''
    forest_cover_1_tif = get_forest_cover(tif1)
    forest_cover_2_tif = get_forest_cover(tif2)
    delta_forest_cover_tif = tif1.clone_shape()

    forest_cover_1_tile = forest_cover_1_tif.get_all_as_tile().m
    forest_cover_2_tile = forest_cover_2_tif.get_all_as_tile().m

    delta_forest_cover_mat = forest_cover_1_tile.m - forest_cover_2_tile.m
    delta_forest_cover_tile = forest_cover_1_tile.clone_shape()
    delta_forest_cover_tile.m = delta_forest_cover_mat
    delta_forest_cover_tif.set_tile(delta_forest_cover_tile)

    return delta_forest_cover_tif

