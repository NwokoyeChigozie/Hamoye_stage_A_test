# Codes for Hamnoye stage A test

import pandas as pd
url = "https://raw.githubusercontent.com/WalePhenomenon/climate_change/master/fuel_ferc1.csv"
fuel_ferc = pd.read_csv(url, error_bad_lines = False)
print(fuel_ferc)

A = [1, 2, 3, 4, 5, 6]
B = [13, 21, 34]

c = A.extend(B)
print(c)


value = fuel_ferc.groupby(['fuel_type_code_pudl']).mean()
print(value)


Print(fuel_ferc.describe(include = "all"))

stand = fuel_ferc.std(axis = 0, skipna = True)
print(round(stand,2))

skewn = fuel_ferc.skew(axis = 0, skipna = True)
print(round(skewn,2))


kurt = fuel_ferc.kurtosis(axis = 0, skipna = True)
print(round(kurt,2))

print(fuel_ferc.isnull().sum())
percent = (180/29522)*100
print(round(percent,3))

print(fuel_ferc.groupby(['report_year']).mean().sort_values(['fuel_cost_per_unit_delivered'], ascending=[False]))

print(fuel_ferc.corr(method ='pearson').sort_values(['fuel_cost_per_unit_burned'], ascending=[False]))

fuel_data.groupby('fuel_type_code_pudl')['fuel_type_code_pudl'].pct_change(fill_method ='ffill')
