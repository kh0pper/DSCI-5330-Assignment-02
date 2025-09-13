#!/usr/bin/env python3
"""
Generate tables for Ford Motor Company Executive Memorandum
"""

import pandas as pd
import numpy as np

# Load the financial data
df = pd.read_excel('Ford_10K_Financial_Ratios_2015_2024.xlsx')

# Calculate additional metrics
df['Operating Margin %'] = (df['Operating Income ($B)'] / df['Revenue ($B)']) * 100
df['Net Margin %'] = (df['Net Income ($B)'] / df['Revenue ($B)']) * 100
df['Gross Margin %'] = ((df['Revenue ($B)'] - df['COGS ($B)']) / df['Revenue ($B)']) * 100
df['Free Cash Flow ($B)'] = df['Cash Flow from Ops ($B)'] - df['Capex ($B)']
df['Current Ratio'] = df['Current Assets ($B)'] / df['Current Liabilities ($B)']
df['Debt to Equity'] = df['Total Debt ($B)'] / df['Shareholders Equity ($B)']
df['ROE %'] = (df['Net Income ($B)'] / df['Shareholders Equity ($B)']) * 100
df['ROA %'] = (df['Net Income ($B)'] / df['Total Assets ($B)']) * 100
df['Interest Coverage'] = df['EBIT ($B)'] / df['Interest Expense ($B)']

print("FORD MOTOR COMPANY - MEMO TABLES")
print("="*50)

# Table 1: Revenue & Profitability Summary
print("\nTABLE 1: REVENUE & PROFITABILITY TRENDS")
print("-"*60)
revenue_table = df[['Year Ended', 'Revenue ($B)', 'Gross Margin %', 'Operating Margin %', 
                    'Net Margin %', 'Net Income ($B)']].copy()
revenue_table['Revenue ($B)'] = revenue_table['Revenue ($B)'].round(1)
revenue_table['Gross Margin %'] = revenue_table['Gross Margin %'].round(1)
revenue_table['Operating Margin %'] = revenue_table['Operating Margin %'].round(1)
revenue_table['Net Margin %'] = revenue_table['Net Margin %'].round(1)
revenue_table['Net Income ($B)'] = revenue_table['Net Income ($B)'].round(1)

print(revenue_table.to_markdown(index=False, tablefmt="grid"))

# Table 2: Cash Flow Analysis
print("\n\nTABLE 2: CASH FLOW & CAPITAL EXPENDITURE ANALYSIS")
print("-"*60)
cashflow_table = df[['Year Ended', 'Cash Flow from Ops ($B)', 'Capex ($B)', 
                     'Free Cash Flow ($B)', 'Cash & Equivalents ($B)']].copy()
cashflow_table['Cash Flow from Ops ($B)'] = cashflow_table['Cash Flow from Ops ($B)'].round(1)
cashflow_table['Capex ($B)'] = cashflow_table['Capex ($B)'].round(1)
cashflow_table['Free Cash Flow ($B)'] = cashflow_table['Free Cash Flow ($B)'].round(1)
cashflow_table['Cash & Equivalents ($B)'] = cashflow_table['Cash & Equivalents ($B)'].round(1)

print(cashflow_table.to_markdown(index=False, tablefmt="grid"))

# Table 3: Balance Sheet Health
print("\n\nTABLE 3: BALANCE SHEET & DEBT STRUCTURE")
print("-"*60)
balance_sheet_table = df[['Year Ended', 'Total Assets ($B)', 'Total Debt ($B)', 
                         'Shareholders Equity ($B)', 'Debt to Equity']].copy()
balance_sheet_table['Total Assets ($B)'] = balance_sheet_table['Total Assets ($B)'].round(0)
balance_sheet_table['Total Debt ($B)'] = balance_sheet_table['Total Debt ($B)'].round(0)
balance_sheet_table['Shareholders Equity ($B)'] = balance_sheet_table['Shareholders Equity ($B)'].round(1)
balance_sheet_table['Debt to Equity'] = balance_sheet_table['Debt to Equity'].round(1)

print(balance_sheet_table.to_markdown(index=False, tablefmt="grid"))

# Table 4: Liquidity & Leverage Metrics
print("\n\nTABLE 4: LIQUIDITY & LEVERAGE RATIOS")
print("-"*60)
liquidity_table = df[['Year Ended', 'Current Ratio', 'Interest Coverage', 'ROE %', 'ROA %']].copy()
liquidity_table['Current Ratio'] = liquidity_table['Current Ratio'].round(2)
liquidity_table['Interest Coverage'] = liquidity_table['Interest Coverage'].round(1)
liquidity_table['ROE %'] = liquidity_table['ROE %'].round(1)
liquidity_table['ROA %'] = liquidity_table['ROA %'].round(1)

print(liquidity_table.to_markdown(index=False, tablefmt="grid"))

# Table 5: Investment NPV Analysis
print("\n\nTABLE 5: INVESTMENT ALTERNATIVES NPV ANALYSIS")
print("-"*60)

def calculate_pv_annuity(payment, rate, years):
    if rate == 0:
        return payment * years
    return payment * ((1 - (1 + rate)**(-years)) / rate)

rates = [0.05, 0.08, 0.10, 0.12, 0.15]
investment_data = []

for rate in rates:
    pv_a = calculate_pv_annuity(50, rate, 20)
    pv_b = calculate_pv_annuity(40, rate, 12)
    advantage = pv_a - pv_b
    
    investment_data.append({
        'Discount Rate': f"{rate*100:.0f}%",
        'Investment A NPV ($M)': f"{pv_a:.1f}",
        'Investment B NPV ($M)': f"{pv_b:.1f}",
        'NPV Advantage A ($M)': f"{advantage:.1f}"
    })

investment_table = pd.DataFrame(investment_data)
print(investment_table.to_markdown(index=False, tablefmt="grid"))

# Summary Statistics Table
print("\n\nTABLE 6: 10-YEAR FINANCIAL SUMMARY STATISTICS")
print("-"*60)
summary_metrics = {
    'Metric': [
        'Revenue ($B)',
        'Operating Margin (%)',
        'Net Margin (%)', 
        'Free Cash Flow ($B)',
        'ROE (%)',
        'Current Ratio',
        'Debt to Equity'
    ],
    'Minimum': [
        df['Revenue ($B)'].min(),
        df['Operating Margin %'].min(),
        df['Net Margin %'].min(),
        df['Free Cash Flow ($B)'].min(),
        df['ROE %'].min(),
        df['Current Ratio'].min(),
        df['Debt to Equity'].min()
    ],
    'Maximum': [
        df['Revenue ($B)'].max(),
        df['Operating Margin %'].max(),
        df['Net Margin %'].max(),
        df['Free Cash Flow ($B)'].max(),
        df['ROE %'].max(),
        df['Current Ratio'].max(),
        df['Debt to Equity'].max()
    ],
    'Average': [
        df['Revenue ($B)'].mean(),
        df['Operating Margin %'].mean(),
        df['Net Margin %'].mean(),
        df['Free Cash Flow ($B)'].mean(),
        df['ROE %'].mean(),
        df['Current Ratio'].mean(),
        df['Debt to Equity'].mean()
    ],
    'Latest (2024)': [
        df.iloc[-1]['Revenue ($B)'],
        df.iloc[-1]['Operating Margin %'],
        df.iloc[-1]['Net Margin %'],
        df.iloc[-1]['Free Cash Flow ($B)'],
        df.iloc[-1]['ROE %'],
        df.iloc[-1]['Current Ratio'],
        df.iloc[-1]['Debt to Equity']
    ]
}

summary_table = pd.DataFrame(summary_metrics)
# Round numeric columns
for col in ['Minimum', 'Maximum', 'Average', 'Latest (2024)']:
    summary_table[col] = summary_table[col].round(1)

print(summary_table.to_markdown(index=False, tablefmt="grid"))

print("\n" + "="*50)
print("Tables generated for executive memorandum")