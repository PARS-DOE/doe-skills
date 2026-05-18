# 16.15 System Submenu

A number of more specialized commands are grouped together on the Admin > System submenu.

## 16.15.1 User Maintenance

The User Maintenance dialog operates in two distinct modes. When the currently logged-in user is an administrator, the dialog operates in admin mode, and allows the user to add and delete users and groups, add users to groups or remove them from groups, change the access of users to the various contracts, and change other attributes of a user. When the currently logged-in user is not an administrator, the dialog operates in non-admin mode, in which case it gives the user a read-only view of only that user's attributes.

### 16.15.1.1 Admin Mode

In Admin Mode, the User Maintenance dialog presents all user and group management options.

In this mode, the user (an administrator) can change all the attributes shown in the dialog for any user in the database. All these changes will be kept in memory until the user presses Save Changes. Thus, for instance, if the user changes some values for Alice, switches to Bob and makes some changes for him, then selects Alice again, all the changes for her will be shown in the dialog. If the user decides to abandon the changes just made, the user just exits the dialog by clicking the X in the upper-right hand corner.

The Users/Groups select box will show all users and groups (with a note in parentheses identifying whether the name is of a user or of a group) except the Administrator. (The administrator always has all rights, so there is no point in including the administrator in the User Maintenance dialog.) The Contracts select box shows all contracts in the current database. Note that Alice is selected and that she is a user, not a group. Furthermore, there are three contracts in the currently open database; Alice has read access to the contract "LAREMD" as indicated by the leading "R," write access to "MOH-2," as indicated by the "W," and no access ("X") to the "BOOMERANG" contract.

This figure also shows:
- Alice is not a member of a group (since the Group select box is blank).
- Alice's user code is "CAM" (user codes can be employed to customize Empower's user interface; see Section 18.7 for more information).
- Alice's publication level is 0 (see Section 18.6 for the significance of the publication level).
- Alice has not been assigned an approval role for narrative workflows.
- Alice is not configured for OS Authentication (see Section 2.2).
- Alice has not been assigned an approval role for narrative workflows.
- Alice's display name is "Liddell, Alice". If a user has a Display Name set, that name will be shown instead of the Empower login name wherever user names are displayed. This can be helpful when your site assigns cryptic letter/number strings for usernames, and you want to use those names in Empower (e.g., when using single sign-on).
- Alice doesn't have an email entered (this would be expected if Alice had a role in narrative workflows).
- Alice has not been granted the ability to login as Admin.
- Alice has a prefilter configured (see Chapter 6). In this case the prefilter will limit the elements shown in the Sort Window to one for which the CAM is "Price."

In the figure below, showing just a portion of the User Maintenance dialog, we see a user who has been added to a group. Note that Bob is identified as a User in the Group G1, and that the Group select box also shows the group to which the user belongs. The significance of group membership will be explained later.

Pressing the +User button brings up the Add User dialog. Multiple users can be added at once by entering a list of user names, separated by semicolons.

Adding groups works just like adding users: press the +Group button and enter one or more group names separated by semicolons.

To delete users and/or groups, select them and press the Delete button. You can select just one user, or multiple users, either in a continuous range, or in a disjoint selection.

The Contracts select box and the Toggle Permissions button allow the administrative user to change the access users have to the various contracts in the current database. Recall that each contract in the Contracts list is preceded by a letter indicating the type of access the selected user has to that contract: (R)ead, (W)rite, and (X) for None.

There are four cases to consider.

In the simplest case, the access of one user to one contract is changed. Select the desired user and the desired contract. Then press the Toggle Permissions button. This will cycle the access flag through the three possibilities (the cycle is X-R-W-X).

The next case is changing the access of multiple users to one contract. Simply select the desired users, either with a continuous selection or disjoint selection, select the desired contract, then press the Toggle Permissions button as necessary to make the selected contract have the desired access flag. Now all the selected users will have that access flag for the selected contract.

The third case is changing the permissions on multiple contracts for one user. Select the desired user and the desired contracts. (Just like the Users select box, the Contracts select box allows extended selection, either continuous or disjoint.) Then press the Toggle Permissions button. The key thing to note here is that the access flag for the first contract in the list will be set to the next value in the cycle, and all the other selected contracts will have their access flags set to the new value for the first contract, regardless of what their access flags were originally. So if the access flags for four selected contracts were originally X, X, R, W, after toggling the permissions, they would be R, R, R, R.

Finally, one can select multiple users and multiple contracts. In this case, select the desired users and contracts, again using continuous or disjoint selection, then toggle the permissions until the access flags are desired. As in the previous case, the access flag for the first selected contract is cycled from its original value, and all the other selected contracts are set to match, regardless of their original values.

Now we return to the concept of groups. Groups offer an efficient way to manage the attributes of a large number of users. A group is created and users are assigned to a group. Then the attributes of a group can be changed (such as changing which contracts they have access to), and all users in that group at the moment, as well as all users subsequently added to the group, will have the same attributes. In fact, when a user is a member of a group and logs into Empower, after Empower validates the specific user (i.e., checks the user's password), Empower acts for most purposes as if the user is really the group.

Note that only actual users can login to Empower; you cannot login as a group.

Adding and deleting groups has been covered above. You add a user to a group by selecting the user (again, you can multiple-select users), then selecting the desired group from the Group select box. To remove a user from a group, select the user, then select the blank entry in the Group select box (this will always be the first entry in the dropdown list).

When a user is in a group, and that user is selected, the user's contract permissions will not be shown in the Contracts select box. In fact, that box will be blank. (You can see this in Figure 16.123.) This is because the user's contract permissions are effectively those of the group, and it would be misleading to show the permissions that were associated with the user when those permissions are irrelevant. If, however, a user is removed from a group, whatever contract permissions the user had before being put in a group will be displayed in the Contracts box. In other words, when a user is put in a group, his or her existing contract permissions are not wiped out; they are kept in the database, but not used until and unless the user is removed from the group.

Note that the above paragraph describes what happens when an administrative user selects a user who is in a group. The situation is different for a non-administrative user using this dialog in non-admin mode, as described in the next section.

If the "Log in as Admin" box is checked, the selected user will be given the ability to login as the Admin user, without actually entering the Admin user's username and password. A user with this ability will logon with his or her usual credentials, and will see their own username when logged in as themselves. Since they have the ability to login as Admin, they will see an additional option in the "File" menu called "Login as Admin."

If they select this menu item, the current user will then be logged in as the Admin user, so "Admin" will show as the current user in the status bar, and the user will be able to perform all the actions that are reserved to the Admin user. The user can also toggle back to their usual credentials by selecting the menu item "File > Log in as <username>." For example, if Price has logged in as Admin, he could toggle back to his own credentials by selecting "Login as Price."

Note that the "Set Password" menu item has been removed so that Price cannot change the password for "Admin" while logged in as the Admin user.

One use case for this capability is an installation where the Admin credentials are restricted to members of the IT team; in this case, Empower users who would normally be Admins (i.e., users who need to add and delete users, import global items, etc.) could be given the "Log in as Admin" ability so they would not have to rely on IT personnel to perform these tasks. (If you have access logging enabled, the access log will show the actual username and that that user logged in as Admin.)

### 16.15.1.1.1 Global Groups

User groups in Empower can be designated as "Global Read" or "Global Write" groups if desired. Note that only one "Global Read" and one "Global Write" group can exist at a time, so you cannot have multiple groups with the same global type. A group can be marked as either "Global Read" or "Global Write" but not both. A "Global Read" group will have "read" permissions for all contracts in Empower, and will automatically gain permissions for any new contracts that are added.

Similarly, a "Global Write" group has "write" permissions for all contracts and automatically gains write permissions for any new contracts that are added.

### 16.15.1.2 Non-Admin Mode

When a non-administrative user brings up the User Maintenance dialog, things work a bit differently. First, when the admin user is logged in, the dialog shows the three non-administrative users (Alice, Bob, and Charlie), and Admin has just granted write access to Alice on contract MOH-2.

In the next figure, Alice has brought up the User Maintenance dialog, and there are a number of changes from the admin user's view.

First, Alice isn't shown, since Alice can't change her own permissions.

Second, most of the action buttons (+User, +Group, Delete, and Clear Password) are disabled (signaled by being grayed out).

From this figure, we can see that Bob (the user highlighted in the Users/Groups listbox) has no permissions ("X") for the MOH-2 contract.

But Alice can change Bob's permissions. That's why the Toggle Permissions and Save Changes buttons are enabled. So if Alice toggles Bob's permissions on MOH-2 to, say, "W", and presses Save Changes, Bob will now have write permissions on MOH-2.

Alice can only do this, however, because the admin user earlier granted Alice write permissions on the MOH-2 contract. Recall that Alice has no permissions on the other four contracts in the database (ALPHA through LAR EMD). That's why, when Alice looks at the User Maintenance dialog, she only sees MOH-2 in the list of contracts: she has only been granted the ability to grant permissions on MOH-2. If she wanted to give Bob some permissions on BOOMERANG, for example, the admin user would first have to grant her write permissions. In other words, a user can't grant permissions on a contract unless he or she has already been granted write permission on that same contract.

So now Alice grants write permission (or read permission, if she prefers) on MOH-2 to Bob, and the dialog looks like the expected state.

She saves the changes, and next we look at what Bob will see when he views the User Maintenance Dialog.

First, we see that Bob is not in the Users/Groups list box; it will only show non-admin users other than the currently logged-in user. Second, he can see that Alice has write permission on MOH-2.

If Bob selected user Charlie, he would see "X - MOH-2" for Charlie's permissions. But since Bob now has write permissions on MOH-2, he could grant permissions to Charlie on that contract (read or write, depending on how generous Bob is feeling).

Note that once a user has been granted write permission on a contract, he or she can now grant permissions to other, less fortunate, users.

Does it work the other way? Can Bob, having been granted write permissions on MOH-2 by Alice, use his new powers take away Alice's permissions, changing her access from write to read, or perhaps to no permission at all? He can! Bob can change Alice's access to read or none ("X"). The fact that Bob was granted his write access by Alice in the first place doesn't mean that there is a hierarchy of non-admin users with Alice above Bob.

## 16.15.2 Open Sessions

This option opens a report in the Empower report pane that displays current active Empower sessions. This is useful for determining which users are currently using Empower and how long they have been logged in.

Notice the text at the bottom of the report; the default session expiration time is eight hours. This can be customized via an Empower configuration setting. Likewise, the time zone used for the "Last Login" time can be customized as well. See the techno note titled "The Empower Configuration File" for more details.

## 16.15.3 Delete Shared Items

This command allows the user to delete various items that are not contract-specific. When selecting "Contractors" in the Item Select box, the select box on the right is labeled "Contractors" and populated with the contractors in the database. If it should happen that the MEGAHERZ ELEC company should be removed from all contracts in the database, the user could select the unfortunate company, press Delete, and that contractor will be deleted from the database.

Note the checkbox labeled "Delete linked records". If this is not checked, and the user attempts to delete an item (contractor, unit, etc.) that is still being used somewhere in the database, a warning will be displayed, and the item will not be deleted.

The user can force deletion of units that are still being used in the database by checking the "Delete linked records" checkbox. All records linked to the selected unit will also be deleted.

Some very large contracts can take a few seconds to be deleted. The Delete button is disabled during this process to keep impatient users from pressing the button again and inadvertently deleting the next contract in the list.

## 16.15.4 Rescale Values

As noted in the dialog box text, this function is rarely needed. You use it to:

1. Change a unit's scale across the entire database. Only the "Admin" user can do this, as it affects every contract and period. The Admin might do so if he or she has decided, say, that Dollars should be stored in "Ones", rather than "Thousands".
2. Correct periods or contracts that have a scale value inconsistent with the rest of the database. Any user can use this function to correct such errors in contracts to which he or she has write access.

It is helpful to remember that the larger the unit scale, the smaller the numbers stored and displayed. For example, if the scale is "0", a value of 1000 is stored and displayed as 1000. If the scale is "3", a value of 1000 is stored and displayed as 1. Nothing has really changed — a single one-thousand dollar bill is the same amount of money as a thousand one-dollar bills. But your wallet (or sort window) will be much fatter in one case than the other.

Note: Rescale Values only rescales the numbers that all the other values depend upon. So, for instance, it will change cumulative BCWS, but not current BCWS, since the latter is calculated as the difference between the current period's BCWS and last period's BCWS. What this means is that you will need to run Recalculate after Rescale Values. Since recalculating is one of the more time-consuming operations in Empower, we don't do the recalculation automatically; we let you decide when you want to do it.

The Rescale Values dialog is reached by the System > Rescale Values command on the Admin menu.

This figure tells us that the dollar amounts for the MOH-2 contract are stored as thousands (note the "3 - Dollars" in the Scale - Unit list box). The amounts for hours and equivalent persons (EQP), on the other hand, are stored in ones (remember that 100 = 1).

Consider the first scenario above. Suppose we decide we'd really like to manage right down to the dollar, so we want to convert the dollar scale from "3" (thousands) to "0" (ones). We check the "Adjust Scale" option below the units list box, and the appearance of the dialog changes.

All contracts are selected, and the button under the "Periods" list box is disabled. The change reminds us that adjusting the scale of a unit affects the entire database — all contracts and all periods.

Now we have to think a bit. The dollar amounts in our database are currently in thousands, as shown in the units list box. To put them in ones, we need to decrease the scale factor by 3 (from 3 to 0) and so we need to make the values stored in the database larger by a factor of 10³. Accordingly, we enter 3 in the text box.

(Seem backwards? Remember that as we make the scale factor smaller, we must make the values stored and displayed larger. Converting "thousands" to "ones" is like trading a single thousand-dollar bill for a thousand one-dollar bills.)

We press the Scale button, and see the status dialog.

Empower runs through all the tables that contain dollar values (starting with BaselineChg and ending with FutureEtc) and multiplies the existing dollar values by 1000 (10³). Then it updates the scale value for Dollars from 3 to 0.

Similarly, if we wanted to convert from thousands to millions, we'd enter "-3" in the "Multiply values" text box. Every value for that unit would decrease by a factor of 1000 (be multiplied by 10⁻³) and the scale factor would increase from 3 to 6.

After adjusting scales, be sure to recalculate all contracts so that derived values (e.g., statistical forecasts) are rescaled appropriately.

Now consider the second scenario: You want to change the unit scaling for just one contract or one period. Say you decide you need to multiply all the dollar values for MOH-2, JAN04 by 1000.

(Aside: You might have to do this if you imported a file that contained values in thousands, but incorrectly identified the scale as ones – that is, the scale factor should have been "3", but was "0" instead. This is an error in the file, and you should complain to whomever provided it! So, after sending a stern email to the offending party...)

You bring up the Rescale Values dialog again, and you enter 3 in the text box. You don't select "Adjust Scale", though. You select the contract and period (MOH-2, JAN04), and press the Scale button under the Period list box. It is important that you press this button; if you press the Scale button under the Contract list box, you'd rescale all periods in MOH-2. Under other circumstances, you might want to do that, but in our scenario, we just want to rescale one period.

Now all the dollar values for JAN 04 will have been multiplied by 1000. If you bring up the Rescale Values dialog, you'll note that the scale for units has not changed; it is still 3.

This is a key point that bears repeating: Adjusting the scale changes the values in the database for whatever unit is selected (dollars, EQP, etc.) and changes the scale factor. Scaling values without checking the "Adjust Scale" checkbox changes the values for the selected contracts/periods/units only, without changing the scale factor.

## 16.15.5 Input Templates

Selecting the Input Templates command brings up the following dialog.

To delete templates, select one or more templates, and press Delete.

To reorder a template, select it, then press the up arrow button or the down arrow button. The selected template will be moved one spot up or down in the list. Repeat until you've got each template where you want it. Then press Reorder to accept your changes.

## 16.15.6 Upload License

Empower requires a valid set of license files to run. This section describes how to upload a new set of license files, assuming that you already have a valid license and can run Empower. This scenario would arise if you were coming to the end of your license period and had renewed, getting a new set of license files as a result, or if you had purchased more client licenses and needed new license files to reflect that fact.

First, click on the Upload License command. You will be asked to provide the location of your new license files.

Once you have selected the zip file containing your new license files, the dialog will update.

After you have pressed Upload, the dialog will display the completion status.

Now the new license information (expiration date, number of users, code) will be shown in the About Box whenever you bring it up.

## 16.15.7 Download Logs

This command downloads the Empower's log files to a zipped file on the user's computer. This can be helpful in the event of unexpected behavior, and you might be asked by Empower technical support staff to download the logs and send them to us so we can better help you.

## 16.15.8 Sanitizing Files

If the ENABLE_SANITIZE option is enabled in your Empower configuration file you will see an additional option in the System submenu. This option is not enabled by default. See the techno note titled "The Empower Configuration File" for more details on how to enable this option.

Sanitizing files can be useful when you would like Empower support to help troubleshoot data but are unable to send the data for security reasons. In particular, this option can be helpful if the issue is related to importing a data file. "Sanitizing" the file will replace text fields like names and descriptions with random strings and, if selected, will also change numeric values using a randomized numeric adjustment value. The resulting downloaded file will have "sanitized" appended to the filename.

Clicking the Sanitize File menu option brings up the dialog. Notice that only specific file formats are supported; data in formats other than those listed in the dialog cannot be run through our sanitizer.

The user clicks Choose File, which brings up a file selection dialog. Once the user has chosen a file through this dialog, Empower's dialog changes slightly. Notice that the option to "Sanitize numeric values" is shown in this dialog.

After clicking "Sanitize" the window will update to show the status of the sanitizing process.

Depending on the type of file you are using, the status messages may look slightly different.

Once the status is completed, the sanitized file will download.

If you select an unsupported file type the dialog will display an appropriate message.

If ENABLE_SANITIZE is enabled, you will also see an additional option in the "Export EDI File" dialog called "Sanitize file". This option is only available for optimized files.

Selecting this option will export the file as usual, but will also sanitize the values in the exported file. This option can be useful if you need to send data to Encore Analytics but the format of the data file does not matter.
