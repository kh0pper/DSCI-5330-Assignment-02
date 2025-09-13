# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a finance and accounting assignment analyzing Ford Motor Company's financial performance from 2015-2024. The project produces an executive memorandum, presentation slides, and comprehensive visualizations following a specific analytical outline structure.

## Key Commands

### Python Analysis Environment
```bash
# Set up virtual environment
python3 -m venv venv
source venv/bin/activate
pip install pandas openpyxl matplotlib seaborn numpy

# Run complete financial analysis
python ford_analysis_per_outline.py

# Generate individual visualization charts
python ford_separate_visualizations.py
```

### Key Data Dependencies
- **Primary Data**: `Ford_10K_Financial_Ratios_2015_2024.xlsx` - Pre-compiled 10-year financial metrics
- **Supporting Documents**: 
  - `10k/` directory - SEC 10-K filings (2015-2024)
  - `Annual Report/` directory - Annual report PDFs
  - `Assignment 2 Finance and Accounting Instruction.docx` - Assignment requirements

## Project Architecture

### Analysis Structure
The project follows a specific 6-section analytical framework defined in `Outline Rough Draft.md`:

1. **Revenue & Profitability** - Margin analysis and cyclical patterns
2. **Cash Flow & Capex** - Operating cash flow vs capital investments
3. **Balance Sheet & Debt** - Asset growth and debt structure (Ford Credit separation)
4. **Liquidity & Leverage** - Current ratios and leverage metrics
5. **Key Risks & Patterns** - Cyclical vulnerabilities and strategic risks
6. **Investment Analysis** - NPV calculations for two investment alternatives

### Core Python Scripts

**`ford_analysis_per_outline.py`** - Main analytical engine:
- Loads Excel data and calculates derived financial ratios
- Performs structured analysis following the 6-section outline
- Generates investment NPV comparisons across discount rates (5%, 10%, 15%)
- Creates consolidated dashboard visualization
- Exports summary metrics to CSV

**`ford_separate_visualizations.py`** - Visualization generator:
- Creates 5 individual chart files to avoid overlapping elements
- Visual 3 (Leverage & Liquidity) requires specific formatting: 14x8 size with current ratio line overlaying bars
- Each chart corresponds to outline sections with specific styling requirements

### Financial Metrics Calculations

Key derived metrics calculated consistently across scripts:
```python
df['Operating Margin %'] = (df['Operating Income ($B)'] / df['Revenue ($B)']) * 100
df['Net Margin %'] = (df['Net Income ($B)'] / df['Revenue ($B)']) * 100
df['Free Cash Flow ($B)'] = df['Cash Flow from Ops ($B)'] - df['Capex ($B)']
df['Current Ratio'] = df['Current Assets ($B)'] / df['Current Liabilities ($B)']
df['Debt to Equity'] = df['Total Debt ($B)'] / df['Shareholders Equity ($B)']
```

### Investment NPV Analysis

Critical function for investment alternative evaluation:
```python
def calculate_pv_annuity(payment, rate, years):
    if rate == 0:
        return payment * years
    return payment * ((1 - (1 + rate)**(-years)) / rate)
```

Investment scenarios:
- **Investment A**: $50M/year × 20 years
- **Investment B**: $40M/year × 12 years

## Output Deliverables

1. **Executive Memo**: `Ford_Executive_Memo_Outline_Based.md` - Formal business memorandum
2. **Presentation**: `Ford_Presentation_Outline_Based.md` - 15 slides + appendices  
3. **Visualizations**: 5 separate PNG files (visual_1 through visual_5)
4. **Data Export**: `ford_summary_metrics_per_outline.csv`

## Critical Ford-Specific Context

### Financial Analysis Considerations
- **Ford Credit Impact**: Total debt figures are inflated by Ford Credit financing operations - distinguish between Automotive and Credit segments
- **Cyclical Patterns**: Automotive industry exhibits strong cyclical performance - losses in 2020 (pandemic) and 2022 are part of normal patterns
- **2021 Outlier**: $17.9B net income includes special items (Rivian investment gains, pension remeasurement)
- **Margin Reality**: Operating margins averaging 2.4% reflect industry norms - thin but consistent with automotive manufacturing

### Visualization Requirements
- **Visual 3 Formatting**: Leverage & Liquidity chart must show Current Ratio line overlaying debt/cash bars (not separate axis)
- **Chart Sizing**: Balance readability with space constraints - 12x7 or 14x8 optimal for most charts
- **Legend Positioning**: Avoid overlapping elements through strategic bbox_to_anchor positioning

## Data Structure Notes

The Excel file contains 18 columns of annual financial data (2015-2024):
- Revenue, COGS, Operating Income, Net Income, EBIT
- Balance sheet items (Assets, Liabilities, Equity, Cash, Debt)
- Cash flow metrics (Operating CF, Capex)
- Industry-standard billions ($B) formatting

This project structure enables rapid financial analysis regeneration while maintaining consistency with academic assignment requirements and professional presentation standards.