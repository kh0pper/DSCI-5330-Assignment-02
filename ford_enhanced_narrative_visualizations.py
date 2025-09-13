#!/usr/bin/env python3
"""
Ford Motor Company - Enhanced Visualizations with Strategic Narrative
Supporting the 2018 restructuring transformation story
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.patches import Rectangle
import matplotlib.patches as mpatches

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

print("Creating enhanced narrative visualizations...")

# Enhanced Visual 1: Revenue & Margin Trends with Three-Phase Story
fig1, ax1 = plt.subplots(figsize=(14, 8))
ax1_twin = ax1.twinx()

# Phase background shading
phase1_patch = Rectangle((2014.5, 0), 3.5, 200, alpha=0.15, facecolor='red', zorder=0)
phase2_patch = Rectangle((2018, 0), 2.5, 200, alpha=0.15, facecolor='yellow', zorder=0)
phase3_patch = Rectangle((2020.5, 0), 3.5, 200, alpha=0.15, facecolor='green', zorder=0)

ax1.add_patch(phase1_patch)
ax1.add_patch(phase2_patch)
ax1.add_patch(phase3_patch)

# Plot data
line1 = ax1.plot(df['Year Ended'], df['Revenue ($B)'], 'b-', marker='o', linewidth=3, 
                 markersize=10, label='Revenue ($B)', zorder=5)
line2 = ax1_twin.plot(df['Year Ended'], df['Operating Margin %'], 'r--', marker='s', 
                      linewidth=2.5, markersize=8, label='Operating Margin %', zorder=5)
line3 = ax1_twin.plot(df['Year Ended'], df['Net Margin %'], 'g--', marker='^', 
                      linewidth=2.5, markersize=8, label='Net Margin %', zorder=5)

# Add phase divider lines
ax1.axvline(x=2018, color='black', linestyle='-', alpha=0.8, linewidth=2, zorder=10)
ax1.axvline(x=2020.5, color='black', linestyle='-', alpha=0.8, linewidth=2, zorder=10)

# Phase labels
ax1.text(2016.75, 180, 'PHASE 1\nDeclining Performance\n(2015-2018)', ha='center', va='center', 
         fontsize=10, fontweight='bold', bbox=dict(boxstyle="round,pad=0.5", facecolor="white", alpha=0.8))
ax1.text(2019.25, 180, 'PHASE 2\nStrategic Pivot\n(2018-2020)', ha='center', va='center', 
         fontsize=10, fontweight='bold', bbox=dict(boxstyle="round,pad=0.5", facecolor="white", alpha=0.8))
ax1.text(2022.25, 180, 'PHASE 3\nTransformation Payoff\n(2021-2024)', ha='center', va='center', 
         fontsize=10, fontweight='bold', bbox=dict(boxstyle="round,pad=0.5", facecolor="white", alpha=0.8))

# Key annotations
ax1.annotate('Crisis Point\n2.0% Operating Margin', xy=(2018, 160.34), xytext=(2017, 140),
             arrowprops=dict(arrowstyle='->', color='red', lw=2),
             fontsize=9, ha='center', color='red', fontweight='bold',
             bbox=dict(boxstyle="round,pad=0.3", facecolor="white", edgecolor="red"))

ax1.annotate('2018 Strategic\nRestructuring', xy=(2018, 150), xytext=(2018.5, 120),
             arrowprops=dict(arrowstyle='->', color='black', lw=2),
             fontsize=9, ha='center', color='black', fontweight='bold',
             bbox=dict(boxstyle="round,pad=0.3", facecolor="yellow", alpha=0.7))

ax1.annotate('Strategy Vindication\n$17.9B Net Income', xy=(2021, 136.3), xytext=(2021, 200),
             arrowprops=dict(arrowstyle='->', color='green', lw=2),
             fontsize=9, ha='center', color='green', fontweight='bold',
             bbox=dict(boxstyle="round,pad=0.3", facecolor="white", edgecolor="green"))

ax1.annotate('All-Time High\n$185B Revenue', xy=(2024, 185), xytext=(2023, 210),
             arrowprops=dict(arrowstyle='->', color='blue', lw=2),
             fontsize=9, ha='center', color='blue', fontweight='bold',
             bbox=dict(boxstyle="round,pad=0.3", facecolor="white", edgecolor="blue"))

# Formatting
ax1.set_xlabel('Year', fontsize=12, fontweight='bold')
ax1.set_ylabel('Revenue ($B)', color='b', fontsize=12, fontweight='bold')
ax1_twin.set_ylabel('Margin (%)', color='r', fontsize=12, fontweight='bold')
ax1.set_title('Ford Motor Company: Strategic Transformation Journey (2015-2024)\nThree Phases of Business Evolution', 
              fontsize=14, fontweight='bold', pad=30)

# Legend
lines = line1 + line2 + line3
labels = [l.get_label() for l in lines]
ax1.legend(lines, labels, loc='upper left', fontsize=11, frameon=True, shadow=True)

ax1.grid(True, alpha=0.3)
ax1.set_xlim(2014.5, 2024.5)
ax1.set_ylim(0, 220)
ax1_twin.set_ylim(-5, 15)

plt.tight_layout()
plt.savefig('visual_1_revenue_margins.png', dpi=300, bbox_inches='tight')
plt.close()

# Enhanced Visual 2: Cash Flow Analysis with Strategic Context
fig2, ax2 = plt.subplots(figsize=(14, 8))
width = 0.25
x = np.arange(len(df['Year Ended']))

bars1 = ax2.bar(x - width, df['Cash Flow from Ops ($B)'], width, label='Operating Cash Flow', 
                alpha=0.9, color='green', edgecolor='darkgreen', linewidth=1.5)
bars2 = ax2.bar(x, df['Capex ($B)'], width, label='Capital Expenditure', 
                alpha=0.9, color='red', edgecolor='darkred', linewidth=1.5)
bars3 = ax2.bar(x + width, df['Free Cash Flow ($B)'], width, label='Free Cash Flow', 
                alpha=0.9, color='blue', edgecolor='darkblue', linewidth=1.5)

# Add phase background shading
ax2.axvspan(-0.5, 3.5, alpha=0.1, color='red', zorder=0)
ax2.axvspan(3.5, 5.5, alpha=0.1, color='yellow', zorder=0)
ax2.axvspan(5.5, 9.5, alpha=0.1, color='green', zorder=0)

# Phase dividers
ax2.axvline(x=3.5, color='black', linestyle='--', alpha=0.6, linewidth=2)
ax2.axvline(x=5.5, color='black', linestyle='--', alpha=0.6, linewidth=2)

# Strategic annotations
ax2.annotate('EV Investment\nRamp-Up', xy=(8.5, 8.68), xytext=(7.5, 15),
             arrowprops=dict(arrowstyle='->', color='purple', lw=2),
             fontsize=10, ha='center', color='purple', fontweight='bold',
             bbox=dict(boxstyle="round,pad=0.3", facecolor="white", edgecolor="purple"))

ax2.annotate('Pandemic\nCash Preservation', xy=(5, 25.24), xytext=(4, 30),
             arrowprops=dict(arrowstyle='->', color='orange', lw=2),
             fontsize=10, ha='center', color='orange', fontweight='bold',
             bbox=dict(boxstyle="round,pad=0.3", facecolor="white", edgecolor="orange"))

# Phase labels
ax2.text(1.75, -8, 'Declining Performance', ha='center', fontsize=10, fontweight='bold')
ax2.text(4.5, -8, 'Strategic Pivot', ha='center', fontsize=10, fontweight='bold')
ax2.text(7.5, -8, 'Transformation Execution', ha='center', fontsize=10, fontweight='bold')

ax2.set_xlabel('Year', fontsize=12, fontweight='bold')
ax2.set_ylabel('Cash Flow ($B)', fontsize=12, fontweight='bold')
ax2.set_title('Ford Motor Company: Cash Flow Through Strategic Transformation\nResilient Cash Generation Enables Strategic Pivot', 
              fontsize=14, fontweight='bold', pad=20)
ax2.set_xticks(x)
ax2.set_xticklabels(df['Year Ended'], rotation=45)
ax2.legend(fontsize=11, loc='upper left', frameon=True, shadow=True)
ax2.grid(True, alpha=0.3, axis='y')
ax2.axhline(y=0, color='black', linestyle='-', alpha=0.5, linewidth=1)
ax2.set_ylim(-12, 35)

plt.tight_layout()
plt.savefig('visual_2_cash_generation.png', dpi=300, bbox_inches='tight')
plt.close()

# Enhanced Visual 3: Balance Sheet Evolution with Strategic Milestones
fig3, ax3 = plt.subplots(figsize=(14, 8))
ax3_twin = ax3.twinx()

# Bar chart for debt and cash
width = 0.4
x = np.arange(len(df['Year Ended']))
bars1 = ax3.bar(x - width/2, df['Total Debt ($B)'], width, alpha=0.7, 
                color='darkred', label='Total Debt ($B)', edgecolor='black', linewidth=1)
bars2 = ax3.bar(x + width/2, df['Cash & Equivalents ($B)'], width, alpha=0.7, 
                color='green', label='Cash & Equivalents ($B)', edgecolor='black', linewidth=1)

# Current ratio line
line = ax3_twin.plot(df['Year Ended'], df['Current Ratio'], 'b-', marker='o', 
                     linewidth=3, markersize=10, label='Current Ratio', zorder=10, alpha=0.8)

# Strategic milestones
ax3.axvline(x=2018, color='red', linestyle='--', alpha=0.8, linewidth=2)
ax3.text(2018, 170, '2018 Restructuring', rotation=90, ha='right', va='center', 
         fontweight='bold', color='red', fontsize=10,
         bbox=dict(boxstyle="round,pad=0.3", facecolor="white", edgecolor="red"))

ax3.axvline(x=2020, color='orange', linestyle='--', alpha=0.8, linewidth=2)
ax3.text(2020, 170, 'Pandemic Response', rotation=90, ha='right', va='center', 
         fontweight='bold', color='orange', fontsize=10,
         bbox=dict(boxstyle="round,pad=0.3", facecolor="white", edgecolor="orange"))

# Key insights
ax3.annotate('Debt Peak\n$161B', xy=(5, 161), xytext=(4, 180),
             arrowprops=dict(arrowstyle='->', color='darkred', lw=2),
             fontsize=10, ha='center', color='darkred', fontweight='bold',
             bbox=dict(boxstyle="round,pad=0.3", facecolor="white", edgecolor="darkred"))

ax3.annotate('Cash Buildup\nPandemic Prep', xy=(5, 25.2), xytext=(6, 40),
             arrowprops=dict(arrowstyle='->', color='green', lw=2),
             fontsize=10, ha='center', color='green', fontweight='bold',
             bbox=dict(boxstyle="round,pad=0.3", facecolor="white", edgecolor="green"))

# Formatting
ax3.set_xlabel('Year', fontsize=12, fontweight='bold')
ax3.set_ylabel('Billions ($)', fontsize=12, fontweight='bold')
ax3_twin.set_ylabel('Current Ratio', color='b', fontsize=12, fontweight='bold')
ax3.set_title('Ford Motor Company: Balance Sheet Evolution Through Transformation\nDebt Management and Liquidity Strategy', 
              fontsize=14, fontweight='bold', pad=20)
ax3.set_xticks(x)
ax3.set_xticklabels(df['Year Ended'], rotation=45, fontsize=11)

# Position legends
ax3.legend(loc='upper left', fontsize=11, frameon=True, shadow=True)
ax3_twin.legend(loc='upper right', fontsize=11, frameon=True, shadow=True)

ax3.grid(True, alpha=0.3, axis='y')
ax3_twin.axhline(y=1.0, color='red', linestyle=':', alpha=0.5, linewidth=1)
ax3_twin.text(2015.5, 1.02, 'Min Threshold', fontsize=9, color='red')

ax3.set_ylim(0, 190)
ax3_twin.set_ylim(0.9, 1.35)

plt.tight_layout()
plt.savefig('visual_3_leverage_liquidity.png', dpi=300, bbox_inches='tight')
plt.close()

# Enhanced Visual 4: Business Performance Evolution
fig4, ax4 = plt.subplots(figsize=(14, 8))
width = 0.4
x = np.arange(len(df['Year Ended']))

bars1 = ax4.bar(x - width/2, df['Operating Income ($B)'], width, 
                label='Operating Income', alpha=0.85, color='steelblue', 
                edgecolor='darkblue', linewidth=1.5)
bars2 = ax4.bar(x + width/2, df['Net Income ($B)'], width, 
                label='Net Income', alpha=0.85, color='darkgreen', 
                edgecolor='black', linewidth=1.5)

# Phase backgrounds
ax4.axvspan(-0.5, 3.5, alpha=0.1, color='red', zorder=0)
ax4.axvspan(3.5, 5.5, alpha=0.1, color='yellow', zorder=0)
ax4.axvspan(5.5, 9.5, alpha=0.1, color='green', zorder=0)

# Strategic milestones
ax4.axvline(x=3.5, color='black', linestyle='-', alpha=0.8, linewidth=3)
ax4.text(3.5, 20, '2018 STRATEGIC\nRESTRUCTURING', rotation=90, ha='right', va='center', 
         fontweight='bold', fontsize=11,
         bbox=dict(boxstyle="round,pad=0.5", facecolor="yellow", alpha=0.8))

# Key annotations
ax4.annotate('Crisis: $0.57B\nOperating Income', xy=(4, 0.57), xytext=(2.5, 10),
             arrowprops=dict(arrowstyle='->', color='red', lw=2),
             fontsize=10, ha='center', color='red', fontweight='bold',
             bbox=dict(boxstyle="round,pad=0.3", facecolor="white", edgecolor="red"))

ax4.annotate('Strategy Vindication\n$17.9B Special Items\n(Rivian, Pension)', 
             xy=(6, 17.91), xytext=(7.5, 25),
             arrowprops=dict(arrowstyle='->', color='green', lw=2),
             fontsize=10, ha='center', color='green', fontweight='bold',
             bbox=dict(boxstyle="round,pad=0.3", facecolor="lightgreen", alpha=0.8))

ax4.annotate('Sustained Recovery\n$5.9B Net Income', xy=(9, 5.89), xytext=(8.5, 12),
             arrowprops=dict(arrowstyle='->', color='darkgreen', lw=2),
             fontsize=10, ha='center', color='darkgreen', fontweight='bold',
             bbox=dict(boxstyle="round,pad=0.3", facecolor="white", edgecolor="darkgreen"))

# Business unit evolution note
ax4.text(7, -8, 'Blue/Model e/Pro Strategy Execution', ha='center', fontsize=11, 
         fontweight='bold', style='italic', color='blue',
         bbox=dict(boxstyle="round,pad=0.3", facecolor="lightblue", alpha=0.7))

ax4.set_xlabel('Year', fontsize=12, fontweight='bold')
ax4.set_ylabel('Income ($B)', fontsize=12, fontweight='bold')
ax4.set_title('Ford Motor Company: Profitability Through Strategic Transformation\nFrom Crisis to Recovery via Three-Business Strategy', 
              fontsize=14, fontweight='bold', pad=20)
ax4.set_xticks(x)
ax4.set_xticklabels(df['Year Ended'], rotation=45)
ax4.legend(fontsize=11, loc='upper left', frameon=True, shadow=True)
ax4.grid(True, alpha=0.3, axis='y')
ax4.axhline(y=0, color='red', linestyle='-', alpha=0.5, linewidth=1.5)
ax4.set_ylim(-10, 30)

plt.tight_layout()
plt.savefig('visual_4_income_comparison.png', dpi=300, bbox_inches='tight')
plt.close()

# Enhanced Visual 5: Investment NPV with Strategic Context
fig5, ax5 = plt.subplots(figsize=(14, 8))

def calculate_pv_annuity(payment, rate, years):
    if rate == 0:
        return payment * years
    return payment * ((1 + rate)**(-years) - 1) / (-rate)

discount_rates = np.arange(0.01, 0.20, 0.001)
pv_a_values = [calculate_pv_annuity(50, r, 20) for r in discount_rates]
pv_b_values = [calculate_pv_annuity(40, r, 12) for r in discount_rates]

ax5.plot(discount_rates * 100, pv_a_values, 'b-', linewidth=4, 
         label='Investment A ($50M × 20 years)', alpha=0.9)
ax5.plot(discount_rates * 100, pv_b_values, 'r-', linewidth=4, 
         label='Investment B ($40M × 12 years)', alpha=0.9)

# Strategic context shading
ax5.fill_between(discount_rates * 100, pv_a_values, pv_b_values, 
                 where=np.array(pv_a_values) > np.array(pv_b_values),
                 alpha=0.2, color='green', label='Investment A Advantage Zone')

# Ford's likely discount rate range
ax5.axvspan(8, 12, alpha=0.2, color='orange', zorder=1)
ax5.text(10, 100, "Ford's Likely\nWACC Range\n(8-12%)", ha='center', va='center',
         fontsize=11, fontweight='bold', color='darkorange',
         bbox=dict(boxstyle="round,pad=0.5", facecolor="white", edgecolor="orange"))

# Mark specific points with strategic context
for rate in [5, 10, 15]:
    pv_a = calculate_pv_annuity(50, rate/100, 20)
    pv_b = calculate_pv_annuity(40, rate/100, 12)
    ax5.plot(rate, pv_a, 'bo', markersize=12, zorder=5)
    ax5.plot(rate, pv_b, 'ro', markersize=12, zorder=5)
    
    # Strategic annotations
    if rate == 10:
        ax5.annotate(f'@ {rate}% WACC:\nA: ${pv_a:.0f}M\nB: ${pv_b:.0f}M\nAdvantage: ${pv_a-pv_b:.0f}M', 
                    (rate, (pv_a + pv_b) / 2), 
                    textcoords="offset points", xytext=(40, 0), 
                    ha='left', fontsize=11, fontweight='bold', color='black',
                    bbox=dict(boxstyle="round,pad=0.5", facecolor="lightyellow", alpha=0.9))

# Strategic transformation context
ax5.text(2, 450, 'Investment A Horizon\nAligns with Ford\'s\n20-Year EV Transformation', 
         fontsize=12, fontweight='bold', color='blue',
         bbox=dict(boxstyle="round,pad=0.5", facecolor="lightblue", alpha=0.8))

ax5.text(17, 250, 'Investment B\nShorter Timeline\nMisses Long-term\nValue Creation', 
         fontsize=11, fontweight='bold', color='red',
         bbox=dict(boxstyle="round,pad=0.5", facecolor="mistyrose", alpha=0.8))

ax5.set_xlabel('Discount Rate (%)', fontsize=12, fontweight='bold')
ax5.set_ylabel('Present Value ($M)', fontsize=12, fontweight='bold')
ax5.set_title('Investment NPV Analysis: Strategic Alignment with Ford Transformation\n20-Year Horizon Matches Three-Business Strategy Timeline', 
              fontsize=14, fontweight='bold', pad=20)
ax5.legend(fontsize=12, loc='upper right', frameon=True, shadow=True)
ax5.grid(True, alpha=0.3)
ax5.set_xlim(0, 20)
ax5.set_ylim(0, 650)

plt.tight_layout()
plt.savefig('visual_5_investment_comparison.png', dpi=300, bbox_inches='tight')
plt.close()

print("\n✓ All enhanced narrative visualizations created successfully!")
print("\nFiles generated with strategic transformation context:")
print("1. visual_1_revenue_margins.png - Three-phase transformation journey")
print("2. visual_2_cash_generation.png - Cash flow resilience through strategic pivot")
print("3. visual_3_leverage_liquidity.png - Balance sheet evolution with milestones")
print("4. visual_4_income_comparison.png - Profitability recovery via restructuring")
print("5. visual_5_investment_comparison.png - Strategic alignment with transformation timeline")