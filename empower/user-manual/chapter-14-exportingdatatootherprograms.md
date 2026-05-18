# Chapter 14: Exporting Data to Other Programs

*From the Empower User Manual*

---

## Chapter 14

Exporting Data to Other Programs

Empower has the ability to export the data displayed in the Sort Window in Microsoft Excel format, for further use in Excel or other applications that support the Excel format. This section and the several following describe these export functions.

(Note: Empower also has the ability to export and import data in formats other than Excel, for Electronic Data Interchange [EDI] purposes. These export and import functions are described in Chapter 16.)

## 14.1 Export Sort Window

The user can export the data in the Sort Window by invoking the File > Export Sort Window menu command. This will create and download to the user's machine a file in Excel format containing the data currently in the Sort Window. The data in the export file will, therefore, be limited to the rows resulting from the currently applied filter. All such rows will be exported even if they are currently scrolled out of view in the Sort window. It will properly generate the color codes and trend arrows.

In Windows, depending on what browser you use, you will be presented with an option to save the file, or open the file directly in Excel. On the Mac OS X, the file will be automatically downloaded to your Download folder. (The Export Sort Window does not work on the iPad due to the advanced formatting in the export file.)

Figure 14.1 shows a sample of the file produced by the Export Sort Window command as opened in Excel.

**Figure 14.1: Excel Export Sample**

Note that this command does not export the WBS Tree mode indicators. (These are the little graphics elements that look like a plus or minus in a box, used to indicate whether a particular node in the tree is showing all its children [expanded], or hiding all its children [collapsed].)

## 14.2 Export DQI Matrix

The File > Export DQI Matrix command (where "DQI" stands for "Data Quality Indicator") will generate an Excel-compatible file for all elements displayed in the Sort Window with an indication of which DQI criterion (if any) was breached for each element. It is recommended that you use a DQI view with a limited number of fields (WBS Number, CAM, LL, etc.) when exporting the DQI Matrix. The fields exported can be used for grouping and filtering in a Microsoft Excel pivot table. The DQI Matrix will include criterion breach information for each element for the data period identified in the Dataset.

**Figure 14.2: Raw DQI Data Viewed in Spreadsheet**

Figure 14.2 shows the exported DQI data file opened in OpenOffice Calc, a spreadsheet program compatible with Microsoft Excel. The spreadsheet has a row for each element and a data quality criterion is shown in each column. For the earned value data, a 1 in the intersection of the WBS and the criterion column indicates that the WBS tested "true" for that criteria. (For example, in Figure 14.2 the BCWS-cum was greater than the BAC for element 6100.) For schedule-related tests, the number can be greater than one at the intersection of the WBS and criterion. This is because a single element (a work package) can have many schedule activities. The intersection of the WBS element and the "High Duration" criterion could have multiple hits, if multiple schedule activities for that account tested true for that criteria. In Figure 14.3, a number of spreadsheet columns have been hidden in order to bring into view columns showing schedule-related breaches of DQI criteria. For example, in element 3200 there are eight activities with no successors defined.

**Figure 14.3: Raw DQI Data Viewed in Spreadsheet, Showing Multiple Schedule-Related DQI Breaches**

The recommended use for the raw data file is to create a pivot table. In the pivot table, place the WBS elements in the pivot table "Row Labels" and criteria in the "Values" area (see Figure 14.4).

If desired, place LL as a Pivot Table Filter. Also, if you wish to group by CAM, insert CAM above WBS Elements in the Row Labels.

**Figure 14.4: Creating a Pivot Table in Excel**

Figure 14.5 below shows a pivot table resulting from the raw data exported from Export. (Some rows have been hidden to bring the element 6100 and the headings closer together in the figure.)

**Figure 14.5: Pivot Table**

## 14.3 Export DQI Trends

The Export DQI Trends command will generate an Excel-compatible file for the selected element that displays what, if any, DQI criteria were breached, broken out by time periods. If this is selected at the total contract level, it will also generate a separate page with a summation of DQI breaches at the lowest level. Figure 14.6 shows a sample export of the DQI trends for element 3200.

**Figure 14.6: Sample Trends Export**

## 14.4 Export DQI IMS

The Export DQI IMS command exports task data to an Excel spreadsheet that displays the DQI schedule tests per-task, instead of grouping and totaling them per element as in the DQI and DQI Trends reports and DQI Trend download. Clicking on the command will create a file named dqi_ims.xlsx in your browser's normal download location.

The figure below shows a small portion of the resulting export.

**Figure 14.7: Sample DQI IMS Export**

## 14.5 Export Audit Relationships

The Export Audit Relationships command exports task data to an Excel spreadsheet that displays the DQI schedule tests per-relationship, instead of by task as in the DQI IMS download. Clicking on the command will create a file named dqi_rel.xlsx in your browser's normal download location.

The figure below shows a small portion of the resulting export.

**Figure 14.8: Sample DQI Relationships Export**

Notice that line 2 indicates which Audit tests use the DQI, while line 3 indicates the DQI number. The description of each DQI can be found on line 5. For ease of use, the DQIs in this download will be listed first by Audit test (if present).

## 14.6 Export Audit Dollar Tests

The Export Audit Dollar Tests command exports Earned Value and DQI data for specific dollar value Audit tests to an Excel spreadsheet called dqi_dol.xlsx. This allows you to filter in Excel to find the numerator and denominator values for each of these tests. The second tab provides filtering notes for each test. The tests displayed will depend on which test sheet is used for the currently selected contract. This export is not available for cross-contract sums. For values like BcwsCum, both the original value and the absolute value of the field are included in this export. Absolute value fields are indicated by ABS in the title of the column.

The figure below shows a small portion of the export with some columns hidden.

**Figure 14.9: Sample Audit Dollar Tests Export**

## 14.7 Export Chart Data

The File > Export Chart Data command will generate an Excel-compatible raw data file for the selected element and chart (including the Gantt chart). You can use this file to create a custom chart in Microsoft Excel or any other compatible application.

Figure 14.10 shows a sample export of chart data for the project element 2200.

**Figure 14.10: Sample Chart Data Export Results**

## 14.8 Export Report HTML

This command downloads the report currently displayed in the report pane as an HTML file. You can then insert this file in a Word document, Excel spreadsheet, or any other file that allows you to insert HTML files. You can, of course, also open the file in a browser. (This command only works with internal reports, i.e., reports displayed in Empower's report pane, not with external reports.)

There is a wrinkle to be noted when inserting such an HTML file into Excel. Excel is zealous about converting anything that looks like a date into a date in its own format, and sometimes it will not be the date you intended. For example, if you have a column heading like "AUG 03", meaning August 2003, Excel will turn this into the 3rd of August in the current year. You can prevent this by setting your contract to display a four-digit year by changing the date format (e.g., "%b%Y"— note the capital "Y"). You can learn more about date formats in the User's Manual, Frequently Asked Question, "What are the formats for dates and fiscal year end?" You change the date format for a calendar in the Date Fmt column of the Calendars tab on the Calendars spreadsheet (which you obtain with Admin > Download Data File command).

Excel will sometimes convert something that wasn't intended to be a date at all into a date. For example, in the Count column of the Schedule Assessment Report, there will likely be a quotient. If the quotient could be interpreted as a date, Excel will do so. For instance, if the quotient was 7/9, Excel will think you meant the 9th of July (again, in whatever the current year is). The easiest way to fix this is to edit the spreadsheet in Excel: enter the intended quotient, prefixed with a single apostrophe, which tells Excel to take what follows literally. So if you wanted 7/9, you would enter '7/9.

## 14.9 Export Open Windows

This command exports any open charts or reports from Empower, including any external charts and reports. This can be useful, for example, if you want to export all of the charts and reports used by a dashboard. Charts are exported as PNG files while reports are exported as HTML.

Each chart or report is downloaded as an individual file, with a small delay between each download. The default for this delay is two seconds, but it can be customized via an Empower configuration setting, see the technical note "The Empower Configuration File," available on our support website http://encoreanalyticsllc.freshdesk.com/support/solutions for more information.

If you do not immediately see all of the downloads that you expect after clicking "Export Open Windows," wait before attempting to download again; you may just have a longer delay setting.

It should be noted that the Gantt chart will not be downloaded if you have it opened in an external window. The Gantt chart can only be downloaded if it is open in the internal tri-pane view, and it is downloaded as an Excel file.

## 14.10 Export Audit Matrix

Exporting the Audit Matrix gives you the answer to the question, "How do I find out which elements or tasks tripped a test metric in the Audit Metrics report?" (Recall that you can customize the name of this report, and the customization will be reflected in the name of this menu item, so it might be, for instance, "Export DCMAA Audit Matrix." See Section 9.22.)

Note that you must recalculate your contract with the "Calculate Audit metrics" option checked before exporting the Audit Matrix.

The command Export Audit Matrix will result in a spreadsheet like the one shown in Figure 14.12:

**Figure 14.11: Audit Matrix**

This figure tells us that WBS element 3400 triggered test 03A101a, as well as the other elements that are relevant for that test. There will be as many rows for a given test as there are elements that are relevant elements or tasks for that test. Some of the rows will be marked as "Flagged," indicated by an 'x' in the Flagged column.

**Figure 14.12: Audit Matrix Tripped Tasks**

Beginning in row 163 of the spreadsheet, we see a series of tasks that tripped test 06A205a. The figure shows that the tasks with UIDs of 35, 47, 49, etc. all associated with WBS element 3200, tripped this test.

Filtering to a specific Test ID will result in the number of rows counted in the Audit Metrics report denominator for the test.

**Figure 14.13: Denominator rows for 03A101a**

Adding another filter, this time on Flagged, results in the number of rows matching the Audit Metrics report numerator for the test.

**Figure 14.14: Numerator rows for 03A101a**

The Audit Matrix export also includes a second tab, called "Summary." This tab contains the content of the Audit Metrics Report for automated tests, allowing users to use the Audit Matrix as a standalone file to do validation without needing to access Empower at the same time.

**Figure 14.15: Audit Matrix Summary Tab**
