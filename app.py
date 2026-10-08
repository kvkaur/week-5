import streamlit as st

from apputil import *

# Load Titanic dataset
df = pd.read_csv(
    'https://raw.githubusercontent.com/leontoddjohnson/datasets/main/data/titanic.csv'
)

st.write(
'''
# Titanic Visualization 1
How did survival rates differ by sex across passenger classes and age groups?
'''
)

# Generate and display the figure
fig1 = visualize_demographic()
st.plotly_chart(fig1, use_container_width=True)

st.write(
'''
# Titanic Visualization 2
How does average ticket fare change with family size across passenger classes?
'''
)

st.write(
    "The last-name counts are related to family size, but they do not match "
    "exactly because passengers with the same last name are not always in the "
    "same immediate family group."
)

# Generate and display the figure
fig2 = visualize_families()
st.plotly_chart(fig2, use_container_width=True)

# Bonus question is optional, so it is not included.