# Chapter 15: Editing Narrative Inputs

*From the Empower User Manual*

---

## Chapter 15

### Editing Narrative Inputs

Users can customize VAR Narratives, EAC Narratives, and the Scope of Work reports by editing a file that will be used as a sort of template for the report. Figure 15.1 below shows the Inputs menu. Picking one of the first three choices or the EAC Narrative choice will bring up Empower's enhanced text editor. The fourth choice on the menu, User EAC, brings up a dialog that allows the user to specify values for the minimum, maximum, and most likely EAC values for each element. We'll begin with the User EAC Inputs, and then explain the use of Empower's narrative editor.

**Figure 15.1: Inputs Menu**

---

## 15.1 User EAC Inputs

Clicking on the User EAC menu option will bring up a dialog like the one shown below for the selected element. The user can generate the estimates for minimum, maximum, and most likely either by picking one of the methods available in the combobox lists on the left (e.g., "Bac", "MovAvg3", "CumCpiFc", etc.), in which case the numerical value is calculated appropriately, the resulting value is placed in the right-hand box, and the box is grayed out, preventing manual data entry; or by choosing "Analyst" as the method and entering a numeric value directly in the right-hand box. When the user chooses "Analyst", he or she can type in some text in the left-hand box to indicate the source of the estimate.

**Figure 15.2: User EAC Inputs for Lowest-Level Element**

You can only input User EAC values for lowest-level elements. If you click on an element that is not at the lowest-level, the dialog will appear, but all the controls will be grayed out and disabled.

To enter User EACs for another element, simply click on that row in the sort window; the dialog will update accordingly. It is not necessary to save your estimates for each element separately, you can make multiple changes and save them all at once.

When you click 'Save Changes', User EAC values are automatically summed up the element hierarchy and the sort window is refreshed to display the new values. Accordingly, you might find it helpful to select a view that displays the User EAC columns when using this dialog.

---

## 15.2 Set VAR Required

This command is used in the narrative approval workflow, and is described in Section 20.5.

---

## 15.3 Set VAR Categories

This command is used to set categories for each variance for the currently selected element. This can provide additional information about the variances when writing and resolving VAR narratives. The dialog will look like the one shown below:

**Figure 15.3: Set VAR Categories**

The categories in the dropdown list should be set per-contract in the Contracts download. Note that these categories can be whatever you like, as long as they do not start with a space. The first letter of each category name will be used as the code for that category, so they should start with distinct letters and/or symbols. For this sample contract, we are using the categories -None-, Performance, Error, and Corrected. The categories are set on the "Settings" tab of the "Contracts" data download.

**Note:** You may need to begin your category list with a single quote when setting the value in Excel so that Excel does not read it as a formula. For example: `-None-,Performance,Error,Corrected`

**Figure 15.4: Setting Categories in Contracts**

The category code is stored in a field called VarCats. Additional calculated fields that break out the category by VAR type are also provided: SvCatCur, CvCatCur, SvCatCum, CvCatCum, and VacCat. These fields can be used in placeholder syntax in VAR narratives, templates, custom user items, etc.

The "VAR Categories" view (available on request from Empower support or easily created via the View editor) displays each of these fields:

**Figure 15.5: VAR Categories View**

---

## 15.4 Add/Edit Actions

This command is used in action item tracking, and is described in Section 21.3.

---

## 15.5 Action Item Kanban

Clicking on the Action Item Kanban menu option will bring up a dialog like the one shown below:

**Figure 15.6: Action Item Kanban**

This dialog syncs to the sort window, displaying existing action items for any elements shown. You can drag and drop the action items into different columns to quickly change their status. The status columns displayed will vary depending on your user's Action Item Role.

The Kanban shown below was opened by a "Submitter" who filtered to WBS "3200" in the MOH-2 contract. Notice that this user only sees the status columns allowed for their Action Item Role. Furthermore, this user can move items out of the "Rejected" column, but cannot move items into the "Rejected" column.

**Figure 15.7: Action Item Kanban for Submitter**

If a user with appropriate permissions drops an action item into the "Rejected" column, they will be prompted to enter a rejection note.

**Figure 15.8: Prompt for Rejection Note**

Clicking "OK" will save your rejection note and update the status of the action item to "Rejected." Clicking on one of the action items in the Kanban dialog will open the "Action Items" report for that action item.

**Figure 15.9: Action Item Report**

Double clicking one of the action items will open the Action Item Editor for that action item.

**Figure 15.10: Action Item Editor**

---

## 15.6 VAR Kanban

Clicking on the VAR Kanban menu option will bring up a dialog like the one shown below:

**Figure 15.11: VAR Kanban**

Like the Action Item Kanban, this dialog syncs to the sort window, displaying existing VARs for any elements shown in the sort window. Drag and drop the VARs into different columns to change their status. The status columns displayed will vary depending on your user's Narrative Role. The Kanban also shows entries for elements that have a Fmt5Var but no VAR written. These entries are listed under the "Unopened" column and cannot be dragged to a different status column. Likewise, VARs in other status columns cannot be dragged to the "Unopened" column.

The Kanban shown below was opened by a "Submitter" who filtered to WBS starting with "3" in the MOH-2 contract. Notice that this user only sees the status columns allowed for their Narrative Role. Furthermore, this user can move items out of the "Rejected" column, but cannot move items into the "Rejected" column.

**Figure 15.12: VAR Kanban for Submitter**

If a user with appropriate permissions drops a VAR into the "Rejected" column, they will be prompted to enter a rejection note.

**Figure 15.13: Prompt for Rejection Note**

Clicking "OK" will save your rejection note and update the status of the VAR to "Rejected." Clicking on one of the VAR entries in the Kanban dialog will open the "VAR Narrative Report" for that VAR.

**Figure 15.14: VAR Narrative Report**

Double clicking one of the VAR entries will open the VAR Narrative Editor for that element.

**Figure 15.15: VAR Narrative Editor**

---

## 15.7 Introduction to the Narrative Editor

Empower's narrative editor supports most of the word processing features one would expect from a word processor like Microsoft Word or OpenOffice: font effects such as bold, italic, color, highlighting etc., paragraph formatting, and so on. One feature of Empower's editor is of particular interest: since these reports are usually viewed as web pages, the Empower editor has the ability to add HTML formatting to the narrative inputs. Figure 15.16 shows the editor window with the editing toolbar. Note that the currently selected element is shown in the editor's title bar ("3100: SENSORS" in this case).

**Figure 15.16: Editor Toolbar and Input Area**

If you've used a word processor such as Microsoft Word or OpenOffice, then most of the functionality provided by the editor will seem familiar, and using these features should be fairly intuitive. The experience you've had with any widely used word processor should carry right over to Empower's editor.

However, whereas a word processor is primarily designed for producing documents which will be printed on paper, the Empower editor is designed for displaying text in the web browser windows. When creating your input using the editor, there are a few things you should always keep in mind:

- There are various web browsers currently in use; all have their own quirks and ways of displaying HTML markup. Firefox, Internet Explorer, Safari, Edge, and Google Chrome are the most popular, but there are others.
- The screen size people will be viewing your content on may vary considerably, from as small as 800×600 pixels to 1900×1200 pixels and greater. However, it is fair to assume that your average user will have a screen size of 1024×768 or greater.
- The range of fonts available on a user's computer may be different from yours, so don't rely on a user having a particular font on their computer. Avoid unusual font choices.

In short, you cannot always guarantee that your content will look exactly the same on someone else's computer.

The Narrative Editor is used for VAR, User, Scope, and EAC Narratives. Note that where appropriate, the Narrative Editor will have multiple options in the "Update" dropdown for the narrative approval workflow. Narratives that do not use the narrative approval workflow (e.g. the EAC Narrative) will have more limited options, such as "copy forward" and "save."

---

### 15.7.1 The Editor Toolbar

The Undo and Redo buttons are shown in Figure 15.17.

**Figure 15.17: The Undo and Redo Buttons**

The Undo button (at the left of the figure) undoes the previous editing action, while the Redo button (on the right) will redo an action previously undone. This button will be disabled unless you have already performed an undo operation.

If you try to switch to a new element prior to saving your changes, the dialog box shown in Figure 15.18 will be displayed. Click the Yes button to save the changed narrative text, or No to discard it.

**Figure 15.18: Narrative Changed Warning Dialog**

---

### 15.7.2 Formatting

To the right of the Undo and Redo buttons you will find buttons that can be used to format your narrative text. In Figure 15.19, from left to right, the buttons allow you to change the color of the text or background, make the text bold or italic, or remove formatting from selected text.

**Figure 15.19: Text Effects Buttons**

The next group of buttons, shown in Figure 15.20, are buttons that, in order from left to right, change the alignment of text; turn selected text into bulleted lists and numbered lists; and decrease and increase the indentation of the current paragraph.

**Figure 15.20: Paragraph Formatting Buttons**

The next two buttons on the toolbar, shown in Figure 15.21, put the editor into source code mode and insert placeholder for database values. We will describe the source code mode now, and discuss the insert button in the next section.

**Figure 15.21: The Source Code and Insert Buttons**

The Empower editor offers users who are comfortable using the HTML markup language to format their text directly with HTML tags.

The page you are editing is stored in a code known as HTML. HTML is the language of the web — it tells your browser exactly how to display your page. If you need to edit the HTML code directly, you can do so by clicking the Source Code button ( ).

Some additional formatting options are available in the menu above these buttons, shown in Figure 15.22. These include additional options such as fonts, table options, and the ability to insert hyperlinks.

**Figure 15.22: Editor Menu**

---

### 15.7.3 Editing a Narrative

Narratives are structured by templates. There are different templates for each type of narrative — VAR, EAC, and SOW. When you select an element in the Sort Window and click on, e.g., Inputs > VAR Narrative, the Editor dialog will appear. If a VAR narrative has not already been started for this element, Empower will load the appropriate template (there are two templates for VAR narratives — one for level 1 and one for all other levels). If a narrative has already been started, Empower will skip the template loading step and load the existing narrative in the editor.

(A note for experienced users: previous versions of Empower had both default and non-default templates. The former were automatically loaded when a new narrative was opened for an element, while non-default templates could be inserted into a narrative with an editor command.)

As mentioned before, narratives are structured by templates. This means that the templates specify the sections that must appear in a narrative and their order. Thus a VAR narrative for a level 1 element will begin with a table summarizing the performance of this element (SV, SV%, CV, CV%, etc.), then has sections for Contract Summary, Formal Reprogramming Analysis, EAC Analysis, and so on. These templates are user items and can be imported and exported with the commands File > Import User Items and File > Export User Items. See Sections 3.2.1.4 and 3.2.1.5. Modifying templates is discussed in Appendix C.

**Note:** Section-based templates are new in Empower 3.6, and are the type described in this manual. However, pre-3.6 style templates (non-section based) still work in this version of Empower.

Let's look at an example of editing a narrative input. (The process is similar for editing EAC, User, or SOW inputs.) We will begin by noting that element 3200 in the familiar MOH-2 contract requires a VAR narrative for cumulative schedule and cumulative cost, as indicated by the upper-case "S" and "C" in the VAR column. See Figure 15.23 below.

**Figure 15.23: Element 3200 Requires VAR Narratives for Cumulative Schedule and Cost**

With element 3200 selected in the Sort Window, we click on Inputs > VAR Narrative and the Narrative Editor window appears, as shown in Figure 15.24. In this case, the narrative has already been written, so we'll see text in the editor window.

**Figure 15.24: VAR Narrative Sample**

Note the second line in the dialog: "VAR: SC": this reminds us that these are the variances we have to discuss in the narrative.

Empower's VAR Narrative editor guides you through the process of writing the narrative. Consider Figure 15.25 below: the "Section" drop-down list is expanded to show the available choices. For each variance, there are three sections—"Cause", "Impact to Task", and "Impact to Contract" — so in our case there are six sections to be completed (three for each the two variances, cumulative schedule and cumulative cost).

**Figure 15.25: Editor showing required sections**

The editor will guide you through the completion of the required sections with the Next button; simply fill out the first section in the big blank editor window, then click Next. The "Section" drop-down list will show the next section you need to work on, and the editor window will be cleared (or it will show any text for this section you may have previously entered). Of course, you can write the narrative in any order you wish by picking the desired section from the drop-down list; running through the sections in order using the Next button is just a convenience.

If you don't enter any text for a section, the words "(Not entered.)" will appear in red in the report. See Figure 15.26 below.

**Figure 15.26: Text not entered for required section**

Let's say we have written the "Cause" section for the Cumulative SV. We click Next and then the next section ("Impact to Task") appears, as shown in Figure 15.27 below.

**Figure 15.27: Narrative showing the next section**

Notice the text (|Vac|) and (|Vacp|) in the editor window. These are placeholders for values that Empower will look up in the database and insert in your report when you open it in the Report Window or export it. (These two are placeholders for Variance at Complete, and Variance at Complete in percent.) How do you enter these placeholders yourself? You could simply type them in if you happened to know the code, but there is a better way. Click on the Insert button on the tool bar, and you'll get a list of templates which you can insert into your narrative. This list can be customized at the server level. For more information, see the technical note "The Empower Configuration File," available on our support website http://encoreanalyticsllc.freshdesk.com/support/solutions.

In Figure 15.28, we are composing a narrative for element 3000 and we find ourselves wanting to include the current cost variance value.

**Figure 15.28: We want to enter a placeholder for Cur CV...**

So we click on Insert, and we see the list of available templates. "CVCUR" is there, as we see from Figure 15.29.

**Figure 15.29: List of available templates**

We choose "CVCUR" and continue editing our narrative, as shown in Figure 15.30.

**Figure 15.30: Narrative after Entering Placeholder**

As mentioned before, the editor stores your narrative as HTML. If you are comfortable with writing and editing HTML, and you want to modify the HTML of your narrative for some reason, the editor lets you edit the HTML directly, using the Source Code button.

When you press the Source Code button, the editor will look something like Figure 15.31. Note you will see a simple text editor which will display your narrative input and any HTML markup.

**Figure 15.31: Source Code Editor**

Once you have made your changes to the HTML, click the Save button to save them, or Cancel to discard them. **Note:** This option is for advanced users who are knowledgeable in HTML. If what you see on this dialog scares you ... click the Cancel button!

Now let's consider the controls at the bottom of the editor dialog. A narrative or action item reviewer would use the Reject Reason text box to give a brief reason for rejecting the narrative (see Section 20.3 for more details).

"Status" shows the status of the narrative in the narrative workflow; see Section 20 for more details.

"Update" shows what actions are available for this narrative. This likewise will depend on the narrative's place in the workflow. When creating a new narrative or after you have edited a narrative, one of the options will be "Save": when this is selected in the list box, the button to the right will be the Save button, and clicking it will, naturally, save your narrative.

To see your VAR Narrative, with all the sections and with the placeholders filled in with values from the database, you can open your report with the Report > VAR Narrative command; your report will appear in the Report Window.

One last note: User Narratives don't have a template. For them, the Section: drop-down list will just say "General", and the prompt will say "Enter narrative text below as required." There will be no section heading in the resulting report (i.e., you won't see the word "General").

---

### 15.7.4 Inserting Parent Percentage Tables

Empower provides five special options on the "Insert" menu that allow you to insert "Parent Percentage" tables into your narrative. These tables detail the percentage of variance that each child of the selected element contributes to the total variance of the element. This utility is useful for cases where you are required to explain a certain percentage of the variance.

The table insert options are: 'SV CUR PP', 'CV CUR PP', 'SV CUM PP', 'CV CUM PP', and 'VAC PP'

Each table shows data for the variance type indicated in the name (Cumulative Cost Variance, Current Schedule Variance, etc.)

Figure 15.32 shows what these options look like in the dropdown.

**Figure 15.32: Insert Menu Dropdown**

If we insert the "CV CUR PP" table into our narrative, we get some placeholder text: (|Meta|CvCurPP|)

**Figure 15.33: Inserted CV CUR PP Table**

Just like the inserted placeholder text described earlier, the table will be populated in the VAR Narrative report when you open it in the Report Window or export it.

Figure 15.34 shows an excerpt of the VAR Report with the table that we inserted.

**Figure 15.34: Report with Inserted CV CUR PP Table**

The table lists the direct children of the selected element, their Cost Variance (CV), and the percentage of the total CV that each child contributes. This table will also keep "running totals" of the CV values and the percentage contributions. The running total columns allow you to easily tell how much of the variance you have explained while writing your VAR report.

Suppose that we only want the table to show rows for the elements that we're going to address in our report. The rows shown can be limited by providing a comma separated list of the rows that you would like shown in the placeholder syntax. Figure 15.35 shows what this syntax looks like if we were to limit our table to only show rows 1, 2, 3, and 5.

**Figure 15.35: Inserted Table with Limited Rows**

If we save our changes, the Report Window will update accordingly, as shown in Figure 15.36.

**Figure 15.36: Report with Limited Rows**

Notice that the table now only displays our selected rows, and the running totals have updated accordingly. The running total columns will always display totals based on what is displayed in the report. In this case, we have selected rows 1, 2, 3, and 5, which are Elements 3200, 3300, 3800, and 3100. The table shows us that the total percentage of the variance that all of these elements explain is 82%.

You can also specify a range of rows to display in the table. To do this, use the syntax #..#. For example, if we wanted to display rows 2-4 of the current cost variance table, we would use (|Meta|CvCurPP|2..4|) to specify that range of rows.

---

### 15.7.5 Spellchecking

The spellcheck function is provided by your browser. Here is how to enable spellchecking if it is not already enabled:

- **Internet Explorer:** Internet Options > Programs > Manage Add-Ons > Spelling Correction. Check "Enable spelling correction".
- **Firefox:** Preferences > Advanced. Check "Check my spelling as I type".
- **Chrome:** Settings > Show Advanced Settings. Under Privacy, click "Use a web service to help resolve spelling errors".
- **Safari:** Edit > Spelling and Grammar. Check "Check Spelling While Typing".

---

## 15.8 Editor Shortcut Keys

### 15.8.1 Windows Keyboards

| Keyboard Shortcut | Action |
|---|---|
| CTRL+A | Highlights the whole editing area |
| CTRL+B | Toggles text between bold face and normal |
| CTRL+C | Copies highlighted area |
| CTRL+I | Toggles text between italic and normal |
| CTRL+U | Toggles text between underlined and normal |
| CTRL+V | Pastes the data from the clipboard |
| CTRL+X | Cuts the highlighted area |
| CTRL+Y | Redo |
| CTRL+Z | Undo |

---

### 15.8.2 Mac OS X Keyboards

| Keyboard Shortcut | Action |
|---|---|
| command+A | Highlights the whole editing area |
| command+B | Toggles text between bold face and normal |
| command+C | Copies highlighted area |
| command+I | Toggles text between italic and normal |
| command+U | Toggles text between underlined and normal |
| command+V | Pastes the data from the clipboard |
| command+X | Cuts the highlighted area |
| command+Y | Redo |
| command+Z | Undo |
