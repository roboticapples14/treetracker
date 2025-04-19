import scgt

def get_forest_cover(tif):
    '''
    Identifies forestcover from a GeoTiff of sattelite imagery at a certain resolution
    TODO: 
        1. Find sattelite dataset that is granular and regularly updated
        2. Define specs of input data based on dataset
        3. Find or develop model to ID forest-cover from data (preferabally generalizable to different datasets/granularities)

    Arguments:
        tif1 (GeoTiff): sattelite imagery Geotiff of a certain area

    Returns:
        Geotiff representing the forest-cover area identified from the input tiff,
        where 1 represents forest and 0 represents non-forest 
    '''
    pass