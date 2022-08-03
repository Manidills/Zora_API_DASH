import sqlite3
from sqlite3 import Connection
import pandas as pd
import plost

from common.date_change import date_change



def connect(db_link):
    data = sqlite3.connect(db_link, check_same_thread=False)
    return data
    
def line_chart(data, table, x, y, title):
    query = f"SELECT * from {table}"
    df = pd.read_sql(query, con=data)

    date_change(df)

    plost.line_chart(
        df,
        x=x,
        y=y,width=500, height=400, title=title)

def line_chart_multi(data, table, x, y, project, title):
    query = f"SELECT * from {table}"
    df = pd.read_sql(query, con=data)

    date_change(df)
   
    plost.line_chart(
        df,
        x=x,
        y=y,
        color=project,
        width=500, height=400, title=title, legend='right')

def bar_chart(data, table, x, y, title):
    query = f"SELECT * from {table}"
    df = pd.read_sql(query, con=data)
    if 'exchange' in df:
        df = df[df['exchange'].notna()]
    plost.bar_chart(
    data=df,
    bar=x,
    value=y, direction='horizontal', title = title)

def pie_chart(data, table, x, y, title):
    query = f"SELECT * from {table}"
    df = pd.read_sql(query, con=data)
    if 'classification' in df:
        df = df[df['classification'].notna()]
    plost.pie_chart(
    data=df,
    theta=x,
    color=y, width=300, height=400, title=title)

def bar_chart_vertical(data, table, x, y, title):
    query = f"SELECT * from {table}"
    df = pd.read_sql(query, con=data)
    date_change(df)
    plost.bar_chart(
    data=df,
    bar=x,
    value=y, width=500, height=400,title = title)

def table(data, table):
    query = f"SELECT * from {table}"
    df = pd.read_sql(query, con=data)
    return df
    
