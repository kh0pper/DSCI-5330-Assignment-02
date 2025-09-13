#!/usr/bin/env python3
"""
Ford Motor Company - Separate Visualizations
Creating individual, clear charts per outline requirements
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set style
plt.style.use('default')
sns.set_palette("husl")

# Load the financial data
df = pd.read_excel('Ford_10K_Financial_Ratios_2015_2024.xlsx')

# Calculate additional metrics
df['Operating Margin %'] = (df['Operating Income ($B)'] / df['Revenue ($B)']) * 100
df['Net Margin %'] = (df['Net Income ($B)'] / df['Revenue ($B)']) * 100
df['Free Cash Flow ($B)'] = df['Cash Flow from Ops ($B)'] - df['Capex ($B)']
df['Current Ratio'] = df['Current Assets ($B)'] / df['Current Liabilities ($B)']
df['Debt to Equity'] = df['Total Debt ($B)'] / df['Shareholders Equity ($B)']

print("Creating separate visualizations...")

# Visual 1: Topline & Margin Trends (dual-axis)
fig1, ax1 = plt.subplots(figsize=(12, 7))
ax1_twin = ax1.twinx()

line1 = ax1.plot(df['Year Ended'], df['Revenue ($B)'], 'b-', marker='o', linewidth=3, 
                 markersize=10, label='Revenue ($B)')
line2 = ax1_twin.plot(df['Year Ended'], df['Operating Margin %'], 'r--', marker='s', 
                      linewidth=2.5, markersize=8, label='Operating Margin %')
line3 = ax1_twin.plot(df['Year Ended'], df['Net Margin %'], 'g--', marker='^', 
                      linewidth=2.5, markersize=8, label='Net Margin %')

ax1.set_xlabel('Year', fontsize=12, fontweight='bold')
ax1.set_ylabel('Revenue ($B)', color='b', fontsize=12, fontweight='bold')
ax1_twin.set_ylabel('Margin (%)', color='r', fontsize=12, fontweight='bold')
ax1.set_title('Ford Motor Company: Revenue & Margin Trends (2015-2024)', 
              fontsize=14, fontweight='bold', pad=20)

# Combine legends
lines = line1 + line2 + line3
labels = [l.get_label() for l in lines]
ax1.legend(lines, labels, loc='upper left', fontsize=11, frameon=True, shadow=True)

ax1.grid(True, alpha=0.3)
ax1.set_xticks(df['Year Ended'])
ax1.set_xticklabels(df['Year Ended'], rotation=45)

# Add annotations for key points
ax1.annotate('Pandemic Impact', xy=(2020, 127.14), xytext=(2020, 115),
             arrowprops=dict(arrowstyle='->', color='red', lw=1.5),
             fontsize=10, ha='center', color='red')
ax1.annotate('Record High', xy=(2024, 184.99), xytext=(2024, 195),
             arrowprops=dict(arrowstyle='->', color='green', lw=1.5),
             fontsize=10, ha='center', color='green')

plt.tight_layout()
plt.savefig('visual_1_revenue_margins.png', dpi=300, bbox_inches='tight')
plt.close()

# Visual 2: Cash Generation (CFO, Capex, FCF)
fig2, ax2 = plt.subplots(figsize=(14, 7))
width = 0.25
x = np.arange(len(df['Year Ended']))

bars1 = ax2.bar(x - width, df['Cash Flow from Ops ($B)'], width, label='Operating Cash Flow', 
                alpha=0.9, color='green', edgecolor='darkgreen', linewidth=1.5)
bars2 = ax2.bar(x, df['Capex ($B)'], width, label='Capital Expenditure', 
                alpha=0.9, color='red', edgecolor='darkred', linewidth=1.5)
bars3 = ax2.bar(x + width, df['Free Cash Flow ($B)'], width, label='Free Cash Flow', 
                alpha=0.9, color='blue', edgecolor='darkblue', linewidth=1.5)

ax2.set_xlabel('Year', fontsize=12, fontweight='bold')
ax2.set_ylabel('Cash Flow ($B)', fontsize=12, fontweight='bold')
ax2.set_title('Ford Motor Company: Cash Generation Analysis (2015-2024)', 
              fontsize=14, fontweight='bold', pad=20)
ax2.set_xticks(x)
ax2.set_xticklabels(df['Year Ended'], rotation=45)
ax2.legend(fontsize=11, loc='upper right', frameon=True, shadow=True)
ax2.grid(True, alpha=0.3, axis='y')
ax2.axhline(y=0, color='black', linestyle='-', alpha=0.5, linewidth=1)

# Add value labels on bars
for bars in [bars1, bars2, bars3]:
    for bar in bars:
        height = bar.get_height()
        if abs(height) > 1:  # Only label significant values
            ax2.text(bar.get_x() + bar.get_width()/2., height + (0.5 if height > 0 else -1),
                    f'${height:.1f}', ha='center', va='bottom' if height > 0 else 'top', 
                    fontsize=8)

plt.tight_layout()
plt.savefig('visual_2_cash_generation.png', dpi=300, bbox_inches='tight')
plt.close()

# Visual 3: Leverage & Liquidity
fig3, ax3 = plt.subplots(figsize=(12, 7))
ax3_twin = ax3.twinx()

# Bar chart for debt and cash
width = 0.4
x = np.arange(len(df['Year Ended']))
bars1 = ax3.bar(x - width/2, df['Total Debt ($B)'], width, alpha=0.7, 
                color='darkred', label='Total Debt ($B)', edgecolor='black', linewidth=1)
bars2 = ax3.bar(x + width/2, df['Cash & Equivalents ($B)'], width, alpha=0.7, 
                color='green', label='Cash & Equivalents ($B)', edgecolor='black', linewidth=1)

# Line for current ratio on secondary axis
line = ax3_twin.plot(df['Year Ended'], df['Current Ratio'], 'b-', marker='o', 
                     linewidth=3, markersize=10, label='Current Ratio', zorder=5)

# Formatting
ax3.set_xlabel('Year', fontsize=13, fontweight='bold')
ax3.set_ylabel('Billions ($)', fontsize=13, fontweight='bold')
ax3_twin.set_ylabel('Current Ratio', color='b', fontsize=13, fontweight='bold')
ax3.set_title('Ford Motor Company: Leverage & Liquidity Analysis (2015-2024)', 
              fontsize=15, fontweight='bold', pad=25)
ax3.set_xticks(x)
ax3.set_xticklabels(df['Year Ended'], rotation=45, fontsize=11)

# Position legends to avoid overlap
ax3.legend(loc='upper left', fontsize=11, frameon=True, shadow=True, bbox_to_anchor=(0.02, 0.98))
ax3_twin.legend(loc='upper right', fontsize=11, frameon=True, shadow=True, bbox_to_anchor=(0.98, 0.98))

# Add grid
ax3.grid(True, alpha=0.3, axis='y')
ax3_twin.grid(False)

# Add horizontal reference line for current ratio
ax3_twin.axhline(y=1.0, color='red', linestyle='--', alpha=0.5, linewidth=1)
ax3_twin.text(2015.5, 1.02, 'Minimum Threshold (1.0)', fontsize=9, color='red')

# Set y-axis limits to provide more space
ax3.set_ylim(0, max(df['Total Debt ($B)'].max(), df['Cash & Equivalents ($B)'].max()) * 1.15)
ax3_twin.set_ylim(0.9, 1.35)

plt.tight_layout()
plt.savefig('visual_3_leverage_liquidity.png', dpi=300, bbox_inches='tight')
plt.close()

# Visual 4: Operating vs Net Income
fig4, ax4 = plt.subplots(figsize=(12, 7))
width = 0.4
x = np.arange(len(df['Year Ended']))

bars1 = ax4.bar(x - width/2, df['Operating Income ($B)'], width, 
                label='Operating Income', alpha=0.85, color='steelblue', 
                edgecolor='darkblue', linewidth=1.5)
bars2 = ax4.bar(x + width/2, df['Net Income ($B)'], width, 
                label='Net Income', alpha=0.85, color='darkgreen', 
                edgecolor='black', linewidth=1.5)

ax4.set_xlabel('Year', fontsize=12, fontweight='bold')
ax4.set_ylabel('Income ($B)', fontsize=12, fontweight='bold')
ax4.set_title('Ford Motor Company: Operating vs Net Income (2015-2024)', 
              fontsize=14, fontweight='bold', pad=20)
ax4.set_xticks(x)
ax4.set_xticklabels(df['Year Ended'], rotation=45)
ax4.legend(fontsize=11, loc='upper left', frameon=True, shadow=True)
ax4.grid(True, alpha=0.3, axis='y')
ax4.axhline(y=0, color='red', linestyle='--', alpha=0.5, linewidth=1.5)

# Add value labels for significant values
for bars in [bars1, bars2]:
    for bar in bars:
        height = bar.get_height()
        if abs(height) > 2:  # Only label significant values
            ax4.text(bar.get_x() + bar.get_width()/2., height + (0.5 if height > 0 else -0.8),
                    f'${height:.1f}B', ha='center', va='bottom' if height > 0 else 'top', 
                    fontsize=9)

# Annotate the 2021 outlier
ax4.annotate('2021 Special Items\n(Rivian, Pension)', 
             xy=(2021, 17.91), xytext=(2021, 21),
             arrowprops=dict(arrowstyle='->', color='orange', lw=2),
             fontsize=10, ha='center', color='orange',
             bbox=dict(boxstyle="round,pad=0.3", facecolor="yellow", alpha=0.3))

plt.tight_layout()
plt.savefig('visual_4_income_comparison.png', dpi=300, bbox_inches='tight')
plt.close()

# Visual 5: Investment NPV Comparison
fig5, ax5 = plt.subplots(figsize=(14, 8))

def calculate_pv_annuity(payment, rate, years):
    if rate == 0:
        return payment * years
    return payment * ((1 - (1 + rate)**(-years)) / rate)

discount_rates = np.arange(0.01, 0.20, 0.001)
pv_a_values = [calculate_pv_annuity(50, r, 20) for r in discount_rates]
pv_b_values = [calculate_pv_annuity(40, r, 12) for r in discount_rates]

ax5.plot(discount_rates * 100, pv_a_values, 'b-', linewidth=3, 
         label='Investment A ($50M × 20 years)', alpha=0.9)
ax5.plot(discount_rates * 100, pv_b_values, 'r-', linewidth=3, 
         label='Investment B ($40M × 12 years)', alpha=0.9)

ax5.set_xlabel('Discount Rate (%)', fontsize=12, fontweight='bold')
ax5.set_ylabel('Present Value ($M)', fontsize=12, fontweight='bold')
ax5.set_title('Investment NPV Comparison Across Discount Rates', 
              fontsize=14, fontweight='bold', pad=20)
ax5.legend(fontsize=12, loc='upper right', frameon=True, shadow=True)
ax5.grid(True, alpha=0.3)

# Mark and label specific points
for rate in [5, 10, 15]:
    pv_a = calculate_pv_annuity(50, rate/100, 20)
    pv_b = calculate_pv_annuity(40, rate/100, 12)
    ax5.plot(rate, pv_a, 'bo', markersize=10, zorder=5)
    ax5.plot(rate, pv_b, 'ro', markersize=10, zorder=5)
    
    # Add labels with better positioning
    ax5.annotate(f'A: ${pv_a:.0f}M', (rate, pv_a), 
                textcoords="offset points", xytext=(0, 15), 
                ha='center', fontsize=10, fontweight='bold', color='blue')
    ax5.annotate(f'B: ${pv_b:.0f}M', (rate, pv_b), 
                textcoords="offset points", xytext=(0, -20), 
                ha='center', fontsize=10, fontweight='bold', color='red')
    
    # Add difference annotation
    diff = pv_a - pv_b
    mid_point = (pv_a + pv_b) / 2
    ax5.annotate(f'Δ = ${diff:.0f}M', (rate, mid_point), 
                textcoords="offset points", xytext=(25, 0), 
                ha='left', fontsize=9, color='green', fontweight='bold',
                bbox=dict(boxstyle="round,pad=0.3", facecolor="lightgreen", alpha=0.5))

# Add shaded region to show where A > B
ax5.fill_between(discount_rates * 100, pv_a_values, pv_b_values, 
                 where=np.array(pv_a_values) > np.array(pv_b_values),
                 alpha=0.2, color='green', label='Investment A Advantage')

ax5.set_xlim(0, 20)
ax5.set_ylim(0, max(max(pv_a_values), max(pv_b_values)) * 1.1)

plt.tight_layout()
plt.savefig('visual_5_investment_comparison.png', dpi=300, bbox_inches='tight')
plt.close()

print("\n✓ All visualizations created successfully!")
print("\nFiles generated:")
print("1. visual_1_revenue_margins.png - Revenue & Margin Trends")
print("2. visual_2_cash_generation.png - Cash Flow Analysis")
print("3. visual_3_leverage_liquidity.png - Leverage & Liquidity (ENLARGED)")
print("4. visual_4_income_comparison.png - Operating vs Net Income")
print("5. visual_5_investment_comparison.png - Investment NPV Comparison")