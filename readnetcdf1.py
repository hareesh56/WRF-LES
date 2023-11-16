import re
from datetime import date, timedelta
from calendar import monthrange
from calendar import month_name

import numpy as np
from netCDF4 import Dataset
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib.colors as color

class ReadNetcdf:
    """ReadNetcdf provides methods to get and plot a map from the RSS microwave data set in netCDF."""

    def __init__(self, *args, **kwargs):
        """Read the dataset."""
        self.filename = args[0]
        self.dataset = Dataset(self.filename)
        print('Dataset read successfully')
        print('Dataset format: ', self.dataset.file_format)
        print()

        self._print_dataset_info(**kwargs)
        self._create_date_objects()
        self._get_platforms()

    def close(self):
        """ Close the dataset. """
        self.dataset.close()

    # ... (rest of the class remains unchanged)

    def _print_dataset_info(self, **kwargs):
        """ Print a list of important dataset and provenance information."""
        if kwargs.get('summary'):
            print('Dataset summary:')
            print(self.dataset)
            print('Variables in dataset:')
            for var in self.dataset.variables:
                print(var, self.dataset.variables[var])

        attrib_list = ['title', 'institution', 'project', 'creator_url', 'creator_email', 'acknowledgement']
        for attrib in attrib_list:
            if hasattr(self.dataset, attrib):
                print(attrib.title() + ': ' + getattr(self.dataset, attrib))
            else:
                print('Cannot find: ' + attrib.title())
        print()
