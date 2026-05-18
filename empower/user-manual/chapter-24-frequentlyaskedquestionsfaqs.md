# Chapter 24: Frequently Asked Questions (FAQs)

*From the Empower User Manual*

---

## 24.1 How do I use the data in my Microsoft Access MDB files?

wInsight allowed standalone use by using the database engine of Microsoft Access to use database files located on the user's own computer, instead of the more typical client-server model where the database resided on central server.

You can use any data you may have in Microsoft Access database files (extension .mdb) by using wInsight to export the data to a wInsight archive, then using Empower's Import EDI File function (Section 16.1) to import the wInsight archive and store it in an Empower database. This works whether you are running standalone Empower or client-server Empower.

## 24.2 What browsers are compatible with Encore Empower?

See section 22.4 of this document.

## 24.3 How do I import cost data?

To import cost data use the Admin > System > Import EDI File command. See Section 16.1 for more details.

## 24.4 How do I import schedule data?

To import schedule data use the Admin > System > Import EDI File command. See Section 16.1 for more details.

## 24.5 Why don't I see all of the linked tasks that I expect for an element?

Most likely the tasks that you don't see have bad or missing links. Check for an element called "[UnlinkedTasks]" in your sort window. Tasks with bad or missing links will be linked to this element during recalculation. See 16.2.15 for details on bad or missing links.

## 24.6 How do I round values to the nearest dollar?

Empower 3.0 introduced a new method of handling units that allows users to track elements of cost (Dollars, and anything measured in dollars) down to the penny. However, the source of the user's data sometimes may not actually be accurate to the penny, and in such cases, users may prefer to round all their EOC data to whole dollars. This FAQ describes how to accomplish such rounding, using the Rescale Values dialog (see Section 16.15.4 for more details on this function).

The process involves dividing by 100, which gets rid of the pennies, then multiplying by 100.

Here are the steps:

1. Open the Admin > Rescale Values dialog.
2. Select the target contract(s).
3. Select target unit(s).
4. Multiply values by 10 to the −2 (that is, put −2 in the text box next to the text "Multiply values for the selected items by 10 to the "). This is where we divide by 100 to get rid of the pennies. Make sure "Adjust Scale" is unchecked. Press the Scale button under the Contract list box (not the one under the Period list box).
5. Click the Rescale Another button.
6. Repeat steps 2 and 3, selecting the same contract(s) and unit(s).
7. Multiply values by 10 to the 2 (that is, put 2 in the text box). This is where we multiply by 100 to get back the same amount in dollars (rounded up if necessary), but with zero cents. Again, make sure "Adjust Scale" is unchecked. Press the Scale button under the Contract list box.
8. Recalculate the target contract(s).

## 24.7 What is the best method for copying charts to PowerPoint?

To download or copy a chart, select the Download button in the chart. Depending upon your browser, it will either download the chart to your "Download Folder" or open another browser window/tab where you can copy the chart.

We have found that the best format for importing into PowerPoint on Windows is SVG, and the best format for PowerPoint on the Mac is PDF.

## 24.8 How do I print or copy a Sort Window?

To print or copy a Sort Window, first export the Sort Window to the Excel format via the File > Excel Export menu selection. Then you may print or copy from Excel (or any compatible spreadsheet) in the normal manner.

## 24.9 How do I print a report?

If you opened your report in Empower's Report Window (the default behavior), copy and paste the report into Word, then print from Word. When copying the report, make sure that you only highlight/select to the final word in the Report Window and do not include the Status Bar.

If you have opened your report in an external window (see Section 9.1), you can simply use your browser's print function.

## 24.10 How do I print a chart?

Use the context menu at the upper right-hand corner of each chart. (See Section 7.6.)

If you have opened your chart in an external window (see Section 7.1), you can simply use your browser's print function.

## 24.11 How do I delete a line from a chart?

In the legend of the chart, click on the data you wish to remove from the chart. (See 7.4.)

## 24.12 Why don't my filters work in the WBS Tree mode?

Filters do work in the WBS Tree mode; however, they work differently than in the non-WBS Tree mode. See Section 4.6 of this document for instructions regarding filters in the WBS Tree mode.

## 24.13 Can I design my own screen layouts in Empower?

Currently the Tripane mode is the only layout supported for Empower's main window. However, you can create custom layouts with external windows for charts and reports using the Dashboard feature (see Chapter 12).

## 24.14 How do I enter numeric or date comparisons for interactive filtering?

Here are the formats for entering numeric or date comparisons in the Filter Bar.

- Equal to: = N
- Not Equal to: <> N
- Greater than: > N
- Less than: < N
- Less or equal: <= N
- Greater or equal: >= N
- Range of values: N1.. N2

## 24.15 How do I filter on color and trend columns?

Here is a quick reference chart of the codes for filtering on the color and trend columns (SV, CV, and VAC):

| Code | Meaning |
|------|---------|
| R    | Red     |
| Y    | Yellow  |
| G    | Green   |
| B    | Blue    |
| U    | Up      |
| D    | Down    |
| F    | Flat    |

When specifying both color and direction, the color code must be given first.

See Section 4.5 for more information.

## 24.16 Why aren't my views showing on the View Menu?

The Global and User View menus show a maximum of 20 views. If you can't find the view you want there, use the View > Apply/Edit command, which lists all the available views in a list box.

See Section 5.2 for more details.

## 24.17 How do I adjust threshold values?

See Section 16.9.12

## 24.18 What are the formats for dates and fiscal year end?

In the Calendar table, using the Download Data and Upload Data commands, you can enter the format you want your dates to be displayed in, and the end of the fiscal year for your contract. Here are the formats for dates.

| Code | Meaning            |
|------|--------------------|
| %Y   | 4-digit year       |
| %y   | 2-digit year       |
| %d   | Numeric day of month |
| %B   | Month name (long)  |
| %b   | Month name (short) |
| %p   | period number      |
| %P   | Short month for period number |
| %f   | 2-digit fiscal year |
| %F   | 4-digit fiscal year |

A leading exclamation point (!) capitalizes the result, as in the first example below.

Here are some examples given the date of January 31, 2004 and the PerNum equal 1:

- "!%b %y": JAN04,
- "%m/%d/%y": 1/31/04
- "P-%Y.%p": P-2004.1
- "%P-%y": Jan-04

For fiscal year end dates, enter the month and day on which the FY ends in the FyEnd field as mm.dd, such as "12.31" or "09.30".

If FyEnd is "09.30", the date of 2004-10-01 with a date format "!%b %y" will display as OCT05 (because October 2004 is in the fiscal year 2005).

## 24.19 How do I edit the Format 5 variance thresholds?

See Section 16.9.12

## 24.20 How do I enter estimates for EAC Narratives?

Use the Inputs > User EAC. See Section 15.1 for the details.

## 24.21 Why aren't elements of cost showing in the EOC report or EOC charts?

Units need to be identified as element of cost units, on a per-contract basis. See Section 16.9.15.

---

## Appendix A: Empower Technical Notes

For Empower's complete listing of technical notes please see our support website:
https://encoreanalyticsllc.freshdesk.com/support/solutions/categories/4000004691/folders/4000017124

---

## Appendix B: Empower Version History

For Empower's complete version history please see:
https://encore-analytics.com/support.html

---

## Appendix C: Writing Templates

This section describes how to modify the templates used for narrative inputs (VAR, SOW, EAC), write your own version of these templates (see Chapter 15), or write templates for narrative or action item emails (see 20.7 and 21.6).

Templates use HTML, so you'll need to be familiar with basic HTML syntax. You can edit template files with any text editor, such as Notepad. Don't use a word processor unless you know how to make the word processor save a file as plain text without any formatting codes.

Template files are made up of two parts, the header and the body. The header is an HTML comment, which gives the name and description of the template, as well as the type of template (VAR, EAC, SOW). Empower uses the type to know which template should be automatically inserted into which kind of narrative.

The body describes the formatting of the report and shows where values from the database will be inserted in the report.

### Template Header Example

First, the header. Consider the listing below. Lines 1–5 are enclosed in HTML comment tags, which means that they will not be printed in the narrative report. The first and last lines of the header (1 and 5 in the example) must be entered exactly as shown.

On line 2, the value next to Name : is the name of the report as it will be displayed by Empower. This is the name you will see in the list shown by the Admin > System > Input Templates command, or by the File > Export User Items command.

In the line beginning with Default, the text VAR tells Empower that this template is to be inserted automatically when you create a new VAR narrative. The text L1 tells Empower to use this template only for a VAR narrative that is for a level 1 element. If the L1 were not present, Empower would insert the non-level 1 VAR template, which is discussed later. Other types of narrative templates are EAC and SOW. If you wanted to use a separate template for VARs that should use an "IPMDAR" template instead of the default VAR template, you would include IPMDAR in the Default line. Similarly, if you wanted to use a separate template for VARs that should use an "PARS" template instead of the default VAR template, you would include PARS in the Default line. A template should only be marked with up to one of IPMDAR or PARS, but not both. You can specify which contracts should use the "IPMDAR" or "PARS" versions of the VAR template by setting VarType, see section 16.9.6 for more information.

```html
<!-- input template
Name : Default L1 VAR Template
Description : Default Level 1 VAR Template
Default : VAR, L1
input template -->
```

### Template Body Example

Now consider the body of the template, beginning at line 6 in the listing below. (Note that some lines, such as line 8, are wrapped to fit the page of this manual.) Here you can put any legal HTML statements. The Level 1 VAR narrative report begins with a table. The first few lines of this table illustrate the syntax for inserting a database value in the report. Note the token (|WbsNum|) in line 8. This is called a placeholder. It tells Empower to look up the WBS number for the current element and insert it in the report where the placeholder is.

Likewise, the token (|SvCur|) in line 12 tells Empower to retrieve the current Schedule Variance for the current element, structure, unit, and period and insert it here.

It is worth noting that the placeholders are only replaced with values from the database when a narrative report is generated; you won't see the substitution in the narrative editor. So if you create a VAR narrative for a given element for a certain period, then open the VAR narrative for editing the next period, the narrative editor will show the placeholder, not the database value.

You might be wondering how you know that SvCur is the name of the database field for the current schedule variance. A quick way to get the names of database fields is to open the Edit View dialog. (See Figure 5.6.) In the Columns list box, you'll see a list of database fields. You can narrow down the list by choosing an appropriate value in the Column Group list box. So by choosing "Earned Value" in the Column Group list box, you'll see only values associated with earned value in the Columns list box, and you won't see, for instance, contract-related columns like "Analyst" or "ContrNum".

(What if you want a SV in other units or from a different period, etc.? Empower's powerful placeholder syntax lets you do this; for details, see the technical note, "Writing Custom Charts and Reports," available on our support website (http://encoreanalyticsllc.freshdesk.com/support/solutions).

```html
<table class="tmpl">
<tr>
<td class="tmpl" width="40%"><span class="tb">
Element:</span> (|WbsNum|) / (|ElemDesc|) <br
/><span class="tb">CAM: </span>(|ProjOff|)</td>
<td class="tmpl tb tc" width="30%">Current Period
</td>
<td class="tmpl tb tc" width="30%">Cumulative to
Date</td>
</tr>
<tr>
<td class="tmpl tb">SCH VAR</td>
<td class="tmpl">(|SvCur|)</td>
<td class="tmpl">(|SvCum|)</td>
</tr>
<tr>
<td class="tmpl tb">SCH VAR %</td>
<td class="tmpl">(|SvpCur|) %</td>
<td class="tmpl">(|SvpCum|) %</td>
</tr>
[...several lines omitted here...]
</table>
```

Recall from Section 15.7.3 that narratives are structured by templates, and that the narrative editor guides you, section by section, through the writing of a narrative. The (|Meta|BeginSection|) and (|Meta|EndSection|) are the magic that accomplishes this. Consider the listing below:

```html
<h4>Contract Summary</h4>
(|Meta|BeginSection|n-cs|N|Contract Summary|Provide a
summary analysis addressing significant problems.
Indicate corrective actions required, including
Government actions. Highlight significant changes since
the previous report.|)
(|Meta|EndSection|)

<h4>Formal Reprogramming Analysis</h4>
(|Meta|BeginSection|n-fr|N|Formal Reprogramming Analysis|
If applicable, identify the authorizing authority and
reason for the formal reprogramming. Discuss how the
change affected the IPMR in regard to cost adjustments
(SV, CV, BAC, MR, UB), and IMS POP.|)
(|Meta|EndSection|)
```

At line 47 we have the section header (<h4>Contract Summary</h4>), which is just basic HTML. Then comes the (|Meta|BeginSection|) token, which tells Empower's narrative editor that a section comes next. The key, n-cs, tells Empower how to tie sections from the input screen to sections in the VAR Narrative Report. Empower stores the VAR narrative text by section, so this key provides the information to tell Empower what text to put in each section of the report, as defined by the template.

Sample keys used in the Empower default templates include:

- n-cs: Contract Summary
- n-fr: Formal Reprogramming Analysis
- n-eac: EAC Analysis
- n-ub: UB Analysis
- n-mr: MR Analysis
- n-ims: IMS Discussion
- n-f3: Format 3 Discussion
- n-F4: Format 4 Discussion
- n-var: Cost and Schedule Variance Analysis
- n-sup: Supplemental Discussions
- n-noir: No Input Required
- m-gen: Manual
- n-sow: Statement of Work
- s-ca: Current SV - Cause
- s-it: Current SV - Impact to Task
- s-ic: Current SV - Impact to Contract
- c-ca: Current CV - Cause
- c-it: Current CV - Impact to Task
- c-ic: Current CV - Impact to Contract
- S-ca: Cumulative SV - Cause
- S-it: Cumulative SV - Impact to Task
- S-ic: Cumulative SV - Impact to Contract
- C-ca: Cumulative CV - Cause
- C-it: Cumulative CV - Impact to Task
- C-ic: Cumulative CV - Impact to Contract
- V-an: Variance at Complete - Analysis

The next entry in the (|Meta|BeginSection|n-cs|N|) token, N, ties the VAR section to the "Category" dropdown for the corresponding Action Items for the selected element. Suppose you clicked "Action Items" in the VAR Narrative Editor while looking at the "Contract Summary" section with the level 1 element for MOH-2 selected in the sort window. The "Add / Edit Actions" dialog box would open, and you would see "N/A" selected under "Category."

If you had a c in this entry instead of N, you would see c - Current CV under "Category" when you opened the "Add/Edit Actions" dialog.

The words Contract Summary identify the section name; they will appear in the Section: drop-down list in the editor. The prompt will appear in the editor just below this drop-down list. Here, the prompt begins with Provide a summary analysis addressing significant problems. Then the end of the section is marked with (|Meta|EndSection|). For good measure, we have included the next section, "Formal Reprogramming Analysis", and the template continues on through the rest of the sections (not shown).

### Non-Level 1 VAR Template Example

Now let's take a look at the non-Level 1 VAR template. Note the absence of L1 in the Default: line of the header (line 4).

```html
<!-- input template
Name : Default VAR Template
Description : Default VAR Template
Default : VAR
input template -->
```

Next comes a table, which we've seen before, so we'll skip over it and move on to describe the emit_if conditional construct.

Line 51 of the listing below says that if the Format 5 variable (placeholder (|Fmt5Var|)) contains an "S", all the text from line 51 to line 78 (i.e, between emit_if and emit_if –>) will be inserted (that is, emitted) into the VAR narrative. You can test for the Format 5 variable including "s", "S", "c", "C", and "V". As you can see, the default non-L1 VAR narrative template includes all five tests.

In the section of the listing below, we see test for a narrative necessary because of a current schedule variance (Format 5 variable="S').

```html
<h4>Impact to the Contract</h4>
(|Meta|BeginSection|c-ic|c|Current CV - Impact to Contract
|Enter the cost impact to the contract.|)
(|Meta|EndSection|)
emit_if -->

<!-- emit_if (contains, (|Fmt5Var|), S)
<h4>Cumulative Schedule Variance: (|SvCum|)</h4>
<table class="tmpl">
<tr>
<td class="tmpl tb">BCWS</td>
<td class="tmpl tb">BCWP</td>
<td class="tmpl tb">SV</td>
<td class="tmpl tb">SV %</td>
<td class="tmpl tb">SPI</td>
</tr>
<tr>
<td class="tmpl">(|BcwsCum|)</td>
<td class="tmpl">(|BcwpCum|)</td>
<td class="tmpl">(|SvCum|)</td>
<td class="tmpl">(|SvpCum|)</td>
<td class="tmpl">(|SpiCum|)</td>
</tr>
</table>

<h4>Cause</h4>
(|Meta|BeginSection|S-ca|S|Cumulative SV - Cause|Enter
explanation of cumulative schedule variance, clearly
identifying the nature of the problem, significant
reasons for schedule variances (i.e., root cause),
including labor rate/usage, material price/usage and
overhead rate issues, as appropriate.|)
(|Meta|EndSection|)

<h4>Impact to Immediate Task</h4>
(|Meta|BeginSection|S-it|S|Cumulative SV - Impact to Task|
Enter the schedule impact to the immediate task/account
.|)
(|Meta|EndSection|)

<h4>Impact to the Contract</h4>
(|Meta|BeginSection|S-ic|S|Cumulative SV - Impact to
Contract|Enter the schedule impact to the contract.|)
(|Meta|EndSection|)
emit_if -->
```

The listing shows emit_if with the contains operator; the operators compares and intersects are also supported. Contact our technical support if you have questions about these operators.

The Meta|Value tag is a construct that allows you to get a single value from a database query, and can be useful with the emit_if operator. You can learn more about this tag in the Empower Technical Note "Writing Empower Custom Reports", available from our support website (http://encoreanalyticsllc.freshdesk.com/support/solutions).

In the listing fragment below, we execute a SQL statement to count the number of Action Items for this element and period that have not been dismissed or moved (that's the bit that begins with select a.ItemID from AiStatus...), then compare that to zero (the compares, >, 0) part, and if the count is greater than zero, we insert the stuff (an HTML table of Action Items) running down to the emit_if –> line.

```html
<!-- emit_if (compares, >, 0, (|Meta|Value|0|select count
(*) from AiStatus a inner join epi on epi.ItemID = a.
ItemID inner join Period p on epi.PeriodID = p.PeriodID
where epi.ElemID = ce_id and p.PeriodID = cd_id and
TypeID = 0 and StateID <= 5|[n0]|))

<h4>Corrective Action Taken/Planned</h4>

<table class="tmpl">
<tr>
<td class="tmpl tb">TITLE</td>
<td class="tmpl tb">CAT</td>
<td class="tmpl tb">PRI</td>
<td class="tmpl tb">% CMP</td>
<td class="tmpl tb">DUE</td>
</tr>

(|Meta|BeginLoop|ai|IDSelect|select a.ItemID from AiStatus
a inner join epi on epi.ItemID = a.ItemID inner join
Period p on epi.PeriodID = p.PeriodID where epi.ElemID
= ce_id and p.PeriodID = cd_id and TypeID = 0 and
StateID <= 5 order by OpenDate, StateID, ItemTitle|)

<tr><td class="tmpl rcgr0" colspan=5></td></tr>

<tr>
<td class="tmpl">(|ItemTitle|:ai:|)</td>
<td class="tmpl">(|Category|:ai:|)</td>
<td class="tmpl">(|Priority|:ai:|)</td>
<td class="tmpl">(|AiStatus|PctCmp|:ai:|[n1]|)</td>
<td class="tmpl">(|DueDate|:ai:|)</td>
</tr>

<tr>
<td class="tmpl tb">STATE</td>
<td class="tmpl" colspan=4>(|State|:ai:|). (|ItemNote|:ai
:|)</td>
</tr>

<tr>
<td class="tmpl tb">ACTION</td>
<td class="tmpl" colspan=4>(|ItemDesc|:ai:|)</td>
</tr>

(|Meta|EndLoop|ai|)

</table>

emit_if -->
```

### EAC Template Example

The standard EAC template looks like a VAR template, except that it only has one section. Here's what it looks like.

```html
<!-- input template
Name : Default EAC Template
Description : Default EAC Template
Default : EAC
input template -->

<table class="tmpl">
<tr>
<td class="tmpl" width="40%"><span class="tb">
Element:</span> (|WbsNum|) / (|ElemDesc|) <br
/><span class="tb">CAM: </span>(|ProjOff|)</td>
<td class="tmpl tb tc" width="30%">Current Period
</td>
<td class="tmpl tb tc" width="30%">Cumulative to
Date</td>
</tr>

<tr>
<td class="tmpl tb">MINIMUM</td>
<td class="tmpl">(|UserMethodMin|)</td>
<td class="tmpl">(|UserEacMin|)</td>
</tr>

<tr>
<td class="tmpl tb">MOST LIKELY</td>
<td class="tmpl">(|UserMethod|)</td>
<td class="tmpl">(|UserEac|)</td>
</tr>

<tr>
<td class="tmpl tb">MAXIMUM</td>
<td class="tmpl">(|UserMethodMax|)</td>
<td class="tmpl">(|UserEacMax|)</td>
</tr>

</table>

<p>

(|Meta|BeginSection|n-eac|N|EAC Analysis|Explain the most
likely, best, and worst case EAC. When the most likely
management EAC differs from that reported on Format 1,
explain the difference.|)

(|Meta|EndSection|)
```

### Action Item Email Template Example

Templates for narrative and action item emails don't have sections. Here is the standard Action item email.

```html
<!-- input template
Name : Action Email
Description : Action Notification Email Template
Default : EMAIL
input template -->

<!DOCTYPE html>
<html>
<style>
body.tmpl { font-family:sans-serif; font-size:8; }
table.tmpl { width:100%; border:1px solid silver; border-
collapse:collapse; }
td.tmpl { border:1px solid silver; border-collapse:
collapse; padding:4px; }
.tb { font-weight:bold; }
</style>

<body class="tmpl">

Dear (|Meta|Recipient|),

<p>

For Period ending (|EndDate|), the following actions
require attention. (|Meta|Note|)

<p>

Regards,

<p>

(|Meta|User|)

<table class="tmpl">
<tr>
<td class="tmpl tb">WBS</td>
<td class="tmpl tb">Title</td>
<td class="tmpl tb">% Cmp</td>
<td class="tmpl tb">State</td>
<td class="tmpl tb">Due Date</td>
<td class="tmpl tb">Past Due</td>
</tr>

<!-- (|Meta|BeginLoop|ai|SyncActionWnd|) -->

<tr>
<td class="tmpl">(|AiStatus|WbsNum|:ai:|)</td>
<td class="tmpl">(|ItemTitle|:ai:|)</td>
<td class="tmpl">(|AiStatus|PctCmp|:ai:|[n1]|)</td>
<td class="tmpl">(|State|:ai:|)</td>
<td class="tmpl">(|DueDate|:ai:|)</td>
<td class="tmpl">(|DaysDue|:ai:|)</td>
</tr>

<tr>
<td class="tmpl">Reject Reason</td>
<td class="tmpl" colspan=5>(|ItemNote|:ai:|)</td>
</tr>

<tr>
<td class="tmpl" colspan=6>(|ItemDesc|:ai:|)</td>
</tr>

<!-- (|Meta|EndLoop|ai|) -->

</table>

</body>
</html>
```
