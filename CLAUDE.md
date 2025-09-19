# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a finance and accounting assignment analyzing Ford Motor Company's financial performance from 2015-2024. The project produces an executive memorandum, presentation slides, comprehensive visualizations, and a GitHub Pages website. The analysis emphasizes Ford's 2018 strategic restructuring into three business units (Blue/Model e/Pro) as the central narrative.

## Key Commands

### Python Analysis Environment
```bash
# Set up virtual environment
python3 -m venv venv
source venv/bin/activate
pip install pandas openpyxl matplotlib seaborn numpy tabulate python-docx

# Run complete financial analysis
python ford_analysis_per_outline.py

# Generate basic visualization charts
python ford_separate_visualizations.py

# Generate enhanced narrative visualizations (recommended)
python ford_enhanced_narrative_visualizations.py

# Generate tables for memorandum
python generate_memo_tables.py

# Create professional Ford-branded memo document
python create_final_memo_corrected.py

# Create works cited document with hyperlinked citations
python create_works_cited_v2.py
```

### GitHub Pages Deployment
```bash
# The site is automatically deployed to: https://kh0pper.github.io/DSCI-5330-Assignment-02/
# index.html serves as the main GitHub Pages site
```

### Key Data Dependencies
- **Primary Data**: `Ford_10K_Financial_Ratios_2015_2024.xlsx` - Pre-compiled 10-year financial metrics (18 columns of annual data)
- **Supporting Documents**:
  - `10k/` directory - SEC 10-K filings (2015-2024) - some with TN highlights
  - `Annual Report/` directory - Annual report PDFs (2016-2024)
  - `Assignment 2 Finance and Accounting Instruction.docx` - Assignment requirements
- **Analysis Outputs**:
  - `Ford_Executive_Memo_Outline_Based.md` and `.docx` - Executive memorandum
  - `memo-final.docx` - Professional Ford-branded memo document
  - `work-cited.docx` - Works cited with hyperlinked GitHub repository citations
  - `Ford_Presentation_Outline_Based.md` - Presentation slides
  - `visual_1` through `visual_5` PNG files - Financial charts
  - `ford_summary_metrics_per_outline.csv` - Exported summary data

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

**`ford_separate_visualizations.py`** - Basic visualization generator:
- Creates 5 individual chart files to avoid overlapping elements
- Visual 3 (Leverage & Liquidity) requires specific formatting: 14x8 size with current ratio line overlaying bars
- Each chart corresponds to outline sections with specific styling requirements

**`ford_enhanced_narrative_visualizations.py`** - Strategic narrative visualizations:
- Enhanced versions of all 5 charts with 2018 restructuring narrative
- Three-phase transformation story (Decline → Pivot → Payoff)
- Strategic annotations, phase markers, and milestone indicators
- Visual 3 fix: Proper year spacing with current ratio overlaying bars

**`generate_memo_tables.py`** - Table generator for memorandum:
- Creates 6 markdown tables for embedding in executive memo
- Revenue & profitability, cash flow, balance sheet, liquidity ratios
- Investment NPV comparison table
- 10-year summary statistics table

**`create_final_memo_corrected.py`** - Professional memo generator:
- Creates memo-final.docx with Ford branding and Warner Brothers template styling
- Includes cover page with Ford logo, table of contents with bookmarks
- Professional formatting: 1.5 line spacing, 12pt Times New Roman, justified text, 1" margins
- Embeds 5 PNG visualizations next to corresponding tables
- Headers with Ford logo and page numbers in footer

**`create_works_cited_v2.py`** - Works cited generator:
- Creates work-cited.docx with hyperlinked citations to GitHub repository
- Professional formatting matching memo style
- Links to Annual Reports and 10-K filings in repository
- Uses "[View Report]" and "[View 10-K]" hyperlinked text instead of showing URLs

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

1. **Professional Memo**: `memo-final.docx` - Ford-branded business memorandum with embedded tables and visualizations
2. **Works Cited**: `work-cited.docx` - Professional bibliography with hyperlinked GitHub repository citations
3. **Executive Memo Source**: `Ford_Executive_Memo_Outline_Based.md` - Markdown source for memorandum
4. **Presentation**: `Ford_Presentation_Outline_Based.md` - 15 slides + appendices with transformation narrative
5. **Visualizations**: 5 separate PNG files (visual_1 through visual_5) - Enhanced versions with strategic context
6. **Data Export**: `ford_summary_metrics_per_outline.csv` - Key metrics summary
7. **GitHub Pages Site**: `index.html` - Professional web presentation with Ford branding and embedded visuals
8. **Supporting Tables**: Generated via `generate_memo_tables.py` for memo integration

## Critical Ford-Specific Context

### 2018 Strategic Restructuring - Central Narrative
- **Catalyst**: Operating margins declined from 4.7% (2015) to 2.0% (2018)
- **Response**: Segmentation into three business units - Ford Blue (ICE), Model e (EV), Pro (Commercial)
- **Three Phases**: 
  - Phase 1 (2015-2018): Declining Performance
  - Phase 2 (2018-2020): Strategic Pivot
  - Phase 3 (2021-2024): Transformation Payoff
- **Validation**: 2021's $17.9B net income proved strategy success

### Financial Analysis Considerations
- **Ford Credit Impact**: Total debt figures are inflated by Ford Credit financing operations - distinguish between Automotive and Credit segments
- **Cyclical Patterns**: Automotive industry exhibits strong cyclical performance - losses in 2020 (pandemic) and 2022 are part of normal patterns
- **2021 Outlier**: $17.9B net income includes special items (Rivian investment gains, pension remeasurement)
- **Margin Reality**: Operating margins averaging 2.4% reflect industry norms - thin but consistent with automotive manufacturing

### Visualization Requirements
- **Visual 3 Critical Fix**: Use actual year values (not indices) for x-axis, current ratio must overlay bars (zorder=15)
- **Chart Sizing**: 14x8 for Visual 3, 12x7 or 14x8 for others - balance readability with space
- **Legend Positioning**: Combined legends to avoid overlap, strategic bbox_to_anchor positioning
- **Narrative Enhancement**: Phase backgrounds, strategic annotations, milestone markers on all charts

## Data Structure Notes

The Excel file contains 18 columns of annual financial data (2015-2024):
- Revenue, COGS, Operating Income, Net Income, EBIT
- Balance sheet items (Assets, Liabilities, Equity, Cash, Debt)
- Cash flow metrics (Operating CF, Capex)
- Industry-standard billions ($B) formatting

## Narrative Integration Strategy

### Transformation Story Arc
The entire analysis is framed around Ford's 2018 strategic restructuring:
- **Memo**: Opens with restructuring context, weaves three-phase story through each section
- **Presentation**: Slide 3 introduces transformation, subsequent slides reinforce narrative
- **Visuals**: All 5 charts include phase markers, strategic annotations, milestone indicators
- **Website**: Professional presentation with embedded visuals supporting the story

### Key Narrative Elements to Maintain
- Always frame 2018 as strategic response to declining margins (not just a reorganization)
- Emphasize three distinct business strategies (Blue=cash, Model e=growth, Pro=stability)
- Position 2021 results as validation of strategy (not just lucky gains)
- Present Investment A recommendation as aligned with 20-year transformation timeline

## Document Generation Workflow

### Creating/Updating Professional Documents
1. **Professional Memo**: Use `create_final_memo_corrected.py` to generate Ford-branded `memo-final.docx`
2. **Works Cited**: Use `create_works_cited_v2.py` to generate `work-cited.docx` with hyperlinked citations
3. **Visualizations**: Run Python scripts to generate PNG files - enhanced narrative version recommended
4. **Tables**: Use `generate_memo_tables.py` to create markdown tables for memo embedding
5. **Data Export**: Main analysis script outputs `ford_summary_metrics_per_outline.csv`
6. **GitHub Pages**: Update `index.html` with Ford branding and professional presentation

### Ford Branding Implementation

**Brand Colors**:
- Primary Ford Blue: #003366
- Secondary Ford Blue: #0066cc
- Gradient backgrounds: `linear-gradient(135deg, #003366 0%, #0066cc 100%)`

**Logo Requirements**:
- `Ford_Motor_Company_Logo.png` must be present in project root
- Used in both Word documents (3" width) and GitHub Pages
- Remove any CSS filters that affect logo visibility

**Document Styling Requirements**:
- Font: Times New Roman, 12pt
- Line spacing: 1.5
- Margins: 1" all sides
- Text alignment: Justified
- Headers/footers with Ford branding
- Table of contents with bookmarks
- Cover page with Ford logo

**Hyperlink Implementation**:
- Works cited uses hyperlinked text instead of showing full URLs
- Format: "[View Report]" and "[View 10-K]" linking to GitHub repository files
- Maintains professional appearance while providing direct access

### GitHub Pages Deployment

**`index.html`** - Professional web presentation:
- Ford-branded styling with gradient headers
- Embedded visualizations and analysis content
- Works cited section with hyperlinked repository citations
- Responsive design with professional layout
- Deployed automatically to: https://kh0pper.github.io/DSCI-5330-Assignment-02/

### Common Tasks
- **Add new financial metrics**: Update calculation section in all Python scripts
- **Modify visualizations**: Focus on `ford_enhanced_narrative_visualizations.py` for best results
- **Update narrative**: Maintain 2018 restructuring as central story across all documents
- **Create professional documents**: Use dedicated Python scripts for consistent Ford branding
- **Update web presentation**: Edit `index.html` with Ford brand colors and styling
- **Regenerate documents**: Run document creation scripts when content changes

### Git Operations
- Do not include Claude co-authorship in commits
- Focus on descriptive commit messages for document updates
- Ensure Ford logo and all assets are committed to repository

This project structure enables rapid financial analysis regeneration while maintaining consistency with academic assignment requirements and professional Ford-branded presentation standards.