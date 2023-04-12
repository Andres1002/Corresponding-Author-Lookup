import streamlit as st
import sys
import plotly.graph_objects as go
import pandas as pd
import os
import plotly.express as px
# Initial Variables

def csvparser(files):
    dfs = list()
    df=pd.DataFrame()
    for file in files:
        st.write("filename:", file.name)
        df= pd.read_csv(file)
        df['file'] = os.path.splitext(file.name)[0]
        dfs.append(df)
    return dfs,df

def barplotter(df):
    fig = go.Figure()
    fig.add_trace(go.Bar(x=dfmaster["Department/Major"], y=df["counts"]))    
    fig.update_layout(
    title="Department/Major", xaxis_title="Date", yaxis_title="Volume")
    st.plotly_chart(fig, use_container_width=True)
    
sys.path.append(r'C:\Users\Andres\Documents\GitHub\test\Functions')
df2=pd.DataFrame()

st.title("Corresponding Author Lookup")


uploaded_files = st.file_uploader("Choose a CSV file", type={"csv", "txt"}, accept_multiple_files=True)
for uploaded_file in uploaded_files:
    st.write("filename:", uploaded_file.name)
    
    if uploaded_file.name =="MasterList.csv":
        dfmaster= pd.read_csv(uploaded_file)
        df2g=dfmaster["StudentOrFaculty"].value_counts().rename_axis('StudentOrFaculty').reset_index(name='counts')
        
        st.header("Corresponding Authors by Classification")
        fig=px.pie(df2g,values="counts", names="StudentOrFaculty")
        fig.update_traces(textposition='inside')
        fig.update_layout(
        height=800,
        width=850,
        uniformtext_minsize=7, uniformtext_mode='hide',
        legend=dict(font=dict(size=12)),
        margin=dict(l=0,r=0,b=0,t=0,pad=0))
        st.plotly_chart(fig, use_container_width=False)
        
        df3g=dfmaster["College"].value_counts().rename_axis('College').reset_index(name='counts')
        st.header("Corresponding Authors by College")
        fig=px.pie(df3g,values="counts", names="College")
        fig.update_traces(textposition='inside')
        fig.update_layout(
        height=800,
        width=850,
        uniformtext_minsize=7, uniformtext_mode='hide',
        legend=dict(font=dict(size=12)),
        margin=dict(l=0,r=0,b=0,t=0,pad=0))
        st.plotly_chart(fig, use_container_width=False)
        
        st.header("Corresponding Authors by Department")
        dfg=dfmaster["Department/Major"].value_counts().rename_axis('Department/Major').reset_index(name='counts')
        barplotter(dfg)

    ######### Department ###########3

    #Try a dummy csv or an if statment before this

        fig=px.pie(dfg,values="counts", names="Department/Major")
        fig.update_traces(textposition='inside')
        fig.update_layout(
        height=800,
        width=850,
        uniformtext_minsize=7, uniformtext_mode='hide',
        legend=dict(font=dict(size=12)),
        margin=dict(l=0,r=0,b=0,t=0,pad=0))
        st.plotly_chart(fig, use_container_width=False)
    ################ End plot ############



        
        df4g=dfmaster["Title/Classification"].value_counts().rename_axis('Title/Classification').reset_index(name='counts')
        st.header("Corresponding Authors by Title")
        fig=px.pie(df4g,values="counts", names="Title/Classification")
        fig.update_traces(textposition='inside')
        fig.update_layout(
        height=800,
        width=850,
        uniformtext_minsize=7, uniformtext_mode='hide',
        legend=dict(font=dict(size=12)),
        margin=dict(l=0,r=0,b=0,t=0,pad=0))
        st.plotly_chart(fig, use_container_width=False)
        
        
        df5g=dfmaster["Dataset"].value_counts().rename_axis('Dataset').reset_index(name='counts')
        st.header("Where The Data is Coming From")
        fig=px.pie(df5g,values="counts", names="Dataset")
        fig.update_traces(textposition='inside')
        fig.update_layout(
        height=800,
        width=850,
        uniformtext_minsize=7, uniformtext_mode='hide',
        legend=dict(font=dict(size=12)),
        margin=dict(l=0,r=0,b=0,t=0,pad=0))
        st.plotly_chart(fig, use_container_width=False)
        
    if uploaded_file.name =="Non Applicables.csv":
        df5= pd.read_csv(uploaded_file)
        st.header("Deeper look into NAs")
        fig=px.pie(df5,values="0", names="Non Applicable")
        fig.update_traces(textposition='inside')
        fig.update_layout(
        height=800,
        width=850,
        uniformtext_minsize=7, uniformtext_mode='hide',
        legend=dict(font=dict(size=12)),
        margin=dict(l=0,r=0,b=0,t=0,pad=0))
        st.plotly_chart(fig, use_container_width=False)

    if uploaded_file.name =="Dual Funded Departments.csv":
        df6= pd.read_csv(uploaded_file)
        st.header("Dual Funded Departments")
        fig=px.pie(df6,values="0", names="Dual Funded")
        fig.update_traces(textposition='inside')
        fig.update_layout(
        height=800,
        width=850,
        uniformtext_minsize=7, uniformtext_mode='hide',
        legend=dict(font=dict(size=12)),
        margin=dict(l=0,r=0,b=0,t=0,pad=0))
        st.plotly_chart(fig, use_container_width=False)
        