# Custom Charts Reports Brittany Hayes

*Source: Custom_Charts_Reports-Brittany Hayes.pptx*

---

## Slide 1: Empower

Custom Charts and Reports Using External Data
July, 2018

---

## Slide 2: Outline

- Adaptive Touch
- Custom Chart Example
- Who Charged Chart overview
- Chart Code
- Custom Report Example
- Who Charged Report overview
- Report Code

---

## Slide 3: Adaptive Touch

Empower allows for the creation of highly customizable charts and reports

"Adaptive Touch" (AT) charts and reports are intended to combine data from Empower with data from an external source

---

## Slide 4: Adaptive Touch

AT charts and reports use a file containing code to generate the chart or report

Any server side language can be used, as long as it follows Common Gateway Interface (CGI) protocol

The code should generate one of the following:
- A valid JSON string
- Standard HTML

---

## Slide 5: Adaptive Touch

Data used in your AT chart/report can come from any source, as long as the data can be accessed from your Empower application server

External data can be accessed in different ways:
- Parsing a .txt file
- Querying a database
- Etc.

---

## Slide 6: Empower

Custom Chart Example

---

## Slide 7: Overview

AT charts must return a valid JSON string accepted by Empower's chart plugin

JSONLint.com: a tool for checking JSON validity

---

## Slide 8: Who Charged Chart

---

## Slide 9: Overview

The "Who Charged" chart is a bar chart showing the hours charged by each resource for an element over the periods of a contract

We will need three files for this chart:
- Who-Charged.txt
- Who_Charged_Chart.txt
- ch_getcharge.cgi

---

## Slide 10: Who-Charged.txt

---

## Slide 11: Who-Charged.txt

- **Contract**: the contract name in Empower
- **WBS**: the WBS number in the contract
- **Name**: Who or What charged
- **ID**: a unique ID assigned to each name. This can be omitted if Name is unique.
- **Date**: Period end date of the charge
- **Hours**: the actual hours charged in the period.

---

## Slide 12: Who_Charged_Chart.txt

---

## Slide 13: Who_Charged_Chart.txt

Plain text file imported on the client side with "File > Import User Items"

Use this file to:
- Tell Empower which file contains the code for the chart
- Specify the data you want from the Empower database

---

## Slide 14: Who_Charged_Chart.txt

Placeholder syntax specifies the data we want from Empower

- `|ContrName|` returns the name of the current contract
- `|WbsNum|` returns the WbsNum of the current element
- The `|Meta|BeginLoop|cd|` construct loops over the periods in the selected contract, returning the EndDate for each period

---

## Slide 15: Empower

Chart Code

---

## Slide 16: Chart Code

Get the parameters from Empower

---

## Slide 17: Chart Code

Parse the input file, skipping any lines that are not relevant

---

## Slide 18: Chart Code

Rearrange the data so that it is in the format Highcharts expects

---

## Slide 19: Chart Code

Set the chart title and subtitle, using the values that were passed from Empower

Note: the "extra" variable is available to all charts and reports. It contains helpful information like the current unit, display scale, a preformatted title, etc.

---

## Slide 20: Chart Code

Construct the "options" object

---

## Slide 21: Chart Code

The "options" object has many options for customization

- https://www.highcharts.com provides documentation on available options for the charting tool
- https://jsfiddle.net is a useful tool for seeing how your chart will look and testing out different Highcharts settings

---

## Slide 22: Chart Code

Return the JSON string

---

## Slide 23: Empower

Custom Report Example

---

## Slide 24: Overview

AT reports must return standard HTML

---

## Slide 25: Overview

The "Who Charged" report compares current and cumulative ACWP from Empower with the data from an external source

We will need three files for this report:
- Who-Charged.txt
- Who_Charged_Report.txt
- getcharge.cgi

---

## Slide 26: Who_Charged_Report.txt

---

## Slide 27: Who_Charged_Report.txt

Plain text file imported on the client side with "File > Import User Items"

Use this file to:
- Tell Empower which file contains the code for the report
- Specify the data you want from the Empower database

---

## Slide 28: Who_Charged_Report.txt

Placeholder syntax specifies the data we want from Empower

- `|ContrName|` returns the name of the current contract
- `|EndDate|[%Y-%m-%d]|` returns the End Date for the current period in the format "yyyy-mm-dd"
- `|AcwpCum|[n5]|%2%|` returns the cumulative Acwp in numeric format with five decimal places in hours

---

## Slide 29: Empower

Report Code

---

## Slide 30: Report Code

Get parameters from the Empower client

---

## Slide 31: Report Code

Convert the input file if necessary

---

## Slide 32: Report Code

Parse the input file

---

## Slide 33: Report Code

Generate the rows of table

---

## Slide 34: Report Code

Format data for the report

---

## Slide 35: Report Code

Return standard HTML

---

## Slide 36: Resources

For more information and examples, see this document on our support site under "Solutions":
Writing Custom Charts and Reports

Support Site: encoreanalyticsllc.freshdesk.com

---

## Slide 37: Resources (cont.)

- https://www.highcharts.com
- https://jsonlint.com
- https://jsfiddle.net

---

## Slide 38: Questions?
