# TN ConfFile (1)

*Source: TN-ConfFile (1).pdf*

---

## Technical Note: The Empower Configuration File

© 2013 Encore Analytics, LLC
April 7, 2025

## Contents

1. [Introduction](#1-introduction)
   - 1.1 [Modifying the Configuration File](#11-modifying-the-configuration-file)
   - 1.2 [Configuration File General Settings](#12-configuration-file-general-settings)

2. [Menu Customization](#2-menu-customization)
   - 2.1 [Configuring the User Interface with User Codes](#21-configuring-the-user-interface-with-user-codes)
   - 2.2 [Configuring the User Interface with Custom Files](#22-configuring-the-user-interface-with-custom-files)
   - 2.3 [Adding Custom Links to the Empower Menu](#23-adding-custom-links-to-the-empower-menu)
   - 2.4 [Adding and Moving Empower Menu Items](#24-adding-and-moving-empower-menu-items)
   - 2.5 [Adding Submenus](#25-adding-submenus)
   - 2.6 [Identifying IDs for Custom Items](#26-identifying-ids-for-custom-items)
   - 2.7 [WebEVM Download/Upload Configuration](#27-webevm-downloadupload-configuration)

3. [Adding EMF Export to the Chart Download Menu](#3-adding-emf-export-to-the-chart-download-menu)

4. [Admin User Configurations](#4-admin-user-configurations)
   - 4.1 [Disabling User Maintenance Items for Admin Users](#41-disabling-user-maintenance-items-for-admin-users)
   - 4.2 [Import Script Restrictions](#42-import-script-restrictions)

5. [Enforcing Complete Narratives on Submit](#5-enforcing-complete-narratives-on-submit)

6. [Customizing the VAR Insert Dropdown](#6-customizing-the-var-insert-dropdown)

---

## 1. Introduction

Several aspects of Empower's operation are controlled by settings in its configuration file, empower.conf. This document describes how to configure Empower using this file.

### 1.1 Modifying the Configuration File

The empower.conf file will be found in Empower's home directory. It is a plain text file and can be edited with your favorite text editor. If you have access to the Empower server, you can edit the file directly.

If, however, you do not have access to the server (often, only system administrators have such access, and Empower administrators are often users with Empower skills but not IT training), you can create a new configuration file on a different machine (e.g., your usual desktop or laptop), and set CONFIG_DIR to the location of your new configuration file in the empower.conf file on your Empower server.

Once CONFIG_DIR is set, Empower will use your new configuration file, allowing you to make configuration changes locally instead of on the Empower server.

After editing the config file, the Empower service should be restarted in order to ensure that the changes are picked up by Empower.

### 1.2 Configuration File General Settings

Here is an example of an Empower configuration file on a Windows system:

```
# Empower configuration file
OS=Windows
# Use_Batik=1
```

The '#' character is used to comment out a line.

Data Source specific customizations can be indicated by creating a section in the configuration file for that data source. Options under a data source section will override and add to any options in the config file that would otherwise apply to the data source. Below is an example of a data source configuration where some menu customizations are made for a data source called "Empower", note that lines have been wrapped for readability:

```
[Empower]
ADD_MB_C=[["var_state", "user_sep1"],
["inputs", 15, "ddown", "Download Data File"],
["inputs", 16, "dup", "Upload Data File"]]
```

Empower will use the general options listed in the config file (i.e. those not listed under a specific data source) unless the same option is specified under the data source specific configuration. In that case, the datasource configuration will override the more general option.

Data source specific configuration sections should be added below any general options; i.e. general options that should apply to all data sources should be listed at the top of the file before any data source specific sections. Multiple data source specific sections can be listed in the same configuration file. Each section should be indicated by a line with the datasource name within square brackets.

---

## Configuration File Variables Reference

**ACTION_WARN**
Threshold (in days) used when coloring the background of due dates in the Action Item Report.

**ADD_MB_**
Used to configure Empower's user interface. See the next sections of this document.

**ALT_AI_NAME**
Used to customize the AI Narrative and SEM AI Narrative report names. Entries should be the text that will replace "AI" in the report names. For example, if you wanted to use the text "Assisted Intelligence" instead of "AI", you would use ALT_AI_NAME=Assisted Intelligence

**ATR_DIR**
Indicates a directory containing cgi files to be used with Empower. Not necessary if using the default directory /empower/cgi/.

**AUDIT_AGENCY**
Used to customize the auditing agency for the Audit Attributes and Test report, and associated menu items. The default is "Audit." See the technote "Empower's Audit Report."

**AUDIT_SHORTDESC**
If set to 1, the Audit Report will use the "ShortDesc" column instead of the "Descr" column.

**AU_DISABLE**
Used to disable items in the "User Maintenance" dialog for specific users. See the section "Disabling User Maintenance Items for Admin Users" for more information.

**AU_ADDCOLS**
Used to enable adding custom fields when importing for specific types of Admin users. If not present, any user can add custom fields when importing. The entry should be a list of characters indicating which values of AdminUser should have the ability to add custom fields. Any users with an AdminUser value not in the list will only be able to update exiting custom fields when importing; they will not be able to add new custom fields via the import. For example, the entry AU_ADDCOLS=LM would allow only users with AdminUser set to 'L' or 'M' to add new custom fields when importing. See the section "Disabling User Maintenance Items for Admin Users" for more information on the AdminUser field.

**AU_RECALC**
Used to disable items in the "Recalculation" dialog. These items will never be disabled for the "Admin" user itself (UserID = 1), but can be disabled for users with "Log in as Admin" permissions. Users that should NOT have these items disabled can be indicated by listing their "AdminUser" values at the beginning of the AU_RECALC entry. For example, the entry AU_RECALC=LM:re_cc;advanced would disable the "Recalculate" button under "Contracts" and the "Show Advanced" button for ALL users except for users with AdminUser = L or AdminUser = M and the "Admin" user. Items that can be disabled include: ev, fetc, sch, dqi, evas, cur, rpt, es, fcst, eqp, f3, f4, decalc, re_cc, re_cd, toggle, advanced

**CHECK_LEVEL**
Specifies the level of additional security validation applied to requests from logged-in Empower users to prevent them from bypassing application-level security to view contract, period or element-level data to which they have not be granted access. See TN-Security.pdf for details.

**CONFIG_DIR**
Used to specify an alternate directory to use for Empower configuration files, such as empower.conf. If not set, defaults to the empower directory.

**CPANM**
Specifies the location of the cpanm Perl package manager; not needed if cpanm is already in the path.

**CPRFLAGS**
Used to set defaults for checkboxes in the "Export IPMRs" dialog. Valid entries are: RPT, CA, LL, INDENT, NOWBS, LONGDESC, NOZERO. For example, if you had CPRFLAGS=NOWBS;LONGDESC, only the "Hide WBS number" and "Use long descriptions" checkboxes would be checked when you open the "Export IPMRs" dialog. All other checkboxes would be unchecked by default. RPT, CA, and LL are used to set the default option for the "Export to" dropdown. If more than one of these options are listed in "CPRFLAGS," the first one listed will be used.

**DASH_DELAY**
Used to configure the delay time for loading data when opening data with a dashboard applied. This can help if some data does not appear to load correctly when a dashboard is applied. The delay is set in milliseconds. For example, DASH_DELAY=2000 would have a two second delay before loading.

**DISABLE_ALL_CC**
Used to disable the "OK" button in "Open Dataset" when opening datasets for all contracts with the "all elements" filter selected. If set to 1, no user can open all contracts for all elements. If set to 2, only users with security prefilters can open "all contracts" for "all elements." Defaults to 0, which does not disable the "OK" button.

**EMAIL_CONFIG**
Used to configure Narrative Workflow email notifications. See tech note, "Email Notifications with Empower."

**EMAIL_SUBJECT**
Ditto

**ENABLE_DATASET_CALENDARS**
Enables the "Calendars" dropdown in the "Open Dataset" dialog. If set to 1, the Calendars dropdown will be enabled, otherwise the dropdown will be greyed out. For more information on this dropdown, see the "Dataset Calendars" section of the Empower User's Manual.

**ENABLE_SANITIZE**
If set to 1 enables the "Sanitize file" option for Export EDI File as well as the "Sanitize File" menu option. See the Empower User's Manual section titled "Sanitizing Files" for more information.

**ENFORCE_PRUNE**
If set to 1, all imports will automatically be pruned. Defaults to 0 if not present, which will not automatically prune imports. See the document "Pruning Data in Empower" for more details on pruning.

**EXPIRE**
Indicates the number of seconds a user can be idle before they are logged out automatically. If not present the default is 8 hours. If set to a number, Empower will prompt users to either continue their session or log out after that number of seconds. If the user does not click either option within a certain amount of time, they will be logged off automatically. This value is also displayed in the "Open Sessions" report. For example, "EXPIRE=1800" would prompt users to continue or log out after they have been idle for 30 minutes. See TN-Security.pdf

**EXPFLAGS**
Used to set defaults for checkboxes in the "Export EDI File" dialog. This parameter should be a list of semicolon separated text entries. Valid entries are: Rpt, Ca, Wp, Ll, Fetc, Sch, Narr, Audit, Altd, COLS, USER, REPR, SANITIZE in the order that they appear in the dialog box. For example, if you had EXPFLAGS=FETC;SCH the Export EDI dialog would have "Export future period data" and "Export schedule data" checked. RPT, CA, and LL are used to set the default selection for the "Export to" drowpdown. If more than one of these options is listed, the first one will be used.

**EXPORT_ALL_DELAY**
Used to configure the delay time between downloads for the "Export Open Windows" menu option. The delay is set in milliseconds. For example, EXPORT_ALL_DELAY=2000 would have a two second delay between each download.

**EXPORT_EMF**
See the section "Adding EMF Export to the Chart Download Menu."

**GANTT_FLAGS**
Use to set defaults for checkboxes in the "Set Gantt Options" dialog. If set to 1, "Show Late Finish" will be checked by default. 2 will check "Show Slips" by default, and 3 will check both options by default.

**HIDE_PRINT_CHART**
When set to 1 hides the "Print chart" option. This is useful when enforcing banners for charts since the "Print chart" option is not compatible with banners. See TN-HeadersandFooters.pdf

**HIDE_MB_**
Used to configure Empower's user interface. See the next two sections.

**HIDE_TB_**
ditto

**HIDE_UNAPPROVED_VAR**
When set to 1, prevents users with no narrative role from seeing VARs that are not yet approved.

**IMPFLAGS**
Use to set defaults for checkboxes in the "Import EDI File" dialog. Valid values are: FETC, SCH, NARR, Audit, Cols, User, Elem, Stru, Unit, Clean, CONVERT, RECALC, PRUNE, SHARED. For example, if you had IMPFLAGS=USER;CLEAN the "Import user data" and "Clean non-ASCII characters" options would be checked by default.

**IMPORT_SCRIPTS**
Use to control which users can import scripts into Empower. See the section "Import Script Restrictions" for more information.

**KEEP_DATASET_OPEN**
Sets the default value for the "Close on OK" checkbox in the "Open Dataset" dialog. If set to 1, the default will be to keep the dataset dialog open on "OK." If set to 0, the default will close the dialog on "OK." This default behavior can be overridden by the user for their individual session. Defaults to 0 if not set.

**LINREG**
If set to 1, directs Empower to calculate a linear regression forecast during recalculation and generation of the Six Period Summary report. This is a time-consuming operation and is disabled by default.

**MAX_LOOKUP**
The maximum number of lines allowed in XML imports. This value defaults to one million rows.

**MB_FILE_**
Used to configure Empower's user interface. See the next two sections.

**MSSQL_HOME**
Indicates the location of the SQL Server command line tools (sqlcmd and bcp). Not necessary if those tools are in the path.

**NARRFLAGS**
Use to set defaults for checkboxes in the "Export Narratives" dialog. Valid values are: VAR, USER, EAC, Sow, Wad.

**NARR_LIMIT**
Use to set a maximum number of narratives to display in the Banded Narrative reports. The default value is 100. Attempting to view more narratives than the limit in the banded narrative report will return a message indicating that you should filter to a smaller number first. Larger values may lead slower performance. When viewing a large number of narratives at once, using the "Admin > Export Narratives" may be preferable.

**NO_BULK**
Importing a file in Empower's optimized format is normally performed using the bulk load facility of the target database. This requires that the command line client for the target database be installed on the Empower server machine. If this is not true for a given database, set NO_BULK equal to the database type (mssql, oracle, psql). Empower will still import the optimized file, but it will not use the native bulk import facility, and the import will not run as quickly as when performing a native bulk import. You may disable native bulk loading for more than one database type by separating the types with semicolons, as in NO_BULK=oracle;mssql. The command line clients are sqlcmd and bcp for SQL Server, sqlldr for Oracle, and psql for Postgres.

**ORA_HOME**
Indicates the location of the Oracle command line tools (sqlldr and sqlplus). Not necessary if those tools are in the path.

**OS**
Set to Windows if Empower is running on Windows. Not used otherwise.

**PG_HOME**
Indicates the location of the PostgreSQL command line client (psql). Not needed if psql is in the path.

**POLL**
Used to set the "polling" interval for operations such as the "Check Status" refresh when queueing is enabled and various export statuses. For example, POLL=5000 would set the polling interval to 5 seconds.

**PWD_TMPL**
Defines rules for user passwords including password length and complexity. The format for the entry is: PWD_TMPL=<length>;<required types>. For example, to set a minimum length of 8 characters, use PWD_TMPL=8. The entry PWD_TMPL=8;aA would require that passwords have a minimum length of 8 characters and have at least one lower-case and one upper case letter. PWD_TMPL=8;Aa0+ would require a minimum length of 8 characters, at least one lower-case letter, at least one upper case letter, at least one number, and at least one symbol. If the PWD_Tmpl entry is omitted, there are no restrictions on user passwords and empty passwords will be allowed. See TN-Security.pdf

**QUEUE**
Used to configure queued recalculations and imports for Empower. See the document titled "The Empower Watchdir Import Facility" for more details.

**QUEUE_DIR**
Used to indicate a directory for Watchdir .pid and _que.log files. The _que.log files are generated when using Empower with "Queue mode" enabled. The default directory is empower. QUEUE_DIR should NOT be set to the empower/temp directory or the directory that has been specified for SHARED_TEMP. This option is primarily intended to allow for the use of "Queue mode" with Empower installations in Docker.

**REFLAGS**
Use to set defaults for checkboxes in the "Recalculate" dialog. Valid values are: FETC, SCH, DQI, EVAS, CUR, RPT, EV, ES, FCST, EQP, F3, F4, DECALC. If this entry is absent, Empower will use the recalc settings set for each contract.

**RLOGN**
Use to specify the full url of the machine hosting the Single Sign On if different than the machine hosting Empower. This should match your server side "rlogn" entry in default.aspx or index.php.

**SHARED_TEMP**
Used to configure Empower to create temporary files in an alternate location to its own temp directory. The entry should be a valid path to an existing directory that Empower has permissions to access. For example: SHARED_TEMP=/shared/temp

**SHOW_ADVANCED**
Used to configure the "Recalculation" dialog display. If present, the "Show Advanced" button will be toggled on by default when opening the dialog, showing the "advanced" recalculation options.

**TB_FILE_**
Used to configure Empower's user interface. See the next two sections.

**TEMP_DIR**
Used to configure Empower to use an alternate directory instead of empower/temp.

**TIME_ZONE**
Used to set which timezone should be used for timestamps in Empower. This entry should be a tzd database time zone name (lists are available online). If not set the time zone will default to "UTC". For example: TIME_ZONE=America/New_York

**USE_BATIK**
When set to 1, tells Empower to use the Apache Batik SVG toolkit. In order to use Batik you will need to install Java on your Empower application server. Not necessary if using rsvg-convert for SVG conversion.

**USE_DIRECT**
When set to 1, adds the "direct" option to Empower's invocation of the Oracle sqlldr utility. See http://docs.oracle.com/cd/B19306_01/server.102/b14215/ldr_modes.htm#g1023818 for information on the direct option.

**USER_NARR_ENFORCE**
Used to prevent submittal of User Narratives with incomplete sections. See the later section in this document for more details.

**VAL_FLT**
Used to indicate custom keys that should be validated as floats. This entry behaves similarly to VAL_INT, but will validate values as floats instead of integers. See the VAL_INT section below.

**VAL_INT**
Used to indicate custom keys that should be validated as integers. This can be useful if you encounter "not validated" error messages in the "empower.log" file when using custom charts or reports. Note that the "not validated" messages indicate that Empower is ignoring an unrecognized key, and should not disrupt the actual operation in Empower. Adding the unrecognized key to VAL_INT or VAL_STR can help remove those warning messages from the log, provided that the value for the key validates without error. For example: VAL_INT=xAxis,yAxis,showInLegend This entry would add xAxis, yAxis, and showInLegend to a list of keys that should be validated by Empower as integers.

**VAL_STR**
Used to indicate custom keys that should be validated as strings. This entry behaves similarly to VAL_INT, but will validate values as strings instead of integers. See the VAL_INT section above.

**VAR_ENFORCE**
Used to prevent submittal of VARs with incomplete sections. See the later section in this document for more details.

**WEBEVM_HOST**
Used to configure WebEVM download/upload options in Empower. WEBEVM_HOST should be set to the URL of the server hosting WebEVM. See the section "WebEVM Download/Upload Configuration".

---

## 2. Menu Customization

### 2.1 Configuring the User Interface with User Codes

Empower's user interface can be modified by removing certain commands from the menus and by removing certain buttons from the toolbar. These changes can be applied to specified classes of users, so that a certain class of users will not see the menu command to display the AI Narrative report.

First, as described in the Empower User's Manual, users can be assigned a User Code, an arbitrary string of one to four characters. (The User Code can be set in the User Maintenance dialog.) For the sake the discussion below, let us assume that your site uses the code "CAM" for Control Account Managers, and "PM" for Project Managers. Furthermore, let us assume that not all of your Empower users have a User Code assigned.

Second, two keys (HIDE_MB_ and HIDE_TB_) can be included in the configuration file to control which user interface elements are removed for a given class of user. The keys will be followed by an equals sign and a list of ids of user interface elements to be removed.

First, let's show where to find these user interface ids. The ids for the menu will be found in the menu.xml file in the empower/www directory. For example, in that file, you will find a line like this:

```
<item id="rp_ai" text="AI Narrative"/>
```

This tells you that the id for the menu item "AI Narrative" (under Reports on the Menu Bar) is rp_ai. Several lines later, you will find this line:

```
<item id="inp_var" text="VAR Narrative"/>
```

It tells you that the command to edit VAR Narratives on the Inputs menu has the id inp_var.

Now, to the keys themselves.

The key HIDE_MB_* is used to remove items from the menu bar. The * in this description is a placeholder. You will either replace the * character with a string that identifies which class of user this key applies to, or you will simply remove it.

If the first letter of a user's User Code matches the first letter of the string that replaced the *, the list of items after the equals sign will be removed from the user interface when that user is running Empower.

If nothing is put in place of the * (i.e., the key is HIDE_MB_), the list of items after the equals sign will be removed for any user whose User Code is blank.

Here are some examples to illustrate the use of this key:

- **HIDE_MB_C=rp_ai;inp_var**
  Removes the AI Narrative report from the Reports menu and the VAR Narrative command from the Inputs menu for all users whose User Code begins with an upper-case "C". This would apply to the users whose code is CAM. Note that multiple user interface ids can be specified and are separated by semicolons.

- **HIDE_MB_P=rp_ai**
  Removes the AI Narrative for users whose User Code begins with an upper-case "P" (thus applying to users whose code is PM). Note that you would typically put both this example and the previous one in the same configuration file, so that the user interface is tailored one way for CAMs and another way for PMs.

- **HIDE_MB_=rp_ai**
  Removes the AI Narrative for any user whose User Code is empty (i.e., is NULL in the database). (Note that the Admin user never has a non-NULL User Code.)

You can also configure the Toolbar with the HIDE_TB_* key. It works the same way as the HIDE_MB_* key, except that the elements it removes from the user interface are, of course, toolbar elements, and the ids are found in the file toolbar.xml.

So, for instance, the entry

```
HIDE_TB_C=tb_child
```

would remove the Children button from the toolbar for all users whose User Code began with "C".

### 2.2 Configuring the User Interface with Custom Files

We have already introduced the menu.xml and toolbar.xml files as the place you go to find the ids of the user interface elements you would like to remove for some or all of your users. You can make wholesale changes to the user interface by replacing the standard files with customized versions of these files for specific User Codes.

The key MB_FILE_ is used to specify a different menu file, while TB_FILE_ is used to specify a different toolbar file.

You can specify custom menu and toolbar files for a given User Code. The key MB_FILE_* is used to specify a custom menu.xml file, and TB_FILE_* specifies a custom toolbar.xml file for a User Code.

Naturally, you will want to take care when using this feature, and we strongly recommend you make a copy of the standard menu and toolbar files and make incremental changes to the copies until you get the user interface looking the way you want it.

It should also be noted that we will never alter your custom menu file. So if you are using a custom menu file, you will not see any new or altered menu items when updating Empower. For this reason, we would generally recommend using the dynamic menu alteration options described in this document unless you are unable to attain your desired result using those options.

As an example, suppose you wanted some users to be able to manage user permissions, but not be able to see any of the data in Empower. You could accomplish this using the following setup, assigning UserCode='A' to any users you want to have this UI configuration:

- Add these lines to empower.conf
  ```
  TB_FILE_A=tb_admin.xml
  MB_FILE_A=mb_admin.xml
  ```

- Create the file tb_admin.xml in your configuration directory (specified by CONFIG_DIR in empower.conf, defaults to the empower/www directory if not set) with these contents:
  ```xml
  <?xml version="1.0"?>
  <toolbar>
  </toolbar>
  ```

- Create the file mb_admin.xml in your configuration directory (specified by CONFIG_DIR in empower.conf, defaults to the empower/www directory if not set) with these contents:
  ```xml
  <?xml version="1.0"?>
  <menu>
  <item id="file" text="File">
  <item id="setpwd" text="Set Password" hidden="true" />
  <item id="login" text="Log Out"/>
  </item>
  <item id="options" text="Options">
  <item id="connection" text="Show Connection"/>
  </item>
  <item id="admin" text="Admin">
  <item id="usermaint" text="User Maintenance"/>
  <item id="license" text="Upload License"/>
  <item id="logs" text="Download Logs"/>
  </item>
  <item id="help" text="Help">
  <item id="manual" text="User's Manual"/>
  <item id="support" text="Support"/>
  <item id="about" text="About"/>
  </item>
  </menu>
  ```

### 2.3 Adding Custom Links to the Empower Menu

Custom links can be added to the Empower menu by adding new items to your custom menu file(s) or the menu.xml file. For example, you could add a link to the Encore-Analytics release history by editing the "help" section of your menu file:

```xml
<item id="help" text="Help">
<item id="manual" text="User's Manual"/>
<item id="daugold" text="DAU 'Gold Card'"/>
<item id="dqi_tests" text="Empower DQI Test Guide"/>
<item id="https://encore-analytics.com" text="Encore Analytics Web Site"/>
<item id="https://www.encore-analytics.com/support.html" text="Empower Release History"/>
<item id="help_ms1" type="separator"/>
<item id="support" text="Support"/>
<item id="about" text="About"/>
</item>
```

Note: some lines have been wrapped to fit the page.

### 2.4 Adding and Moving Empower Menu Items

Empower menu items can also be added or moved via the ADD_MB_ entry in empower.conf. The entry for ADD_MB_ should be a JSON array of arrays. The inner arrays should have this format:

```
[parent_id, position, id, text]
```

The entries for the inner array are defined as follows:

- **parent_id**: menu id of the parent item from menu.xml. If parent_id = null, the new item is at the top-level of the menu.
- **position**: the 0-based index of the new item under the parent item.
- **id**: the menu id of the new item or a link that should be opened when the menu item is clicked.
- **text**: the text that will appear in the menu for the new item.

If the value for "id" is an existing menu item, the item will be removed from its current position, then added at the new position that you specify. Items are added in the order that they are supplied, which may affect the positions of the items.

User codes work as usual for this item, see the previous sections of this document for more details.

Note: If HIDE_MB_ precedes ADD_MB_ in empower.conf it may affect the position of the added items.

#### 2.4.1 Example

```javascript
ADD_MB_=[["help", 4, "https://www.encore-analytics.com/news.html", "Empower News"],
["report", 3, "rp_cust1", "BAC Delta"],
[null, 9, "test", "Test"],
["test", 0, "rp_sixper", "Six Period Summary"],
["test", 1, "ch_workoff", "Schedule Work-off"]]
```

This entry would do the following:

1. add an "Empower News" item to the "Help" menu at position 4
2. move the "BAC Delta" custom report to the main reports menu
3. create a new top-level menu called "Test"
4. move the "Six Period Summary" report and "Schedule Work-off" chart to the new "Test" menu

Note that the "id" for the "BAC Delta," which is a custom report, is "rp_cust1." The "1" indicates the report ID. Should the report ID change (e.g. if the report was deleted, then reimported), then the entry for ADD_MB_ will need to be updated accordingly. See section 2.6 for more information on how to find this ID for custom items.

#### 2.4.2 Adding Separators to Custom Menus

You can also use ADD_MB to add separators to custom menus. The format for separator entries should be: [nextto_id, id] where nextto_id is the id of the menu item after which the separator will be inserted and id is the ID for your new separator.

```javascript
ADD_MB_C=[["var_state", "user_sep1"],
["inputs", 15, "ddown", "Download Data File"],
["inputs", 16, "dup", "Upload Data File"]]
```

This entry would move the "Upload Data File" and "Download Data File" from the "Admin" menu to the "Input" menu for users with UserCode C. It will also create a separator after the menu item with the ID "var_state" and assign it an ID of "user_sep1". This separator ID should be unique in your menu customizations. Menu item IDs can be found in the menu.xml file on your Empower server. Notice that the positions of items after the separator are incremented by one more than what they would be if the separator was not added.

#### 2.4.3 Adding the VAR-1 Report to Custom Menus

Empower also has a report called "VAR-1" that can be added via the ADD_MB option. This report displays the VAR Narrative report from the previous period. To add this report to a menu, use ADD_MB as usual, using rp_varp1 as the ID of the menu item. For example:

```javascript
ADD_MB_=[["report", 5, "rp_varp1", "VAR-1"]]
```

### 2.5 Adding Submenus

The ADD_MB option can also be used to add submenu levels to your menus. Both standard and custom items can be added to submenus, and multiple layers of submenus can be created. To add a submenu, create a menu item with a unique ID and the text you want to use for your submenu. Recall that in general entries have this format: [parent_id, position, id, text]

The parent_id should be the id of the menu one level above your submenu, the position should indicate where in the menu you would like to place your submenu, the id should be a unique identifier for your submenu, and the text should be the text that you want to display in the menu for the submenu.

Once you have created the submenu item, you can use its id as the parent_id of any menu items that you want to add to your submenu, including additional submenus.

For example:

```javascript
ADD_MB_=[["report", 2, "rp_sub1", "A Report Submenu"],
["rp_sub1", 1, "rp_cust2", "12 Period Summary"],
["rp_sub1", 2, "rp_sub2", "Another Submenu"],
["rp_sub2", 1, "rp_user", "User Narrative"],
["rp_sub2", 2, "rp_buser", "Banded User"],
["rp_sub1", 3, "rp_cust3", "12 Period Forward"]]
```

This entry would result in a menu that looks like Figure 2.1:

**Figure 2.1: Custom Report Submenu**

Notice that the parent_id of our submenu item is report. This indicates that we want to add the submenu to the "Reports" menu. The items with parent_id rp_sub1 are placed under our first submenu (including our second submenu), while items with the parent rp_sub2 are placed under the second submenu.

As a matter of consistency, we recommend that your submenus use IDs like the following:

- file_sub for the File menu
- opt_sub for the Options menu
- ch_sub for the Charts menu
- rp_sub for the Reports menu
- inp_sub for the Inputs menu
- dash_sub for the Dashboards menu
- vw_sub for the Views menu
- pf_sub for the Prefilters menu
- admin_sub for the Admin menu
- script_sub for the Scripts menu
- help_sub for the Help menu

Increment the number at the end of the ID for each submenu you add to the menu.

#### 2.5.1 Example

Suppose we wanted to add some submenus to the "Views" menu for users with UserCode C. To do this, we could use a ADD_MB entry like the following:

```javascript
ADD_MB_C=[["view", 2, "vw_sub1", "A View Submenu"],
["vw_sub1", 1, "view2:0", "Standard"],
["vw_sub1", 2, "vw_sub2", "Another Submenu"],
["vw_sub2", 1, "view4:0", "CPR"],
["vw_sub2", 2, "view5:0", "Current CPR"],
["vw_sub1", 3, "view22:1", "Task (G)"]]
```

This would result in a menu that looks like figure 2.2 for users with UserCode C.

**Figure 2.2: View Submenu**

Notice that the unique item IDs for views include either :0 or :1; these indicate either cost or Gantt views. This is explained in more detail in section 2.6. Also, notice that we used 2 for the position of our first submenu, but the submenu shows up as the second item in the list (recall that the position is 0-indexed). This is because of the hidden "User" view menu item. If the user had their own custom views, they would have an additional item above our submenu, see figure 2.3.

**Figure 2.3: View Submenu with User Menu**

Of course you can place the submenu at any position you like, but keep in mind that hidden items should be taken into account when choosing your "position" value.

### 2.6 Identifying IDs for Custom Items

When moving custom items, keep in mind that you must know the correct menu ID for the item. IDs for custom items cannot be found in menu.xml since they will be unique to your setup. Instead, you can find the ID by using the "Raw Data" window. These items include charts, reports, dashboards, views, filters, and scripts.

The IDs for custom items can be found by using this method:

1. open the 'Raw Data' window with "Options > Show Raw Data"
2. refresh Empower while logged in or click in the sort window until text begins to appear in the 'Raw Data' window
3. open the desired custom item in Empower
4. review the entry that appears in the 'Raw Data' window to find the numeric ID for the custom item. See the list below to determine where to look for the numeric ID of each type of item

Once you have the numeric ID, combine it with the standard text portion for the type of item that you are using to get the full ID for the custom item.

Using the "Raw Data" window, the full ID for each type of item can be found by using this reference for the appropriate item type:

**Reports**
The first part of the ID for custom reports will be rp_cust. The numeric part of the ID will be indicated by "rid="

Figure 2.4: Raw Data Entry for Custom Report

In this example, the full ID would be rp_cust1

**Charts**
The first part of the ID for custom charts will be ch_cust. The numeric part of the ID will be indicated by "cid="

Figure 2.5: Raw Data Entry for Custom Chart

In this example, the full ID would be ch_cust8

**Dashboards**
The first part of the ID for dashboards will be dash. The numeric part of the ID will be indicated by "id=" in the entry with "func=open_dash"

Figure 2.6: Raw Data Entry for Dashboard

In this example, the full ID would be dash2

**Sort Views**
The first part of the ID for views will be view. For sort window views, look for an entry with "vw=". This will give you part of the ID for the view. The entry should also have some information like the name of the view which can help you confirm that you are looking at the correct 'Raw Data' entry.

Figure 2.7: Raw Data Entry for View

The full ID for the view will be the number from 'Raw Data' plus :0 to indicate that this is a sort view. So for the view in figure 2.7, the second portion of the ID would be 4:0 and the full ID would be view4:0

**Gantt Views**
The first part of the ID for views will be view. For Gantt views, look for "vw=" to find the unique part of the View ID. You should also see something like "gantt":1 in the 'Raw Data' output.

Figure 2.8: Raw Data Entry for Gantt View

The full ID for a Gantt view will be the number from 'Raw Data' plus :1 to indicate that this is a Gantt view. So for the view in figure 2.8, the second portion of the ID would be 22:1 and the full ID would be view22:1

**Sort Window Filters**
The first part of the ID for filters will be filter. For filters, look for "fid=" to find the unique portion of the Filter ID.

Figure 2.9: Raw Data Entry for Sort Filter

Similar to views, the full ID for filters will include an indicator to show whether the filter is a sort filter or a Gantt filter. For sort filters, add :0 to the ID. For the filter in figure 2.9, the second portion of the ID would be 5:0 and the full ID would be filter5:0

**Gantt Filters**
The first part of the ID for filters will be filter. For Gantt filters, look for "fid=" to find the unique portion of the Filter ID.

Figure 2.10: Raw Data Entry for Gantt Filter

Similar to views, the full ID for filters will include an indicator to show whether the filter is a sort filter or a Gantt filter. For Gantt filters, add :1 to the ID. For the filter in figure 2.10, the second portion of the ID would be 13:1 and the full ID would be filter13:1

**Scripts**
The first part of the ID for scripts will be script. The numeric part of the ID will be indicated by "id="

Figure 2.11: Raw Data Entry for Script

In this example, the full ID would be script8

The "full" ID is the value that should be used in the empower.conf file for your customization. This value must be correct in order for the menu item to function properly.

### 2.7 WebEVM Download/Upload Configuration

WebEVM download/upload allows you to download WebEVM Etc data from WebEVM for the contract that is currently open in Empower. You can also make changes to your WebEVM data using the "upload" option. By default, the WebEVM Etc download/upload is not enabled. To enable, add a WEBEVM_HOST entry to your empower.conf file with your WebEVM URL, then add menu items for the download and upload options. For example, adding the following entry to empower.conf would add a new option called "WebEvm" to the menu bar with the options "Download ETC" and "Upload ETC" under it:

```javascript
ADD_MB_=[[null, 9, "cevm", "WebEvm"], ["cevm", 0, "cevm_etc_dn", "Download ETC"], ["cevm", 1, "cevm_etc_up", "Upload ETC"]]
```

**Figure 2.12: WebEvm Menu Option**

To make changes, you could use "Download ETC" to download your data from WebEVM, make any necessary changes in the download file, save, then upload the changed file with "Upload ETC."

---

## 3. Adding EMF Export to the Chart Download Menu

The Chart Download menu (found in the upper right-hand corner of the Chart window) by default allows the user to download the current chart to a file in PDF, PNG, or SVG format. Some users prefer to download charts in the EMF (Windows Enhanced Metafile) format for ease of inserting into PowerPoint slides.

Three steps are necessary to enable EMF chart downloads in Empower:

1. Include the line EXPORT_EMF=1 in your empower.conf configuration file. (Setting EXPORT_EMF=0 will, of course, disable the EMF download capability.)
2. Install Java on the Empower server machine.
3. Verify that you have the Java archive file svg2emf.jar in your empower directory.

When these steps have been followed correctly, "Download EMF metafile" will appear on the Chart download menu.

---

## 4. Admin User Configurations

### 4.1 Disabling User Maintenance Items for Admin Users

The AU_DISABLE option allows you to disable items in the "User Maintenance" dialog for specific Admin users. This entry should be in a format like the following (note that the line is wrapped in this example):

```
AU_DISABLE=L:addusr,addgrp,delusr,groups,os,au,remove;
M:addusr,addgrp,delusr
```

Notice the semicolon separated sections of the entry. Each section begins with a letter, followed by a colon, then a comma separated list. The letter indicates which Admin users the items should be disabled for, and the comma separated list indicates which items to disable. The letter should correspond to the "AdminUser" value for any users that you want this customization to apply to. The "AdminUser" field can be found in the "Users" table, available via "Download Data Download."

For example, with the above AU_DISABLE entry, users with "AdminUser=L" would see the following in the "User Maintenance" dialog when they are logged in as "Admin":

**Figure 4.1: UM dialog for "L" users**

Notice that the "+User", "+Group", and "Delete" buttons are disabled, as well as the "Remove" button and the "OS Authentication" and "Login as Admin" checkboxes.

With the same AU_DISABLE entry, users with "AdminUser = M" would see the following in the "User Maintenance" dialog when logged in as "Admin":

**Figure 4.2: UM dialog for "M" users**

For this user, only the "+User", "+Group", and "Delete" buttons are disabled.

Valid IDs for "User Maintenance" items that can be disabled can be found in the www/um.html file by looking at the IDs of the HTML elements in that file. A list of the IDs with the "User Maintenance" items they correspond to is provided here for your convenience.

- **adduser** - corresponds to the "+User" button
- **addgrp** - corresponds to the "+Group" button
- **deluser** - corresponds to the "Delete" button
- **toggle** - corresponds to the "Toggle Permissions" button
- **remove** - corresponds to the "Remove" button, used when removing users from groups.
- **pwd** - corresponds to the "Clear" button
- **pval** - corresponds to the Password textbox
- **set** - corresponds to the "Get" button
- **groups** - corresponds to the "Group" dropdown
- **code** - corresponds to the "User Code" textbox
- **pl** - corresponds to the "PubLevel" textbox
- **os** - corresponds to the "OS Authentication" checkbox
- **varroles** - corresponds to the "Narrative Role" dropdown
- **airoles** - corresponds to the "Action Item Role" dropdown
- **dsplnm** - corresponds to the "Display Name" textbox
- **email** - corresponds to the "Email" textbox
- **au** - corresponds to the "Login as Admin" checkbox
- **filters** - corresponds to the "Prefilter" dropdown
- **pftext** - corresponds to the "Prefilter" textbox

Note that to completely disable editing of "Prefilters", you'll probably want to disable both the Prefilter dropdown and the textbox beneath it.

### 4.2 Import Script Restrictions

The IMPORT_SCRIPTS configuration option can be used to control which users can import scripts into Empower via File > Import User Items. Note that this option does not limit who can run scripts, only those who can import them.

Valid entries are:

- **IMPORT_SCRIPTS=2** or if the entry is omitted; only users logged in as "Admin" can import scripts.
- **IMPORT_SCRIPTS=1**; only the "Admin" user can import scripts.
- **IMPORT_SCRIPTS=0**; scripts cannot be imported.

It should be mentioned that a user who can "log in as Admin" is different than the "Admin" user. The "Admin" user inputs "Admin" as their username in the Empower login screen. Other users may have the ability to "log in as Admin", but there is a distinction between those users and the "Admin" user.

For example, if IMPORT_SCRIPTS=2, a user who is not "logged in as Admin" will receive the following message when attempting to import a script:

**Figure 4.3: Importing Script not Logged in as Admin**

If IMPORT_SCRIPTS=1, any user who is not "Admin" will receive the following message when attempting to import a script:

**Figure 4.4: Importing Script as a non-Admin user**

---

## 5. Enforcing Complete Narratives on Submit

The VAR_ENFORCE entry can be used to regulate the submittal of VARs within incomplete sections. Note that by "incomplete" we mean that the section is blank, i.e. has no text entered.

Valid values for VAR_ENFORCE are 0, 1, and 2. When set to 0, no extra rules for VAR completeness will be enforced; the same behavior you would see when the entry is not present. When set to 1, users will receive a warning when submitting a VAR if their VAR has incomplete sections. The VAR will still be submitted, but the user will see something like the following:

**Figure 5.1: Warning for Blank VAR Sections**

If VAR_ENFORCE is set to 2, users will see an error message when they attempt to submit a VAR with incomplete sections, and the VAR will not be submitted.

**Figure 5.2: Error for Blank VAR Sections**

Users can always "Save" their VARs, regardless of the VAR_ENFORCE setting.

The USER_NARR_ENFORCE entry can be used in the same way to regulate the submittal of User Narratives with incomplete sections. This option behaves the same way as VAR_ENFORCE, just applied to the User Narrative instead of the VAR Narrative.

---

## 6. Customizing the VAR Insert Dropdown

By default, the Insert dropdown in the VAR Narrative Editor lists some common useful fields that can be easily inserted into your VAR Narrative. However, this list can be customized at the server level. This allows you to rearrange, add to, or remove items from the list based on what is most useful for your site.

To customize the list, edit or create the ins-cust.js file in the empower/www directory on your Empower server. You can find a blank template for this file in the empower/setup directory. Note that the contents of this file must be an array of arrays called ins. The default list for ins looks like:

```javascript
var ins = [
['WBS', 'WbsNum'],
['SV CUR PP', 'Meta|SvCurPP'],
['CV CUR PP', 'Meta|CvCurPP'],
['SV CUM PP', 'Meta|SvCumPP'],
['CV CUM PP', 'Meta|CvCumPP'],
['VAC PP', 'Meta|VacPP'],
['SV CUR', 'SvCur'],
['CV CUR', 'CvCur'],
['SV CUM', 'SvCum'],
['CV CUM', 'CvCum'],
['VAC', 'Vac'],
['SV CUR %', 'SvpCur'],
['CV CUR %', 'CvpCur'],
['SV CUM %', 'SvpCum'],
['CV CUM %', 'CvpCum'],
['VAC %', 'Vacp'],
['SPI CUM', 'SpiCum'],
['CPI CUM', 'CpiCum'],
['TCPI EAC', 'TcpiEac'],
['BAC', 'Bac'],
['EAC', 'Lre'],
['TOTAL FLOAT', 'TotalFloat'],
['RATE VAR', 'RateVar'],
['EFF VAR', 'EffVar']
];
```

The first item in each inner array will be the text that is displayed in the dropdown, while the second item is the field that should be inserted. For the fields, use the same field names that you would when using our placeholder syntax. (See our documentation on Custom Charts and Reports for more details on placeholder syntax.) You can also specify a specific table to pull the field from if necessary. This can be useful if different tables have fields with the same name. When specifying a table, use a | to separate the field and table names. For example, if we wanted to specify the ProjOff field from the Element table, we could add this entry to the list:

```javascript
['CAM', 'Element|ProjOff']
```
