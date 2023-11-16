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

    def get_map(self, var, **kwargs):
        """Get a map for a particular variable and time."""

        """
            Arguments:
            var = variable name (string)
           
            Keyword arguments:
            month = month (integer)            
            year = year (integer)

            Notes:
            year is not specified for 'climatology' variable
            year and month are not specified for 'linear_trend' and 'time_lat' variables

            Returns:
            map of variable (a numpy array)
            date of map (a datetime.date object)
            list of satellites used (list)

            Behavior:
            If no valid data are available, returns None.
        """

        year = kwargs.get('year')
        month = kwargs.get('month')
       print('Get map for year = ' + str(year) + ', month = ' + str(month))

        self.long_name = getattr(self.dataset.variables[var], 'long_name')
        print('Get map of ' + self.long_name)
            
        self._extract_one_map(var, year=year, month=month)        
        self._find_satellites_used()

        print('Satellites used:', self.satellites)
        print()
        
        return self.one_map, self.map_date, self.satellites

    def plot_map(self, var, **kwargs):
        """Plot a map for a particular variable and time."""

        """
            Arguments:
            var = variable name (string)
           
            Keyword arguments:
            month = month (integer)            
            year = year (integer)

            Notes:
            year is not specified for 'climatology' variable
            year and month are not specified for 'linear_trend' and 'time_lat' variables
            defaults for optional keyword arguments are set in _set_plot()

            Optional keyword arguments:
            baddatacolor = color used for no/bad data (default = 'black')
            colorbar_orientation = colorbar orientation (default = 'horizontal')
            colormap = matplotlib colormap name ('jet' unless 'anomaly' in var then 'BrBG')
            facecolor = background color for plot (default = 'white')                        
            lattickspacing = latitude tick-spacing (default = 30 deg)
            lonshift = shift map by this amount in longitude in degrees (default = 30 deg)                        
            lontickspacing = longitude tick-spacing (default = 30 deg)           
            maxval = maximum data value for colorbar (default = valid_max)            
            minval = minimum data value for colorbar (default = valid_min)
            titlefontsize = font size for plot title (default = medium)
            yeartickspacing = year tick-spacing (default = 5 years)            
            
            Returns:
            an image to the screen
        """

        one_map, map_date, satellites = self.get_map(var, **kwargs)
        if one_map == None: return
        
        self._set_plot(var, **kwargs)
        fig = plt.figure(facecolor=self.facecolor)

        year = kwargs.get('year')
        month = kwargs.get('month')
        title = self.long_name
        if month: title = title + ' for ' + month_name[month]
        if year : title = title + ' ' + str(year)       
        plt.title(title, fontsize=self.titlefontsize)

        palette = cm.get_cmap(self.cmap)

        palette.set_bad(self.baddatacolor)        
        no_data = np.where(one_map == self.fillvalue)
        one_map[no_data] = np.nan

        palette.set_under(self.icecolor)        
        ice = np.where(one_map == self.icevalue)
        one_map[ice] = -1e30
        
        coords = getattr(self.dataset.variables[var],'coordinates')
        if 'longitude' in coords:
            one_map = np.roll(one_map, -1*self.lonshift*self.lonperdeg, axis=1)
        else:
            one_map = np.transpose(one_map)
        
        one_map = np.flipud(one_map)            
        aximg = plt.imshow(one_map, cmap=self.cmap, vmin=self.vmin, vmax=self.vmax)
        
        cbar = fig.colorbar(aximg, orientation=self.cbar_orientation)           
        cbar.set_label(self.units)

        plt.yticks(self.yloc,self.ylab)
        plt.xticks(self.xloc,self.xlab)                            
        
        filename = kwargs.get('filename')
        if filename: fig.savefig(filename)

        plt.show()
        plt.close()

    def print_anomaly_timeseries(self, var):
        """Print time series for a variable."""
        """
            Arguments:
            var = variable name (string)

            Returns:
            prints the time series
        """
        
        print(var)
        for imonth, month in enumerate(self.dates['time']):
            print(month.strftime('%b %Y'), self.dataset.variables[var][imonth])

    def print_linear_trend(self, var):
        """Print linear trend in a variable."""
        """
            Arguments:
            var = variable name (string)

            Returns:
            prints the trend for variable
        """
        
        print (getattr(self.dataset.variables[var], 'long_name'))
        attr = 'linear_trend'
        print (attr + ' in ' + var + ' =', getattr(self.dataset.variables[var], attr))

    # The functions that follow support the get_map() and plot_map() methods.

    # Functions for setting the plot appearance:

    def _set_plot(self, var, **kwargs):
        """Set the look of the plot."""

        self.lonshift = kwargs.get('lonshift')
        if not self.lonshift: self.lonshift = 30

        self.lattickspacing = kwargs.get('lattickspacing')
        if not self.lattickspacing: self.lattickspacing = 30

        self.lontickspacing = kwargs.get('lontickspacing')
        if not self.lontickspacing: self.lontickspacing = 30

        self.yeartickspacing = kwargs.get('yeartickspacing')
        if not self.yeartickspacing: self.yeartickspacing = 5

        self.dlat = getattr(self.dataset,'geospatial_lat_resolution')            
        self.dlon = getattr(self.dataset,'geospatial_lon_resolution')
        self.latperdeg = int(1/self.dlat)            
        self.lonperdeg = int(1/self.dlon)
        
        self._set_axes(var, **kwargs)

        self.fillvalue = getattr(self.dataset.variables[var],'_FillValue')
        self.units = getattr(self.dataset.variables[var],'units')

        try: self.icevalue = getattr(self.dataset.variables[var],'IceValue')
        except AttributeError: self.icevalue = None
        self.icecolor = 'white'

        self.vmin = kwargs.get('minval')
        if not self.vmin: self.vmin = getattr(self.dataset.variables[var], 'valid_min')

        self.vmax = kwargs.get('maxval')
        if not self.vmax: self.vmax = getattr(self.dataset.variables[var], 'valid_max')
      
        self.cmap = kwargs.get('colormap')
        if not self.cmap:
            if 'anomaly' in var: self.cmap = 'BrBG'
            else: self.cmap = 'jet'

        self.cbar_orientation = kwargs.get('colorbar_orientation')
        if not self.cbar_orientation: self.cbar_orientation = 'horizontal'

        self.facecolor = kwargs.get('facecolor')
        if not self.facecolor: self.facecolor = 'white'       

        self.baddatacolor = kwargs.get('baddatacolor')
        if not self.baddatacolor: self.baddatacolor = 'black'

        self.titlefontsize = kwargs.get('titlefontsize')
        if not self.titlefontsize: self.titlefontsize = 'medium'
        
    def _set_axes(self, var, **kwargs):
        """Set axes for plot."""
        
        tsy = self.lattickspacing
        tsx = self.lontickspacing
        ls = self.lonshift
        dj = self.latperdeg
        di = self.lonperdeg

        self.yloc, self.ylab = zip(*[ [dj*tsy*j, str(-1*(tsy*j-90))]
                                      for j in range(180/tsy +1) ])

        coords = getattr(self.dataset.variables[var],'coordinates')
        if 'longitude' in coords:
            self.xloc, self.xlab = zip(*[ [di*tsx*i, str(tsx*i+ls) if tsx*i+ls<360 else str(tsx*i+ls-360)]
                                          for i in range(360/tsx +1) ])
        else:
            y1, m1, d1 = self._parse_date(getattr(self.dataset,'time_coverage_start'), prefix='')
            y2, m2, d2 = self._parse_date(getattr(self.dataset,'time_coverage_end'), prefix='')            
            year_list = [y1+y for y in range(y2-y1+1)]
            indx_list = [(y-y1)*12 for y in year_list]
            self.xloc, self.xlab = zip(*[ [indx, item] for item, indx in zip(year_list,indx_list)
                                          if item%self.yeartickspacing == 0 ])

    # Function for getting the data:

    def _extract_one_map(self, var, **kwargs):
        """Extract one map for a particular variable and time."""

        year = kwargs.get('year')        
        month = kwargs.get('month')

        self.one_map = None
        self.map_date = None
        
        if np.ndim(self.dataset.variables[var]) == 2:
            self.one_map = np.array(self.dataset.variables[var][:,:])
            return

        if getattr(self.dataset,'time_coverage_resolution') != 'P1M':
            print('ReadNetcdf expects monthly average time resolution')

        self.timevar = getattr(self.dataset.variables[var],'coordinates').split()[0]
        if 'time' not in self.timevar: print('ReadNetcdf could not find time coordinate')

        yearin = year
        if not year: year = self.basedate[self.timevar].year
        
        mindate = date(year,month,1)
        maxdate = mindate + timedelta(days=monthrange(year,month)[1])

        datecheck = [True if d >= mindate and d < maxdate else False for d in self.dates[self.timevar][:]]

        try: indx = datecheck.index(True)
        except ValueError:
            print 'No map available this date' 
            return
        
        self.one_map = np.array(self.dataset.variables[var][indx,:,:])
        self.map_date = self.dates[self.timevar][indx]

        if not yearin: self.map_date = None

    # Functions for finding satellites:

    def _get_platforms(self, *args, **kwargs):
        """Get platform names from satellites_used comment."""

        self.satellite_index_list = []
        self.satellite_name_list = []

        var = kwargs.get('var')
        if not var: var = 'satellites_used'
        self.satellitesused_variablename = var
        
        attr = kwargs.get('attr')
        if not attr: attr = 'comment'

        prefix = kwargs.get('prefix')
        if prefix == None: prefix = 'index list '
        
        comment = getattr(self.dataset.variables[var], attr)
        
        m = re.search(prefix+'(.+)$', comment)
        if m == None: print 'ReadNetcdf expected to find platform index list in comment.'
        
        satlist = m.group(1).split(',')
        for sat in satlist:
            s = sat.split('==')
            print s
            try:
                self.satellite_index_list.append(int(s[0]))
                self.satellite_name_list.append(str(s[1]))
            except ValueError:
                continue

    def _find_satellites_used(self, *args, **kwargs):
        """ Find satellites used."""

        self.satellites = None
        if self.one_map == None: return

        self.satellites = self.satellite_name_list        
        if self.map_date == None: return            
       
        try:
            indx = self.dates[self.timevar].index(self.map_date)
            satused = list(self.dataset.variables[self.satellitesused_variablename][indx])
            satname = self.satellite_name_list
            self.satellites = [item for item, flag in zip(satname,satused) if flag==1]
        except ValueError:
            self.satellites = None
        
        return

    # Functions for date handling:

    def _create_date_objects(self, *args, **kwargs):
        """Create datetime date objects."""
        
        self.dates = {}

        try: varlist = args[0]
        except IndexError: varlist = ['time', 'climatology_time']

        for var in varlist:
            self._get_base_date(var, **kwargs)
            self._convert_days_to_dates(var)            

    def _get_base_date(self, var, **kwargs):
        """Get the base date (the date in 'days since ...')."""

        self.basedate = {}
        
        datestring = self.dataset.variables[var].units
        yy, mm, dd = self._parse_date(datestring, **kwargs)        
        
        self.basedate[var] = date(yy,mm,dd)

    def _parse_date(self, datestring, **kwargs):
        """Parse a date string."""

        prefix = kwargs.get('prefix')
        if prefix == None: prefix = 'days since '

        m = re.search(prefix+'(\d+)-(\d+)-(\d+).*', datestring)
        if m == None: print ('ReadNetcdf expects time units of the form: days since y-m-d ...')

        return int(m.group(1)),int(m.group(2)),int(m.group(3))
        
    def _convert_days_to_dates(self, var):
        """Convert days since base date to datetime.date."""

        self.dates[var] = []
        
        for days in self.dataset.variables[var]:
            self.dates[var].append(self.basedate[var] + timedelta(days=int(days)))

    # Function for printing information:

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
