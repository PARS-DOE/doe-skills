# Chapter 5: Views

*From the Empower User Manual*

---

## Chapter 5 - Views

Section 2.5 describes how to customize the appearance of the Sort Window by showing or hiding, reordering, and resizing columns. A collection of such settings is called a "view." Switching views allows the user to move quickly from one collection of settings to another, and it is often helpful to use different views for different analysis tasks. Figure 5.1 shows the Views Menu with our sample views.

**Figure 5.1: Views Menu**

---

## 5.1 Sort Views and Gantt Views

Empower uses views in the Sort Window and in the grid portion of the Gantt Chart (see Section 7.17). Sort Views and Gantt Views (as they are respectively called) are very similar; differences between the two types of views will be mentioned when appropriate. Sort Views and Gantt Views are listed together on the Global and User menus, as well as any command that lists the available views (Apply/Edit, Delete/Reorder). It is conventional to end the name of Gantt views with " (G)".

Empower knows which views are for the Sort Window and which are for the Gantt Chart; there is no danger of the user inadvertently trying to apply a Sort View to the Gantt Chart, for example.

---

## 5.2 Global and User

Empower has the notion of Global and User items. The items can be views, custom charts, custom reports, and prefilters. The difference between Global and User items is that Global items are created by the Empower administrator (the "Admin" user) and available to all Empower users, while User items are created or imported by a non-admin user and only available for use by that user.

On the View menu, the first option will always be Global. If the user has created views, there will also be an option called User. These two menu choices allow the user to choose a view and apply it to the Sort Window. The difference is that the Global version shows a list of views created by the Empower administrator and available to all Empower users, while the User version shows only the user's own list of views, created or imported by that user.

All views created by the Admin user will be Global, so the User submenu is never shown for the Admin user. This is the case for all items that can be classified as Global or User: views, custom charts, custom reports, and prefilters.

Note that user items (Views, Charts, Reports, Prefilters) will be stored under that user's id, shown in the User submenu, and not available to other users, even if that user is a member of a group. This is significant, since a user belonging to a group is, for some purposes, treated as having the group's identity instead of the user's own identity, most notably when it comes to contract access permissions. (See Section 16.15.1 for more on the concept of users being in groups.)

The maximum number of views displayed on this menu is twenty Global and twenty User views, due to limitations on screen real estate. If a view cannot therefore be displayed on one of these two menus, it will always be accessible via the Views > Apply/Edit command (see below).

---

## 5.3 Edit Sort View, Edit Gantt View

These two commands allow the user to edit the currently chosen Sort or Gantt view. If the Gantt chart is not currently open, the Views menu will only show the Edit Sort View command. If the Gantt chart is open, the Edit Gantt View command will be added to the menu. Both commands bring up the Edit View dialog; the use of this dialog is described below under the Apply/Edit command.

---

## 5.4 Add Column(s)

Another way to alter a Sort View is to use the Views > Add Column(s) menu. This is most appropriate when you only need to add one or two columns, and don't care about formatting attributes (Title, Width or Alignment). This command will bring up the dialog shown in Figure 5.2; it will show a list of all columns that could be added to the Sort Window. Below the list of columns is another box showing the description of the selected column.

**Figure 5.2: Views > Add Column(s)**

You can select just one column, or a range of columns by clicking on one column, holding down the Shift key and clicking the mouse again, or any number of non-contiguous columns by clicking on your first choice of column, then holding down the Ctrl key on Windows or the Command key on Mac OS X, and clicking on each additional column you wish to add.

Once you have chosen the columns you want, click the Add Selected button, and the new columns will be added to the Sort Window, just to the right of the WBS column. You may then drag and drop each new column to the appropriate location in the Sort Window. Once the view is structured as desired, select the Views > Edit Sort View command and give the view a new name.

---

## 5.5 Custom Sort

This option opens the "Custom Sort" dialog box, allowing multi-tiered custom sorting on any columns in the current view.

**Figure 5.3: Custom Sort Dialog**

Applying the sort indicated in the above figure would sort the contents of the sort window by CAM name, then would sort by SPI within each CAM. Notice that we choose to sort CAM in ascending order, while SPI is sorted in descending order.

The current sort direction of each item in your custom sort is indicated by an arrow next to the column name. The direction of the sort for a column can be toggled via the selection option at the bottom right of the dialog box.

---

## 5.6 Apply/Edit

This command can do two distinct things; it can be used to select a view to apply to the Sort Window or Gantt Chart, or to select a view to edit. These two functions are grouped together on the same menu option, however, because they start with the same action, namely choosing a view to operate on.

The first functionality offered by this command is the ability to choose a view to apply to the Sort Window or Gantt Chart. This brings up the question: How do you know whether a view will be applied to the Sort Window or to the Gantt Chart?

The simple answer is that Empower knows what kind of view every view is and will only apply Sort Views to the Sort Window, and likewise with Gantt Views. Empower can tell the type of view by looking at the fields in the view: if the fields in the view are fields that are only shown in the Sort Window, the view is a Sort View. If the fields in the view are fields that are only available in the Gantt Chart, the view is a Gantt View. The user can make the same determination by opening the view in the View Editor, described below. To save you a step, we recommend the convention of naming Gantt Views with a trailing " (G)" so you can tell from the view name what kind of view it is.

(Wait: we just said that a given field can only appear in either the Sort Window or the Gantt Chart, but not both. What about, for example, BCWS, which shows up in the Columns list for Sort Views and for Gantt Views? The answer is that these are actually two different fields with different data. There is a BCWS column which holds the BCWS for a given element (i.e., a row in the Sort Window). There is a different BCWS field which holds the BCWS for an associated task, which is what you see if you create a Gantt View with BCWS. In database-speak, there are two fields: EarnedValue.BcwsCum — cumulative BCWS for an element in the WBS (or OBS, or other structure), and Task.BcwsCum — cumulative BCWS associated with a task in the schedule.)

The alert reader might wonder why we need a separate command to apply a view, when the same thing can be accomplished by using the Views > Global or Views > User commands. To answer that question, consider the dialog that results from the Views > Apply/Edit command, shown below in Figure 5.4:

**Figure 5.4: Views > Apply/Edit List Box**

Note the view named "[Fred]." The brackets around the view name indicate that this view is not shown in the Views > User or Views > Global commands. Some Empower users have developed so many views that it is impractical to show them all in the Views > User or Views > Global menus. So users can choose to list the most commonly used commands in those menus, and access the less frequently used commands by means of the listbox in the Views > Apply/Edit command. These less frequently used commands can only be applied through this command, and they are all marked by the enclosing square brackets.

Note also the "+" before the views "Mike's View," "View-3," and "View-2." The leading plus sign indicates that these views are User views, not Global views. (Think of User views as views "added" — plus — to the standard set of Global views.) It is important to distinguish between Global and User views because non-administrators can't edit Global views, though, as we will see, users can start with a Global view, edit it, and then save the resulting view under a new name as a User view.

The "User" and "Global" checkboxes on the side of the dialog allow you to filter which views appear in the "Apply/Edit" dialog. These checkboxes will not display if you are logged is as the "Admin" user since all of "Admin's" user items are "Global." The text box at the bottom of the dialog displays the View description if it has one. The dropdown at the top of the dialog allows you to choose which type of user item you want to see, including charts, reports, views, etc.

When a view is applied, the name of the view will be appended to the name of the dataset in the dataset pane, as shown in the figure below ("CPI vs TCPI EAC" is the name of the active view):

**Figure 5.5: Active View Shown with Dataset Title**

If a dashboard is applied, its name will appear before the current view's name, as seen in Figure 12.3.

The second functionality available through the Views > Apply/Edit command is the ability to create or modify a view, using the powerful Edit View dialog box (see Figure 5.6) which provides a highly interactive and intuitive methodology for creating and customizing views.

**Figure 5.6: Edit View Dialog Box**

Available columns (fields) are shown on the left side of the dialog box. The Column Group selector is used to filter the Columns selector by the type of column (All, Contract, Element, Earned Value, Adjusted OTB, Schedule, DQI EVMS, DQI IMS, Gantt, Action, Audit EVMS, Audit IMS, SEM EVMS, or SEM IMS) to make column selection more intuitive. Further, a short description of the selected column and its attributes are shown below the column selector to aid in selecting the correct column.

To add a column to the existing view, select the desired column from the Columns box and press the Add > button. The new column will be added below the currently selected column in the View Columns box. To remove a column from the view, press the < Remove button. To relocate a column in the View Column box, use the up and down arrows to the right of View Columns box. You can change the display attributes (Title, Width and Alignment) of any column by selecting the column in the View Columns box. You can also add a description for the view in the text field at the bottom of the dialog box. To save the changes to the current view, press the Save button.

Note the dropdown list below the text box that shows the short description of the selected column. This list contains the names of prefilters (see Chapter 6) and allows the user to assign a filter to a view, which is run automatically when the view is applied. There are some fine points to note regarding this linkage between views and filters: (a) if a filter assigned to a view is deleted, the filter is automatically uncoupled from the view; and (b) when exporting a view that has a filter assigned to it, any linked filters are also exported.

Now let's discuss editing the two different kinds of views (Sort and Gantt).

In Figure 5.7, we have opened the Empower Default view. It is a Sort View, since the columns in the View Columns list box are columns that are only available in the Sort Window.

**Figure 5.7: Edit View Dialog Showing the Empower Default View**

If we have the Gantt chart open and select "Edit Gantt View" notice that "Gantt" is displayed in the Column Group list box. Note that the Columns shown in the Columns list box are now Gantt Chart columns.

**Figure 5.8: View changed to a Gantt View**

All the Sort View column group categories have been removed from the Columns Group list box; since this is a Gantt View, only columns from Gantt column groups can be added. These include the task level calculations for some DQIs, Audit Metrics, and Schedule Execution Metrics.

To create a new view, change the view name and then press the Save button. To restore the view to its original state, press the Reset button prior to applying the view.

A maximum of twenty views can be displayed on the Global View and User View Menus. To make a view visible on the menu, check "Show in Menu." Recall that views that have not been made visible on the menu will still be accessible via the Views > Apply/Edit command, where they will be shown with brackets around the view name.

---

## 5.7 Delete/Reorder

This command allows the user to delete User views or to change the order in which User views appear in the Views > User menu. Figure 5.9 shows the dialog. Note that views that have not been selected for display in the Views > User menu are shown with square brackets around their names.

**Figure 5.9: Views > Delete/Reorder Dialog**

To reorder a view, click on the view, then click on the up arrow or down arrow buttons to shift the view by one position. When you have the views ordered to your satisfaction, click the Reorder button, then close the dialog by clicking on the X in the upper-right hand corner of the dialog. Note: if you reorder the views in the list with the up and down arrows, and then close the dialog without clicking the Reorder button, your changes will not take effect.

To delete a view, click on the view, then click the Delete button. Repeat until you've finished deleting the views you want to get rid of, then close the dialog as described above.

---

## 5.8 Task Mode

Earlier in this chapter we discussed the difference between a Sort View and a Gantt View. (see section 5.6) When opened normally with a click, Gantt Views are applied to the Gantt chart in the chart pane. However, Gantt Views can also be opened so that they are applied to the Sort Window instead. In this section, we will use the term "Task Mode" to refer to "Gantt Views" that are opened in the Sort Window.

Note that Task Mode is not available for cross-contract datasets.

**Figure 5.10: Task Mode in Sort Window**

To use Task Mode in the sort window, use Shift-click when selecting the Gantt view (much like you would when opening an external chart or report). Notice that rows in the sort window no longer correspond to elements, instead each row is a task. Using Task Mode allows the use of interactive filters on schedule fields.

**Figure 5.11: Filtering in Task Mode**

Task (or Gantt) views can only contain schedule fields. When editing a Gantt View, only valid fields will appear in the "Edit Sort View" dialog, so only those fields can be used in Task Mode. These include fields from the Gantt and DQI IMS sections.

**Figure 5.12: Editing a Gantt View**

When using Task Mode, some features will not be available. If you attempt to use these features when in Task Mode, you will see a message like:

**Figure 5.13: Not available for Task Mode**

In order to use these functions, first switch to a standard Sort View.

Certain reports will display differently when in Task Mode. These include the "Data Quality Indicators," "Six Period DQI Trends," and "Schedule Assessment" reports.

The "Data Quality Indicators" report will display IMS DQI information for the selected task.

**Figure 5.14: DQI Report with a Task Mode**

Similarly, the "Six Period DQI Trends" report will display DQI trend information for the selected task.

**Figure 5.15: DQI Trends Report in Task Mode**

The "Schedule Assessment" report will display schedule information related to the selected task, and will also display summary task information if the "SUM" row is selected.

**Figure 5.16: Schedule Assessment Report in Task Mode**
