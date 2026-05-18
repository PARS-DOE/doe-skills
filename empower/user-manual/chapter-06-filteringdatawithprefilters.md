# Chapter 6: Filtering Data with Prefilters

*From the Empower User Manual*

---

## Chapter 6: Filtering Data with Prefilters

Filters are a way of controlling which rows of data appear in the Sort Window and the grid part of the Gantt Chart. Empower has both interactive filters and prefilters. Interactive filters are applied to the records currently in memory in the Sort Window. They are executed by typing parameters in the boxes above the columns in the Sort Window. Interactive filters are executed on user's computer, after the data has already been transmitted from the server hosting Empower. Chapter 4 further describes interactive filtering.

Prefilters, on the other hand, are filters that are executed on the server and limit the data that is sent from the server to the user's computer. Rows that do not meet the prefiltering criteria will never even get to the user's computer and are therefore not available for analysis and interactive filtering.

For example, assume that you have a project with 1,000 WBS elements and that you ran a prefilter where CAM=Smith. Assume that Smith is responsible for 200 WBS elements. The interactive filtering would only know about the 200 elements that were returned by the CAM=Smith prefilter.

Typically, users will have a number of prefilters already set up for them by the administrator; see Section 3.2.1.4 on importing user items (prefilters are a kind of user item).

The prefilter functionality is accessed through the Prefilters menu, shown in Figure 6.1 below. Many of these commands operate in a way very similar to the like-named commands in the Views menu.

---

## Figure 6.1: Prefilters Menu

As mentioned above, Empower has separate filters for the Sort Window and the Gantt Chart, just as Empower has Sort and Gantt types of views. The differences between Sort and Gantt prefilters are the same as the differences between Sort and Gantt views. Thus, to avoid repetition, please refer to Chapter 5 for details. Note that Gantt prefilters can be applied to the sort window in "Task Mode" by using Shift+Click.

---

## 6.1 Global and User

As with views, there are two Global and User prefilters (see the first two menu items in Figure 6.1). Global prefilters are created, modified, and deleted by the Empower administrator and are available for use by all users. User prefilters are created, modified, and deleted by non-administrator users. They are normally only available to the user who created them, although, just like views, they can be shared with other users by saving them in an XML file, then imported by other users.

Since all prefilters created by the Admin user must be Global, the User menu is not shown when the current user is Admin (see Section 5.2). In Figure 6.1, we see the User menu item, so we know we're logged in as a non-Admin user.

As with all user items, they are stored under the user's id, even when that user is a member of a group. (See 5.2.)

---

## Applying Prefilters

There are two ways to apply a prefilter. The first way is simply to choose the desired prefilter from the Prefilters > Global or Prefilters > User commands (if the desired prefilter is displayed on one or the other of these menus). However, the maximum number of Global and User prefilters displayed in the menu is twenty (each), due to limitations on screen area. Some installations of Empower may have too many global prefilters to display in a menu, or some users may have created too many user prefilters to display in a menu. So the list of prefilters in these two commands is not always complete. That leads to the second way to apply a prefilter: the Prefilters > Apply/Edit command, discussed below in Section 6.2.

To turn off prefiltering, choose Prefilters > Global > All Elements.

The user can always identify if a prefilter is in use, and if so, what the name of the current prefilter is by checking the Status bar. Figure 6.2 illustrates how the Status bar shows the currently applied prefilter (note the "[PF: Interesting Stuff]" at the right of the figure).

---

## Figure 6.2: Status Bar Showing the Current Prefilter

The primary purpose of adding prefilters to Empower was to support existing filters built for wInsight; however, they do add a more flexible and powerful alternative to filtering if the interactive filters do not meet your needs.

---

## 6.2 Apply/Edit

This command, like the Views > Apply/Edit, gives the user the choice of doing two distinct things. This command can be used to apply a prefilter by selecting from the complete list of available prefilters (recall that all prefilters might not be displayed in the Prefilters > Global or Prefilters > User menus due to space limitations). The second use of this command is, naturally, to edit prefilters. Both functions begin with selecting a prefilter; when the user chooses this command, the Apply/Edit Dialog box is displayed (as shown in Figure 6.3 below).

---

## Figure 6.3: Prefilter Apply/Edit Dialog Box

There are several things to notice on this dialog:

1. Square brackets around the filter name (e.g., "[CV Trend Down]") indicate that this is a prefilter that isn't shown on either the Prefilters > Global or Prefilters > User menu, due to limited space on the menu.

2. A leading plus (+) sign (e.g., "+ Jim-PF-1" means this is a User ("added") prefilter, not a Global filter provided by the administrator.

3. Square brackets and the leading plus sign can be combined (e.g., "+ [Cam-Price]") to indicate that this prefilter is a user prefilter (the plus sign), and it is not shown on the menu (the brackets).

4. It is possible to have Global and User prefilters with the same name. On the menus, it is easy to tell them apart, since they will be under either the Global or User menu item. In this dialog, where all prefilters are shown together in the same list, you can tell the User prefilters from the Global prefilters by the presence or absence of the leading + sign. (We do not generally recommend having Global and User prefilters with the same name, but it can happen, and Empower trusts users to act sensibly.)

5. The checkboxes on the side of the dialog allow you to filter which prefilters are shown.

6. If the selected prefilter has a description, it will display in the text box at the bottom of the dialog.

Once the list of available prefilters is displayed, the user can apply a prefilter by clicking on the desired prefilter and pressing the Apply button. If the prefilter requires no additional information, the dialog will go away and the prefilter will be applied. Some prefilters require additional input. For instance, if the user chose to apply the "CAM/IPT" filter, a simple dialog box asking for the name of the CAM or IPT to be used in the filter will be shown. The user enters this information, then dismisses the Apply/Edit dialog by means of the X cancel button in the top-right of the dialog.

Note that if the prefilter requires one or more parameters, as in the CAM/IPT example, the prefilter name and the parameter value(s) will be displayed in the Status Bar, as shown in Figure 6.4 below.

---

## Figure 6.4: Status Bar Showing Current Prefilter and Parameter

If you wish to edit instead of apply a filter, press the Edit button. This brings up the Prefilters Edit dialog (Figure 6.5).

Note that users can select either one of their own User prefilters or a Global prefilter for editing. Editing a Global prefilter and saving it as a User prefilter is a convenient way of creating a custom prefilter, assuming that a Global prefilter exists that is similar to the desired custom prefilter.

But since Global prefilters are under the control of the Empower administrator, users can't save changes to a Global prefilter as a Global prefilter. Instead, users can start with a Global prefilter, edit it, and then save it as a User prefilter. When a Global prefilter is selected for editing by a non-administrator, the Edit dialog will show the filter name in gray, and the Save button will be disabled; the user will need to click the Save As button instead.

Note that, as is the case with Views, there can be User and Global prefilters with the same name. Again, this is not recommended practice, but Empower allows it.

So, with these preliminary comments out of the way, the user selects a prefilter and clicks the Edit button. This opens the Edit Prefilter dialog box (Figure 6.5) which provides a highly interactive and intuitive methodology for creating and customizing filters. This filter operates in much the way that the Views Edit dialog does.

---

## Figure 6.5: Prefilter Edit Dialog

Figure 6.5 shows the Edit Filter Dialog box in the process of building up a complex user prefilter. Note that the Column Group and Columns list boxes help the user choose the correct data items (making it impossible to chose a database column that doesn't exist, say by misspelling it). The Prelogic and Postlogic edit boxes are a way to add arbitrary text at the beginning and end of a single condition. The read-only box toward the bottom of the dialog shows the SQL filter condition as it is being built up by use of the dialog. The text box at the very bottom of the dialog allows you to enter a description for the prefilter.

Note that interactive filters always execute with an "and" operator between filter items. For instance, if you chose CAM="Smith" and DQI="F" in the filter boxes, only elements that meet both criteria will be displayed.

You can use dates as the value in your prefilter expressions, just as you can in interactive filtering (see Chapter 4). However, in prefilter expressions, you will need to enter the dashes between the year, month, and day parts of a date. So you would enter January 15, 2016 as 2016-01-15, whereas you can enter the same date as 20160115 in an interactive filter.

By contrast, prefilters allow the user to create much more complicated filter expressions. Prefilters can include the "or" operators, can compare values of columns (i.e., AcwpCum > Eac), can have nested arguments and even include a SQL statement.

Note the checkbox at the upper right corner of the dialog: "Show in Menu." Checking this will cause the prefilter to show in either the Prefilters > Global or Prefilters > User menus (if space allows). Unchecking this will mean that the prefilter will not be shown in either of these menus; it will only be visible in the list boxes in the Apply/Edit and Delete/Reorder dialogs (see below), and they will be listed inside square brackets to indicate their "non-menu" status.

In the previous example, the filter values were hardcoded. You can also build prefilters where Empower will prompt for part of the filter condition. Figure 6.6 shows how to prompt for a value that will be used in the prefilter condition. In the Value textbox, enter the prompt string surrounded by parentheses. When you move the cursor away from the Value textbox, Empower will put single quotes around the text. When you apply this prefilter, Empower will show a dialog box that says "Enter CAM/IPT", then use the value you enter in the test. In this case, that means that elements whose ProjOff equals the CAM/IPT you entered will be displayed in the Sort Window.

---

## Figure 6.6: Using a Prompt in a Prefilter

If you plan to use a prefilter with a prompt in a Dashboard, note that the usual behavior for such filters is to use whatever value was entered for the prefilter when constructing the Dashboard. If you would like the prefilter to prompt each time the Dashboard is opened, enter '???' (without the quotes) in the filter prompt, then save your Dashboard. This will tell Empower to prompt for the prefilter each time the Dashboard is opened.

You can also use special characters, called wildcards, in prefilters. There are two wildcard characters: the percent character (%) matches zero or more characters, while the underscore (_) matches exactly one character. When using wildcards, the string of characters containing the wildcard is called the pattern. An important thing to remember is that when using wildcards, you use the operators "like" or "not like" instead of equals (=) and not equals (<>).

The following table gives some examples:

| Pattern | Input | Matched? |
|---------|-------|----------|
| 3 | 35 | no; input isn't exactly '3' |
| 3% | 3 | yes; % matches zero characters |
| 3% | 35 | yes; % matches the '5' |
| 3% | 31234 | yes; % matches the '1234' |
| 3% | 73 | no; the input doesn't begin with '3' |
| %3% | 3 | yes |
| %3 | 73 | yes; the % matches the '7' |
| %3 | 789 | no; input doesn't end with '3' |
| 3_ | 35 | yes; the _ matches the '5' |
| 3_ | 3 | no; the '3' isn't followed by exactly one character |

Figure 6.7 shows how to use a wildcard character in a prefilter (combined with a prompt).

So when you select the "WBS Contains" prefilter, Empower will prompt you for the WBS number (actually, part of a WBS number), then match any elements whose WBS number contains the text you entered.

---

## Figure 6.7: Using a Wildcard in a Prefilter

So, using the MOH-2 contract as an example, if you entered "22" at the prompt, you'll see WBS=2200 in the Sort Window. If you entered "20", you'll get elements 2000, 2200, 3200, 5200, and 6200. If you just wanted elements that began with "20", you would remove the first % in the pattern, so that the test would read "WbsNum like '(WBS)%'".

Here is an example of a prefilter that requires two inputs. Figure 6.8 shows the Filter editor; we are going to filter elements with a given CAM and which have a percent complete less than an input value.

---

## Figure 6.8: A Prefilter with Two Inputs

When we choose the filter, we see the dialog in Figure 6.9. Note that the dialog tells us it is prompting for the first argument, and that there are two arguments in total for this prefilter. In this figure, we have already entered the CAM.

---

## Figure 6.9: Two-Input Prefilter Requesting First Input

Now we click the OK button. We next see the dialog of Figure 6.10, asking for the second of the two arguments. We enter a value (50 in this case), click OK, and the prefilter is applied.

---

## Figure 6.10: Two-Input Prefilter Requesting Second Input

Once the prefilter is applied, the Status Bar will show the name of the current prefilter and the two arguments entered by the user, as shown in Figure 6.11.

---

## Figure 6.11: Status Bar Showing Two-Argument Prefilter Applied

---

## 6.3 Edit Sort Filter and Edit Gantt Filter

These two commands allow the user to edit the currently chosen Sort or Gantt prefilter. If the Gantt chart is not currently open, the Prefilters menu will only show the Edit Sort Filter command. If the Gantt chart is open, the Edit Gantt Filter command will be added to the menu. Both commands bring up the Edit Filter dialog; the use of this dialog is described below under the Apply/Edit command.

---

## 6.4 Delete/Reorder

This command allows the user to delete any of their own prefilters (recall that only the administrator can delete Global prefilters), or to change the order these prefilters appear in the Prefilters > User menus. Ordinary users can neither delete nor reorder Global prefilters. Figure 6.12 shows the dialog box that appears when the user selected the Prefilters > Delete/Reorder command.

---

## Figure 6.12: Prefilter Delete/Reorder Dialog Box

To reorder a prefilter, click on the prefilter, then click on the up arrow or down arrow buttons to shift the prefilter by one position. When you have the prefilters ordered to your satisfaction, click the Reorder button, then close the dialog by clicking on the X in the upper-right hand corner of the dialog.

Note: if you reorder the prefilters in the list with the up and down arrows, and then close the dialog without clicking the Reorder button, your changes will not take effect.

To delete a prefilter, click on the prefilter, then click the Delete button. Repeat until you've finished deleting the prefilters you want to get rid of, then close the dialog as described above.

---

## 6.5 Security Prefilters

We have said that there are two kinds of prefilters, user and global. There is actually another quite different type of prefilter, called a "Security Prefilter." This is a prefilter that is created by the administrator and associated with a user's Empower account. The purpose of a security prefilter is to limit a user's access to parts of a contract, but in this case, for reasons of security rather than efficiency. The security prefilter will not appear on the Prefilters menu, and the user will not be able to see what the filtering criteria are. The security prefilter is largely invisible to the user, which is why we've left it to last in this section. The only indication to the user that a security prefilter has been applied is the "SPF" notation at the far right on the status bar, as shown in Figure 6.13.

---

## Figure 6.13: Toolbar, Showing Application of Security Prefilter

---

## 6.6 Display Name Prefilters

When creating a prefilter, the "DisplayName" option in the "Value" dropdown has its own special behavior.

---

## Figure 6.14: Value dropdown, Showing DisplayName option

This option allows you to create a filter that dynamically replaces "DisplayName" with the name of the current Empower user without prompting them for an input. To be precise, the value used will be the user's "DisplayName" (see the User Maintenance dialog) if one is set, or the "UserName" of the user if they do not have a "DisplayName" set.

For example, we could create a filter that compares ProjOff to DisplayName.

---

## Figure 6.15: ProjOff DisplayName Filter

If the user "Spataro" applied this filter, the data would be filtered to elements where the ProjOff is called "Spataro". While this filter in particular is similar to the "CAM/IPT" filter discussed earlier in this chapter, the distinction here is that the user will not be prompted for any input when applying the filter. This behavior can be especially useful for use with the LOGIN_FILTER_UC configuration option for setting default filters on login. (See the technical note, "The Empower Configuration File," available on our support website http://encoreanalyticsllc.freshdesk.com/support/solutions for more details.)
