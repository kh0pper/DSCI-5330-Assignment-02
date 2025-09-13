# DSCI-5330 Assignment 02: Ford Motor Company Financial Analysis

## Project Overview

This repository contains a comprehensive financial analysis of Ford Motor Company covering the period 2015-2024. The analysis follows a structured approach examining revenue, profitability, cash flow, balance sheet health, and strategic investment decisions.

## Assignment Deliverables

- **Executive Memorandum**: Professional business memo with findings and recommendations
- **Presentation Slides**: 15-slide presentation with supporting appendices  
- **Financial Visualizations**: 5 detailed charts analyzing key financial metrics
- **Investment Analysis**: NPV comparison of two long-term investment alternatives

## Key Findings

- Revenue growth of 23.7% over 10 years ($149.6B to $185.0B)
- Strong cash generation with $91.7B total free cash flow
- Cyclical profitability with challenges in 2020 (pandemic) and 2022
- **Investment Recommendation**: Choose Investment A ($50M × 20 years) for superior NPV

## Project Structure

```
├── CLAUDE.md                                    # Development guidance
├── README.md                                    # Project documentation
├── ford_analysis_per_outline.py                 # Main financial analysis
├── ford_separate_visualizations.py              # Visualization generator
├── Ford_Executive_Memo_Outline_Based.md         # Executive memorandum
├── Ford_Presentation_Outline_Based.md           # Presentation slides
├── Ford_10K_Financial_Ratios_2015_2024.xlsx     # Primary financial data
├── Outline Rough Draft.md                       # Analysis framework
├── visual_1_revenue_margins.png                 # Revenue & margin trends
├── visual_2_cash_generation.png                 # Cash flow analysis
├── visual_3_leverage_liquidity.png              # Leverage & liquidity
├── visual_4_income_comparison.png               # Income comparison
├── visual_5_investment_comparison.png           # Investment NPV analysis
├── ford_summary_metrics_per_outline.csv         # Summary metrics
├── 10k/                                         # SEC 10-K filings
└── Annual Report/                               # Annual report PDFs
```

## Quick Start

1. **Set up Python environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install pandas openpyxl matplotlib seaborn numpy
   ```

2. **Run financial analysis:**
   ```bash
   python ford_analysis_per_outline.py
   ```

3. **Generate visualizations:**
   ```bash
   python ford_separate_visualizations.py
   ```

## Analysis Framework

The analysis follows a 6-section structure:

1. **Revenue & Profitability** - Cyclical patterns and margin analysis
2. **Cash Flow & Capex** - Operating cash flow vs capital investments  
3. **Balance Sheet & Debt** - Asset growth and leverage (Ford Credit considerations)
4. **Liquidity & Leverage** - Current ratios and debt management
5. **Key Risks & Patterns** - Strategic vulnerabilities and opportunities
6. **Investment Analysis** - NPV evaluation of long-term alternatives

## Investment Recommendation

**Recommendation: Investment A**

- **Investment A**: $50M/year × 20 years → NPV: $456.4M (@ 9% discount)
- **Investment B**: $40M/year × 12 years → NPV: $286.4M (@ 9% discount)
- **Advantage**: $170M superior NPV across all reasonable discount rates

## Course Information

- **Course**: DSCI-5330 Finance and Accounting
- **Institution**: University of North Texas
- **Assignment**: Assignment 2 - Corporate Financial Analysis
- **Company**: Ford Motor Company (NYSE: F)