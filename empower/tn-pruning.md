# TN Pruning

*Source: TN-Pruning.pdf*

---

## Technical Note: Pruning Data in Empower

© 2013 Encore Analytics, LLC
October 13, 2023

## Contents

1. Pruning in Empower . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2
   1.1 Requirements for pruning . . . . . . . . . . . . . . . . . . . . . . . . . . . 2
   1.2 What pruning does . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3
   1.3 How to prune . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4
   1.4 Pruning Example . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4
   1.5 Check Prune Status . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8

2. Exporting Pruned Data . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 10
   2.1 Export to Reporting Level for Pruned Structures . . . . . . . . . . . . 10

---

## Chapter 1: Pruning in Empower

Empower allows you to "prune" data so that lowest-level and control account data is only stored once for a contract. This is especially helpful for sites with multiple large contracts. Pruning these contracts reduces the amount of data that needs to be stored in the database, which can greatly improve performance and recalculation times.

Another advantage of pruning is that it allows DQIs and cost schedule dates (CSD) to be displayed for alternate structures. When your data is not pruned, DQIs and CSDs are only available for the WBS. Similarly, if your alternate structures are pruned, then "TaskLink" only needs to be filled out for your WBS structure. You will see your schedule data displayed when viewing a pruned non-WBS structure, even if "TaskLink" is not filled out for that structure.

Note: Throughout this document we will use CA/SLPP. These are values for "ElemType" (element type) that should match the CaSym and SlppSym settings for your contract, as set in the "Contracts" file.

### 1.1 Requirements for pruning

Pruning is an optional operation and depends on the ElemType field. We will refer to the structure we want to prune as the "target structure." In order to be "prunable" a contract must meet certain criteria:

1. Every lowest-level element in the WBS (excluding PMB and the Unlinked Tasks element) must have a control account in its ancestry.
2. Every CA/SLPP in the WBS must also appear in the target structure.
3. There are no non-CA/SLPP elements in the target structure that are marked CA/SLPP in the WBS.
4. Every CA/SLPP element in the target structure must appear in the WBS.
5. No CA/SLPP element in the WBS can have a CA/SLPP ancestor.
6. No CA/SLPP element in the target structure can have a CA/SLPP ancestor.

Note that pruning will not reduce the size of your WBS structure.

For non-WBS structures, the lowest-level will be the level above CA/SLPP after pruning. Pruning automatically creates a mapping that ties WBS summary elements to their counterparts in non-WBS structures. This mapping can be viewed by downloading "ElementMapping" via "Admin > Download Data File."

The advantage of pruning alternate structures is that your lowest-level and control account data is only stored once; for the WBS structure. Typically, this will reduce the amount of data stored for each alternate structure by about 90%. For very large contracts this can yield significant improvements in recalculation times.

### 1.2 What pruning does

When you "prune" a structure in Empower, the pruning process will do the following:

1. Create "ElemLink" records that map CA/SLPP elements in the WBS to the parents of matching CA/SLPP elements in the structure that is being pruned. Note that children of CA/SLPP will remain attached to their original CA/SLPP parents.

2. Delete the children of CA/SLPP elements in the alternate structure that's being pruned, along with all associated data for those children.

3. Delete CA/SLPP elements from the structure that's being pruned, along with all associated data for those elements.

Note that this process will permanently delete data. Recall that when we "prune," we only store data for CA/SLPP and lower-level elements in the WBS, so those items will be removed from the structure that is being pruned. Empower will "unprune" data on export where appropriate, see the section titled "Exporting Pruned Data" later in this document for more details.

### 1.3 How to prune

There are two ways to prune data in Empower. The first is to select the "Prune Alternate Structures" option when importing your data. This option will prune your data, if possible. If pruning is not possible for a structure, that structure will not be pruned. To see which structures, if any, have been pruned, use the "Check Prune" user script (available from Encore Analytics support).

If you would like to prune all data that you import into Empower (where possible), you can set the "ENFORCE_PRUNE" option in the Empower configuration file. See the technical document titled "The Empower Configuration File" for more details.

The second option allows you to prune alternate structures for contracts that are already in Empower. To do this, first make sure that a recalculation has been done on the contract, then run the "Can Prune" user script to determine if the contract can successfully be pruned. This script will return an Excel file with information on whether or not the selected contract and structure can be pruned. If the contract can be pruned, run the "Do Prune" user script to prune the selected structure for the contract. If not, you can use the information from "Can Prune" to find and correct any issues with the structure. After running "Do Prune," recalculate a period for the contract.

The "Can Prune" and "Do Prune" scripts are available on request from Encore Analytics support.

### 1.4 Pruning Example

Suppose that we want to prune the OBS structure for the contract MOH-2.

#### 1.4.1 Can Prune

First, run the "Can Prune" script for the OBS structure to determine if it can be pruned.

**Figure 1.1: Can Prune Script**

This script will prompt you to select the contract and structure that you would like to check.

The resulting XLSX file will have six tabs, each of which lists any elements that fail the check for that tab. These checks correspond to the pruning requirements listed earlier in this document.

The first line of each tab describes the test being done for that tab. If any elements are listed on a tab, use the description of the check to determine the appropriate action necessary to fix. Once you have made your fixes, run "Can Prune" again. When all of the tabs are empty the structure can safely be pruned.

The checks for each tab are shown below:

**Figure 1.2: Can Prune Result, Check 1**

Check 1 lists any lowest-level WBS elements that do not have a control account somewhere in their ancestry. The element's Bac and Lref for the most recent period (if any) are shown as well.

**Figure 1.3: Can Prune Result, Check 2**

Check 2 shows any CA/SLPP elements in the WBS structure that are not found in the target structure.

**Figure 1.4: Can Prune Result, Check 3**

Check 3 lists any non-CA/SLPP elements in the target structure that are marked as CA/SLPP in the WBS.

**Figure 1.5: Can Prune Result, Check 4**

Check 4 lists CA/SLPP elements in the target structure that are not found in the WBS.

**Figure 1.6: Can Prune Result, Check 5**

Check 5 lists CA/SLPP elements in the WBS structure that have at least one CA/SLPP descendant. In order to be prunable, CA/SLPP elements in the WBS cannot have a CA/SLPP ancestor.

**Figure 1.7: Can Prune Result, Check 6**

Similar to the previous check, Check 6 lists CA/SLPP elements in the target structure that have at least one CA/SLPP descendant.

#### 1.4.2 Do Prune

Next, run the "Do Prune" user script to prune the target structure. At least a per-period recalc should be run on the contract that you want to prune before running this script.

**Figure 1.8: Do Prune Script**

Note that, depending on the size of your data, this script may take some time to run. The script will prompt you to select the contract and structure that you want to prune.

**Figure 1.9: Select a Structure**

Finally, once the script completes, run another per-period recalculation on the contract.

Note: We do have a server-side script that can repair and prune all contracts and structures in a specified data source automatically. If you have many contracts that should be "prunable," you can contact Encore Analytics tech support to discuss particulars and the possibility of using this script.

### 1.5 Check Prune Status

You can check the current prune status and prunability of your contracts by running either the "Check Prune" or "Check Prune All" scripts. For best results these scripts should be run after running a recalculation for the contract. A result file for "Check Prune" is shown below:

**Figure 1.10: Check Prune Result**

The "CanPrune" column in the resulting file indicates whether the structure can be pruned, while the "IsPruned" column indicates whether or not that structure is pruned. The "Check Prune All" is similar, but will list results for all of your contracts instead of a selected contract.

If you encounter an unusual result (e.g. CanPrune blank with IsPruned = 1), the contract likely needs to be recalculated. If the issue persists, there is likely a problem in the structure for the contract.

These scripts are available on request from Encore Analytics support.

---

## Chapter 2: Exporting Pruned Data

When exporting non-optimized format EDI files, Empower will automatically unprune data where appropriate.

For UN/CEFACT and wInsight exports, if "Export to reporting level" is not selected the data will be automatically unpruned on export.

When exporting, you have the option to export to the reporting level, control account level, or lowest level. Exporting to the control account will include data at and above the control account level. Exporting to the lowest level will export from the lowest level of the tree and up. Exporting to the reporting level will behave as usual for unpruned structures (see the section titled "Setting the Reporting Level" in the Empower User's Manual), but does have some restrictions for pruned structures.

### 2.1 Export to Reporting Level for Pruned Structures

Consider the pruned OBS for the "MOH-2" contract. The screenshot below shows a portion of the "Elements" download for the pruned OBS structure.

**Figure 2.1: MOH-2 OBS Element Download**

If we download the "Element Reporting" table for the OBS we see the following:

**Figure 2.2: MOH-2 OBS Element Reporting**

The "RptElemE" field in the "Element Reporting" download allows you to set the reporting level for EDI exports, while "RptElem" sets the reporting level for IPMR exports. We will focus on "RptElemE" for this example, but the same logic applies for "RptElem."

An attempt to do an EDI export of the OBS for this contract with "Export to Reporting Level" selected and these RptElemE settings will fail with the following message:

**Figure 2.3: MOH-2 EDI Export Message**

The reason we get this message is because of the way we have the reporting level set for the OBS elements "ENG" and "ENG-T." The way the reporting level is set currently, "ENG-T" is the lowest level that we're exporting for that branch of the tree. However, if we look at the Element Links for the OBS, notice that we have control accounts linked to both "ENG-T" and its parent, "ENG."

**Figure 2.4: MOH-2 OBS Elem Links**

Notice that "5000" is mapped to "ENG" and "6000" is mapped to "ENG-T." So we have a CA mapped to the "lowest level" that we're exporting, as well as a CA mapped to that element's parent. If we opened the OBS in the sort window and turned on tree mode, we would see this tree structure:

**Figure 2.5: MOH-2 OBS Tree**

Notice that "ENG-T" and "5000" both contribute to "ENG", but recall that "5000" is a CA, so it is not actually stored in the OBS. Since Empower automatically unprunes on export, "5000" would not be included in this export, were it to continue.

If we were to export this data with our current "RptElemE" settings, the value for "ENG-T" would overwrite any contributions that "5000" would have made to "ENG" since we will sum up from the bottom of the reporting structure. If the export were to continue instead of exiting with a message, the exported file would not sum correctly. When exporting to the "Reporting Level," Empower will sum from the level that you indicate as the lowest level.

We could also adjust the "RptElemE" settings so that "ENG-T" is not being exported. For example, we could use these settings instead:

**Figure 2.6: MOH-2 OBS RptElemE Settings**

Since "ENG-T" is no longer being exported, we will not encounter the summing problem and can export as usual.

**Figure 2.7: MOH-2 EDI Export**
