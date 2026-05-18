# 16.9 Download Data File

The previous sections "Export EDI File" and "Export IPM Reports" covered importing and exporting data to and from the database in XML format. That functionality is primarily to facilitate transfer of data from one system to another. Empower also provides the ability to import and export data in the form of Excel spreadsheets. The idea is that a user can export some data to an Excel spreadsheet, modify the data in the spreadsheet, and then import the data back into Empower. This offers a way to make manual changes to the database.

Selecting Download Data brings up the dialog box shown in Figure 16.47 below.

## Download Data - Step 1 (Contracts)

The user can select virtually every data item to export. First, the user selects a data type to export from the lower select box. Depending on this choice, some or all of the select boxes above will be populated. For example, in Figure 16.47, "Contracts (all)" has been selected, and this choice requires no additional input. The user can just press the Download button, and all contracts will be exported.

But if the user selects, say, "Earned Value Data", the dialog's appearance will change, as shown in Figure 16.48. Note that now all four of the upper select boxes have been populated, and the user can narrow the choice by selecting a contract, a period, a structure, and the units. Note that only one option can be selected for contract, period, and structure while multiple units can be selected. If multiple units are selected, any records for the selected units will be included in the download.

## Download Data - Step 1 (Earned Value Data)

When the user presses the Download button, Empower will create and download an Excel file. (Depending on which browser the user has and what the browser's download settings are, the Excel file will be downloaded to the user's machine automatically, or the browser will present a dialog box asking where the file should be saved.)

Note that attempting to download a data file that would have more than one million rows will not download all of those rows; instead the downloaded file will contain a message informing you that the download would have more rows than are allowed in Excel, so further refinement before downloading may be required.

Here is a portion of the downloaded file that results from choosing "Contracts (All)" being viewed in Excel:

## Downloaded Data Viewed In Excel

The table in Excel begins with fields (columns) that will be familiar from the normal appearance of the Sort Window. User-defined fields will show up at the far right of the regular columns for the table.

Note that the downloaded spreadsheet can have more than one tab, as shown at the bottom of Figure 16.50. In this case, one of the tabs is titled "Notes." This tab contains information on the fields in the download that you can use as a reference.

## Downloaded Data Viewed In Excel, Showing Multiple Tabs

The user can now edit the Excel spreadsheet, giving instructions to add, delete, or change data in the database. Figure 16.51 shows the Excel spreadsheet containing contract data modified to make changes in the database.

For instance, if the user wanted to delete contract "ALPHA," he or she would put a "d" in the first column (the "action" column) for the "ALPHA" row (cell A9 in Excel). Note that the user does not actually delete the row in the Excel spreadsheet!

If the user felt that the Jeep 240z contract name should be in all capital letters, to match the other contracts, the change would be made in cell C11, and a "c" would be entered in the "action" column (cell A11) to indicate that this row should be changed. Likewise, the user could enter a completely new contract by filling out row 14 appropriately and putting an "a" in the "action" column for cell A14.

The user can also delete the text from a field by entering the text "NULL" (all upper-case and without the quotes) in the relevant field, and putting a "c" in the action column for that row.

Note that certain cells have a yellow background. Ordinarily, these cells should not be changed since they contain key database fields. In general, fields in blue indicate informational fields provided to give context in the data download; in most cases these fields should not be changed.

## Downloaded Data Edited In Excel

Once the desired changes have been made in the Excel file, the changes can be made in the database by using the Upload Data File command, described in Section 16.10.

The following sub-sections discuss some useful things the user can do with the Download Data/Upload Data commands.

## 16.9.1 Setting the Reporting Level

You can use the Download Data/Upload Data cycle to control which elements are included in EDI exports, CPR and IPMR report generation, and exporting narratives.

Each "Element Reporting" record has two fields for this purpose: the RptElem field controls the reporting level for CPR and IMPR report generation and exporting narratives, and the RptElemE (note the "E" at the end) field controls reporting level for EDI exports. This way you can have two different reporting levels for EDI export and, say, IPM report generation.

In the following discussion, we will refer just to the RptElem field. If you want to set the reporting level for EDI exports, just substitute RptElemE for RptElem.

You can use the Download Data/Upload Data cycle to set the RptElem field for records in the "Element Reporting" download in order to control which elements get exported for the following commands: Export EDI File, Export IPM Report, Export Narratives.

Begin by downloading the data type "Element Reporting" from the MOH-2 contract and the WBS structure. Open the resulting RptElems file in Excel. The key thing here is to set the RptElem field to 1 for the parent of each element you want to export. Refer to Figure 16.52. (In this figure, we've hidden and reordered a few columns to draw attention to the changes we're making.) We want to see elements 2000, 3000, 4000, and so on, so we've set RptElem for their parent, element 1000, to 1. Say we also want to export 3100 through 3800, so we set RptElem for element 3000 to 1. We make sure to set the action field accordingly and save our Excel file.

## Downloaded Element Reporting: Setting RptElem Field

Now we upload the Excel file. The status dialog is shown in Figure 16.53; note that Empower has made changes based on rows 9 and 14 of the spreadsheet, as expected.

## Uploading Data with Modified RptElem Fields

After uploading the changes, run a recalculation on the data with "Set reporting elements" checked.

To verify that our changes worked, we do an IPMR export, making sure to select "Export to reporting level".

## Exporting to Specified Reporting Level

This will result in an .xlsx file being downloaded to your computer. If you look at the first tab of the .xlsx file you'll see under the Work Breakdown Structure section that the only elements that appear are 2000 and the other multiples of 1000, [OH], and the children of 3000: 3100, 3200, and on through 3800, just as we requested.

## 16.9.2 Setting Formal Reporting Structure Names

You can also use the Download Data/Upload Data cycle to control the names used for your reporting structures.

To set a name for a "Formal Reporting" structure, use the "Contract Structures" data download to set the "FRName" field for any structures that you want to use as "Formal Reporting" structures.

## Setting FRName Field

To set an element as "non-reporting", use the "Element Reporting" download to set RptElem = -1 and RptElemE = -1 for that element. Note that the children of elements that have been marked with RptElem = -1 will have RptElem = -2. In general, we assume that RptElem and RptElemE will match. To mark non-reporting elements as "non-add" as well, you would set NAFlag to -1 for those elements.

## 16.9.3 Setting Gantt Filter Color Thresholds

One interesting thing the user might wish to do with this ability to modify the database is change the thresholds used to calculate the Gantt filter colors (see Section 7.17.1.1). With the exception of white, which is set to filter out completed tasks, the user can modify the formula Empower uses to calculate these colors.

This is an advanced feature, and it requires familiarity with SQL. First, ensure the Data Type is set to "Shared (selected)" and then download the Columns table by selecting Columns in the Items select box. Download the file as usual, and open the resulting spreadsheet. Figure 16.56 shows the bottom of the first tab of this spreadsheet.

## Downloaded Column Data Viewed In Excel

Note the value 1023 in the lower-left hand corner. (This will be column B in the spreadsheet.) This identifies the row we are interested in. As a double check that you have the right row, verify that the row contains the comment "SQL used to set Red, Yellow, Green flags for schedule filtering" in column L.

Next note the cell that begins with "CASE WHEN (NumSlips = 3... " in this row. (It's column M in the spreadsheet, headed "SQLL" — note the extra "L".) This is the fragment of SQL that is used to set the colors.

Here is the complete contents of that cell, reformatted for easier reading:

```sql
CASE WHEN (NumSlips = 3 OR FloatVal < -5 OR SlipVal > 30)
  THEN 'R'
WHEN (NumSlips = 2 OR (FloatVal >= -5 AND FloatVal < 0)
  OR (SlipVal >= 15 AND SlipVal <= 30))
  THEN 'Y'
ELSE 'G'
END
```

As you can see, this SQL fragment calculates a result of red, yellow, or green (R, Y, G) depending on the number of slips taken, the size of the slips, and so on.

This is what you will edit. For instance, if you are more forgiving of how many slips your managers take, you could edit the first part to read something like this:

```sql
CASE WHEN (NumSlips = 5 ...
```

When you have edited the SQL to your satisfaction, invoke the Upload Data File command as described in the next section. Now all the contracts in this database will have their Gantt filter colors calculated according to the new formula.

But wait, you say. The SQL statement in column M is in a cell with a yellow background, which, according to cell A3 in the spreadsheet and the statement earlier in this manual, is not to be edited or moved by users. Well, every rule has an exception, and this is it. This cell can be edited by users. The worst that will happen if you enter an invalid SQL fragment is that the Gantt filter colors will not be calculated as you expected.

If you are not confident of your SQL skills, please call Encore Analytics support and we will provide you with an SQL statement, based on your requirements, that you can simply paste into this cell.

## 16.9.4 Setting Threshold Color Values for SPI, CPI, etc.

Download the Contracts table to an Excel spreadsheet by selecting the "Contracts (all)" Data Type and clicking on the Download button. Note that the spreadsheet has two tabs, named Header and Settings. Select the Settings tab. The result will look similar to Figure 16.57. You will see that columns E, F, and G allow you to enter the percentages for the threshold values. The figure shows the bottom of this spreadsheet, with the red, yellow, and green values for the MOH-2 contract boxed to make them stand out.

## Setting SPI, CPI Color Threshold Values for a Contract

Simply set the percentages to your desired values (you can set them for all contracts in the database at once, if you desire), remembering to enter the "c" action code in the first column for each row that you have modified, and save the spreadsheet file. Then import the data into the database, using the Upload Data command.

## 16.9.5 Setting a Contract Alias

Using a contract alias allows you to display an easily readable or recognizable name for your contract in the Empower UI while leaving the actual contract name unchanged. Exports of the contract will still have the original contract name, only the name displayed in Empower will change.

To set the Contract Alias, download the Contracts table, then enter the alias for your contract in the "ContrAlias" field.

## Setting Contract Alias

Next put a "c" in the action column, save, and import the change with the Upload Data File command. If you reopen the contract with the alias, the contract alias will now be displayed in the Empower UI.

## Contract Alias in the Empower UI

## 16.9.6 Setting VAR Type

The "VarType" field allows you to specify an alternative VAR template for contracts that should use an "IPMDAR JSON" template instead of the default VAR template. Typically this value will be set automatically based on the import file format used when the contract is first created, but you can adjust the value if necessary.

To set the VAR Type for a contract, download the Contracts table and find the "VarType" field on the "Settings" tab. For contracts that should use the "IPMDAR JSON" VAR template, change the VarType to 1. Any contracts that should use the "PARS JSON" VAR template should have VarType 2. Any contracts that should not use the "Default" VAR template should have 0 as their VarType. Next, put a "c" in the action column, save, and upload the changed file with "Admin > Upload Data File."

## Setting VAR Type

## 16.9.7 Setting IPMDAR Custom Fields

The IpmdarCA, IpmdarWP, and IpmdarTask fields in the Contracts table allow you to indicate fields that should be exported as IPMDAR custom fields for each contract. There are a maximum of 10 fields each for CA, WP, and Task. CA custom fields can be set with the IpmdarCA field, WP with IpmdarWP, and Task with IpmdarTask.

Entries should be comma separated lists of field names. The order of the entries in each line will determine the name of the field in the IPMDAR JSON file export. The first field listed will be FIELD_01, the second FIELD_02, etc. The "Name" section of the export will be populated with the field name from Empower, or the field alias if present.

## 16.9.8 Cost Date Calculation Settings

The CalcCostDates field in the Contracts table is used to indicate whether Empower should calculate cost schedule dates for this contract from any available schedule data during recalculation, or should use set values input for the contract. This setting can be found on the "Audit" tab of the Contracts download, see Figure 16.61. Note that some columns have been hidden for readability.

## Contract Download: CalcCostDates

The default value for this field is 1, indicating that Empower should calculate cost schedule dates during recalculation. If the value is set to 0, Empower will use values from the CostDates table. CostDates values can be input via Data Download/Upload of "CostDates".

## CostDates Download

## 16.9.9 VAR Kanban Customization

The OwnerColID field in the Contracts table is used to indicate which field should be used to populate information about the item owner in the VAR Kanban. This setting will control both the title and the contents of that section of the Kanban.

To set the OwnerColID, find the ColumnID of the field that you want to use for the names of the people that you want to be associated with your VARs in the Kanban. You can find the ColumnID in the Columns data download. Please note that only certain fields can be used; fields must be in the "Elements" or "NarrName" tables.

For example, if you wanted to use the VAR Submitter name in the Kanban, you could assign OwnerColID a value of 809, which corresponds to the NarrName.Submitter field. Since this field has an Alias of "VAR SUBM", that Alias will be used for the title in the VAR Kanban.

## Customized VAR Kanban

## 16.9.10 Generating Data Entry Worksheets

The Download Data File/Upload Data File cycle can also be used to add earned value, future ETC, or hours/equivalent heads data to elements that don't already have such data. When adding such data through an Excel spreadsheet with the Download Data File process, however, there is a rule of thumb that must be observed.

To illustrate, in the contract Jeep 240z, there is an element with WBS number 1.3.1.10. This element has no values for any of the Earned Value fields (BCWS, BCWP, ACWP, etc.) and it does not appear in the Sort Window. If, however, you use the Download Data File command (Download Data File, choose Earned Value Data, then the contract, period, structure, and units) and open the resulting spreadsheet of Earned Values, you will see something like Figure 16.64:

## Downloaded Earned Value Data Viewed In Excel

Note that the element 3.3.6.2.1 601281380 1004 (ElemID = 1516) has no values for BcwsCum and so on, and it has no PeriodID or UnitID. If you have some earned value data for element 1.3.1.10 and you want to put it into the database, you can edit the spreadsheet, and then upload the data. Let's say we have some data for this element, and let's also say that we have discovered that the true value for BAC for the element whose ElemID is 1487 should be 12.5. We enter those numbers, as shown in Figure 16.65.

## Downloaded Earned Value Data as Edited In Excel

Note carefully that for the element with ElemID = 1487, we set the action code to "c". This is because we are changing a row that already exists in the database. But for the element with ElemID = 1516, we set the action code to "a", not "c". This is because we are really going to add a new row to the database. The data we're looking at is drawn from two database tables: the Element table which has the WbsNum and ElemID fields, and the EarnedValue table which has the rest of the fields you see. We're not adding anything to the Element table, but we are adding a row to the EarnedValue table, so we use the action code for adding. You don't actually have to know this information about the innards of the Empower database, however, to get it right.

Just follow this rule of thumb: if any of the PeriodID, UnitID, ContrID, or StruID fields are blank in the spreadsheet and you fill them in, use the "a" action code. Otherwise, use the "c" action code.

We've illustrated this capability with Earned Values, but you can do the same thing with the FutureEtc and Manpower tables. (The Manpower table refers to Staffing; it was named in a less-sensitive age.) Just use Download Data File to download the appropriate data, edit the resulting spreadsheet in Excel (remembering the rule about when to use the "a" and when to use the "c" action codes), and upload, as described in Section 16.10.

## 16.9.11 Adding Children to a Lowest-Level Element and Plug Elements

It sometimes happens that you decide you need to split a lowest-level element into one or more children. Using the Download Data/Upload Data features, you can do this with Empower. First, use the Download Data command to download the Elements table for the desired contract, and open the spreadsheet in Excel. Suppose that you want to decompose the MOH-2 contract's element 2100 (Project Management) into two sub-elements. Next, modify the spreadsheet to look like Figure 16.66. To do this, insert a couple of blank lines in the spreadsheet, and fill in the details for the new elements, which in our example are 2110 - IDENTIFY CULPRITS and 2120 - FIX BLAME. (Instead of inserting blank lines in the spreadsheet, you could just add the new elements at the end of the existing data, but we wanted to show the new children just under their parent.) Don't fill in the ElemID fields for these elements; Empower will do that. You do need to fill in the ContrID and StruID fields (which you'll see are the same as for the other elements in the spreadsheet).

Note also that, since you've just filled in these ID fields, you're really going to be adding rows to a table, and you'll need to use the "a" action code. It is very important that you enter the correct ParentID value. Since both the new elements will be children of WBS element 2100, whose ElemID is 3, you enter 3 for the ParentID of the new children. You should also enter values for the SortVal field; in this case we just used the WBS number. Finally, enter the code "a" in the action field for the rows containing the new elements and save the changes to the spreadsheet file.

## Adding New Lowest-Level Elements

Next, upload the data file, using the Upload Data File command (described more fully in Section 16.10). Once you've chosen the file containing the modified spreadsheet and told Empower to upload the file, you should see a series of status messages like those shown in Figure 16.67. You'll note that Empower has inserted two new rows into the Element table, just as we requested in Excel.

## Importing the Modified Elements Table

Now use the Download Data command to download the Earned Value table for our contract, and open the resulting spreadsheet. You'll see a new element, called in this case PLUG-1594. This plug element is generated by Empower, and its purpose is to maintain the history of the parent element after you add children. The values for BCWS and so on for the PLUG-1594 element are the same values element 2100 had before we gave it children.

The two new children have ElemIDs, generated by Empower, but they don't have a PeriodID or UnitID, or any values for the earned value numbers (BCWS and the rest). So we fill in the PeriodID and UnitID values, based on the rest of the elements. Then we fill in the earned value numbers for the children. They should add up to the same values as for the plug element, since adding children to a parent does not change how much money the parent has (unlike in real life). Now, remembering the rule from Section 16.9.10 about using the action code "a" when we're setting ID values, we put "a" in the two rows for elements 2110 and 2120. (We're adding two rows to the EarnedValue table.)

Finally, we delete the plug element from the EarnedValue table by putting the code "d" in its action field. The PLUG-1594 element will be deleted from the EarnedValue table (though it will remain forever in the Element table as a matter of history).

After all this, the EarnedValue spreadsheet looks like Figure 16.68.

## Adding Earned Values to the New Elements

Use the Upload Data command to upload this spreadsheet file, and you will see the status messages in Figure 16.69. Notice that, as expected, Empower deleted one row (the plug element), and added two rows (the new children).

## Importing the Earned Value Table

Now, recalculate (Section 16.2), and look at the Sort Window. It should look like Figure 16.70, with the two new children, properly placed under their parent and marked as level 4 elements (and as lowest-level elements). Scroll to the right and you'll see the earned value numbers we entered in the spreadsheet as well.

## The Two New Child Elements

## 16.9.12 Adjusting Thresholds

Thresholds are used during Recalculation when setting the Fmt5Var field (which usually shows up in views as "VAR") for each element in the contract. You can set thresholds for variances in current cost, cumulative cost, current schedule, cumulative schedule, and variance at complete, for both dollar and/or percentage thresholds. You can set different thresholds for different elements in each contract.

Finally, you can use different threshold criteria for the same element, for positive and negative values, and adjust those depending on the percent complete for that element. The ability to set wider positive variance thresholds is particularly useful when a more lenient or wider threshold is desired for positive variances. By doing so, the number of variance analysis write-ups can be reduced when performance is favorable. However, even favorable variances that seem too good to be true (e.g. actuals not charged to the correct account) can still be flagged with the wider positive threshold.

The next section describes what threshold criteria are available and how they are applied. The following section shows how to modify threshold criteria, and how to associate different threshold criteria with the elements in your contracts, using the Download Data File and Upload Data File commands.

First we need to explain how Empower handles threshold data.

### 16.9.12.1 Threshold Data

We begin by presenting a view of the Threshold table. When you download the Threshold table from Empower, you will get a spreadsheet that is very wide. In the figure below, we have transposed the spreadsheet (making it run vertically rather than horizontally) to make it easier to display on the page, and easier to refer to the figure as the discussion unfolds.

## Threshold Data

This figure shows that there are two Threshold records in the database, named "(Default)", and "Thresh8-2". You can have as many threshold records as you want, and you can associate a different threshold record with each element in your contract. (We will explain how to associate threshold records with elements later.)

A threshold record is made up of four blocks of data. In the figure, the first block is in rows 3 to 14, the next block in rows 15 to 26, and so on. Note that each field name in a block ends with a digit (1 to 4) identifying which block it is in. These four blocks are used to provide different variance thresholds depending on how complete the element is. If the percent complete value for an element is less than or equal to the PctCmpN value (where N is the block number, from 1 to 4), Empower will use the threshold criteria in that block. So, looking at the default threshold record, if a given element is less than or equal to 97 percent complete, Empower will use the criteria ending in 1 (rows 3 through 14). If the element's percent complete is greater than 97, but less than 98 (see cell B15), Empower will use the criteria in rows 16 to 26.

What if you don't want to use all four groups of variance criteria? As we will explain in more detail below, you can put the letter "N" in the AndOrN field for the Nth block to tell Empower to ignore these criteria.

Next we describe what these criteria are, and how Empower applies them. There are five kinds of criteria: current cost, current schedule, cumulative cost, cumulative schedule, and variance at complete. For each of these kinds of criteria that are tripped, a letter is added to the Fmt5Var, according to the following table:

| Criterion | Code |
|-----------|------|
| current cost | c |
| current schedule | s |
| cumulative cost | C |
| cumulative schedule | S |
| variance at complete | V |

So an element that trips the first and third criteria will show "cC" in the VAR column in Empower's Sort Window, while an element that trips the first, second, third, and fifth would show "scCV".

The five kinds come in pairs: CurCostD1 means the current cost variance in dollars (hence the D), while CurCostP1 means the current cost variance in percent (the P). CurSchD1 means the current schedule variance in dollars, and CurSchP1 means the current schedule in percent, and so on. (The trailing 1, of course, means we are in the first block, used when percent complete is less than or equal to 97 in the example.)

The final value in each block, AndOrN, indicates what Empower will do with the pairs of criteria. AndOrN can take on any of nine possible values: the single letters A through G, O, or N.

When the AndOrN is set to "N" for a block, Empower will not apply the criteria listed in that block. So if you had a set of criteria for elements that are less than 97 percent complete, and a second set for elements that are greater than 97 but less than 100 percent complete, you would only need to use two blocks. You would set the values ending in 1 and 2, and then set AndOr3 and AndOr4 equal to "N". Whatever values you had for, say, CurCostD3, would be ignored.

What if you want to suppress VAR threshold checking for an element? You create a threshold record with the AndOrN fields set to "N" for all four blocks in a record, then assign this record to all the elements for which you wish to suppress VAR threshold checking. (We describe the mechanics of this in the next sub-section.)

If the AndOr is "A" (meaning "And", each of the criteria will be tripped if both the dollar part AND the percent part is exceeded. So, referring to the Default thresholds in the figure, if for a given element, CurCostD1 > 50,000 dollars, AND CurCostP1 > 10 percent, the current cost threshold is breached for that element and a "c" will be added to the element's Fmt5Var. Likewise, if CurSchD1 > 50,000 dollars and CurSchP1 > 10 percent, the current schedule threshold is breached and a "s" will be added to the Fmt5Var, and so on through the remaining three pairs (CumCostD1/CumCostP1, CumSchD1/CumSchP1, and VacD1/VacP1).

Note that the dollar values you enter in the Threshold table should be consistent with how dollars are stored in your database. If your database stores dollars in thousands (i.e., a BCWS of 15 in an earned value record means $15,000), then the dollar values in the Threshold table should also be in thousands. (See Section 19 for a discussion of how Empower stores and displays units.)

Note that if you had some thresholds that were expressed in dollars and others that were expressed in other units, such as EQP, you would create one Threshold record for the dollar thresholds, and another Threshold record for the EQP thresholds converted to dollars. Then, using the technique explained below, you would associate the first Threshold record with elements whose thresholds are in dollars and the second Threshold record with elements whose thresholds were specified in EQP (in our example).

When the AndOr value is "O", an OR is used to determine whether a threshold is breached. Say that AndOr1 was "O" in the Default threshold record, and an element's percent complete was less than 97. Then the current cost threshold would be breached if either CurCostD1 > 0 dollars OR CurCostP1 > 10 percent, and likewise for the other four pairs.

In the preceding three cases, all five pairs of threshold criteria are handled the same way: either they are all ignored (AndOr = N for a block), they are all combined with AND (AndOr = A), or they are all combined with OR (AndOr = O).

What if you want to compare some pairs of threshold criteria with AND and other pairs with OR? Empower lets you do that—you can set a different logical operator (AND, OR) for the current, cumulative and variance at complete thresholds.

To get this flexibility, we add to the range of letters you can use in the AndOrN field. Consider the table in the figure below:

## AndOr Table

What this table tells us is that if we put an "A" in the AndOrN field (cell A2), Empower uses the logical operators in row 2, which are AND for current values, AND for cumulative values, and AND for VAC. Likewise, if we put an "O" in the AndOrN field (cell A9), Empower uses the logical values in row 9 (which are all OR). These are two of the three cases we've looked at so far.

We can get more interesting combinations, however, by using the letters in rows 3 through 8. If we put "B", for instance, in the AndOrN field, AND will be used to calculate whether the current and cumulative thresholds were tripped, while OR will be used for the VAC threshold.

If we put "C" in the AndOrN field, AND will be used to calculate whether the current thresholds were tripped, OR will be used to see if the cumulative thresholds were tripped, and AND will be used for the VAC threshold.

As you can see from the figure, there are six possible combinations for these mixed combinations (letters B through G).

### 16.9.12.2 Positive Thresholds

Notice the PThreshID field in our Threshold data download file. This ID is used to indicate if a threshold should have different thresholds for positive variances. By default the value of this field is set to zero, which indicates that there is no separate positive threshold. This feature is backwards compatible; if you make no changes to your thresholds they will work as usual.

To create a different threshold for positive values, first create the threshold for negative values in the normal manner. Then create a new Threshold for the positive values. Finally, in the negative threshold row, enter the positive threshold ThreshID in the PThreshID column.

For example, consider Figure 16.73.

## Threshold Table With Positive Thresholds

Notice that we have added two new thresholds. The first, called "Negative" is just a copy of the "Default" threshold. We've renamed it here for demonstration purposes since this threshold will be used for negative variances. The second new threshold is called "Positive." This threshold will be used for positive variances. We have assigned PThreshID to 5 in the line for the "Negative" threshold, indicating that when this threshold is assigned to an element we should use the "Positive" threshold for positive variances.

Assigning a threshold to an element is described in more detail in the next section.

When assigning a threshold that has separate positive and negative sections to an element, the ThreshID that should be used in EuwtLink is the ThreshID for the "negative" section.

Using the thresholds in 16.73, when an element is marked to use ThreshID = 4 (i.e. "Negative"), that row will be used for the negative variances and ThreshID = 5 (i.e. "Positive") will be used for positive variances.

## Assigning a Threshold for an Element

For example, we would use ThreshID 4 if we wanted to assign our "Negative" and "Positive" thresholds to element 3300.

### 16.9.12.3 Using Download and Upload Data to Adjust Threshold Values

Now that we understand how Empower stores the threshold information, we are ready to modify some threshold values.

There are two scenarios, and the flow is a bit different between them.

**Scenario 1:** You want to change the set of default threshold values.

**Scenario 2:** You want to create a whole new set of threshold values and associate that set with one or more existing contracts.

First, Scenario 1: Change the Default thresholds.

Get the current set of thresholds with Admin > Download Data File, and select "Shared" in the Data Type list and "Thresholds" in the Items list.

## Downloading the Thresholds

Click Download, and you'll get an Excel spreadsheet like this:

## Threshold Table as an Excel Spreadsheet

You'll see that ThreshID 1 is the default, which a contract gets unless you do something special (see scenario 2). If you want to change some Threshold values for every contract in the database, you'd probably change the values in the (Default) row. Note that if you want to update a row, you edit the values as desired (but not the yellow cells), then put a 'c' in the action column for that row ('c' for change).

Let's say we want to change the first three columns. The spreadsheet will now look like the figure below:

## Threshold Spreadsheet after Editing

Then you upload the data in the spreadsheet using the Upload Data File command, and you're done. Empower will tell you what rows were changed as a result of the upload, as shown in the figure below.

## Result of Uploading the Threshold Spreadsheet

Scenario 2: Add a new set of Thresholds.

You're going to change the thresholds for a contract or for some elements of a contract, so you need to know what thresholds the contract uses currently. Execute the Download Data File command, but this time chose "Element Weights/Thresholds..." in the Data Type list, and your contract in the Contracts list (along with the appropriate structure and unit), as shown in the figure below, then click Download.

## Downloading Element Weights/Thresholds Links

You'll see a spreadsheet like this:

## Element Weights/Thresholds Links Spreadsheet

What this spreadsheet tells you is that when Empower is calculating the Fmt5Var for the element 1000 in the MOH-2 contract and the unit is dollars (Note UnitID = 1, which is Dollars), it will use the Threshold record with a ThreshID of 1. Indeed, every element in this contract and the WBS structure uses the same Threshold record (i.e., the same set of threshold values). It is possible, as the spreadsheet suggests, to use a different set of threshold values for each element of the contract.

As we said, the spreadsheet tells you that MOH-2 currently uses 1, the default set of threshold values. If your elements were already using some custom values, you'd see a ThreshID other than 1, and you'd need to note that down.

(If you downloaded the equivalent spreadsheet for MOH-2, but chose Hours as the unit, the spreadsheet would look the same, except that the UnitID would be 2 (= Hours) for all the elements.)

Now we either add or change the thresholds: Get the current set of thresholds with Download Data File, and selecting "Shared" in the Data Type list and "Thresholds" in the Items list. Click Download, and you'll get an Excel spreadsheet like this:

## Thresholds Spreadsheet

**(A)** If your contract was already using a non-default threshold set, say ThreshID = 2, then you'd edit the values for that row (row 10 in the spreadsheet). Put a 'c' in the action column to show that this row has been changed. Then use the Upload Data command to put that data into the database, and you're done.

**(B)** If, on the other hand, your contract was using the default set, and you wanted to create a new set of threshold values, instead of editing a row, you'll add a row. Let's do that. Type in all the new values in a blank row (row 12 is handy), leaving the ThreshID blank, and putting an 'a' in the action column to indicate you're adding a row.

## Thresholds Spreadsheet Ready for Uploading

Do the Upload Data File command to put the new row in the database. Empower will tell you that it added a new row to the database, just as we expected:

## Status Message After Adding a Row

Now download the Thresholds data to a spreadsheet again:

## Thresholds Spreadsheet After Adding a Row

You'll see the row you added, and (this is the key thing) you'll see the ThreshID it generated for the new row in column B. In this case it is 4. You need this value to link the new set of thresholds to your contract.

Next download the EuwtLinks spreadsheet, as you did at the beginning of this scenario. Now that you know the ThreshID of the new set of threshold values, you put that value (4 in this case) in the ThreshID column of that spreadsheet, making sure to put a 'c' in each row that you edited. Of course, if you only want the new set of threshold values to apply to certain elements of the contract, you'd only edit those rows of the spreadsheet. Here's the EuwtLinks spreadsheet ready for uploading:

## EuwtLinks Spreadsheet Ready for Uploading

Finally, use Upload Data to put this data in to the database, and you're done. Empower will notify you of every row that was updated, as below.

## Result of Uploading the EuwtLinks Spreadsheet

If you were using one set of threshold criteria when the units were dollars, and a different set when the units were, say, EQP, you would need to edit two EuwtLinks tables, one for dollars and one for EQP.

## 16.9.13 Manually Creating New Contracts, Periods, and Projects

Normally, users get their contract data from an earned value and/or scheduling system which export(s) a file that can be imported by Empower. However, sometimes users might wish to build a contract "by hand" instead of by importing. This section describes how to do that using the commands to download and upload data.

The workflow is:

1. Download, fill out, and upload the "New_Contract" template using the Download Data File command. This command will create a spreadsheet that you can populate with the data for the new contract (general contract data, WBS and OBS elements). You only do this step once for a new contract.

2. For each new period, you download, fill out, and upload the "New_Period" spreadsheet. This spreadsheet has tabs on which you fill out CPR/IPMR report header information, baseline changes, staffing data, earned value data, and future period data.

3. For each new period, if you have schedule (task) data, you will download, fill out, and upload the "New_Project" spreadsheet. This spreadsheet allows you to enter schedule data: tasks and task predecessors, including lead/lag relationships.

Here is an example of creating a contract manually. Here we download the new contract spreadsheet:

## Downloading the New_Contract Spreadsheet

The New_Contract spreadsheet will have several tabs on which you will enter data. The first thing to notice is that there is a Notes tab that explains how to fill out each tab. Make sure you read this. Here is the Contract tab:

## Blank New_Contract Spreadsheet

We enter the name of our new contract ("MOH-3") below the ContrName label:

## New Contract Name

We select the Structure-WBS tab and enter the WBS structure, making sure we enter the elements in hierarchical order.

## Entering the WBS Elements

We do the same on the Structure-OBS tab, as shown in the figure below. As the Notes tab informs us, we can add other structures by adding a tab to the spreadsheet.

## Entering the OBS Elements

On the Calendar tab, we choose not to go with the default calendar, named "(Default)" and create our own (named "MOH-3") instead. We enter the period end dates for our calendar under Calendar Detail.

## Entering the Calendar Data

We have finished filling out the New_Contract spreadsheet. We upload it with the Upload Data command, to get the following in the status windows, as shown in Figure 16.93.

## Uploading the New_Contract

Next, we create a new period by selecting "Manually Create New Period" and the MOH-3 contract in the Download Data dialog.

The New_Period spreadsheet has several tabs; Empower will pre-enter some of the period information for you. As before, reading the Notes tab first will help you fill out this spreadsheet correctly.

We fill out relevant information on the various tabs of this spreadsheet; Figure 16.94 shows the Period Data tab.

## Period Data Tab Filled Out

Figure 16.95 shows the Baseline Changes tab filled out; there are also tabs for Staffing-EAC and Staffing-BAC, not shown here.

## Baseline Changes Tab Filled Out

Figure 16.96 shows the Earned Value tab. Notice that you can enter data on this tab for multiple structures and units. In this figure, we see values for WBS Dollars, WBS Hours, OBS Dollars, OBS Hours, and WBS EQP.

## Earned Value Tab Filled Out

In the same way, you can enter multiple structures and units for Future ETC, as shown in Figure 16.97.

## Future ETC Tab Filled Out

Once we're done filling it in, we upload the New_Period spreadsheet and we see the status window shown in Figure 16.98:

## Uploading the New_Period Spreadsheet

Next, we download the New_Project Spreadsheet, which should be a familiar process by now. Again, read the Notes tab first. We do that, and fill out the Project and Tasks tabs. Here is part of the Tasks tab, in which we enter the tasks, their predecessors, and any lead/lag relationships. We also enter the WBS number to which the tasks should be linked. We have also added a tab for OBS links (per the Notes) and entered those links.

## New_Project Spreadsheet, Tasks Tab

Finally, we upload this spreadsheet. Assuming all has gone well, we recalculate the contract and we are ready to use Empower's features to analyze our data. When we have a new period's worth of data, we repeat the process above for the new period and project.

## 16.9.14 Entering CFSR Data

To enter CFSR (Contract Funds Status Report) data, we begin by downloading the Thresholds table using the Download Data File command. The Thresholds table is a shared item, so it is listed in the upper list box. The Thresholds spreadsheet has two tabs, named "Thresholds" and "CFSR"; we open the spreadsheet and choose the CFSR tab. The result is shown in Figure 16.100.

## The CFSR Thresholds Download

A default set of CFSR thresholds exists (row 9). We will add a new set for use with the MOH-2 contract. Figure 16.101 shows the table with the data for the new row. We have entered a name ("MOH-2") in the CfsrThDesc column. The next two columns (TpDol and TpPct) contain the threshold values for the Target Price, in dollars and percent. The TpAndOr column indicates how the dollar and percent thresholds will be combined to form the test. The "A" means "And". Taken together, these three columns mean that the Target Price test will fail if the actual price exceeds the target price by more than 1000 dollars AND the actual price exceeds the target price by more than 1 percent. The CFSR test logic is like the VAR threshold logic; see Section 16.9.12 for more details. The rest of the columns work the same way for Not Definitized (Nd), Accrued Expenditures (Ae), and Actual Expenditures (Ac). Finally we put an "a" in the action column since we will be adding a record to the database.

## Entering CFSR Threshold Values for MOH-2

Once we have finished filling out the threshold values, we upload the spreadsheet. Then we download it again to get the ID that Empower has assigned to the row it added. The downloaded spreadsheet is shown in Figure 16.102; the ID for our new row is 2 (in the CfsrThID column). We make a note of this.

## The New CfsrThID Value for MOH-2

We need to associate this set of thresholds with the MOH-2 contract. To do this, we download the Contracts table, go to the Settings tab, and put the CfsrThID value we just made note of in the CfsrThID column. This is shown in Figure 16.103. (The CfsrThID column is many columns to the right of the ContrName; we have hidden the intervening columns to make the figure clearer.) Note that we have put "c" in the action column because we are changing an existing row in the Contract table, not adding a row. Once the change has been made, we upload the spreadsheet.

## Assigning the new CFSR Threshold Record to the MOH-2 Contract

Now we download the CPR Headers table for the MOH-2 contract, open the resulting spreadsheet, and select the CFSR tab. See Figure 16.104.

## CPR Headers, CFSR Tab

We fill in the relevant information and put an "a" in the action column, since we are going to be adding a record to the database. (How do you get the Period ID? You can download the Periods table for the relevant contract, or open the contract and period in Empower, choose Options > Show IDs from the menu, and get the Period ID from the value of cd, which is our shorthand for the Period ID. Knowing how to do this qualifies you as a power user.)

Also notice the "Notes" tab in the Cprs download file; this tab lists descriptions of the fields in this download for use as a reference when filling out information.

## CPR Headers, CFSR Tab with Data

We upload this spreadsheet and open the CFSR Reconciliation Report, shown in Figure 16.106.

## CFSR Report

Note: The only EDI export/import format that currently includes the CFSR data is the Empower optimized format, so if you are going to export files containing CFSR data, make sure you check "Empower-optimized" on the Export EDI File dialog.

## 16.9.15 Setting EocType for Element of Cost Units

You must identify a unit as an element of cost for that unit to be treated as such in the Element of Cost report and the Element of Cost charts. This is done on a per-contract basis; so, for instance, LAB $ could be an Element of Cost in contract A, but not in contract B, if you wished.

To set the EocType for units in a given contract, use Admin > Download Data, select Contract Units and the desired contract, and click Download. In the resulting spreadsheet, set EocType to 1 for all units you want treated as Elements of Cost.

Figure 16.107 shows (in the red box) the five units that are Elements of Cost for the contract MOH-2.

## Setting ContrUnit.EocType

Then put a "c" in the action column for all changed rows and upload as usual.

## 16.9.16 Setting Contract Templates

Templates for items like VAR, SOW, or EAC narratives can be assigned by contract using the "Contract Templates" data download.

## Data Download for Contract Templates

The resulting download has two tabs. The first tab lists contract template assignments for the selected contract.

## Contract Templates First Tab

The second tab is informational. This tab lists available templates, and can be used as a reference when assigning templates on the first tab. The "DefaultFor" column indicates what the template is used for. Only one of each "DefaultFor" (aside from 32 which indicates email templates) can be assigned to a given contract.

## Contract Templates Second Tab

Note that assigning templates does not apply to Email Templates. When choosing an email template, all available templates of that type will be listed, regardless of contract assignment. If a contract does not have a template assigned, Empower will default to using whichever template of that type is available.
