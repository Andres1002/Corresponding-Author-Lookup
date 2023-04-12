# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 21:27:06 2022

@author: Andres
"""
import plotly.graph_objects as go
import streamlit as st

def csvparser(files):
    dfs = list()
    df=pd.DataFrame()
    for file in files:
        st.write("filename:", file.name)
        df= pd.read_csv(file)
        df['file'] = os.path.splitext(file.name)[0]
        dfs.append(df)
    return dfs,df

def lineplotter(cnt,dfs):
    x=0;
    fig = go.Figure()
    while (x<cnt):
    
        fig.add_trace(go.Scatter(x=dfs[x]["Date"], y=dfs[x]["Close"],name=str(dfs[x].at[0,"file"])))       
        fig.update_layout(
            title="Stock Prices of Selected Stocks", xaxis_title="Date", yaxis_title="Close Price")
        x=x+1
    ## END while

    st.plotly_chart(fig, use_container_width=True)    

def barplotter(cnt,dfs):
    x=0;
    fig = go.Figure()
    while (x<cnt):
        fig.add_trace(go.Bar(x=dfs[x]["Date"], y=dfs[x]["Volume"],name=str(dfs[x].at[0,"file"])))    
        fig.update_layout(
            title="Volume of Selected Stocks", xaxis_title="Date", yaxis_title="Volume")
        x=x+1
    ## END while
    st.plotly_chart(fig, use_container_width=True)