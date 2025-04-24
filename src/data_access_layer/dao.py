import earthaccess

class dao:
    def __init__(self):
        self.earth_access_authenticate()

    def earth_access_authenticate(self):
        earthaccess.login(strategy="netrc")

    def get_earth_access_dataset(dataset_shortname, count=1, version=None, doi=None, daac=None, 
                                        provider=None, temporal_range=None, bounding_box=None):
        '''
        Gets NASA Earth science data, based on the dataset name and specified geographic and temporal constraints.
            Search for datasets in the catalog: https://search.earthdata.nasa.gov/search
        Arguments:
            short_name: dataset short name, e.g. ATL08
            count: Number of records to get, -1 = all
            version: dataset version
            doi: DOI for a dataset
            daac: e.g. NSIDC or PODAAC
            provider: particular to each DAAC, e.g. POCLOUD, LPDAAC etc.
            temporal: a tuple representing temporal bounds in the form (date_from, date_to)
            bounding_box: a tuple representing spatial bounds in the form (lower_left_lon, lower_left_lat, upper_right_lon, upper_right_lat)

        Returns:
            a list of DataGranules that can be used to access the granule files by using download() or open().
        Ex call:
            results = earthaccess.search_data(
                short_name='ATL06',
                bounding_box=(-10, 20, 10, 50),
                temporal=("1999-02", "2019-03"),
                count=10
            )
        '''
        return earthaccess.search_data(
            short_name=dataset_shortname,
            count=count,
            version=version,
            doi=doi,
            daac=daac,
            provider=provider,
            bounding_box=bounding_box,
            temporal=temporal_range,
        )

    def download_earth_access_dataset(data_granules, file_dir="./"):
        '''
        Download the earthaccess dataset to the given file directory
        '''
        files = earthaccess.download(data_granules, file_dir)
        return files
