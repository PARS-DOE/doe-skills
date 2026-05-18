# 16.5 Export IPM Reports

This menu option allows the user to export the Integrated Program Management Report (IPMR) as an Excel spreadsheet file.

(The IPMR format is similar to the older CPR format. Whether this command will produce one of the IPMR formats or a CPR format depends on the value of the CprDid field in the Contract table "Settings" tab for the given contract. A CprDid value of 1 generates the CPR format and a value of 2 produces the 2015 IPMR format. To change this value in the database, use the Download Data File and Upload Data File commands, as explained in Section 16.9.)

Clicking this menu option brings up the Export IPMR dialog shown below:

## Figure 16.38: Export IPMR Dialog

The user chooses the contract, the period, and the units with the selection boxes across the top of the dialog.

The "Export to" dropdown allows you to select what level you would like to export to: Reporting Level, Control Account Level, or Lowest Level. These levels are controlled by setting the RptElem field in the "Element Reporting" data download. Section 16.9.1 explains how to do this.

You can indent the WBS/OBS numbers and descriptions to show the hierarchical structure by checking "Indent by level:"; you can set the amount of indentation with the associated text box. This option is on by default.

If the option "Hide WBS number" is checked, the WBS numbers will not be written in the list of elements in block 8.a of the IPMR Format 1 (and the equivalent block in the Format 2).

If the option "Use long descriptions" is checked, the long description (instead of the short descriptions) will be shown in the block 8.a of the Format 1 (and equivalent for Format 2).

If "Ignore null-value elements" is checked, elements without data will not be shown in the output.

The two dropdown lists on the right side of the dialog allow the user to export Format 1 and Format 2 with the selected reporting structure.

## Figure 16.39: Export IPMR Dialog, Multiple Units

Figure 16.39 shows that you can export CPRs or IPMRs for multiple units with one command by selecting multiple units and clicking the Export button as usual.

Once you have chosen the desired contract, period, units and options, press the Export button. Empower will generate the requested Excel file and the browser will download the file in its usual fashion.

## 16.5.1 How Empower Populates the IPM Report after an OTB

Empower ONLY displays values in IPMR Block 8 columns 12a, 12b, 13 and Block 9 when an OTB date is entered in the CPR Header table for that period and the OTB date is prior to the end date of that period.

For the dollar unit, Block 9b Column 14 is the CBB entered in the CPR Header table for that period. Block 9b Column 15 it is the Most Likely EAC (EacML) entered in the CPR Header table for that period.

For any unit other than dollars, Block 9b Column 14 is a calculated field. This is done since there is typically no CBB for units other than dollars. For other units, the calculation for Block 9b Column 14 is to subtract the total budget adjustment (Block 8g Column 13) from the total budget (Block 8.g Column 14). In other words, the CBB = TAB - OTB Budget Adjustment.
