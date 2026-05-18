# Chapter 21: Action Item Tracking

*From the Empower User Manual*

---

## Chapter 21: Action Item Tracking

Empower offers integrated action item tracking. Action items can be created, updated and viewed directly in Empower's action item editor, which reflects the user's role and current action status via a customizable workflow. Action item templates allow seamless integration with VAR narratives, with action items automatically appearing in the appropriate VAR narratives. Action item views provide powerful sorting/filtering of current status and can display changes over time. The Action Item Report tracks the sort/filter state of the action view to make it simple to generate customized reports. Email notifications can be generated manually or automatically using a role-based email template.

## 21.1 The Default Empower Action Item Workflow

An action item workflow consists of a set of roles, a set of states an action item can be in, a set of actions that users can perform on an action item, and a set of rules that specify what actions a given role can perform on an action item in a given state, and what new state that action item will be in as a result. This section describes the default Empower action item workflow.

In this workflow, there are three roles: Submitter, Reviewer, and Approver. Action items can be in one of the following states: Unopened, Opened, Submitted, Reviewed, Approved, Rejected, Closed, and Dismissed. These actions can be performed on an action item: Open, Submit, Review, Reject, Approve, Close, and Dismiss. As we will see below, users can only perform actions allowed by their role; for instance, a submitter cannot approve an action item. The rules can be most conveniently shown in tabular form:

| Row | Role | State | Action | NextState |
|-----|------|-------|--------|-----------|
| 1 | Submitter | Unopened | Open | Opened |
| 2 | Submitter | Unopened | Submit | Submitted |
| 3 | Submitter | Opened | Open | Opened |
| 4 | Submitter | Opened | Submit | Submitted |
| 5 | Submitter | Submitted | Open | Opened |
| 6 | Submitter | Submitted | Submit | Submitted |
| 7 | Submitter | Rejected | Open | Opened |
| 8 | Submitter | Rejected | Submit | Submitted |
| 9 | Reviewer | Unopened | Open | Opened |
| 10 | Reviewer | Unopened | Submit | Submitted |
| 11 | Reviewer | Unopened | Review | Reviewed |
| 12 | Reviewer | Unopened | Reject | Rejected |
| 13 | Reviewer | Opened | Open | Opened |
| 14 | Reviewer | Opened | Submit | Submitted |
| 15 | Reviewer | Opened | Review | Reviewed |
| 16 | Reviewer | Opened | Reject | Rejected |
| 17 | Reviewer | Submitted | Open | Opened |
| 18 | Reviewer | Submitted | Submit | Submitted |
| 19 | Reviewer | Submitted | Review | Reviewed |
| 20 | Reviewer | Submitted | Reject | Rejected |
| 21 | Reviewer | Reviewed | Open | Opened |
| 22 | Reviewer | Reviewed | Submit | Submitted |
| 23 | Reviewer | Reviewed | Review | Reviewed |
| 24 | Reviewer | Reviewed | Reject | Rejected |
| 25 | Reviewer | Rejected | Open | Opened |
| 26 | Reviewer | Rejected | Submit | Submitted |
| 27 | Reviewer | Rejected | Review | Reviewed |
| 28 | Reviewer | Rejected | Reject | Rejected |
| 29 | Approver | Unopened | Open | Opened |
| 30 | Approver | Unopened | Submit | Submitted |
| 31 | Approver | Unopened | Review | Reviewed |
| 32 | Approver | Unopened | Reject | Rejected |
| 33 | Approver | Unopened | Approve | Approved |
| 34 | Approver | Unopened | Dismiss | Dismissed |
| 35 | Approver | Unopened | Close | Closed |
| 36 | Approver | Opened | Open | Opened |
| 37 | Approver | Opened | Submit | Submitted |
| 38 | Approver | Opened | Review | Reviewed |
| 39 | Approver | Opened | Reject | Rejected |
| 40 | Approver | Opened | Approve | Approved |
| 41 | Approver | Opened | Dismiss | Dismissed |
| 42 | Approver | Opened | Close | Closed |
| 43 | Approver | Submitted | Open | Opened |
| 44 | Approver | Submitted | Submit | Submitted |
| 45 | Approver | Submitted | Review | Reviewed |
| 46 | Approver | Submitted | Reject | Rejected |
| 47 | Approver | Submitted | Approve | Approved |
| 48 | Approver | Submitted | Dismiss | Dismissed |
| 49 | Approver | Submitted | Close | Closed |
| 50 | Approver | Reviewed | Open | Opened |
| 51 | Approver | Reviewed | Submit | Submitted |
| 52 | Approver | Reviewed | Review | Reviewed |
| 53 | Approver | Reviewed | Reject | Rejected |
| 54 | Approver | Reviewed | Approve | Approved |
| 55 | Approver | Reviewed | Dismiss | Dismissed |
| 56 | Approver | Reviewed | Close | Closed |
| 57 | Approver | Rejected | Open | Opened |
| 58 | Approver | Rejected | Submit | Submitted |
| 59 | Approver | Rejected | Review | Reviewed |
| 60 | Approver | Rejected | Reject | Rejected |
| 61 | Approver | Rejected | Approve | Approved |
| 62 | Approver | Rejected | Dismiss | Dismissed |
| 63 | Approver | Rejected | Close | Closed |
| 64 | Approver | Approved | Open | Opened |
| 65 | Approver | Approved | Submit | Submitted |
| 66 | Approver | Approved | Review | Reviewed |
| 67 | Approver | Approved | Reject | Rejected |
| 68 | Approver | Approved | Approve | Approved |
| 69 | Approver | Approved | Dismiss | Dismissed |
| 70 | Approver | Approved | Close | Closed |
| 71 | Approver | Dismissed | Open | Opened |
| 72 | Approver | Dismissed | Submit | Submitted |
| 73 | Approver | Dismissed | Review | Reviewed |
| 74 | Approver | Dismissed | Reject | Rejected |
| 75 | Approver | Dismissed | Approve | Approved |
| 76 | Approver | Dismissed | Dismiss | Dismissed |
| 77 | Approver | Dismissed | Close | Closed |
| 78 | Approver | Closed | Open | Opened |
| 79 | Approver | Closed | Submit | Submitted |
| 80 | Approver | Closed | Review | Reviewed |
| 81 | Approver | Closed | Reject | Rejected |
| 82 | Approver | Closed | Approve | Approved |
| 83 | Approver | Closed | Dismiss | Dismissed |
| 84 | Approver | Closed | Close | Closed |

A typical action item might move through this workflow as follows: A submitter creates and opens an action item (row 1). The submitter submits the action item (row 2). The reviewer rejects the action item (row 20). The submitter edits the action item, saves, and submits it again (row 8). The reviewer reviews the action item (row 19). Finally, the approver approves it (row 54).

You may have noticed the "Dismiss" action in the table above. It may happen that you create an action item, then later decide that no such action is really necessary. Empower keeps complete history of each action item, never deleting any revision of any action. Thus to indicate that an action item is no longer "in play", it can be dismissed. Dismissed action items will be shown in views that display action item history, but not in views or reports that show only the current version of an action item.

As mentioned, this is the action item workflow Empower provides as installed. The workflow can be customized to fit the action item workflow requirements of your organization. Doing so is a topic beyond the scope of this user's manual; please contact Empower Technical Support if you wish to implement a custom workflow.

The action item approval workflow is as follows. The first three steps are start-up steps typically performed once for each contract.

1. Define user roles. In this step you identify which users will be submitting action items, which will be reviewing them, and which will be approving them, who the submitters, reviewers, and approvers will be for each element of each contract, and entering the emails of these users (for use by the email notification system).

2. Configure the action item email system. This is an administrative task; it is described in the technical note "Automating Narrative Workflow Emails with Empower," available on our support website, http://encoreanalyticsllc.freshdesk.com/support/solutions.

3. Write action item email templates (or obtain samples from us, which you can use as is or customize).

(Naturally, you may need to redo some of the above steps from time to time due to changes in contractual threshold requirements or personnel.)

The steps listed below constitute the action item workflow process proper and are repeated for each period of the contract:

1. Import a new period of data and recalculate. See Sections 16.1 and 16.2.

2. Write, edit, and approve action items.

3. View the action item status using action item views and various prefilters. See Section 21.4.

4. Notify submitters, reviewers, and approvers via manual or automated emails of tasks they need to perform with respect to action items.

5. Generate action item reports. See Section 21.4.

Some of the steps above are not unique to the action item workflow process and have already been described elsewhere in this User's Manual. The other steps will be described in more detail in the following sections.

## 21.2 Defining User Roles

We begin by setting the action item role and email address for each user who will be involved in the action item workflow. Figure 20.1 shows us doing this with the User Maintenance dialog for user Bond. Note that you can set different narrative roles and action item roles for a user. A user can have different roles for narratives and action items, being, for instance, a Submitter for narratives and a Reviewer for action items. (The narrative workflow was discussed in Chapter 20.)

**Figure 21.1: Setting a User's Action Item Role and Email Address**

## 21.3 Creating, Modifying, and Approving Action Items

**Figure 21.2: Creating a New Action Item**

When you open a new action item, `<New Action>` will appear in the Action listbox. When you enter a title (in the Title textbox) and save, the title will be copied up to the Action box. The Action dropdown can also be used to create a new action item for a WBS element that already has an action item. (You might want to do this if, for example, an element has both a cumulative cost variance and a cumulative schedule variance — S and C in the Format 5 VAR column in the Sort Window — and you need to create separate action items for each variance.) Say an element already has an action item associated with it. You click Inputs > Add / Edit Actions, and you see the existing action. To create a new one, click on the Action dropdown and select `<New Action>`. The Title box will be cleared and you can begin editing the new action.

When you select a WBS (or OBS, etc.) element in the Sort Window, then open an action item, the WBS textbox on the Add/Edit Actions dialog will automatically be filled in. You can edit this textbox if you want to move an action item to a different WBS element. Say you have started an action for WBS 2100 and saved it. Later you realize that this action really should apply to WBS 6200. You would open the action item (by selecting 2100 in the Sort Window and opening the Add / Edit Actions dialog), then you would edit the WBS field to say 6200, perhaps edit the description, add a note, etc., then save the action. It will now be associated with 6200. The choices in the Type dropdown list are VAR Corrective Action, CAR Corrective Action, Other Action, or TBD.

In the Category dropdown list, you can choose variances for current cost, current schedule, cumulative cost, cumulative schedule, or VAC (the csCSV codes familiar to you from the Format 5 VAR column of the Sort Window), or N/A.

Priority, OpenDate, and DueDate, are straightforward. PctCmp refers to how much of the action item has been completed.

A submitter can assign any submitter to this action item; the Reviewer and Approver list boxes will be grayed out. A reviewer can assign the submitter and/or reviewers, but the Approver listbox will be grayed out. An approver can assign any of the three roles.

Next we see a full-featured edit control in which you can write a description for the action.

At the bottom of the dialog, the user chooses which action to invoke (with the Update list box). The options available will vary depending upon the state of the action item and the role of the current user. When the "Apply" button is clicked, the action will be performed.

## 21.4 Viewing Action Item Reports and Status

After you have created a few actions, you will want to generate reports of your action items and a view of their status. We begin by applying the Action Status view. A typical result is shown in Figure 21.3 below.

**Figure 21.3: Action Status View, Showing All Revisions**

Most of what you will see in the view is what you would expect from having edited the actions in the action item dialog. A few items call for comment, however.

The most significant fact is that you can have multiple rows with the same WBS number. (See the boxed WBS numbers in the figure.) This happens in no other Sort Window view in Empower. There are two ways you can get multiple rows for a given WBS number. One way is when you are displaying multiple versions of a given action item. Empower keeps a history of the successive versions of an action item. Note in the figure there are three rows for WBS 3600. Looking at the Rev (for "Revision") column of the view, we see that they are revisions 0, 1, and 2. Revision 0 is always the most recent revision, and the highest number revision is the earliest. Each action item is assigned a unique number — the random-looking hexadecimal string in the Num column of the view. In the figure we see the number for 3600's action item is d3d602, and all the revisions for that action item have the same number.

Another way you might see multiple rows in the Action Status view for a given WBS element is that you actually have more than one distinct action item for that element, as mentioned earlier. You might have created an action for a cumulative cost variance and another for a cumulative schedule variance, both for the same WBS element. These action items will have different numbers, which will see in the Num column.

If we opened the Action Item report (command Reports > Action Items), we would see something like Figure 21.4 below.

**Figure 21.4: Action Items Report (All Action Items)**

In this figure we have shown the title, the first action item in the report (for WBS 1000), then snipped out part of the report so we can see the actions for 3600. Note that for WBS 3600, all three versions of the action item are listed, in the same order as in the view (i.e., oldest to newest). You can see how the percent complete moves from 0, to 10, and then 70 in the three versions. The note (the text after the state) also has been edited: rev 2 has "Initial creation", rev 1 has "Reviewed baseline plan", and the latest revision has "Reviewed actuals, developed ETC".

This figure also shows color coding for the due date field. If the action item is overdue, the due date will be shown against a red background. If the due date is within some threshold number of days of the current date, the background will be colored yellow as a warning. (The warning period defaults to 10 days; it can be customized with the key ACTION_WARN in the empower.conf configuration file. See our technical note, "The Empower Configuration File," available on our support website http://encoreanalyticsllc.freshdesk.com/support/solutions.)

Let's say we only want to see the most recent action item status for each action in the view. We can filter the view by putting a zero in the Rev column. Figure 21.5 shows the result: we only see the most recent version of each action item.

**Figure 21.5: Action Status View with Filter Applied**

The filter applied in the Sort Window will be reflected in the Action Item Report as well. Figure 21.6 shows the Action Item Report including only the most recent revisions. (Note that the title of the report shows that a filter on the Rev column has been applied.)

**Figure 21.6: Action Items Report (Only Latest Revisions)**

We can also look at the history of a single action item by filtering on the Num field. Recall that there can be multiple action items associated with a single WBS (or OBS, etc.) element, and that each action item has a unique number. We can filter the action item's unique number in the Num column of the Action Status view to see just that action item in the view, then look at the detailed history of the item in the Action Items Report.

Figure 21.7 shows that element 3200 has two action items, one with the number d0fd09 (for the cumulative schedule corrective action) and the other numbered 4edf4f (the vaguely titled "Another Action Item").

**Figure 21.7: Action Status View, Showing Multiple Action Items for 3200**

Suppose we want to see the history of the cumulative schedule corrective action. We filter the view by putting d0fd09 in the Num column, and we see Figure 21.8.

**Figure 21.8: Action Status View, Filtered to One Item for 3200**

Once we've done that, the Action Items report will look like Figure 21.10:

**Figure 21.9: Action Items Report, Showing History for One Item**

Note that we see the two revisions for action item d0fd09, and that the text "(PF: Num)' in the report title reminds us that this report was filtered by action item number.

So far we have been looking at opening the Action Items Report while using the Action Status view. If we have any other view applied in the Sort Window, select a WBS element, and open the Action Items Report (or select an element while the Action Item Report is already open), the report will display the actions items (if any) for just that element, and only the latest revision for each action item.

**Figure 21.10: Action Items Report Opened from Normal Sort View**

## 21.5 Action Items in VAR Narratives

The default VAR narrative templates will insert any action items applicable to the narrative's WBS element at the end of the narrative. Figure 21.11 shows the VAR Narrative Report with the action item information filled in.

**Figure 21.11: VAR Narrative Report, Showing Action Item**

## 21.6 Writing Action Item Email Templates

When you send emails to submitters and approvers of actions they need to take (see Section 20.8), you will be asked to specify a template that will be used to generate the email text.

Action item email templates are just another type of Empower template. General instructions for writing Empower templates can be found in Appendix C. Here we note special considerations for email templates.

To identify a template as an email template (meaning it will be displayed in the Template listbox on the Send Email Notification dialog), you must put the line:

```
Default : EMAIL
```

in the template header. The template name is what will be displayed in the Template listbox.

Several placeholders are available for use in email templates. The placeholders `(|Note|)`, `(|AiStatus|)`, `(|ItemTitle|)`, `(|ItemDesc|)`, `(|State|)`, and `(|DueDate|)` will be familiar from the Add/Edit Action Item dialog.

`(|User|)` expands to the current user. `(|Role|)` expands to Submitter, Reviewer, or Approver, depending on which was picked in the Recipient listbox. `(|DaysDue|)` is calculated from the action's due date and the current date.

Sample templates are available upon request. We describe most of these placeholders using the sample template shown below.

Templates can include HTML formatting or be in plain text (which you might prefer if your recipients have an email system that does not handle HTML formatting in emails).

The lines:

```
(|Meta|BeginLoop|ai|SyncActionWnd|)
```

and

```
(|Meta|EndLoop|ai|)
```

are special codes that loop through all the action items in an action view. (You can learn more about looping constructs from the technical note, "Writing Empower Custom Reports," available on our support website (http://encoreanalyticsllc.freshdesk.com/support/solutions).

### Sample Email Template

```html
<!-- input template -->
Name : Action Email
Description : Action Notification Email Template
Default : EMAIL
<!-- input template -->

<!DOCTYPE html>
<html>
<style>
body.tmpl { font-family:sans-serif; font-size:8; }
table.tmpl { width:100%; border:1px solid silver; border-collapse:collapse; }
td.tmpl { border:1px solid silver; border-collapse: collapse; padding:4px; }
.tb { font-weight:bold; }
</style>
<body class="tmpl">
Dear (|Meta|Recipient|),
<p>
For Period ending (|EndDate|), the following actions require attention. (|Meta|Note|)
<p>
Regards,
<p>
(|Meta|User|)
<table class="tmpl">
<tr>
<td class="tmpl tb">WBS</td>
<td class="tmpl tb">Title</td>
<td class="tmpl tb">% Cmp</td>
<td class="tmpl tb">State</td>
<td class="tmpl tb">Due Date</td>
<td class="tmpl tb">Past Due</td>
</tr>
<!-- (|Meta|BeginLoop|ai|SyncActionWnd|) -->
<tr>
<td class="tmpl">(|AiStatus|WbsNum|:ai:|)</td>
<td class="tmpl">(|ItemTitle|:ai:|)</td>
<td class="tmpl">(|AiStatus|PctCmp|:ai:|[n1]|)</td>
<td class="tmpl">(|State|:ai:|)</td>
<td class="tmpl">(|DueDate|:ai:|)</td>
<td class="tmpl">(|DaysDue|:ai:|)</td>
</tr>
<tr>
<td class="tmpl">Reject Reason</td>
<td class="tmpl" colspan=5>(|ItemNote|:ai:|)</td>
</tr>
<tr>
<td class="tmpl" colspan=6>(|ItemDesc|:ai:|)</td>
</tr>
<!-- (|Meta|EndLoop|ai|) -->
</table>
</body>
</html>
```

## 21.7 Notify Submitters, Reviewers, and Approvers of Required Actions

The Admin > Send Email Notifications allows the user to send emails to submitters, reviewers, or approvers who have required actions to perform regarding action items.

Sending email notifications can be done manually or as part of an automated process. Here, we will describe the manual process. Setting up the automated process is an administrative task; it is described in the technical note "Automating Narrative Workflow Emails with Empower," available on our support website, http://encoreanalyticsllc.freshdesk.com/support/solutions.

The first step is to filter the Sort Window to show just elements for which you wish to send email notifications, using interactive filtering and/or a prefilter.

When sending action item emails, we expect you will have opened an action item view and filtered it appropriately for the intended recipients (e.g., for Reviewers, you would filter Rev=0, since Reviewers should only be reviewing the most recent version of an action item, and status="Submitted", since such action items are the only ones that require a Reviewer's attention). Nothing terrible happens if you use a regular view with actions or an action view with narratives, but you might have extra or omitted emails depending on the circumstances, so we don't recommend it.

Figure 21.12 shows the Send Email Notifications dialog. Under Recipient, the user chooses to send the emails to Submitters, Reviewers, or Approvers. Under Template, the user chooses which template to use. (Writing such templates was covered in the previous section.)

**Figure 21.12: Sending Email Notifications to Submitters**

In addition to the text provided as part of the template, the user can enter an optional note that will be added to each generated email. The note can be formatted, as you can see from the formatting toolbar on the dialog. In the figure, we have added the text "A friendly reminder!" To get your note text to appear as a new paragraph after the text in the email template, you need to enter a blank line in the Note editor, as we have done in the figure.

If you want to do a "dry run" to see what emails will be generated, without actually sending them, check the "Generate emails only (do not send)" checkbox (as we have done in the figure).

When you are ready to send (or to do a dry run), click Submit. The generated emails will be shown in the Status window of the dialog, as you see in Figures 21.12 and 21.13.

**Figure 21.13: Generated Emails, Excerpt 1**

In Figure 21.14 we've scrolled the listing so you can see the tabular formatting of the action item in the email.

**Figure 21.14: Generated Emails, Excerpt 2**
