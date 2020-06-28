###############################################################################
#                         Import Python dependencies                          #
###############################################################################
import pandas as pd;

###############################################################################
#                 Convert the units of raw iPhone DataFrame                   #
###############################################################################

def convert_iPhone_units(df):
    """
    DESCERIPTION:
    This function accepts a pandas DataFrame called df at input.
    This dataframe is assumed to consist of a time-contiguous 
    multi-sensor iPhone array/tensor collected via the SensorLog
    app available in the iOS App Store. All accelerometer-derived
    signals report samples in gravitational units (1G = 9.81 m/s^2).
    This function converts acceleration units to SI units of m/s^2.
    Modifications are made in-place on input, df, before returning.
    
    INPUT & OUTPUT:
    :param df: a dataframe containing raw iPhone sensor data
    :type df: pandas.core.frame.DataFrame
    :returns: a modified copy of input df, with converted units
    :rtype: :type df: pandas.core.frame.DataFrame
    """
    
    # Data fields (column headers), converting acceleration
    # from gravitational units (G) to meters/second^2 (m/s^2)
    fields = [fd.replace('(G)','(m/s^2)') for fd in df];
    
    # Overwrite column names
    df.columns = fields;
    
    # Convert accelerations from G to m/s^2
    df[['accelerometerAccelerationX(m/s^2)',
       'accelerometerAccelerationY(m/s^2)',
       'accelerometerAccelerationZ(m/s^2)',
       'motionUserAccelerationX(m/s^2)',
       'motionUserAccelerationY(m/s^2)',
       'motionUserAccelerationZ(m/s^2)',
       'motionGravityX(m/s^2)',
       'motionGravityY(m/s^2)',
       'motionGravityZ(m/s^2)']] *= 9.81;
    
    # Return modified dataframe
    return df;

###############################################################################
#               Convert the units of raw appleWatch DataFrame                 #
###############################################################################

def convert_appleWatch_units(df):
    """
    DESCERIPTION:
    This function accepts a pandas DataFrame called df at input.
    This dataframe is assumed to consist of a time-contiguous 
    multi-sensor Apple Watch array/tensor collected via the SensorLog
    app available in the iOS App Store. All accelerometer-derived
    signals report samples in gravitational units (1G = 9.81 m/s^2).
    This function converts acceleration units to SI units of m/s^2.
    Modifications are made in-place on input, df, before returning.
    
    INPUT & OUTPUT:
    :param df: a dataframe containing raw iPhone sensor data
    :type df: pandas.core.frame.DataFrame
    :returns: a modified copy of input df, with converted units
    :rtype: :type df: pandas.core.frame.DataFrame
    """
    
    # Data fields (column headers), converting acceleration
    # from gravitational units (G) to meters/second^2 (m/s^2)
    fields = [fd.replace('(G)','(m/s^2)') for fd in df];
    
    # Overwrite column names
    df.columns = fields;
    
    # Convert accelerations from G to m/s^2
    df[['accelerometerAccelerationX(m/s^2)',
       'accelerometerAccelerationY(m/s^2)',
       'accelerometerAccelerationZ(m/s^2)',
       'motionUserAccelerationX(m/s^2)',
       'motionUserAccelerationY(m/s^2)',
       'motionUserAccelerationZ(m/s^2)',
       'motionGravityX(m/s^2)',
       'motionGravityY(m/s^2)',
       'motionGravityZ(m/s^2)']] *= 9.81;
    
    # Return modified dataframe
    return df;