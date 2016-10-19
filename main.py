import numpy as np
import pandas as pd
from pandas import DataFrame
import urllib2
import matplotlib.pyplot as plt
from collections import Counter
from bokeh.charts import Line, show, output_file
from bokeh.models import Legend, ColumnDataSource
from bokeh.layouts import widgetbox
from bokeh.models.widgets import Select
from bokeh.layouts import column
from bokeh.plotting import Figure
from bokeh.models.layouts import HBox, VBox
import bokeh.io
from bokeh.models import CustomJS



def remove_zeros(frame):
    for x in frame['SALE PRICE']:
        if x == 0:
            frame.drop(x)
    return frame

def hood_price(frame):
    hood_price = frame['SALE PRICE'].groupby(frame['NEIGHBORHOOD'])
    mean_hood_price = hood_price.mean() #remove zeros from mean calculation?
    return mean_hood_price

def mean_price(frame):
    #if x in frame['SALE PRICE'] == 0:
        #frame.drop(x)
    return frame['SALE PRICE'].mean()

def ppunit(frame):
        price = frame['SALE PRICE'].mean()
        ppu = price/frame['TOTAL UNITS']
        return ppu

def nsales(frame):
        return len(frame.index)

def percent_change(frame):
    for x in frame:
        pass



df2003= pd.read_excel('/Users/twitter/Desktop/Python projects/Sample Data/NYC_Real_Estate/Manhattan_Sales_Prices/sales_manhattan_03.xls', header=3)
MH2003 = DataFrame(df2003)


df2004 = pd.read_excel('/Users/twitter/Desktop/Python projects/Sample Data/NYC_Real_Estate/Manhattan_Sales_Prices/sales_manhattan_04.xls', header=3)
MH2004 = DataFrame(df2004)


df2005 = pd.read_excel('/Users/twitter/Desktop/Python projects/Sample Data/NYC_Real_Estate/Manhattan_Sales_Prices/sales_manhattan_05.xls', header=3)
MH2005 = DataFrame(df2005)


df2006 = pd.read_excel('/Users/twitter/Desktop/Python projects/Sample Data/NYC_Real_Estate/Manhattan_Sales_Prices/sales_manhattan_06.xls', header=3)
MH2006 = DataFrame(df2006)


df2007 = pd.read_excel('/Users/twitter/Desktop/Python projects/Sample Data/NYC_Real_Estate/Manhattan_Sales_Prices/sales_2007_manhattan.xls', header=3)
MH2007 = DataFrame(df2007)


df2008 = pd.read_excel('/Users/twitter/Desktop/Python projects/Sample Data/NYC_Real_Estate/Manhattan_Sales_Prices/sales_2008_manhattan.xls', header=3)
MH2008 = DataFrame(df2008)


df2009 = pd.read_excel('/Users/twitter/Desktop/Python projects/Sample Data/NYC_Real_Estate/Manhattan_Sales_Prices/2009_manhattan.xls', header=3)
MH2009 = DataFrame(df2009)


df2010 = pd.read_excel('/Users/twitter/Desktop/Python projects/Sample Data/NYC_Real_Estate/Manhattan_Sales_Prices/2010_manhattan.xls', header=3)
MH2010 = DataFrame(df2010)


df2011 = pd.read_excel('/Users/twitter/Desktop/Python projects/Sample Data/NYC_Real_Estate/Manhattan_Sales_Prices/2011_manhattan.xls', header=4)
MH2011 = DataFrame(df2011)


df2012 = pd.read_excel('/Users/twitter/Desktop/Python projects/Sample Data/NYC_Real_Estate/Manhattan_Sales_Prices/2012_manhattan.xls', header=4)
MH2012 = DataFrame(df2012) #headers end \n


df2013 = pd.read_excel('/Users/twitter/Desktop/Python projects/Sample Data/NYC_Real_Estate/Manhattan_Sales_Prices/2013_manhattan.xls', header=4)
MH2013 = DataFrame(df2013) #headers end \n
MH2013.columns = ['BOROUGH', 'NEIGHBORHOOD', 'BUILDING CLASS CATEGORY', 'TAX CLASS AT PRESENT', 'BLOCK', 'LOT', 'EASE-MENT', 'BUILDING CLASS AT PRESENT', 'ADDRESS', 'APARTMENT NUMBER', 'ZIP CODE', 'RESIDENTIAL UNITS', 'COMMERCIAL UNITS', 'TOTAL UNITS', 'LAND SQUARE FEET', 'GROSS SQUARE FEET', 'YEAR BUILT', 'TAX CLASS AT TIME OF SALE', 'BUILDING CLASS AT TIME OF SALE', 'SALE PRICE', 'SALE DATE']


df2014 = pd.read_excel('/Users/twitter/Desktop/Python projects/Sample Data/NYC_Real_Estate/Manhattan_Sales_Prices/2014_manhattan.xls', header=4)
MH2014 = DataFrame(df2014) #headers end \n
MH2014.columns = ['BOROUGH', 'NEIGHBORHOOD', 'BUILDING CLASS CATEGORY', 'TAX CLASS AT PRESENT', 'BLOCK', 'LOT', 'EASE-MENT', 'BUILDING CLASS AT PRESENT', 'ADDRESS', 'APARTMENT NUMBER', 'ZIP CODE', 'RESIDENTIAL UNITS', 'COMMERCIAL UNITS', 'TOTAL UNITS', 'LAND SQUARE FEET', 'GROSS SQUARE FEET', 'YEAR BUILT', 'TAX CLASS AT TIME OF SALE', 'BUILDING CLASS AT TIME OF SALE', 'SALE PRICE', 'SALE DATE']


df2015 = pd.read_excel('/Users/twitter/Desktop/Python projects/Sample Data/NYC_Real_Estate/Manhattan_Sales_Prices/2015_manhattan.xls', header=4)
MH2015 = DataFrame(df2015) #headers end \n
MH2015.columns = ['BOROUGH', 'NEIGHBORHOOD', 'BUILDING CLASS CATEGORY', 'TAX CLASS AT PRESENT', 'BLOCK', 'LOT', 'EASE-MENT', 'BUILDING CLASS AT PRESENT', 'ADDRESS', 'APARTMENT NUMBER', 'ZIP CODE', 'RESIDENTIAL UNITS', 'COMMERCIAL UNITS', 'TOTAL UNITS', 'LAND SQUARE FEET', 'GROSS SQUARE FEET', 'YEAR BUILT', 'TAX CLASS AT TIME OF SALE', 'BUILDING CLASS AT TIME OF SALE', 'SALE PRICE', 'SALE DATE']



total_sales = nsales(MH2003) + nsales(MH2004) + nsales(MH2005) + nsales(MH2006) + nsales(MH2007) + nsales(MH2008) + nsales(MH2009) + nsales(MH2010) + nsales(MH2011) + nsales(MH2012) + nsales(MH2013) + nsales(MH2014) + nsales(MH2015)
mean_annual_sales = total_sales/13

print "Total Sales:", total_sales
print "Mean Sales per year:", mean_annual_sales
#print "Mean price (2015): $", int( mean_price(MH2015))

manhattan = []
for x in [MH2003, MH2004, MH2005, MH2006, MH2007, MH2008, MH2009, MH2010, MH2011, MH2012, MH2013, MH2014, MH2015]:
    manhattan.append(mean_price(x))


frame = DataFrame(hood_price(MH2003))
frame.columns = ['2003']
frame['2004'], frame['2005'], frame['2006'], frame['2007'], frame['2008'], frame['2009'], frame['2010'], frame['2011'], frame['2012'], frame['2013'], frame['2014'], frame['2015'] = hood_price(MH2004), hood_price(MH2005), hood_price(MH2006), hood_price(MH2007), hood_price(MH2008), hood_price(MH2009), hood_price(MH2010), hood_price(MH2011), hood_price(MH2012), hood_price(MH2013), hood_price(MH2014), hood_price(MH2015)
frame = frame.T
frame = frame.rename(columns=lambda x: x.strip()) #strips white space from column names

#CustomJS
source = ColumnDataSource(data={'ALPHABET CITY':frame['ALPHABET CITY'], 'CHELSEA':frame['CHELSEA'], 'CHINATOWN':frame['CHINATOWN'], 'CIVIC CENTER':frame['CIVIC CENTER'], 'CLINTON':frame['CLINTON']})



code="""
        var data = source.get('data');
        var r = data[cb_obj.get('value')];
        var {var} = data[cb_obj.get('value')];
        //window.alert( "{var} " + cb_obj.get('value') + {var} );
        for (i = 0; i < r.length; i++) {{
                {var}[i] = r[i];
                data['{var}'][i] = r[i];
        }}
        source.trigger('change');
     """
#issue is with one of the two (or both) "y"'s 

callbacky = CustomJS(args=dict(source=source), code=code.format(var="y"))

plot = Figure(title=None)

plot.line(x=frame.index, y="CHELSEA", line_width=2, source=source)

#list boxes
yaxis_select = Select(title="Select Neighborhood:", value="CHELSEA", options=['ALPHABET CITY', 'CHELSEA', 'CHINATOWN', 'CIVIC CENTER', 'CLINTON'], callback=callbacky)

controls = VBox(yaxis_select)

layout = HBox(plot, controls, width=800)

bokeh.io.show(layout)


