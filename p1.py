import pandas as pd


def add_series(series1, series2):
    return series1 + series2

def subtract_series(series1, series2):
    return series1 - series2


def multiply_series(series1, series2):
    return series1 * series2

def divide_series(series1, series2):
    return series1 / series2

series1 = pd.Series([10, 20, 30, 40])
series2 = pd.Series([5, 10, 15, 20])

print("Series 1:")
print(series1)
print("\nSeries 2:")
print(series2)

print("\nAddition:")
print(add_series(series1, series2))

print("\nSubtraction:")
print(subtract_series(series1, series2))

print("\nMultiplication:")
print(multiply_series(series1, series2))

print("\nDivision:")
print(divide_series(series1, series2))
