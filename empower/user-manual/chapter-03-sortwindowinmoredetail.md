# Chapter 3: Sort Window (in more detail)

*From the Empower User Manual*

---

## Chapter 3: Sort Window (in more detail)

The most important and most frequently used commands and options available in Empower have been introduced in the previous chapter. This chapter describes the Sort Window in more detail and systematically covers the Menu Bar and Toolbar.

## 3.1 More About Sorting Rows and Adding Columns

### 3.1.1 Add/Delete Columns

If you wish to add a field to the view, go to the Views Menu and select "Add Column." A list of all fields in the database will be displayed. The selected field will be added to the far right of the Sort Window. See the paragraph below to move the column to the desired location.

The Sort Window shows your data in a tabular, spreadsheet-like format. You control which columns of data are displayed, the order in which they appear, and the width of the columns by choosing a view. Empower comes with several predefined views, and a View Editor that allows you to easily create your own view.

There are some things you can do to make quick changes to the currently applied view without using the View Editor: you can hide some of the columns in the view, and you can reorder the columns.

To hide one or more columns in the view, right click anywhere in the view header. (The view header consists of the row that shows the names of the columns and the row immediately beneath that has the filter boxes.) A popup menu will appear, listing all the columns in the current view, along with a checkbox. The checked items are being displayed. To temporarily hide a column in the view, uncheck the column name. Click anywhere outside the menu to remove the menu. To unhide the column, right click again, and check the box next to the column you wish to display again.

You can reorder the columns in the current view by left-clicking the header of the column you wish to move, keeping the mouse button down, dragging the column to the desired location, and releasing the mouse button.

These changes are temporary; they do not (without a further step) make a permanent change in the current view. You can save the current arrangement with the Views > Edit Sort Window command.

To make more changes to a view or to create a completely new view, see Sections 5.4 and 5.6.

You will also notice that, by default, several columns on the left of the view (Hier, WBS, and Description) remain visible when scrolling horizontally. This is to make it easy to keep track of which element you are looking at when scrolling to the right end of a wide view. (This is called freezing, and can be toggled with the Options > Unfreeze WBS/Desc command; see Section 3.2.2.10.) When scrolling with a track pad, mouse wheel, or tablet using gestures, you must gesture to the right of the frozen columns.

## 3.2 The Menu Bar

The Menu Bar gives access to most of Empower's commands. Some of the more commonly used commands are duplicated, for convenience's sake, on the Toolbar. (A few commands are only available on the Toolbar; these are noted as they occur in the discussion below.)

### 3.2.1 File Menu

The File menu is shown in Figure 3.1 below:

**Figure 3.1: File Menu**

Some of the commands on this menu were introduced in Chapter 2. This section describes the commands in the File menu in more detail.

#### 3.2.1.1 Open Dataset

See Section 2.4.

#### 3.2.1.2 Open eNotebook

An eNotebook is an electronic notebook, a place to gather, store, and update related information in electronic format. Empower supports the integration of eNotebooks with its analytics tools by providing a connection between elements of a project and the related eNotebook.

The Open eNotebook menu item will open the webpage associated with the selected element. This webpage is intended to be the location where CAM eNotebook-type information (such as basis of estimate, work authorizations, variance analysis reports, corrective actions, etc.) that is related to the active element or control account is stored. Whether it launches as a new browser window or new tab depends upon how your browser is configured.

The address (URL) for this eNotebook page is entered in the Empower Elements table via a field called "ENotebook." URLs can be entered for each element in your structure if desired. These entries can only be made by the Empower Administrator.

#### 3.2.1.3 Export Commands

The next few commands on the File menu (Export Sort Window, Export DQI Matrix, Export DQI Trends, Export DQI IMS, Export Chart Data, Export Report HTML, Export Open Windows, Export Audit Relationships, Export Audit Dollar Tests, and Export Audit Matrix) allow the user to export data from Empower in a form that can be used for analysis or presentation with third-party software, such as Microsoft's Excel and PowerPoint, or compatible applications. These commands are discussed further in Chapter 14.

#### 3.2.1.4 Import User Items

User items are objects such as views, prefilters, custom reports and charts, templates, scripts, and dashboards that are used to customize and extend Empower's capabilities. Such items can be imported and exported with the Import User Items and Export User Items commands. For instance, you might import a custom report developed by someone else, or export a view that you have created for use by other Empower users in your organization.

To import a file containing user items (this of course means someone, perhaps yourself, has first created this file by exporting the user items), you invoke the command File > Import User Items. That brings up the dialog shown in Figure 3.2.

**Figure 3.2: Importing User Items, Step 1**

Click on the Choose File button. A "open file" dialog will appear, allowing you to find your user items file and select it. As the dialog text points out, user item files will have extensions of txt, html, xml, or zip. (See the next section, Section 3.2.1.5, for details.) When you have selected a file to import, the dialog will look like Figure 3.3. Note that the file name you chose appears next to the Choose File button.

**Figure 3.3: Importing User Items, Step 2**

Click Upload; the dialog will then look similar to Figure 3.4.

**Figure 3.4: Importing User Items, Step 3**

The dialog will list the various files that can be imported. In this case, we chose a zipped file containing several xml files, one for each of the six types of user items in this particular export file. Here, the export file contains at least one user item from each of the following: charts, filters, views, scripts, templates, and reports, as you can see from the list box. You could decide to import, say, just charts, or you could select multiple files to import.

If the export file contained just one user item, say the VAR_Header template, the list box will just show VAR_Header.html. If the export file contained one or more views, say, and no other type of user item, the list box would just show views.xml.

Next, you decide how the items in the import file will be merged with the existing items. The three choices are:

- **Add only**: Only new items will be imported and added to the list of items already in Empower.
- **Add and update**: New items will be added, as in the previous choice, but items with names that are the same as existing items will also be imported, thus updating those existing items. This is the default option and the one you are most likely to want to use.
- **Add, update, and delete**: As the previous choice, except that any existing items that are not in the existing list of imported items will be deleted. In other words, after this choice is executed, the user will have only the items in the imported files.

Note that these rules are applied within the type of item being imported. So, for instance, while importing views, if you have chosen the "Add and update" option, Empower will only update views that have names matching views in the import file.

We select all the files, and click Import. We next see the dialog shown in Figure 3.5.

**Figure 3.5: Importing User Items, Final Step**

Note that the dialog shows each of the files we have imported.

#### 3.2.1.5 Export User Items

This command allows you to export any type of user item. Clicking on File > Export User Items brings up the dialog shown in Figure 3.6.

**Figure 3.6: Export User Items Dialog**

The dropdown box at the top of the dialog contains all the types of user items; the list box below shows all the items of the selected type that have been imported into the database Empower is connected to.

In Figure 3.7 we see the dropdown list in its "dropped" state, showing the seven types of user items. To choose to export one or more reports, you would select "Reports" in the dropdown list. Then all the custom reports available would be shown in the list box.

**Figure 3.7: Choosing a Type of User Item to Export**

In a single export operation you can export as many items of as many types as you wish. To build up an export you choose the first type of item you wish to export, say Views for example, then pick the views you want to export; you can select one view or multiple views. Then you would use the dropdown list to pick the next type of user item you wish to export, say Filters, then pick the filters you want, and so on.

When you select items of one type, they remain selected when you move on to select items of a different type. This behavior is what allows you to build up an export of items from multiple types. What if you have selected two views, then decide you don't want to select any views? To clear all your selections for a type, close the dialog and reopen it with the Export User Items command.

When you have selected the items you want to export, click the Export button and a file will be downloaded to the folder your browser typically uses for downloads. If you are downloading more than one item, the result will be a zipped file named useritems.zip. If you choose to export just one item, the name will be as follows: for charts, views, filters, and dashboards, the name will be the type, with an xml extension, e.g., charts.xml. If the item is a report, chart, or a script, the file name may be the item name with a txt extension, e.g., BAC_Delta.txt. If the item was a template, the result will be the item name with a html extension, e.g., VAR_Header.html.

The reason for the difference between the types that end in xml and the others is that users can edit some charts, reports, scripts, and templates in a text editor, while the exports of views, charts, filters, and dashboards are typically used just to save and exchange such items. As you will learn later in this manual, users can create and edit views, filters, charts, and dashboards in the Empower user interface itself.

#### 3.2.1.6 Set Password

This menu choice brings up a dialog that allows you to change your password for the Empower application. See Figure 3.8 below.

**Figure 3.8: Set Password Dialog**

Note that you will have to input your current password when changing your password.

#### 3.2.1.7 Logout

The Logout menu selection will log out the current user. Empower will then display the login screen (see Figure 2.1).

### 3.2.2 Options Menu

This menu, shown in Figure 3.9, allows the user to change the display, such as hiding or showing the Toolbar or Status Bar, or showing the WBS elements in a tree structure, and so on.

**Figure 3.9: Options Menu**

#### 3.2.2.1 Hide/Show Toolbar

This selection toggles the Toolbar on and off.

#### 3.2.2.2 Hide/Show Status Bar

This selection toggles the Status Bar on and off.

#### 3.2.2.3 Hide/Show Filter Bar

This selection toggles the Filter Bar on and off.

#### 3.2.2.4 Text-Only Grid / Use Colors in Grid

This menu choice toggles the display of the color and trend columns. These columns provide a graphical display of key indicators for each element (see Section 4.5 for more information). Normally, the cells in these columns are color-coded with arrows. For the benefit of users who have a form of color-blindness, the Text-Only Grid command changes the display from color-coded to purely textual indicators. The command Use Colors in Grid toggles these columns back to the colored graphical display.

Interactive filtering of the color/trend columns is unaffected by the display mode.

#### 3.2.2.5 Set Decimals

This command allows the user to change the number of digits displayed to the right of the decimal point for the current unit. Invoking this command brings up the following dialog:

**Figure 3.10: Set Decimals Dialog**

Say that a value for BCWS stored in the database is 7,278,600.00 and this value represents dollars. Assume further that for this contract, dollars are set to be shown in thousands and the number of decimal places is set to 1. BCWS will therefore be shown as 7,278.6 (that is, 7,278.6 thousand dollars, or $7,278,600).

If you then use the Set Decimals command and enter 3 in the dialog, 7,278.600 will now be shown for BCWS.

This command will not change the database's record of the default number of decimal places to be shown. To do that, see the Section 19, "Units in Empower". Say the default number of decimals for dollars in a given contract is one, and you use the Set Decimals command to set the number of decimals to three. You will see three digits to the right of the decimal point. If you call the Set Decimals command again and leave the value blank, Empower will go back to displaying one decimal place (that is, the default in the database).

The value you set with the Set Decimals command is saved in a cookie, so if you set decimals to, say, three for a given contract and unit, exit Empower, and start Empower again, when you open the same contract with the same unit, you will still see three decimal places provided the browser cookies have not been cleared.

#### 3.2.2.6 Hide/Show WBS Tree

This selection toggles the WBS Tree mode on and off. Figure 3.11 shows the Tree Mode off and Figure 3.12 shows the Tree mode on (sorted by WBS Hierarchy).

Note that in the WBS Tree mode, sorting and filtering work differently than in the non-WBS Tree mode. When sorting in the WBS Tree mode, the hierarchical nature of the tree will be maintained. For example, in Figure 3.13, the data is sorted by Cost Variance (CV) with the worst level 2 CV element (3000:Prime Equipment) placed directly below level 1 (1000:MOH-2). Directly under Prime Equipment are its children sorted by CV, worst to best. Project Management is then the next worst level 2 element, followed by its children sorted by CV worst to best. Filtering in the Tree mode is discussed in later in Section 4.6.

**Figure 3.11: Non-WBS Tree Mode**

**Figure 3.12: WBS Tree Mode Sort by WBS Hierarchy**

**Figure 3.13: WBS Tree Mode Sorted by Cost Variance (CV)**

#### 3.2.2.7 Hide/Show Gantt Tree

This selection toggles the Gantt Tree mode on and off.

Figure 3.14 shows the Tree mode on (sorted by WBS Hierarchy). Note that when sorting in a Gantt view, if the Gantt tree mode is enabled, tasks will be sorted first by parent, then by the sort criteria. If the Gantt tree is not enabled tasks will be sorted only by the sort criteria.

**Figure 3.14: Gantt Tree Mode**

#### 3.2.2.8 Show/Hide Legend Data

See Section 7.5.

#### 3.2.2.9 Show Thresholds

See Section 7.2.2.

#### 3.2.2.10 Freeze/Unfreeze WBS/Description

This selection toggles the freezing of the WBS and Description columns. Note that any columns inserted between the WBS and Description columns while in the unfreeze mode will not be displayed in the freeze mode. When scrolling with a track pad or via gestures on a tablet PC or iPad, you must gesture to the right of the frozen columns.

#### 3.2.2.11 Show Reporting Structures

This selection will display the reporting structures for Format 3 and Format 4 for the current contract, as set by the "F3StruID" and "F4StruID" fields in the "Contracts" download.

**Figure 3.15: Show Reporting Structures**

Note that if the "F3StruID" or "F4StruID" are not recognized as valid structure IDs, you will receive a message like the following:

**Figure 3.16: Structure Not Found**

If order for your IPMR Format 1 and Format 3 to be consistent with each other (and likewise Format 2 and Format 4), the "F3StruID" and "F4StruID" settings in "Contracts" should correspond to the reporting structures used for Format 1 and Format 2 respectively. If they do not match and need to be changed, the "F3StruID" and "F4StruID" settings can be changed via data download/upload of "Contracts." After changing these settings you will need to recalculate in order to update your data accordingly.

#### 3.2.2.12 Set Tree Options

This selection is used to set the filter options while in the WBS Tree mode. Figure 3.17 shows the dialog box that will appear. In the WBS Tree mode, filters are executed at a specified level. Enter 0 (zero) to apply filters to the lowest level, -1 for all levels, or enter a specific level. When in the Children drill-down mode, the filter level is automatically set to -1.

**Figure 3.17: Set Tree Options**

#### 3.2.2.13 Set Gantt Options

This section is used to set Gantt display options for Late Finishes or Slips in the Gantt Chart. Figure 3.18 shows the dialog box that will appear.

**Figure 3.18: Set Gantt Options**

Checking the boxes will display a sample of what the selected option will look like. For example, checking "Show Late Finish" would display something like Figure 3.19.

**Figure 3.19: Show Late Finish**

Similarly, if you check "Show Slips" you will see something like Figure 3.20.

**Figure 3.20: Show Slips**

Click "OK" to keep your changes, or "Cancel" to discard any changes you have made in the dialog.

#### 3.2.2.14 Set Chart Value Range

This option is used to set chart display options for charts that are currently open. Figure 3.21 shows the dialog box that will appear.

**Figure 3.21: Set Chart Value Range**

The 'Minimum' and 'Maximum' inputs allow you to set the maximum and minimum for the y-axis of the chart. The 'Step' input allows you to specify the interval between tick marks on the y-axis. All three of these inputs should be numeric. Setting one of these inputs to a blank value will allow the charting tool to determine the value for that input. This can be used to fix one end of the y-axis while allowing the other end to change.

On opening, this dialog will be automatically populated with the current chart's min, max, step, and scale (if applicable). If range options have already been set for the current chart, the dialog will be populated with the currently set values. Clicking 'OK' will set the values for the chart range and close the dialog. Selecting 'Cancel' will close the dialog without setting chart range values. 'Reset' will remove any previously set range options for the current chart. Chart range option settings are chart specific, so if you change charts the range settings will not apply to the new chart. Chart range settings are session specific, they will not carry over to new Empower sessions.

The 'Scale' input allows you to change the scale of the charted data for some charts. Changing scale will automatically adjust the max, min, and step values.

**Figure 3.22: Change Chart Scale**

Scaling is not available for all charts. The scaling dropdown will be greyed out for charts where it is unavailable.

For dual-axis charts, max, min, and step settings are applied to the left axis.

Chart range settings can be saved in a dashboard by setting the desired range for the chart, then saving the dashboard.

Note that the charting tool may adjust the final maximum, minimum, or step as necessary to correctly display the chart.

#### 3.2.2.15 Set Chart Date Range

This option is used to set chart display options for charts that are currently open. Figure 3.23 shows the dialog box that will appear.

**Figure 3.23: Set Chart Date Range**

This dialog allows you to set an x-axis range for charts that use date categories. Note that this option is not available for all charts; for charts that cannot use the date range functionality the dialog will not display any dates and the "OK" button will be disabled.

On opening this dialog, the "zoom" button will be enabled to allow you the largest range of data possible. Select "From" and "To" dates and click "OK" to set the range for your chart.

Click "Reset" to remove the set range for the current chart. Note that the set range will be removed when changing datasets.

#### 3.2.2.16 Show IDs

This option shows database keys for certain pieces of data and is of interest primarily to the Empower support staff.

#### 3.2.2.17 Show Connection

This option shows information about the database connection and is likewise of interest primarily to the Empower support staff.

#### 3.2.2.18 Show Raw Data

When this command is selected, Empower will display the raw data returned from the database for each successive function. This command can be useful for debugging. If you need to contact our Tech Support, you might be asked to run this command and send us the results.

For the curious, the figure below shows some sample raw data output. We issued the Show Raw Data command, then opened the Cost/Schedule Variance Trends chart (func=ch_csvar), then the Current Variance chart (func=ch_cvr), and finally the Six Period Summary Report (func=rp_sixper). Those of you who are really interested may note that some of the raw data is in textual format and some in JSON (JavaScript Object Notation) form.

**Figure 3.24: Sample Raw Data Output**

### 3.2.3 The Charts, Reports, Inputs, Views, Prefilters, and Admin Menus

These menus all lead to functions which are described in detail in their own chapters.

### 3.2.4 Help Menu

The Help menu is shown in Figure 3.25. It provides access to the Users' Manual (this document), the DAU "Gold Card" (a quick reference card that defines common Earned Value terminology, produced by the Defense Acquisition University), a dialog showing how to contact Encore Analytics technical support, and the obligatory About box.

**Figure 3.25: Help Menu**

The option Empower DQI Test Guide downloads as a spreadsheet that lists Empower's Data Quality Indicators. The spreadsheet shows the internal ID number, alias, test group, and title for each DQI. This information can be helpful for, among other things, removing unwanted DQIs from DQI reports (see Section 11.4 for more information).

Here is the support dialog:

**Figure 3.26: Support Dialog**

And here is the About box. When you contact technical support, you may be asked for the version number and date shown in this dialog. The dialog shows your license expiration date; if you have purchased the software (as opposed to leasing it), the expiration date will be "Never". The dialog also shows the expiration date of your maintenance contract. As a gentle reminder, when the Admin user is logged in and the current date is within 60 days of the maintenance expiration, a message showing the number of days left will appear in the Status Bar.

**Figure 3.27: About Dialog**

## 3.3 The Toolbar

As mentioned earlier, the Toolbar provides access to commonly used functionality, some of it duplicated from the File Menu, and some of it only available on the Toolbar.

### 3.3.1 Dataset Button

The Dataset button is an alternate way of invoking the File > Open Dataset command, described in paragraph 2.4.

### 3.3.2 Layout Button

The Layout button will refresh the Tripane window sizing to optimize the current browser window. This is very useful after resizing your browser window or if you need to restore to the original layout state after minimizing/maximizing other windows. This functionality does not exist on the File Menu.

### 3.3.3 Clear Button

The Clear button will clear all of the filter boxes and refresh the Sort Window. This functionality does not exist on the File Menu.

### 3.3.4 Lowest (Level) Button

The Lowest Level button will toggle the Lowest Level filter on and off. Toggling this button is exactly equivalent to typing an "x" in the LL filter box, or clearing the filter box. This functionality does not exist on the File Menu.

### 3.3.5 Sum Button

The Sum button adds a new row at the bottom of the Sort Window, which summarizes each column in a way appropriate to the contents of the column. The summary row is shown in the figure below; note that the WBS and DESCRIPTION columns contain the word "SUMMARY".

**Figure 3.28: Summary Button Turned On**

1. For columns containing numbers such as dollars or hours (e.g., BCWS, BAC, etc.), the summary is simply the arithmetic sum of all the values in the column.
2. For columns containing percentages, indexes, or trends (e.g., % CMP, SPI, the SV trend column), the summary is calculated by using the relevant totals of the displayed rows. For example, the summary SPI will be calculated by dividing the total BCWP of the displayed rows by the total BCWS of those rows.
3. For color/trend columns based on a percentage or an index, the colors and trends are again calculated using the relevant totals for the displayed rows. For example, the color and trend assigned to the SPI will be based on summary values calculated as described above, using the color and trend thresholds defined for the active contract. In a cross-contract query, the color and trend thresholds from the first contract (alphabetically) will be used.
4. For User KPI columns, an average value is computed (1 for red, 2 for yellow, 3 for green, 4 for blue), and a color is assigned accordingly. (User KPI trends are based on simple comparisons of the average values between the current and prior period; the threshold value is not used.) Similarly, the user-assigned Risk Level and Risk Color summary columns are an average (1 for low, 2 for medium, 3 for high).
5. No summarization is performed for the DQI column.

Toggling the Sum button off removes the summary line.

The Sum button will also automatically toggle off under certain circumstances. The general rule is that the button toggles off whenever it is possible that the contents of the rows in the Sort Window might change, either by changing the number of rows in the Sort Window, or by changing the contents of one or more rows in the Sort Window. So applying a filter or a prefilter, or opening a dataset, will turn off the Sum button and remove the summary row.

In addition, turning on the WBS Tree Mode toggles off the summary. However, Empower remembers that summary mode was on, so if you had summary mode on, then turned WBS Tree Mode on and off, you will be back in summary mode.

#### 3.3.5.1 Reports and Charts with Summary Rows

The user can generate charts and reports by selecting the summary row, just as with non-summary rows. This section gathers together the differences that appear in charts and reports when they are based on summary rows. (If you're not already familiar with charts and reports, you'll want to skip ahead to the relevant sections, then come back here.)

In general, charts and reports work with summary rows as you would expect. The captions for charts and reports change to reflect the fact that they are based on a summary row. Instead of the element WBS number, the word "SUMMARY" will appear, followed by any filter or prefilter. As an example, we used the contract MOH-2, set an interactive filter with CAM="Troop", and clicked the sum button. We then selected the summary row, and opened the Current Variance chart and the Six Period DQI Trends report. Here is the resulting chart:

**Figure 3.29: Chart from Summary Row**

And here is the report:

**Figure 3.30: Report from Summary Row**

Charts that don't make sense when based on a summary row aren't created. For instance, trying to generate a Format 3 Baseline > Baseline Changes chart will result in a dialog saying: "Not available for summary row."

A Bull's Eye Bubble Chart on a summary row will only have bubbles for the "children" of the summary row, that is, the rows that are summarized. So when we set our filter to "Troop", we got elements 3700 and 3800. These will be the two elements displayed as bubbles in the chart, as shown below:

**Figure 3.31: Bull's Eye Bubble Chart from Summary Row**

Charts and reports can also be generated from a summary row in a cross-contract query. To illustrate this, we did a cross-contract query with a number of sample contracts and set up an interactive filter with CAM = "Troop". We then clicked on the Sum button, selected the resulting summary row, and opened the Current Variance chart. The result is shown below:

**Figure 3.32: Chart from Summary Row in Cross-Contract Query**

A cross-contract sum is most easily interpreted when all the contracts being summarized use the same calendar and have been statused through the same period. Empower doesn't require this, however, since very often the data can be meaningfully combined even when the calendars don't match perfectly.

Instead, Empower sums together data from the most recent period in each contract (CUR-0), data from the next most recent period (CUR-1), data from the third most recent period (CUR-2), and so on. To provide a point of reference, the title of a cross-contract summary chart or report contains the date of the most recent of the periods being summarized.

In this case, you'll see from the caption that "DEC 10" is the most recent of the periods being summarized. The horizontal axis labels are "CUR-0" (the most recent period in each contract), "CUR-1" (the one before that), "CUR-2" (the one before that) and so on.

For charts that show future data, the same procedure is followed; labels will continue with CUR+1, CUR+2, etc.

The Sum button works with Schedule Gantt charts when viewing one contract, but by design it is not supported for cross-contract queries.

### 3.3.6 Group By

You can group the rows of the Sort Window to gain further insight into your data. Click the Group button, and the Group By dialog appears, shown below in Figure 3.33. You will see a list of columns by which you can group the Sort Window Rows.

**Figure 3.33: Group By Dialog Box**

For our example, we'll group by the CAM, so we select "CAM - (ProjOff)" and click Group By. Figure 3.34 shows what the Sort Window looks like now. Note that Brown is CAM for two WBS elements (the "2" in parentheses), and Brown's two elements are listed below his name.

**Figure 3.34: Sort Window with Group By Applied**

If you have Group By applied and you click the Sum button, you get the subtotals for each of the groups of rows, so if you are grouping by CAM, you'll get a Summary Row for each CAM's elements. This is shown in Figure 3.35.

**Figure 3.35: Sort Window with Group By and Sum Button Applied**

Finally, if you export the Sort Window with Group By or Group By plus the Sum Button, the resulting spreadsheet will reflect your group and sum choices, as shown in Figure 3.36 below.

**Figure 3.36: Sort Window with Group By and Sum Button Exported to Excel**

### 3.3.7 Chart Style Button

As this button refers to Empower's charting capabilities, it is described in Section 7.2.

### 3.3.8 Zoom Button

The Zoom button usually shows all periods of data for a selected chart. Since this button relates exclusively to charts, it is discussed in detail in Section 7.7.

### 3.3.9 Pin Button

The Pin button, when active, prevents the editor and/or VAR Narrative Report from being updated automatically when a new element is selected. See Chapter 15 for more about using the editor for narrative reports.

### 3.3.10 Children Button

The purpose of the Children button is to drill-down and drill-up from selected levels in the WBS/OBS. For example, assume that the Sort Window was filtered to display only Control Accounts sorted by cumulative cost variance; however, the database's lowest level was actually the work package. Select the control account in question and press the Children button. The Sort Window will be redrawn in the WBS Tree mode showing the Control Account with all related Work Packages sorted by cumulative cost variance. It will also show the elements above the Control Account in the hierarchical tree.

In Figure 3.37, we selected WBS element 1.3, then pressed the Children button. Note that the Sort Window is now in WBS Tree mode and that all of 1.3's immediate children are shown. You can also see that the Children button is depressed.

**Figure 3.37: Sort Window Showing Children**

Note the little plus signs before the WBS numbers of the child elements. If you click on a child, that child's children will be displayed (if there are any). In Figure 3.38, we clicked on WBS 1.3.2, and so we now also see that element's two children.

**Figure 3.38: Sort Window Showing Children of a Child**

To return to the control account level Sort Window press the Children button again. The Sort Window will be returned to its original state with the appropriate Control Account selected.

The Children functionality does not exist on the File Menu; it can only be accessed from the Toolbar.

### 3.3.11 Drill Up/Drill Down Buttons

The Drill Up and Drill Down buttons on the Toolbar offer a quick way of navigating through the WBS hierarchy, which can be a considerable time-saver in very large contracts.

Initially the Toolbar displays just the Drill Down button at the far right, as shown in Figure 3.39.

**Figure 3.39: Drill Down Button**

Clicking on this button will change the Sort Window so that it displays only the children of the selected element. To illustrate, select element 3000 in the MOH-2 contract, then click the Drill Down button. The Sort Window will only show 3000's children, as seen in Figure 3.40.

**Figure 3.40: Sort Window After Pressing Drill Down**

After you press the Drill Down button, the Toolbar will display three buttons: one for drilling down, one for drilling up, and a button to turn off the drill up/drill down behavior. See Figure 3.41.

Also, once the drilling functionality has been invoked, the status bar will display the text "[Drilling]" to remind you that you're only seeing in the Sort Window those elements that result from a drill down or up.

**Figure 3.41: Drill Up, Down, and Off Buttons**

The Drill Up button changes the Sort Window to display just the parent of the selected element, and all the parent's siblings. So if you selected element 3600, then pressed Drill Up, the Sort Window would look like Figure 3.42. Note that 3600's parent (3000) is shown, along with all of 3000's siblings: 2000, 4000, and all the other elements that are at level 2 (as indicated by the LVL column).

**Figure 3.42: Sort Window After Drilling Up**

Clicking the Off button turns off the drill up/drill down behavior and makes the Toolbar look like Figure 3.39 again.

The Drill button, in addition to its behavior when clicked, also has a dropdown menu feature. If you have an element selected and you want to start by drilling up, rather than down, you can click on the arrow at the right side of the button, and you'll get a dropdown menu that allows you to drill down or up. See Figure 3.43. From there on, the three buttons of Figure 3.41 appear and the behavior is as described above.

**Figure 3.43: Drill Button Dropdown Menu**

The interaction of the drilling feature with prefilters requires some discussion. First of all, consider what happens when the drilling feature is used in tandem with a user prefilter. (See Section 6.5 for the difference between user prefilters and security prefilters.)

The drilling feature will override any user prefilters currently applied. Imagine that we have a prefilter that selects only elements whose CPI is less than 0.95; we apply that prefilter and the Sort Window for our sample MOH-2 contract will look like Figure 3.44. Note that the only children of element 3000 showing are 3200 and 3600, since they meet the prefilter criterion. So far, this is just what we'd expect.

**Figure 3.44: Prefilter Applied, No Drill Down**

But now we select element 3000, and press the Drill button to go into drill-down mode. The result is shown in Figure 3.45. Note that all of 3000's children are showing, even though several have CPI greater than 0.95. This shows that drilling down overrides the filter criteria of a user prefilter.

**Figure 3.45: Drilling Overrides User Prefilter**

Now glance at the Status Bar, shown in Figure 3.46. Note at the far right of the figure that the Status Bar is telling us that Empower is in drilling mode and that the prefilter is still applied.

**Figure 3.46: Status Bar: Drilling with Prefilter**

When we turn off drilling, however, the prefilter reasserts itself, and the Sort Window will just display elements meeting the prefilter criterion. The only children of element 3000 now showing will be the prefilter-matching 3200 and 3600.

When, on the other hand, a security prefilter has been applied, drilling behavior changes. Recall that drilling down while a user prefilter is applied effectively overrides the user prefilter criteria. Of course we don't want a user to be able to override a security feature, so drilling up will not negate the effect of a security prefilter. So for example, if user Bob has a security prefilter in effect which limits him to viewing elements whose CAM is Troop, he will see (in our sample MOH-2 contract) only elements 3700 and 3800. (Recall Figure 3.45, which shows the various CAMs for the children of element 3000.) If Bob tries to outsmart us by selecting either of these elements and drilling up, he'll find that his Sort Window is blank: the security prefilter is still limiting him to elements with Troop as the CAM, and none of 3700's or 3800's parents or ancestors meet that criterion.

### 3.3.12 Gantt Toolbar Buttons

When the Gantt chart is being displayed, additional buttons appear on the Toolbar. These buttons are explained along with the Gantt chart (see section 7.17.1).

## 3.4 Customizing the User Interface

The Empower user interface can be customized by removing menu items and toolbar items. This can make Empower easier to use by removing functions that aren't of interest to each particular class of users.

The Empower user interface is customized by editing the empower.conf configuration file in the Empower home directory, and can only be done by somebody with access to this directory on the server, typically one of your site's system administrators. Editing this configuration file is therefore beyond the scope of the User's Manual. However, we mention this capability here so that users will be aware that it is possible that some of the menu and toolbar items described in this manual might have been removed by their Empower administrators.
