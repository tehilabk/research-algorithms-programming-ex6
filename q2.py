import pandas as pd

# read the csv
df = pd.read_csv('national-budget.csv')

#returns the education budget per year
def education_budget(year:int)->int:
    data = df[df["שנה"] == year]
    data = data[data["הוצאה/הכנסה"] == "הוצאה"]
    data = data[data["שם תכנית"].str.contains("חינוך")]
    return data["הוצאה נטו"].sum()

# returns the security budget ratio per year
def security_budget_ratio(year:int)->float:
    csv_year = df[df["שנה"] == year]
    all_years = csv_year (year["הוצאה נטו"].sum()) & \
                      (csv_year[year["שם תחום"] == "בטחון"])
    security_budget = csv_year["הוצאה נטו"].sum()
    return security_budget / all_years

# returns the largest budget year per office
def largest_budget_year(office:str)->int:
    csv_office = df[df["שם סעיף"] == office]
    (max_year, max_budget) = (0, -1)
    for year in df["שנה"].unique():
        budget_per_year = csv_office[csv_office["שנה"] == year]["הוצאה נטו"].sum()
        if (budget_per_year > max_budget):
            (max_year, max_budget) = (year, budget_per_year)

    return max_year


