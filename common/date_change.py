import pandas as pd

def date_change(df):
    if 'time' in df :
        df['time'] = pd.to_datetime(df['time'])
    
    if 'mindate' in df :
        df['mindate'] = pd.to_datetime(df['mindate'])
    
    if 'week' in df :
        df['week'] = pd.to_datetime(df['week'])

    if 'Week' in df :
        df['Week'] = pd.to_datetime(df['Week'])
    
    if 'hour' in df :
        df['hour'] = pd.to_datetime(df['hour'])

    if 'date' in df :
        df['date'] = pd.to_datetime(df['date'])
    
    if 'Date' in df :
        df['Date'] = pd.to_datetime(df['Date'])

    if 'date_trunc' in df:
        df['date_trunc'] = pd.to_datetime(df['date_trunc'])
    
    if 'day' in df:
        df['day'] = pd.to_datetime(df['day'])
    
    if 'Day' in df:
        df['Day'] = pd.to_datetime(df['Day'])
    
    if 'minute' in df:
        df['minute'] = pd.to_datetime(df['minute'])
    
    if 'dt' in df:
        df['dt'] = pd.to_datetime(df['dt'])

    if 'times' in df :
        df['times'] = pd.to_datetime(df['times'])

    if 'evt_block_time' in df :
        df['evt_block_time'] = pd.to_datetime(df['evt_block_time'])            
    
    if 'month' in df :
        df['month'] = pd.to_datetime(df['month'])    

    if 'datex' in df :
        df['datex'] = pd.to_datetime(df['datex'])   
         
    if 'time_unit' in df :
        df['time_unit'] = pd.to_datetime(df['time_unit']) 
