#!/usr/bin/env python3
"""
Ford Motor Company Financial Analysis (2015-2024)
Following the specific outline structure provided
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.gridspec import GridSpec

# Set style
plt.style.use('default')
sns.set_palette("husl")

# Load the financial data
df = pd.read_excel('Ford_10K_Financial_Ratios_2015_2024.xlsx')

# Calculate additional metrics needed for the outline
df['Operating Margin %'] = (df['Operating Income ($B)'] / df['Revenue ($B)']) * 100
df['Net Margin %'] = (df['Net Income ($B)'] / df['Revenue ($B)']) * 100
df['Free Cash Flow ($B)'] = df['Cash Flow from Ops ($B)'] - df['Capex ($B)']
df['Current Ratio'] = df['Current Assets ($B)'] / df['Current Liabilities ($B)']
df['Debt to Equity'] = df['Total Debt ($B)'] / df['Shareholders Equity ($B)']

print("=" * 80)
print("FORD MOTOR COMPANY FINANCIAL ANALYSIS (2015-2024)")
print("Following Outline Structure")
print("=" * 80)

# Section 1: Revenue & Profitability
print("\n1. REVENUE & PROFITABILITY")
print("-" * 40)
print(f"• Revenue Range: ${df['Revenue ($B)'].min():.0f}B (2020 pandemic) to ${df['Revenue ($B)'].max():.0f}B (2024)")
print(f"• Operating Income Range: ${df['Operating Income ($B)'].min():.1f}B to ${df['Operating Income ($B)'].max():.1f}B")
print(f"• 2021 Outlier: Net Income = ${df[df['Year Ended']==2021]['Net Income ($B)'].values[0]:.1f}B (special items)")
print(f"• Average Operating Margin: {df['Operating Margin %'].mean():.1f}%")
print(f"• Average Net Margin: {df['Net Margin %'].mean():.1f}%")

# Section 2: Cash Flow & Capex
print("\n2. CASH FLOW & CAPEX")
print("-" * 40)
print(f"• CFO Range: ${df['Cash Flow from Ops ($B)'].min():.1f}B to ${df['Cash Flow from Ops ($B)'].max():.1f}B")
print(f"• Average Annual Capex: ${df['Capex ($B)'].mean():.1f}B")
print(f"• Free Cash Flow (10-year total): ${df['Free Cash Flow ($B)'].sum():.1f}B")
positive_fcf_years = len(df[df['Free Cash Flow ($B)'] > 0])
print(f"• Years with Positive FCF: {positive_fcf_years}/10")

# Section 3: Balance Sheet & Debt
print("\n3. BALANCE SHEET & DEBT")
print("-" * 40)
print(f"• Total Assets: ${df.iloc[0]['Total Assets ($B)']:.0f}B (2015) → ${df.iloc[-1]['Total Assets ($B)']:.0f}B (2024)")
print(f"• Total Debt Range: ${df['Total Debt ($B)'].min():.0f}B to ${df['Total Debt ($B)'].max():.0f}B")
print(f"• Current Cash Holdings (2024): ${df.iloc[-1]['Cash & Equivalents ($B)']:.1f}B")
print(f"• Peak Cash (2020-2021): ${df['Cash & Equivalents ($B)'].max():.1f}B")

# Section 4: Liquidity & Leverage
print("\n4. LIQUIDITY & LEVERAGE")
print("-" * 40)
print(f"• Current Ratio Range: {df['Current Ratio'].min():.2f} to {df['Current Ratio'].max():.2f}")
print(f"• Current Ratio (2024): {df.iloc[-1]['Current Ratio']:.2f}")
print(f"• Debt-to-Equity Range: {df['Debt to Equity'].min():.1f}x to {df['Debt to Equity'].max():.1f}x")
print(f"• Debt-to-Equity (2024): {df.iloc[-1]['Debt to Equity']:.1f}x")

# Section 5: Key Risks & Patterns
print("\n5. KEY RISKS & PATTERNS")
print("-" * 40)
loss_years = df[df['Net Income ($B)'] < 0]['Year Ended'].tolist()
print(f"• Loss Years: {loss_years}")
print(f"• Cyclical Pattern: Down years (2019-2020, 2022) vs recovery years")
print(f"• EV Transition Evidence: Capex increased from ${df.iloc[0]['Capex ($B)']:.1f}B to ${df.iloc[-1]['Capex ($B)']:.1f}B")

# Section 6: Investment Analysis
print("\n6. INVESTMENT ALTERNATIVES ANALYSIS")
print("-" * 40)

# Calculate PV for different discount rates
def calculate_pv_annuity(payment, rate, years):
    """Calculate present value of an annuity"""
    if rate == 0:
        return payment * years
    return payment * ((1 - (1 + rate)**(-years)) / rate)

# Test different discount rates
rates = [0.05, 0.10, 0.15]
for rate in rates:
    pv_a = calculate_pv_annuity(50, rate, 20)
    pv_b = calculate_pv_annuity(40, rate, 12)
    print(f"\nAt {rate*100:.0f}% Discount Rate:")
    print(f"  Investment A (50M × 20yr): PV = ${pv_a:.1f}M")
    print(f"  Investment B (40M × 12yr): PV = ${pv_b:.1f}M")
    print(f"  Advantage to A: ${pv_a - pv_b:.1f}M")

print("\n✓ RECOMMENDATION: Choose Investment A")
print("  - Higher annual cash flow ($50M vs $40M)")
print("  - Longer duration (20 years vs 12 years)")
print("  - Superior NPV across all reasonable discount rates")

# Create visualizations per outline
fig = plt.figure(figsize=(16, 12))
gs = GridSpec(3, 2, figure=fig, hspace=0.3, wspace=0.25)

# Visual 1: Topline & Margin Trends (dual-axis)
ax1 = fig.add_subplot(gs[0, 0])
ax1_twin = ax1.twinx()
line1 = ax1.plot(df['Year Ended'], df['Revenue ($B)'], 'b-', marker='o', linewidth=2.5, markersize=8, label='Revenue')
line2 = ax1_twin.plot(df['Year Ended'], df['Operating Margin %'], 'r--', marker='s', linewidth=2, markersize=6, label='Operating Margin')
line3 = ax1_twin.plot(df['Year Ended'], df['Net Margin %'], 'g--', marker='^', linewidth=2, markersize=6, label='Net Margin')
ax1.set_xlabel('Year', fontsize=10)
ax1.set_ylabel('Revenue ($B)', color='b', fontsize=10)
ax1_twin.set_ylabel('Margin (%)', color='r', fontsize=10)
ax1.set_title('1. Topline & Margin Trends', fontsize=12, fontweight='bold')
lines = line1 + line2 + line3
labels = [l.get_label() for l in lines]
ax1.legend(lines, labels, loc='upper left', fontsize=9)
ax1.grid(True, alpha=0.3)
ax1.set_xticks(df['Year Ended'])
ax1.set_xticklabels(df['Year Ended'], rotation=45)

# Visual 2: Cash Generation (CFO, Capex, FCF)
ax2 = fig.add_subplot(gs[0, 1])
width = 0.25
x = np.arange(len(df['Year Ended']))
bars1 = ax2.bar(x - width, df['Cash Flow from Ops ($B)'], width, label='CFO', alpha=0.8, color='green')
bars2 = ax2.bar(x, df['Capex ($B)'], width, label='Capex', alpha=0.8, color='red')
bars3 = ax2.bar(x + width, df['Free Cash Flow ($B)'], width, label='FCF', alpha=0.8, color='blue')
ax2.set_xlabel('Year', fontsize=10)
ax2.set_ylabel('Cash Flow ($B)', fontsize=10)
ax2.set_title('2. Cash Generation: CFO, Capex, FCF', fontsize=12, fontweight='bold')
ax2.set_xticks(x)
ax2.set_xticklabels(df['Year Ended'], rotation=45)
ax2.legend(fontsize=9)
ax2.grid(True, alpha=0.3)
ax2.axhline(y=0, color='black', linestyle='-', alpha=0.5, linewidth=0.5)

# Visual 3: Leverage & Liquidity
ax3 = fig.add_subplot(gs[1, 0])
ax3_twin = ax3.twinx()
bars = ax3.bar(df['Year Ended'], df['Total Debt ($B)'], alpha=0.6, color='darkred', label='Total Debt')
line = ax3.plot(df['Year Ended'], df['Cash & Equivalents ($B)'], 'g-', marker='o', linewidth=2.5, markersize=8, label='Cash')
cr_line = ax3_twin.plot(df['Year Ended'], df['Current Ratio'], 'b--', marker='s', linewidth=2, markersize=6, label='Current Ratio')
ax3.set_xlabel('Year', fontsize=10)
ax3.set_ylabel('Billions ($)', fontsize=10)
ax3_twin.set_ylabel('Current Ratio', color='b', fontsize=10)
ax3.set_title('3. Leverage & Liquidity', fontsize=12, fontweight='bold')
ax3.set_xticks(df['Year Ended'])
ax3.set_xticklabels(df['Year Ended'], rotation=45)
# Combine legends
h1, l1 = ax3.get_legend_handles_labels()
h2, l2 = ax3_twin.get_legend_handles_labels()
ax3.legend(h1+h2, l1+l2, loc='upper left', fontsize=9)
ax3.grid(True, alpha=0.3)

# Visual 4: Ford Credit vs Automotive (simulated - using Operating Income as proxy)
ax4 = fig.add_subplot(gs[1, 1])
# Note: Since we don't have segment data, we'll show Operating vs Net Income
width = 0.35
x = np.arange(len(df['Year Ended']))
bars1 = ax4.bar(x - width/2, df['Operating Income ($B)'], width, label='Operating Income', alpha=0.8, color='steelblue')
bars2 = ax4.bar(x + width/2, df['Net Income ($B)'], width, label='Net Income', alpha=0.8, color='darkgreen')
ax4.set_xlabel('Year', fontsize=10)
ax4.set_ylabel('Income ($B)', fontsize=10)
ax4.set_title('4. Operating vs Net Income by Year', fontsize=12, fontweight='bold')
ax4.set_xticks(x)
ax4.set_xticklabels(df['Year Ended'], rotation=45)
ax4.legend(fontsize=9)
ax4.grid(True, alpha=0.3)
ax4.axhline(y=0, color='red', linestyle='--', alpha=0.5)

# Visual 5: Investment Comparison
ax5 = fig.add_subplot(gs[2, :])
discount_rates = np.arange(0.01, 0.20, 0.01)
pv_a_values = [calculate_pv_annuity(50, r, 20) for r in discount_rates]
pv_b_values = [calculate_pv_annuity(40, r, 12) for r in discount_rates]

ax5.plot(discount_rates * 100, pv_a_values, 'b-', linewidth=2.5, label='Investment A ($50M × 20 years)')
ax5.plot(discount_rates * 100, pv_b_values, 'r-', linewidth=2.5, label='Investment B ($40M × 12 years)')
ax5.set_xlabel('Discount Rate (%)', fontsize=11)
ax5.set_ylabel('Present Value ($M)', fontsize=11)
ax5.set_title('5. Investment NPV Comparison Across Discount Rates', fontsize=12, fontweight='bold')
ax5.legend(fontsize=10)
ax5.grid(True, alpha=0.3)
# Mark specific points
for rate in [5, 10, 15]:
    pv_a = calculate_pv_annuity(50, rate/100, 20)
    pv_b = calculate_pv_annuity(40, rate/100, 12)
    ax5.plot(rate, pv_a, 'bo', markersize=8)
    ax5.plot(rate, pv_b, 'ro', markersize=8)
    ax5.annotate(f'${pv_a:.0f}M', (rate, pv_a), textcoords="offset points", xytext=(0,10), ha='center', fontsize=9)
    ax5.annotate(f'${pv_b:.0f}M', (rate, pv_b), textcoords="offset points", xytext=(0,-15), ha='center', fontsize=9)

plt.suptitle('Ford Motor Company Financial Analysis Dashboard (2015-2024)', fontsize=14, fontweight='bold', y=1.02)
plt.savefig('ford_analysis_dashboard_per_outline.png', dpi=300, bbox_inches='tight')

# Export summary data
summary_df = pd.DataFrame({
    'Metric': [
        'Revenue Range',
        'Operating Margin Avg',
        'Net Margin Avg',
        'CFO Average',
        'Capex Average',
        'FCF Total (10yr)',
        'Total Assets 2024',
        'Total Debt 2024',
        'Cash 2024',
        'Current Ratio 2024',
        'Debt-to-Equity 2024'
    ],
    'Value': [
        f"${df['Revenue ($B)'].min():.0f}B - ${df['Revenue ($B)'].max():.0f}B",
        f"{df['Operating Margin %'].mean():.1f}%",
        f"{df['Net Margin %'].mean():.1f}%",
        f"${df['Cash Flow from Ops ($B)'].mean():.1f}B",
        f"${df['Capex ($B)'].mean():.1f}B",
        f"${df['Free Cash Flow ($B)'].sum():.1f}B",
        f"${df.iloc[-1]['Total Assets ($B)']:.0f}B",
        f"${df.iloc[-1]['Total Debt ($B)']:.0f}B",
        f"${df.iloc[-1]['Cash & Equivalents ($B)']:.1f}B",
        f"{df.iloc[-1]['Current Ratio']:.2f}",
        f"{df.iloc[-1]['Debt to Equity']:.1f}x"
    ]
})

summary_df.to_csv('ford_summary_metrics_per_outline.csv', index=False)
print(f"\n\n✓ Analysis complete")
print(f"✓ Dashboard saved: ford_analysis_dashboard_per_outline.png")
print(f"✓ Summary saved: ford_summary_metrics_per_outline.csv")