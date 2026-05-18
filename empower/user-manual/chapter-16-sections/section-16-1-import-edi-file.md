# 16.1 Import EDI File

The complementary functions Import EDI File and Export EDI File allow the user to import and export data to/from files in a variety of formats. This section describes the import functionality; the next describes the exporting.

Empower can import files in the following formats:

1. Empower's optimized archive format. This format is designed for rapid loading into the database, but it is not easily read by humans, as is Empower's native XML format. The optimized archive consists of a .zip file, containing a series of .txt files, each corresponding to a table in Empower's database.

2. XML files created by Empower itself or by wInsight. The user can import several XML files at once (if they are all in the same .zip archive), and choose to import all or parts of a file. The XML file can contain several datasets. (Recall that a dataset means a particular combination of contract, period, structure, and unit.)

3. CPR/IPMR files in the UN/CEFACT format. Empower can import files in IPMR Formats 1–4, 6, and 7.

4. Files in the ANSI X12 839 format (*.trn) for electronic data interchange.

5. Empower-compatible XLS exports from Primavera P6. (A manual step is required before importing P6 exports; see Section 16.1.1.)

6. Files in the wInsight archive format (*.wsa).

7. IPMDAR JSON cost (CPD) and schedule (SPD) files.

8. DOE CPP JSON files.

In addition, Empower can import zip files containing one or more Empower or wInsight XML, UN/CEFACT, ANSI X12 or P6 files.

The Import EDI File menu option brings up the following dialog box:

**Figure 16.3: Import EDI File Dialog, Before Choosing File**

Note that the input file could be a plain XML file (typically with a .xml file extension), a zipped file containing one or more XML or .txt files (.zip extension), a file in the ANSI X12 format (.trn extension), or a file in the wInsight archive format (.wsa extension). Empower will recognize the format of each file and import the data appropriately.

(See http://dcarc.cape.osd.mil/CSDR/Default.aspx for more information on the UN/CEFACT standards.)

The user clicks Choose File, which brings up a file selection dialog. Once the user has chosen a file through this dialog, Empower's dialog changes slightly, as shown below. Note that now the name of the chosen file appears (ThreeContracts.zip in this example).

**Figure 16.4: Import EDI File Dialog, File Chosen**

Now the user presses Upload, and the dialog changes appearance to look like the figure below.

**Figure 16.5: Import EDI File Dialog, After Upload**

Note that the Upload step is just the first part of the import process. At this point, Empower has opened the selected import file and listed all the XML files it contains (recall that zipped and WSA import files can contain multiple XML files).

Now the user selects which file(s) he or she wants to import, and various import options. In Figure 16.5, importation of custom fields and user data has not been selected, and the user has not asked to recalculate after the import (see Section 16.2 on recalculating). We will discuss the import options later in this section.

Now the user presses Import.

Once Import has been pressed, the dialog gives a real-time update on the progress of the operation, as shown in the upper portion of Figure 16.6.

**Figure 16.6: Import EDI File Dialog, Import Completed**

In the figure, the progress is reported in increments of 10 percent. This is the default. If the file being imported is larger than usual, the progress will be reported in steps of 5 percent. The progress on really large files will be reported like this: "1..2..3..".

When the operation is complete, the dialog will show the results. In Figure 16.6, note that the import has completed successfully.

## 16.1.1 Importing Primavera P6 Schedule Files

Empower can import schedule files that were exported from Primavera P6 in an XLS format.

To import such a file, Empower needs some information that is not natively contained in the P6 export. For instance, the P6 file doesn't identify the contract name or period end date, and there are a few other pieces of information necessary for importation into Empower. Accordingly, after exporting the file from P6, the user needs to perform a manual step before importing the file into Empower.

Begin by opening the P6 export file in your spreadsheet program. Add a sheet named "EMPOWER", and add to this sheet the additional information we require, as described below.

The EMPOWER sheet can be in any location. The information you will need to add to the EMPOWER sheet is listed below. The field labels (e.g., "ContractName") go in Column A, while the actual values go in Column B.

| Column A | Column B |
|----------|----------|
| ContractName | The name of a contract already in your Empower database. |
| PeriodEndDate | The end date of an existing period in the named contract. |
| ProjectName | Optional; if not provided defaults to Contract name. |
| WBSPrefix | Optional; if provided Empower strips this off the TASK.wbs_id values when populating the LinkVal of the task. Note that the separator (in the figure below, '.') is included in the text that will be stripped off. |
| BaselinePrefix | The prefix of the columns that should be used for the baseline. Primavera stores multiple baselines; on the TASK tab, you'll see, e.g., target_start_date, base_start_date, primary_base_start_date, secondary_base_start_date, etc., along with their corresponding end dates. Note that the separator (in the figure below, '_') is included in the text that will be stripped off. |

(You can also add column mapping information on this tab; we will discuss this refinement at the end of this section.)

Here is an example of a populated Empower sheet of a P6 file that will be imported into Empower.

**Figure 16.7: EMPOWER Tab for P6 Import**

And here is part of the TASK tab of the same P6 file:

**Figure 16.8: TASK Tab for P6 Import**

This tells you that Empower will match the tasks in the P6 file with the WBS elements in the Empower database by stripping off "Missile-Sys." from the wbs_id value; so that the task with Activity ID of "A1110" and wbs_id of "Missile-Sys.1" in the P6 file will be attached to the element in the Empower database with a WBS of "1".

Likewise, the Baseline Prefix value of target_ means that Empower will pick the start date from target_start_date, the end date from target_end_date, and so on.

After adding the EMPOWER sheet and populating it, the user should save the file as an XLSX. (Empower will still read it if you leave it as an XLS file, but we recommend XLSX, since an XLSX is a compressed format and loads more quickly.)

Once you have finished this manual step, you can import the P6 file you have just modified using the Import EDI File command.

It sometimes happens that your P6 export might have column headings that are different from the default column headings Empower expects. You can handle that situation by mapping the columns as they appear in your P6 export to the one that Empower expects. You do this on the EMPOWER tab you have already added, which allows you to leave alone the information on the tabs generated by the P6 import process.

Here is a description of the mapping process: For instance, we expect sheet TASK, cell D1 to be "wbs_id". But if your P6 export writes "wbs" there, you can set a mapping so that you don't have to change that cell. To do that, on the EMPOWER tab, you would enter "LinkVal" in cell A6, and "wbs" in B6.

If there is another change, add that at row 7, and so on.

Order doesn't matter, but in case of duplicates, last row wins. For example, you can already specify which baseline fields to use, via the BaselinePrefix entry at line 5. But if you add BaselineStart, BaselineFinish, or BaselineDuration lines at row 6 or below, those will override the value specified in Row 5.

The default mappings are shown below. You shouldn't change what is in column A. Whatever you enter in column B must appear in row 1 of the TASK or TASKPRED sheets.

**For headings appearing on the TASK tab:**

| Empower | P6 |
|---------|-----|
| UIDD | task_code |
| TaskName | task_name |
| Summary | (not applicable) |
| Milestone | task_type |
| Critical | actv_code_critical_id |
| Duration | total_drtn_hr_cnt |
| BaselineDuration | target_drtn_hr_cnt |
| ActualDuration | act_drtn_hr_cnt |
| RemainingDuration | remain_drtn_hr_cnt |
| Start | start_date |
| Finish | end_date |
| ActualStart | act_start_date |
| ActualFinish | act_end_date |
| BaselineStart | target_start_date |
| BaselineFinish | target_end_date |
| EarlyStart | early_start_date |
| EarlyFinish | early_end_date |
| LateStart | late_start_date |
| LateFinish | late_end_date |
| PercentComplete | drtn_complete_pct |
| AssessedPctCmp | calc_phys_complete_pct |
| FreeFloat | free_float_hr_cnt |
| TotalFloat | total_float_hr_cnt |
| ConstraintDate | cstr_date |
| ConstraintType | cstr_type |
| Slip | var_end_date_drtn_hr_cnt |
| StartVar | var_start_date_drtn_hr_cnt |
| LinkVal | wbs_id |

**For headings appearing on the TASKPRED tab:**

| Empower | P6 |
|---------|-----|
| TaskID | task_id |
| PredID | pred_task_id |
| LagVal | lag_hr_cnt |
| LagType | pred_type |

### 16.1.2 Contract Merging

Now to backtrack a bit and explain the "Merge with" select box visible in Figure 16.5.

Contract merging is designed for a situation in which the prime contractor has subcontracted out part of the work detailed in the WBS. When the subcontractor supplies earned value information to the prime contractor in electronic form, the "Merge with" option allows the prime to merge the subcontractor's data with the data the prime already has in its Empower database. In general, for this to work, the subcontractor has to use the same WBS numbers, period end dates, and unit names as the prime since Empower uses those items to match the merged data with the data already in its database.

For each element in the import file, Empower searches for a matching element in the "Merge with" contract. For each matching element, the earned value and future ETC numbers in the imported file are added to the equivalent numbers in the database.

For example, assume that in contract MOH-2, element 3100 had a BCWS of 394.4. Imagine further that a subcontractor provides a file where element 3100 has a BCWS of 100. If the input file is merged with contract MOH-2, element 3100 will have a BCWS of 494.4 after the merge.

Note that summing only happens during the merge if multiple subs are contributing to the same element in the prime. If there is no overlap between the elements in the sub and the elements in the prime, naturally no summing will take place.

When merging a source contract (the import file) into a target contract (in Empower), if the source exists in Empower as a separate contract from the target, the user doing the merge must have at least "read" access to the source contract in order to perform the merge.

### 16.1.3 Import As

The "Import As" text box allows you to import a contract under a new contract name. This feature can be used to troubleshoot imports without impacting existing contracts. For example, if we uploaded a file for the MOH-2 contract but input MOH_TEST in the "Import as" box (see Figure 16.9), we would create a new contract called MOH_TEST instead of importing into the MOH-2 contract.

**Figure 16.9: Import EDI File, Import As**

Note that you cannot use the name of an existing contract for "Import As."

### 16.1.4 Add new Elements/Structures/Units

The three checkboxes: "Add new elements", "Add new structures", and "Add new units" have similar behavior. If, say, "Add new elements" is not checked, Empower will not add any new elements it finds in the import file to its database. So, for instance, if a certain element occurs in the input file, but it isn't already in the database and "Add new elements" is unchecked, this element will not be added to your database, and any other data (e.g., earned value data) associated with that element will likewise be ignored on import. This can be useful if you or organization is importing files from sub-contractors and these files contain elements, structures, and/or units that do not occur at the lowest level of your WBS or OBS. You don't want to clutter up your database with units that your sub-contractors use but which you don't ever use. Unchecking one or more of these checkboxes as appropriate can avoid that problem.

### 16.1.5 Import Future Period Data

When this option is checked, future period data will be imported.

### 16.1.6 Import Schedule Data

If this option is checked, schedule data will be included in the import.

### 16.1.7 Import User Narratives and Inputs

When this option is checked, user input data (e.g. VAR Narratives) will be imported. Note that in order for user input data to be imported, the user should either already exist in the database, or be included in the import file and imported with "Import user data" checked.

### 16.1.8 Import Shared Items

When this option is checked, shared data such as Thresholds, Weights, and Calendars will be imported.

### 16.1.9 Import User and Portfolio Data

When checked, user information from the import file will be added or updated in Empower.

### 16.1.10 Import Custom Fields and Data

If this option is checked, custom fields that are present in the import file but not in the database that you are importing into will be added. Any data for those fields will also be added.

If this option is not checked, the import will ignore any fields that do not exist in your database. In the import status, you may see messages like "Ignoring in Cpr.txt: PlanEstCompl". This indicates that a field was ignored in the import.

### 16.1.11 Import Audit Metrics and Inputs

The "Import Audit metrics and inputs" checkbox is an advanced option and should usually be left unchecked. Checking this box will import Audit reports, tests, and values from the import file. This can be useful when transferring data within the same organization, but should not be used if the file contains different tests than the ones used at your site to avoid unintentional overwriting of your local Audit reports and tests.

### 16.1.12 Show Periods

On import, if the uploaded file is an Empower optimized data file with an "ALLPER" entry, you'll see an additional checkbox toggle called "Show periods" appear in the Import EDI dialog.

**Figure 16.10: Show Periods, not toggled**

On toggle, a list of the periods for the selected contract will appear in the selector.

**Figure 16.11: Show Periods, toggled**

Unchecking the option will toggle back to show the list of "ALLPER" entries.

### 16.1.13 Clean non-ASCII Characters

If "Clean non-ASCII characters" checkbox is checked, Empower will change any non-ASCII characters in the input file to one or more "#" characters as it imports. (The input file will remain unchanged.) So, for instance, if a text field in the input file contained the word "über", in the Empower database it would be changed to "#ber" or "##ber" (depending on the original encoding in the input file).

### 16.1.14 Download Converted Files

If "Download converted files" is checked, the imported file will be written out to a file on your computer. This can be useful for debugging purposes. The downloaded file will be in Empower format. It will be typically named "converted.zip" and saved where Empower normally saves downloaded files. Note that if "Download converted files is checked", nothing will actually be imported into Empower; you will only download the converted file.

### 16.1.15 Prune Alternate Structures

This import option allows you to prune data on import, only storing lowest-level data once. This is especially helpful for sites with multiple large contracts. Pruning these contracts on import reduces the amount of data that needs to be stored in the database.

When importing into an existing pruned structure, the data being imported must be prunable or pruned. If this option is not checked when importing into a pruned structure, the import will automatically be pruned.

**Figure 16.12: Import EDI File, Pruning Import File**

If importing a file into a unpruned structure with "Prune alternate structures" checked, the import will not be pruned, and you will see a message like:

**Figure 16.13: Import EDI File, Target Unpruned**

If the import file is not prunable, you may see a message like:

**Figure 16.14: Import EDI File, Not Pruning Import File**

If the import file and target contract pruning status are incompatible, the import will abort with a message indicating the discrepancy. If the import file is pruned, but the target contract is not pruned, you may see a message like the following:

**Figure 16.15: Import EDI File, Not Importing**

If the import file is not prunable, but the target is pruned, you may see a message like:

**Figure 16.16: Import EDI File, File Not Prunable**

For more information, see the technical note "Pruning Data in Empower," available on our support website http://encoreanalyticsllc.freshdesk.com/support/solutions.

### 16.1.16 Validate Import File

When importing an Empower optimized file, the option "Validate import file" is available. This feature is only available for optimized files. If checked, this option will check the import file for common data problems. Validation failures or warnings will appear in the status messages, but the data will not actually be imported.

**Figure 16.17: Import EDI File Dialog, Validate Import File**

For example, you might see some of the following messages when validating a file:

**Figure 16.18: Validate Import File Messages-1**

**Figure 16.19: Validate Import File Messages-2**

**Figure 16.20: Validate Import File Messages-3**

These messages indicate problems in the import file and provide details on the type of error and location of the problem in the import file. The intent of this feature is to find data problems in import files before actually importing the data so that those problems can be corrected in the source.

If there are no errors in the file like the ones listed above in Figures 16.18, 16.19 or 16.20, the validator will also run checks on the element hierarchy.

**Figure 16.21: Hierarchy Check Messages**

The hierarchy validation will check for the following:

- Elements present in the import file that are not in the database
- Elements that have a different parent in the import file than they do in the database
- Elements that are in the database but not in the import file

These warnings indicate changes to the hierarchy, but do not necessarily indicate an error if those changes are intentional.

### 16.1.17 Optimized File Import Formatting Issues

On import of an Empower optimized file, you may encounter a message like this:

**Figure 16.22: Optimized Import Message**

The message indicates the "BaselineChg.txt" file in your import file has a formatting issue related to the number of fields in the file. This could mean that your file has a record (or records) with a different number of entries than the number of fields that should be in the file as indicated by the list of fields at the top of the file. Notice that the message provides a number [216]; this indicates the line in the "BaselineChg.txt" file where the problem was encountered.

Since the "Optimized" file format is a zip file containing tab delimited text files, a likely cause of formatting issues is having extra or missing tabs in your file.

Other formatting issues include but are not limited to:

- Wrong table name in the file header
- Incorrect or missing field format codes in the file header (e.g. numeric fields 'n' marked as date fields 'd')
- Text files missing key fields such as ID fields
