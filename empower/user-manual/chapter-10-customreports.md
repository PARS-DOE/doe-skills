# Chapter 10: Custom Reports

*From the Empower User Manual*

---

## Overview

Custom Reports are reports custom coded for each customer's needs, often accessing a variety of data sources (beyond the standard Empower database).

Custom reports can be categorized in two different ways, resulting in four possibilities. First, custom reports can be internal or external. Internal reports are (normally; see below for a qualification) displayed in Empower's usual report pane, just like standard reports. External reports are displayed in a separate browser window. Typically, a custom report would be implemented as an external report if its design was significantly different than the standard reports, perhaps because it used stylesheets that conflicted with the standard set of styles or if the report required more screen real estate than usually available in the report pane.

Custom reports can also be categorized as displaying only data that is available in Empower (known as "template reports") or as displaying data from arbitrary sources (known as "Adaptive Touch Reports"). An example of the latter type might get some of its data from Empower's database, and access other data from a source or sources somewhere else on the network or Internet.

These categories can be visualized schematically as follows:

| | Template | Adaptive Touch |
|---|---|---|
| Internal | Internal Template | Internal Adaptive Touch |
| External | External Template | External Adaptive Touch |

Now for the qualification: though reports developed as internal reports are usually shown in Empower's report pane, all such reports can be displayed externally by holding down the appropriate modifier key (Control, Shift, or Alt/Option). See Section 9.1 for more detail.

In general, users don't need to know about the different categories of custom reports. All such reports appear together on the Custom Reports submenu without distinguishing among the various categories, and they work pretty much like the standard reports. There are just two points the average user needs to keep in mind:

1. External custom reports will open in a separate window, so if you don't see the report in the report pane, look for it in a different browser window.
2. It is possible to have reports display data from sources other than Empower's database, so if you find yourself wishing you could have such a report, know that it can be done with Empower.

The writing of custom reports is beyond the scope of this User's Manual; you can download the Empower Technical Note "Writing Empower Custom Reports" from our support website (http://encoreanalyticsllc.freshdesk.com/support/solutions).

Figure 10.1 shows the Custom Reports menu.

**Figure 10.1: Custom Reports Menu**

As with a number of other items in Empower (e.g., Views, Prefilters, Custom Charts), there can be global custom reports and user custom reports. Global custom reports are those uploaded by the administrator and available to all users, while user custom reports are uploaded by a non-admin user and only available to that user. In this figure, several global custom reports are available (12 Period Summary, and so on). Furthermore, custom reports uploaded by a user are stored under that user's id, even when the user is a member of a group (see 5.2).

## 10.1 Open/Edit

This command brings up the Open/Edit Report Dialog, which is shown in Figure 10.2.

**Figure 10.2: Open/Edit Custom Report Dialog**

In this case, we are running Empower as a non-administrative user, and we have imported several User reports. Following the same convention used in the list of views, User reports are listed with a leading plus sign (+) to show that they are not Global reports. Brackets around a report name indicate that that report is not listed in either the Global or User submenus. As with views, Custom Reports that are not listed in the submenu can always be opened from this dialog.

This dialog lists both custom and standard reports, and allows you to filter the reports shown via the checkboxes on the side of the dialog. The dropdown at the top of the dialog allows you to change which type of user item you want listed. (e.g. Charts, Reports, Prefilters) Standard reports cannot be edited, but can be opened through this dialog.

To view a report, select a report in the list and click the Open button. Internal reports will appear in Empower's report pane. External reports will be displayed in a separate browser window, as illustrated in the next figure. (As it draws data from outside Empower, it is an example of an Adaptive Touch-external report.)

**Figure 10.3: A Custom Report Displayed Externally**

Note also that some custom reports display information about an entire project, while others are specific to an element of a project. For the latter type of report, changing the selected element in the Sort Window will automatically update the custom report in its tab or window.

Figure 10.4 shows a Work Authorization Document (WAD) reconciliation report as an example of a custom report that draws from an external data source and which is displayed in Empower's report pane. That is, it is an example of an Adaptive Touch-internal report. This report was generated by Empower, using data in Empower's native database, along with simulated data from a separate source (in this example, located on the encore-analytics.com website, but in real scenarios drawn from the customer's own sources).

**Figure 10.4: Sample Custom Report: WAD Reconciliation**

To edit a report, click the Edit button on the Open/Edit Custom Report Dialog. (When a Global report is selected, the Edit button is disabled; non-administrator users can only open custom reports, not edit them.) Pressing the Edit button brings up the dialog shown in Figure 10.5 below.

**Figure 10.5: Edit Custom Report Dialog**

There are two things a user can do while editing a custom report: change the report's name, using the text box next to the "Name:" label, and choose whether or not to have the report show in the menu. (Recall that, as with Views and Prefilters, the menu will only display a maximum of twenty reports, due to limitations on screen real estate, but all reports will always be available through the Open/Edit dialog.)

## 10.2 Delete/Reorder

This command allows the user to either delete a report from the list of available reports, or to change the order in which reports show in the Global or Users submenu. Selecting this command brings up the dialog shown in Figure 10.6 below.

**Figure 10.6: Delete/Reorder Custom Report Dialog**

To delete a report, select it in the listbox, then click the Delete button. Admin users can only delete Global reports. Non-admin users can only delete their own User reports. In each case, this dialog will only show the reports that can be deleted.

To change the order in which a report is displayed on the submenus, select the report, then press the up or down arrow buttons. When you are satisfied with the order of the reports, click the Reorder button. Leaving the dialog without clicking the Reorder button will leave the order as it was before. As with the Delete function, admin users will only be able to reorder Global reports and non-admin users will only be able to reorder their own User reports.
