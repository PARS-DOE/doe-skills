# Chapter 13: Dialog Templates

*From the Empower User Manual*

---

## Dialog Templates

Some dialog windows in Empower support the use of dialog templates. Dialog templates allow you to save preset options for some dialog windows with multiple selectable options, such as the "Export EDI File" and "Import EDI File" dialogs. This allows you to easily switch between standardized options for these dialogs with a simple dropdown instead of selecting all of the options yourself.

## 13.1 Export Templates

Export templates can be used to save configurations of options selected in the "Export EDI File" dialog. Notice the bottom section of the "Export EDI File" dialog; you'll see a dropdown box and two buttons. This section is used for creating and applying templates for the "Export EDI File" dialog.

**Figure 13.1: Export EDI Dialog Templates**

Clicking the down arrow for the dropdown box will show the list of available templates for the current user.

**Figure 13.2: Export EDI Dialog Dropdown**

Selecting a template will automatically change the selections in the dialog, including the exporting level, checkbox selections, selected units, and selected structures. If we select the IPMDAR_C template the dialog will change to look like figure 13.3.

**Figure 13.3: Export EDI Dialog, Template Selected**

Selecting the reporting_export template will change the dialog options again as shown in 13.4.

**Figure 13.4: Export EDI Dialog, Template Selected**

The "Save" and "Save As" buttons can be used to create new templates or save changes to existing templates. Note that names for templates must be unique. Attempting to save a template under a name that is already in use will prompt you to enter a new name.

If we wanted to save the reporting_export template under a new name, we could use the "Save As" button.

**Figure 13.5: Export EDI Dialog, Save As**

To clear the currently applied template simply remove any text from the template dropdown and click off of the dropdown.

## 13.2 Import Templates

Import templates can be used to save configurations of options selected in the "Import EDI File" dialog. Like the "Export EDI File" dialog, the bottom section of the "Import EDI File" dialog shows a dropdown list to select a template as well as "Save" and "Save As" buttons to create and edit import templates.

**Figure 13.6: Import EDI Dialog Templates**

Selecting a template will change the selected options in the dialog.

**Figure 13.7: Import EDI Dialog, Template Selected**

## 13.3 Assigning Dialog Templates

Dialog templates can be assigned to users or groups of users. The "Admin" user can see and edit all dialog templates, while other users can only see and edit templates that they have either been assigned access to or created themselves.

Templates can be assigned to users via a data download/upload of "UserDlgTmpls" (short for User Dialog Templates). The "UserDlgTmpls" option is under the "shared" section in "Download Data."

**Figure 13.8: Download Data, UserDlgTmpls**

The resulting data file has two tabs; the first is called "UserDlgTmpls" and the second is "DlgTmpls."

Figure 13.9 shows what some entries in the first tab of the download might look like:

**Figure 13.9: UserDlgTmpls Tab**

The "UserName", "DlgTmplName", and "DlgType" columns are informational. The "UserID" and "DlgTmplID" fields are required when adding new records to this download. Note that "DlgType" indicates which dialog the template can be used by; type 1 is used by "Export EDI" and type 2 is used by "Import EDI."

The "CanEdit" column indicates whether the user has permissions to alter the assigned template and defaults to "N". If "CanEdit" is "N" then the user cannot edit or delete the template. If "CanEdit" is "Y" then the user can make changes to or delete the assigned template.

The "DlgTmpls" tab lists the existing templates for reference when assigning templates to users.

**Figure 13.10: DlgTmpls Tab**

For example, if we wanted to give "Smith" permission to use the reporting_export template, we could add this record:

**Figure 13.11: UserDlgTmpls Upload**

After saving our changes, we upload the file via "Admin > Upload Data File."

**Figure 13.12: UserDlgTmpls Upload Result**

Users will only see templates that they have "UserDlgTmpls" entries for. Note that templates can also be assigned to groups. In that case, users will also see templates that are assigned for any groups that they are in. The highest valid permissions for a template are always used; if a user is in a group that has 'Y' permissions for a template then they will also have 'Y' permissions to edit that template.

For example, if "Smith" is logged in they would see a list like this:

**Figure 13.13: Smith Export EDI Templates**

Since Smith is in the Instructors group, he sees both the templates that he has "UserDlgTmpl" entries for as well as those that the Instructors group has permissions to use.

## 13.4 Delete/Reorder Dialog Templates

**Figure 13.14: Dialog Templates**

The Dialog Templates menu option under the Admin > System submenu allows you to delete or reorder dialog templates. Reordering templates changes the order in which the templates are displayed in their respective dialogs.

**Figure 13.15: Delete/Reorder Dialog Templates**

To delete a dialog template, select the item that you want to delete, then press the Delete button.

To reorder a dialog template, select the template you wish to reorder and move it up or down in the list of templates using the up and down arrow buttons. When you have the item where you want it, press the Reorder button to finalize your change.

## 13.5 Exporting Dialog Templates

Dialog templates can be exported via "File > Export User Items" like other user items. This export will not include user dialog template assignments or permissions, but can be used to transfer templates between environments.

**Figure 13.16: Export User Items**

In order to transfer user dialog template information, you can generate an "Empower-optimized" export via "Export EDI File" with the "Export user and portfolio data" option checked.
