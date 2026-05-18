# Chapter 17: Using Empower's Element Mapping Functionality

*From the Empower User Manual*

---

## Chapter 17: Using Empower's Element Mapping Functionality

The element mapping functionality of Empower gives the user the ability to link elements in one structure to elements in another structure. The advantage of this is that earned value data can be loaded for just one structure, and then distributed to other structures. A common use case is to load data for the WBS structure, then use the element mapping functionality to link WBS elements to OBS elements.

In summary, the workflow is as follows:

1. Recalculate, if you are mapping from one or more summary-level elements, and haven't already done so.
2. Download the ElemLinks table, using the Download Data File command.
3. Edit the resulting ElemLinks spreadsheet. This is where you assign elements from the source structure to elements of the target structure.
4. Upload the ElemLinks spreadsheet. This creates ElemLinks records in Empower's database.
5. Run a User Script to copy the earned value data from records in the source structure to records in the target structure.
6. Recalculate. This completes the generation of data for the target structure.

Here is a detailed description of the procedure.

If you haven't already recalculated your contract, and you will be mapping from one or more summary-level elements, recalculate. This will populate the data for the source structure's summary elements.

---

## Downloading the ElemLinks Table

Next, download the ElemLinks table. We issue the Admin > Download Data File command to get the dialog box shown in Figure 17.1. In the Data Type list box, select "Element Mapping". The Contracts list box will be populated with all the contracts in our database. Select "MOH-2". The Source and Target list boxes will now be populated with the structures available in the MOH-2 contract. Select "WBS" in the Source list box and "OBS" in the target list box. The Download Data dialog should look like the figure below:

**Figure 17.1: Downloading the ElemLinks Table**

Click Download. A spreadsheet file will be created and saved on your computer.

The resulting spreadsheet will have two tabs, one for the source structure (SRC-WBS in this case) and one for the target structure (TGT-OBS). In the figure below, we show the tab for the source structure. Note the source WBS numbers in the SRC-WBS column, and the empty column headed TGT-OBS. Soon we will fill in this column to indicate our desired mappings.

---

## Source and Target Tabs

**Figure 17.2: Source Tab in the ElemLinks Spreadsheet**

The figure below shows the target tab (TGT-OBS). In our example, it is the OBS structure. The crucial column is headed WbsNum; it contains the values we will put in the TGT-OBS column on the previous tab. (Note that the column really does contain OBS element names, even though the spreadsheet calls it WbsNum; here "WbsNum" is really a generic way of referring to element numbers of any structure.)

---

**Figure 17.3: Target Tab in the ElemLinks Spreadsheet**

Now we return to the source tab, where we will fill in the TGT-OBS column with the appropriate values. We can assign the OBS element names either at the summary level or at the lowest level. In this example, for educational purposes, we will use both approaches.

(You might find it helpful to use Excel's validation capability here. Tell Excel to validate the cells in the TGT-OBS column against the list of OBS elements on the OBS tab. Once you do this, you will see a dropdown list next to each cell in the TGT-OBS column, telling you what the valid OBS element numbers are and keeping you from entering a non-existent OBS code in this column).

Let's say that WBS element 2000 and all its children should be mapped to the PM (PROJECT MANAGEMENT) OBS element. We put "PM" in the TGT-OBS column for the source element 2000. This is a summary element: notice that it is a level 2 element, and there are three level 3 elements that have element 2000 as their parent, as you can verify by inspecting the ParentID of elements 2100–2300. Since 2000 is a summary level element, this mapping will apply to all of 2000's children. Therefore, we don't need to put any values in the TGT-OBS column for 2000's children (elements 2100, 2200, and 2300) and you will see these cells left blank in the figure below.

Next we turn to WBS element 3000 and its children. Let's assume that the children of 3000 will be assigned to various OBS elements. We thus do the mapping at the lowest level, assigning each of 3000's children individually to an OBS element. (We can see that elements 3100–3800 are at the lowest level because they have no children.)

We assign WBS 4000 to the MFG OBS element, map 5000's children at the lowest level, and 6000 at the summary level.

Each row in the spreadsheet that we have changed will eventually result in a new row in the ElemLinks table in the database. Remembering the rule for downloading and uploading data (see Section 16.9 if you need a refresher), namely that edits that will result in added rows require the letter "a" in the action column, we put "a" in each row we changed. The SRC-WBS tab of our spreadsheet now looks like Figure 17.4. (We don't make any changes to the TGT-OBS tab.) Make sure you save the spreadsheet.

---

**Figure 17.4: ElemLinks Target Tab after Assigning Elements**

---

## Uploading the ElemLinks Spreadsheet

Once we've finished editing our spreadsheet and saved it, we upload it with Admin > Upload Data File. The status window (seen in the next figure) shows each of the new rows being inserted into the database.

**Figure 17.5: Upload Data File Status**

---

## Running the Copy Linked Script

Next we run a script that completes the mapping. Issue the command Admin > Scripts > Run/Edit. In the resulting list you will see the scripts "Copy Linked by Contract" and "Copy Linked by Period". As you might expect, the former script will copy data, according to our mapping, for all periods in the contract, while the latter will just copy data for the given period. Since this is the first time we have mapped elements for this contract, we will run the "by contract" script. Select it and click Run.

**Figure 17.6: "Copy Linked" Scripts**

The script begins by telling us what the script will do. Click Next >.

**Figure 17.7: Copy Linked by Contract Script Description**

The script will next ask us which contract we want to apply the mapping to. Select "MOH-2", then press Run.

(If we were running the by period script, it would ask us for the desired period next, then show us the Run button.)

**Figure 17.8: Choosing the Contract in the Copy Linked Script**

The script will run, then show us a completion screen:

**Figure 17.9: Copy Linked Script Complete**

The final step is to recalculate. Since in this example we are applying the mapping to the contract for the first time, we will recalculate the entire contract (see Section 16.2 for more on recalculating).
