import streamlit as st
import pandas as pd
import numpy as np
import matplotlib
import seaborn as sns

df=pd.read_csv('reddit_vm.csv')
tips=df.head(20)
st.table(tips)
st.header("Visualisation using Seaborn")
st.balloons()
sns.displot(tips['comms_num'])
st.pyplot()
sns.jointplot(x='comms_num',y='score',data=tips,kind='scatter')
st.pyplot()
