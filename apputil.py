import plotly.express as px
import pandas as pd

# update/add code below ...
df = pd.read_csv("train.csv")
# Rename columns to lowercase-underscore format
df.columns = (
    df.columns
    .str.replace(r"(?<!^)(?=[A-Z])", "_", regex=True)
    .str.replace(" ", "_")
    .str.lower()
)
# Exercise 1: Survival Demographics

def survival_demographics():
    data = df.copy()

    data["age_group"] = pd.cut(
        data["age"],
        bins=[0, 12, 19, 59, float("inf")],
        labels=["Child", "Teen", "Adult", "Senior"],
        include_lowest=True
    )

    grouped = data.groupby(
        ["pclass", "sex", "age_group"],
        observed=False

    )
    summary = grouped.agg(
    n_passengers=("passenger_id", "count"),
    n_survivors=("survived", "sum"),
    survival_rate=("survived", "mean")
).reset_index()
    
    summary = summary.sort_values(
    ["pclass", "sex", "age_group"]
).reset_index(drop=True)
    return summary

def visualize_demographic():
    data = survival_demographics()

    fig = px.bar(
        data,
        x="pclass",
        y="survival_rate",
        color="sex",

        facet_col="age_group",
        barmode="group",
        labels={
            "pclass": "Passenger Class",
            "survival_rate": "Survival Rate",
            "sex": "Sex",
            "age_group": "Age Group"
        },
        title="Titanic Survival Rates by Class, Sex, and Age Group"
    )

    return fig

# Exercise 2 
def family_groups():
    data = df.copy()
    data["family_size"] = data["sib_sp"] + data["parch"] + 1

    grouped = data.groupby(
       ["pclass", "family_size"],
    )

    summary = grouped.agg(
    n_passengers=("passenger_id", "count"),
    avg_fare=("fare", "mean"),
    min_fare=("fare", "min"),
    max_fare=("fare", "max")
).reset_index()
    
    summary = summary.sort_values(
    ["pclass", "family_size"]
).reset_index(drop=True)
    return summary

def last_names():
    last_name = df["name"].str.split(",").str[0]

    return last_name.value_counts()

def visualize_families():
    data = family_groups()

    fig = px.bar(
        data,
        x="family_size",
        y="avg_fare",
        color="pclass",
        labels={
            "family_size": "Family Size",
            "avg_fare": "Average Fare",
            "pclass": "Passenger Class"
        },
        title="Average Ticket Fare by Family Size and Passenger Class"
    )

    return fig
