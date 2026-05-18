# 16.4 Export EDI File

This menu option allows the user to write all or part of an Empower database to an external file.

The data can be exported to an XML file in Empower's native XML data exchange format, to Empower's optimized format, to an UN/CEFACT XML file, IPMDAR JSON CPD or SPD, DOE CPP JSON, or to a wInsight-compatible archive. The user can write one dataset, or several datasets. The default is to write the data to a zipped file (extension `.zip`) containing one or more XML or text files, although the user can choose to create a wInsight archive.

A wInsight archive differs from Empower's native XML format in the following ways (in addition to the change in file extension):

- A FILELIST.TXT file is added to the zip file
- Empower-only fields aren't exported
- The headers of the XML files are changed to match wInsight's header format, not Empower's

Despite the different file extension, wInsight archives are compressed in the same way as .zip files and can be uncompressed using the same unzipping tools, though some tools might require you to change the extension to `.zip`.

To export from Empower and import into wInsight, you must check the option "wInsight XML."

Selecting the Export EDI File command brings up the dialog shown in Figure 16.33 below.

## Export Dialog Overview

Figure 16.33: Export EDI File Dialog, Choosing What to Export

The user can select one or more contracts to export by selecting the appropriate entries in the Contracts select box. If the user wishes to export all periods in the database for the selected contracts, they just press the Export button below this select box.

If, on the other hand, the user wishes to export only certain periods, they select the contract as before, but then choose the desired periods in the Periods select box and press the Export button below the Periods select box.

**Note:** Selecting an export by period is limited to one contract. If multiple contracts are selected in the select box, the periods shown in the Periods select box will be those from the uppermost selected contract.

The export can be further refined by choosing which structures and units to export, using the appropriate select boxes at the top of the dialog. If only the Work Breakdown Structure, for instance, is desired, the user would select just "WBS" in the Structures box.

In addition, the user can customize the export with the checkboxes in the lower part of the dialog. The user can choose to export or leave out of the export things like future period data, schedule data, and so on, as shown in the figure above.

The first three options are checked by default, while the last five, being used less often, are unchecked by default.

### Multiple Structures with the Same Export Name

When exporting, if you select multiple structures with the same export name you may see a message like one of the following:

Figure 16.34: Exported Multiple WBS Structures

Figure 16.35: Exported Multiple Structures With the Same Name

This could happen, for example, if you have both a WBS structure and a WBS formal reporting structure with the same export name and have selected both before exporting.

**Important:** Structures with the same export name cannot be included in the same export. (See Section 16.9.2).

## 16.4.1 Export to EDI Reporting Level

The "Export to (level)" dropdown deserves some explanation. The dropdown options include:

- Reporting Level
- Control Account
- Work Package
- Lowest Level

### Reporting Level

"Reporting Level" will use the reporting level to limit the exporting of EDI files (as described in this section), IMP Reports (Section 16.5), and Narratives (Section 16.6).

(Setting the reporting level is described in Section 16.9.1)

Here is the rule to keep in mind while setting the reporting level for an EDI export:

> If you define a reporting level for any structure in an export (i.e., every structure that you have highlighted in the Structures list box on the Export EDI dialog), you should define a reporting level for every structure in the export.

For example, suppose you have to report WBS and OBS, but you track WBS, OBS and IPT. You don't need to set a reporting level for IPT if you only export WBS and OBS.

### Control Account

"Control Account" will export everything down to and including your control accounts.

### Work Package

"Work Package" will export everything down to and including your work packages.

### Lowest Level

"Lowest Level" will export elements from the lowest level up.

## 16.4.2 Export Audit Metrics and Inputs

The "Export Audit metrics and inputs" option will export your audit reports, tests, and values. This is an advanced option and generally should only be used when moving data within the same organization or when using only the default reports and tests.

The recipient of the data should have the same tests as those in the exported file.

## 16.4.3 Use Alternate Calendar

The option "Use alternate calendar" allows you to export your data using a different calendar. You may want to use this option if, for example, you are submitting to a customer that uses a different calendar than you do.

To set up an alternate calendar for a contract, enter the alternate dates in the "AltDate" field in the "CalendarDet" table. This can be accomplished via a data download/upload of "Calendars."

The "AltDate" field is used to substitute EndDates in both the Period and the FutureEtc table when exporting with this option checked.

## 16.4.4 Export Recalc Products

The "Export recalc products" option allows you to export data calculated during recalculation of a contract, such as DQIs, colors/trends, and calculated Task and Earned Value fields for the "Empower optimized" format. You can then import those recalc products into a different Empower database, eliminating the need to recalculate the data in the new database after import.

Exporting **WITHOUT** this option checked reduces the size of the exported file and can help speed up the export/import process, but will require a recalculation after import.

## 16.4.5 Export Format

At the bottom of the dialog, there are several checkboxes to control what format the export is generated in. The resulting file or files are usually contained in a compressed file (i.e., a zip file), as indicated by the text "(ZIP)" after the first four options.

wInsight exports are handled in a slightly different manner, as described below.

### Default Format

The default is to export to Empower's optimized format. See Section 16.1 for more on this format.

### Empower XML Format

You can export to Empower's XML format by checking "Empower XML (ZIP)".

### UN/CEFACT Format

Checking one or both of the UN/CEFACT options will create an export according to the UN/CEFACT standard.

- Checking "1–4" exports the CPR/IPMR cost data (i.e., Formats 1 to 4)
- Checking "7" exports the time-phased cost data (i.e., Format 7)

Per the standard, Format 1–4 data and Format 7 data will be in separate files.

Furthermore, if you select multiple periods for a Format 1–4 export, each period will be in a separate file. (As usual, if the result is multiple files, they will be downloaded as a single zip file.)

**Important Note:** If you select a UN/CEFACT export, you can only export periods from one contract, as signaled by the graying-out of the Export button under the Contracts list box.

See [http://dcarc.cape.osd.mil/CSDR/Default.aspx](http://dcarc.cape.osd.mil/CSDR/Default.aspx) for more information on the UN/CEFACT standards.

### Formal Reporting Structures

Some export formats allow you to choose which structures to use as your "Formal Reporting Structures." For those formats, you will see two dropdowns on the right side of the dialog.

Figure 16.36: Export EDI File Dialog With Reporting Structure Dropdown

You will see these dropdowns for the UN/CEFACT and IPMDAR export formats.

### wInsight Export Format

You can export to a file compatible with wInsight by checking "wInsight XML".

As the dialog indicates:

- If you export a whole contract, the file will be in the wInsight archive format (WSA)
- If you export a single period, the result will be in a single XML file (no zipping)
- If you export multiple periods, the result will be multiple XML files contained in a single zip file

Exporting multiple periods by holding down the Shift key then clicking the "Export" button will result in a single XML file contained in a WSA file.

For the UN/CEFACT and wInsight exports, if "Export to reporting level" is not selected the data will be automatically unpruned on export.

### IPMDAR JSON Format

IPMDAR JSON cost or schedule files can be exported by checking "IPMDAR JSON cost" or "IPMDAR JSON schedule" respectively. These exports are done for a single period at a time.

Note that the IPMDAR JSON format requires that parents of work or planning packages be marked as control accounts or summary-level planning packages.

When the user presses either Export button, the dialog looks something like Figure...
