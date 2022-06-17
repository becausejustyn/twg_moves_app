
import streamlit as st
import pandas as pd

df = pd.read_csv('moves_table.csv')

#'Move Name': 
#'Minimum Damage': int, sortable
#'Maximum Damage': int, sortable
#'Attack Bonus': int, sortable
#'Wounding Bonus': int, sortable
#'Required Position': 
#'Obtained Position':
#'Forced Position': 
#'1st Ability': making this filterable as 1st OR 2nd
#'2nd Ability': making this filterable as 1st OR 2nd
#'Total Abilities': int, sortable

required = df['Required Position'].drop_duplicates() 
obtained = df['Obtained Position'].drop_duplicates()
forced = df['Forced Position'].drop_duplicates()
abilities = df['1st Ability'].drop_duplicates()

with st.sidebar:
    required_choice = st.sidebar.multiselect(
    'Required Position:', required, default = required)
    obtained_choice = st.sidebar.multiselect(
    'Obtained Position:', obtained, default = obtained)
    forced_choice = st.sidebar.multiselect(
    'Forced Position:', forced, default = forced)
    abilities_choice = st.sidebar.multiselect(
    'Choose Abilities:', abilities, default = abilities)
    min_slider = st.slider('Min Damage', 0, 20, 0)
    max_slider = st.slider('Max Damage', 0, 66, 0)
    ab_slider = st.slider('Min AB', 1, 30, 0)
    bb_slider = st.slider('Min Bleed', 0, 25, 0)
    total_abilities_slider = st.slider('Total Abilities', 0, 86, 0)
    
user_values = [required_choice, obtained_choice, forced_choice, abilities_choice, min_slider, max_slider, ab_slider, bb_slider, total_abilities_slider]

def table_values(df, user_values):
    
    df = (df[
        df['Minimum Damage'] > user_values['min_slider'] &
        df['Maximum Damage'] < user_values['max_slider'] &
        df['Attack Bonus'] > user_values['ab_slider'] &
        df['Wounding Bonus'] > user_values['bb_slider'] &
        df['Required Position'].isin([user_values['required']]) & 
        df['Obtained Position'].isin([user_values['obtained']]) & 
        df['Forced Position'].isin([user_values['forced']]) & 
        df['1st Ability'].isin([user_values['abilities_choice']]) | df['2nd Ability'].isin([user_values['abilities_choice']]) &
        df['Total Abilities'] == user_values['total_abilities_slider']
        ])

    return(df)

st.dataframe(df)

