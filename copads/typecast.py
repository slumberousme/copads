'''
Functions to type cast between different objects.

Date created: 20th July 2016

Licence: Python Software Foundation License version 2
'''

from dataframe import Series
from dataframe import Dataframe
from dataframe import MultiDataframe

def Series_Dataframe(source_object):
    '''
    Function to convert from dataframe.Series object to dataframe.Dataframe 
    object.
    
    @param source_object: object to be type casted / converted.
    @type source_object: dataframe.Series object
    @return: dataframe.Dataframe object
    '''
    return source_object.toDataframe()
    
def Dataframe_Series(source_object, series_name):
    '''
    Function to convert from dataframe.Dataframe object to dataframe.Series 
    object.
    
    @param source_object: object to be type casted / converted.
    @type source_object: dataframe.Series object
    @param series_name: name of series to extract
    @type series_name: string
    @return: dataframe.Series object
    '''
    return source_object.toSeries(series_name)
    
def Dataframe_MultiDataframe(source_object):
    '''
    Function to convert from dataframe.Dataframe object to 
    dataframe.MultiDataframe object.
    
    @param source_object: object to be type casted / converted.
    @type source_object: dataframe.Dataframe object
    @return: dataframe.MultiDataframe object
    '''
    mdf = MultiDataframe()
    mdf.addDataframe(source_object, False)
    return mdf
    