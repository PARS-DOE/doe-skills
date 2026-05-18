# Chapter 9: Standard Reports

*From the Empower User Manual*

---

## Chapter 9: Standard Reports

Empower can display two types of reports: standard and custom. Empower provides a rich set of standard reports, which are installed with the core application and are found on the main Reports menu. This chapter discusses the standard reports.

Custom reports are developed by Empower users or consultants to meet site-specific reporting needs, but are implemented and displayed in the same way as standard reports. Custom reports have their own submenu on the Reports menu, and are discussed in the next chapter.

### Figure 9.1: Reports Menu

Figure 9.1 shows the Reports menu.

---

## 9.1 Opening Reports in External Windows

Usually, reports are opened in Empower's Report Window. However, you can choose to open many reports in an external window. You might want to do this to gain more screen real estate for a densely populated report. Another reason for opening a report in a separate window is that using the browser's print functionality is a simpler way to print a report than copying the report from Empower's Report Window and pasting it to a word processor, then using the word processor to print.

To open a report in an external window, press and hold a modifier key (to be described in a moment), then click on the report name.

Different browsers treat the modifier keys in different ways; some browsers will co-opt a given modifier key to perform some browser function, meaning that the key is not available to be used by an application. Empower handles that by recognizing any of the following three as the key to open a report or chart externally:

- Control
- Shift
- Alt/Option (Alt on Windows, Option on Macs)

If one of those keys doesn't open reports externally on your browser, try the next in the list until you find one that works, and then use it all the time.

If you are opening a custom report using the Open/Edit dialog (see Section 10.1), instead of clicking on the report name from the menu, the procedure is similar. Just select the report you want to open from the list of reports in the dialog, then hold down the modifier key and click the Open button.

This ability to open reports externally is available for both standard and custom reports. However, reports that are written to be external reports (i.e., reports containing their own `<html>` tag) are always opened externally without the need to press a modifier key.

As with opening charts in external windows, you can have multiple windows open at the same time, each displaying a different chart or report (see Section 7.1 for more details).

---

## 9.2 AI Narrative Report

The AI Narrative report is a rule-based report that converts the project performance metrics to a sentence-based analysis. Figure 9.2 displays a portion of the AI Narrative report for element 3600 in the MOH-2 sample contract.

### Figure 9.2: AI Narrative Report

---

## 9.3 Six Period Summary

The Six Period Summary displays the last six periods of raw performance data and the resulting calculated metrics.

Cumulative values are denoted by the abbreviation or acronym without a trailing "_c" (e.g., "BCWS"). Values for a given period are called incremental or current values, and denoted by a trailing "_c" (e.g., "BCWS_c"). Think of the "c" in the suffix as meaning "current."

The report is grouped by current/incremental values, cumulative values, values at completion, and statistical forecast values. The report is rather long, so we show it spread out over three figures. Figure 9.3 displays the top portion of the Six Period Summary report.

### Figure 9.3: Six Period Summary Report, Top Third

Next is the middle part of the report. Note the CPLI (Critical Path Length Index) line; CPLI is one of DCMA's 14-Point Assessment Metrics. In this case, the CPLI of 0.773 falls short of the 1.0 target value.

### Figure 9.4: Six Period Summary Report, Middle Third

And here is the rest of our example Six Period Summary Report:

### Figure 9.5: Six Period Summary Report

---

## 9.4 Validity Report

The Validity Report computes data checks against the earned value data. The severity of failed validation checks is color-coded as:

- Red (Warning)
- Yellow (Caution)
- Gray (Informational)

The Validity Report also provides information as to whether a particular forecast is reliable based on certain data conditions (i.e., a divide by zero error in the formula). Figure 9.6 displays a sample Validity report. Note that the failed validation checks are grouped by severity.

### Figure 9.6: Validity Report

---

## 9.5 Data Quality Indicators (DQI) Report

The DQI report is based upon a number of documents, which are displayed in the report header. Data Quality Indicators are checked for the earned value data, schedule data, reasonableness of the forecast, and cost/schedule integration. Use the DQI field in the Sort Window to identify accounts that have DQI issues. The current database does not contain schedule activity constraint information, so the DQIs do not identify constraint issues (i.e., Must Finish On dates) in the schedule.

Figure 9.7 displays a sample DQI report.

### Figure 9.7: DQI Report

---

## 9.6 Six Period DQI Trends Report

The Six Period DQI Trends Report shows the number of DQI breaches in various categories for each of the last six periods. In Figure 9.8, for instance, we see that for element 3200, that the CPI-TCPI < −0.1 criterion has been breached each of the last four months, while for the latest period, there were 19 tasks with negative float.

### Figure 9.8: Six Period DQI Trends Report

---

## 9.7 Schedule Assessment Report

The Schedule Assessment Report (Figure 9.9) displays color-coded performance vs. target performance for a variety of schedule metrics. Figure 9.9 shows a sample of this report.

### Figure 9.9: Schedule Assessment Report

---

## 9.8 Schedule Execution Metrics Report

The Schedule Execution Metrics Report (Figure 9.10) displays calculated schedule metrics over a six month period, including six month average and trend slope values. Note that these fields are set during recalculation. The slope fields referenced in the report require a linear regression calculation; linear regression calculations can be time-consuming, so they are not enabled by default. To enable linear regression calculations your site must have the LINREG server setting enabled. (See the technical note, "The Empower Configuration File," available on our support website http://encoreanalyticsllc.freshdesk.com/support/solutions for more details.)

Figure 9.10 shows a sample of this report.

### Figure 9.10: Schedule Execution Metrics Report

If we wanted to drill down into which specific tasks are being counted for the numerator and denominator fields in this report, we could create a view to use in "Task Mode" (see 5.8 for more information) and filter on the field of interest.

To do this, we could create a Gantt view using the view editor, choosing the "SEM IMS" column group to find the task-level calculations for the fields in the SEM report.

### Figure 9.11: Schedule Execution Metrics View Editor

After applying the view in "Task Mode," we can filter the columns to find which tasks are included in the numerator/denominator values. For example, say we wanted to find out which four tasks are counted in "HitPlanCmp" for element 1000 (notice that HitPlanCmp=4 for JAN17 in our earlier screenshot). To find these tasks, we filter the HitPlanCmp column to find values greater than 0.

### Figure 9.12: Schedule Execution Metrics View

---

## 9.9 SEM AI Narrative Report

The Schedule Execution Metrics AI Narrative report is a rule-based report that converts the schedule execution metrics to a sentence-based analysis. Figure 9.13 displays a portion of the SEM AI Narrative report for element 1000 in the MOH-2 sample contract.

### Figure 9.13: SEM AI Narrative Report

---

## 9.10 Task Detail Report

The Task Detail report displays detailed information for the selected task in the Gantt Chart. In order to display information, the Gantt chart must be open. Clicking a different row of the Gantt chart will display information for the selected task. Figure 9.14 shows a sample of the beginning of the report.

If the Gantt chart has not been opened for the current contract, the report will display the message "No task selected."

### Figure 9.14: Task Detail Report

---

## 9.11 Elements of Cost Report

This report (Figure 9.15) shows the elements of cost for the selected element in the Sort Window.

### Figure 9.15: Elements of Cost Report

For a given unit to appear in this report as an Element of Cost, its EocType must be set to 1 for each contract that uses the unit as an EOC; see Section 16.9.15 on how to do this.

---

## 9.12 Time-Phased Plan Report

This report (Figure 9.16) shows Bcws, Bcwp, Acwp, and Etc values over time for the selected element and its direct children. Data is shown for dollars, hours and units marked as EOC units for the selected contract.

### Figure 9.16: Time-Phased Plan Report

Note that due to the nature of this report, loading may be slower for elements with large numbers of children.

---

## 9.13 BCWS Volatility Report

This report (Figure 9.17) shows BCWS values over time, providing an indication of how much they have changed (or remained the same).

### Figure 9.17: BCWS Volatility Report

---

## 9.14 ETC Volatility Report

This report (Figure 9.18) shows ETC values over time, providing an indication of how much they have changed (or remained the same).

### Figure 9.18: ETC Volatility Report

---

## 9.15 Format 3 Volatility Report

This report (Figure 9.19) shows F3 values over time, providing an indication of how much they have changed (or remained the same).

### Figure 9.19: Format 3 Volatility Report

---

## 9.16 Executive Summary Report

This report (Figure 9.20) presents an overview of the contract. Since the report applies to the whole contract, it remains the same no matter which element is selected (just like the Contract Performance Chart). This report is rather long; the figure below shows the first part of it.

### Figure 9.20: Executive Summary Report (Partial View)

---

## 9.17 CFSR Reconciliation Report

This report (Figure 9.21) shows the Contract Funds Status Report. Section 16.9.14 explains how to enter the data used to generate this report.

### Figure 9.21: CFSR Reconciliation Report

---

## 9.18 EVMS/IMS Integration Report

This report (Figure 9.22) shows the agreement or differences between the values for baseline start and finish dates in the schedule system (IMS) and the equivalent dates in the cost system (EVMS). EVMS data (BCWS and ACWP/ETC) is tagged to a period, not a specific day. Schedule dates that do not fall between the corresponding cost dates, which are in the column immediately to the right of the schedule date, are highlighted in red.

### Figure 9.22: EVMS/IMS Integration Report

---

## 9.19 WAD Baseline Integration Report

This report (Figure 9.23) shows integration (or lack thereof) of Work Authorization Documents (WAD) and data in the earned value system. It compares the BAC, CAM name, and baseline dates from the WAD to the IMS and EVMS data.

### Figure 9.23: WAD Baseline Integration Report (Partial View)

---

## 9.20 WAD Revisions

This report (Figure 9.24) shows revisions and any entered scope information for WADs attached to the currently selected unit.

### Figure 9.24: WAD Revisions (Partial View)

---

## 9.21 WAD Narrative

This report (Figure 9.25) shows scope information for WADs attached to the currently selected unit for the most recent revision.

### Figure 9.25: WAD Narrative

---

## 9.22 Audit Attributes and Tests Reports

The Audit Metrics report and Audit Trends report by default show the results of quality checks specified in DCMA or DOE Attributes and Tests Guidelines. They also map test results back to the Electronic Industries Alliance Standard-748 EVMS (EIA-748), known as the "32 Guidelines."

Note that:
- Out-of-tolerance values are presented against a light red background
- Values that are non-zero but within tolerance have a yellow background
- Values of zero have a green background

### 9.22.1 Audit Metrics Report

This report provides a detailed view of the Audit test results for the currently selected period.

Figure 9.26: Audit Metrics Report (Partial View)

Some of the tests shown in audit reports are calculated from data which is not normally available to Empower and thus must be provided manually. Here we describe how to set these manual values.

We begin by looking at the beginning of an Audit report, shown in Figure 9.27:

### Figure 9.27: Audit Report Output Showing Manual Tests

Note the asterisks in the M, Value, Total, and Percent columns: this means that this test (01A101a) is a manual test, and the values necessary to calculate the test metric must be input manually. Once this has been done, you will see numbers in the Value, Total, and Percent columns of the report, but the asterisk will remain in the M column to remind you that this test is based on manually entered values.

### 9.22.2 Audit Trends Report

This report shows the results of your audit tests over six periods, providing an overview of the Audit test results for the selected contract.

### Figure 9.28: Audit Trends Report (Partial View)

### 9.22.3 Entering Audit Values

To enter values manually, we download the Audit Test Notes and Values spreadsheet, specifying the contract and period, as shown in Figure 9.29.

### Figure 9.29: Downloading the Audit Values Spreadsheet

In the first sheet of the resulting spreadsheet, we add the numerator (Num) and denominator (Denom) values that will be used to calculate the test value, and put an "a" in the Action column. (We use "a" — for add — because we are adding a row for each row we edit. If there were values in the Num and/or Denom columns, perhaps because updated values have become available for this period, we would enter the new values and put "c" in the Action column, as we would now be changing an existing record.) On the second sheet, the Note field can be used to add details or explanations about the manual test we are adding, and the Link field can be used to add a link to data external to Empower.

In Figure 9.30, we have added values for two tests, 01A101a and 03A103b.

### Figure 9.30: Entering Manual Audit Values

### Figure 9.31: Entering Manual Audit Notes

Next we upload the AuditVals spreadsheet and recalculate. Opening the Audit Metrics report, we see the results of our labors:

### Figure 9.32: Manually Entered Values for Test 01A101a

### Figure 9.33: Manually Entered Values for Test 03A103b

Note the asterisk denoting manual tests.

Clicking the "Note" column header or a "..." entry in the column will expand the note, as we see in Figure 9.34. Clicking "Note" again or clicking the note text itself will collapse the Note column.

### Figure 9.34: Expanding the Note Column

Notice the link icon in the "Test" column. This icon will only appear for tests that have an entry in the "Link" column for the current period. Clicking the link icon will open the "Link" URL for that test in an external window. Depending on your browser, you may need to allow popups in order to use clickable links in the Audit Metrics report. Clickable links are not available in the Audit Metrics Report if it is opened as an external report or for cross-contract summary elements.

Notes and links can also be added to automatic tests. To add a note or link to an automatic test, download the Audit Test Notes and Values spreadsheet like before, specifying the contract and period, as shown in Figure 9.35

### Figure 9.35: Downloading the Audit Values Spreadsheet

In the "AuditNotes" tab of the resulting spreadsheet, we can add a note to an automatic test by putting text in the "Note" column and adding an "a" to the Action column. If we wanted to add a link, we would put text in the "Link" column and add an "a" to the Action column. If we wanted to change a note or link that already existed, we would use a "c" instead of "a" in the action column. If there is already a note or link for a test, you should use "c" in the action column.

### Figure 9.36: Entering Automatic Audit Notes

After uploading the spreadsheet and recalculating, we see our note when we open the Audit Metrics report:

### Figure 9.37: Note for Automatic Test 03A101a

The Audit reports are highly customizable. For more information on this, see the Empower technical report, "Empower's Audit Report," available on our support website (http://encoreanalyticsllc.freshdesk.com/support/solutions).

---

## 9.23 VAR Narrative Report

The VAR report displays the narrative text entered in the VAR entry screen. If edits to the VAR inputs were made with change tracking enabled, the text will be shown in different colors. Hovering over the text will display a Tool Tip with the Empower username of the person who edited the text and a time/date stamp. Figure 9.38 shows a sample VAR report with the change tracking turned on. Note the ToolTip indicating changes made by user Bob on 12/7/2012.

### Figure 9.38: VAR Narrative Report Showing Change Tracking

---

## 9.24 User Narrative Report

The User Narrative report is similar to the VAR report; it displays the narrative text entered in the User Narrative entry screen.

---

## 9.25 EAC Narrative Report

The EAC Narrative report is similar to the VAR report; it displays the narrative text entered in the EAC Narrative entry screen.

---

## 9.26 Scope of Work (SOW) Report

The Scope of Work (SOW) report is similar to the VAR report; it displays the narrative text entered in the Scope of Work entry screen.

---

## 9.27 Banded Narrative Reports

The Banded Narrative submenu has four reports, corresponding to the VAR, WAD, User, EAC, and SOW narrative reports. However, the "banded" versions of these reports will sync to the current state of the sort window.

### Figure 9.39: Banded Narrative Menu

If you filter in the sort window, a "banded" report will only display narrative reports for the elements displayed in the sort window.
