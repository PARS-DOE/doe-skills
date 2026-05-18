# Chapter 20: Narrative Approval Workflow

*From the Empower User Manual*

---

## 20 - Narrative Approval Workflow

The Empower narrative input editor includes workflow support, allowing the user to perform in-place submission, review, and approval or rejection of narratives. Sort Window views and prefilters make it easy to identify elements that require narrative submissions and the status of those submissions. The workflow engine is fully integrated with an email notification system that can be launched manually as required, or be configured to run automatically to match your organization's business rhythm.

Empower supports the collection and processing of internal narrative analyses (User Narrative), as well as those required for the formal Format 5 submission of the IPMR (VAR Narratives).

---

## 20.1 The Default Empower Narrative Workflow

A narrative workflow consists of a set of roles, a set of states a narrative can be in, a set of actions that users can perform on a narrative, and a set of rules that specify what actions a given role can perform on a narrative in a given state, and what new state that narrative will be in as a result. This section describes the default Empower narrative workflow. In this workflow, there are three roles: Submitter, Reviewer, and Approver. Narratives can be in one of six states: Unopened, Saved, Submitted, Reviewed, Approved, and Rejected. There are six actions that can be performed on a narrative: Save, Submit, Review, Reject, Approve, and CopyForward. As we will see below, users can only perform actions allowed by their role; for instance, a submitter cannot approve a narrative. The rules can be most conveniently shown in tabular form:

### Workflow Rules Table

| Row | Role     | State     | Action    | NextState |
|-----|----------|-----------|-----------|-----------|
| 1   | Submitter| Unopened  | CopyForward | Saved   |
| 2   | Submitter| Unopened  | Save      | Saved     |
| 3   | Submitter| Unopened  | Submit    | Submitted |
| 4   | Submitter| Saved     | CopyForward | Saved   |
| 5   | Submitter| Saved     | Save      | Saved     |
| 6   | Submitter| Saved     | Submit    | Submitted |
| 7   | Submitter| Submitted | Save      | Saved     |
| 8   | Submitter| Submitted | Submit    | Submitted |
| 9   | Submitter| Rejected  | Save      | Saved     |
| 10  | Submitter| Rejected  | Submit    | Submitted |
| 11  | Reviewer | Unopened  | CopyForward | Saved   |
| 12  | Reviewer | Unopened  | Save      | Saved     |
| 13  | Reviewer | Unopened  | Submit    | Submitted |
| 14  | Reviewer | Unopened  | Review    | Reviewed  |
| 15  | Reviewer | Unopened  | Reject    | Rejected  |
| 16  | Reviewer | Saved     | CopyForward | Saved   |
| 17  | Reviewer | Saved     | Save      | Saved     |
| 18  | Reviewer | Saved     | Submit    | Submitted |
| 19  | Reviewer | Saved     | Review    | Reviewed  |
| 20  | Reviewer | Saved     | Reject    | Rejected  |
| 21  | Reviewer | Submitted | Save      | Saved     |
| 22  | Reviewer | Submitted | Submit    | Submitted |
| 23  | Reviewer | Submitted | Review    | Reviewed  |
| 24  | Reviewer | Submitted | Reject    | Rejected  |
| 25  | Reviewer | Reviewed  | Save      | Saved     |
| 26  | Reviewer | Reviewed  | Submit    | Submitted |
| 27  | Reviewer | Reviewed  | Review    | Reviewed  |
| 28  | Reviewer | Reviewed  | Reject    | Rejected  |
| 29  | Reviewer | Rejected  | Save      | Saved     |
| 30  | Reviewer | Rejected  | Submit    | Submitted |
| 31  | Reviewer | Rejected  | Review    | Reviewed  |
| 32  | Reviewer | Rejected  | Reject    | Rejected  |
| 33  | Approver | Unopened  | CopyForward | Saved   |
| 34  | Approver | Unopened  | Save      | Saved     |
| 35  | Approver | Unopened  | Submit    | Submitted |
| 36  | Approver | Unopened  | Review    | Reviewed  |
| 37  | Approver | Unopened  | Reject    | Rejected  |
| 38  | Approver | Unopened  | Approve   | Approved  |
| 39  | Approver | Saved     | CopyForward | Saved   |
| 40  | Approver | Saved     | Save      | Saved     |
| 41  | Approver | Saved     | Submit    | Submitted |
| 42  | Approver | Saved     | Review    | Reviewed  |
| 43  | Approver | Saved     | Reject    | Rejected  |
| 44  | Approver | Saved     | Approve   | Approved  |
| 45  | Approver | Submitted | Save      | Saved     |
| 46  | Approver | Submitted | Submit    | Submitted |
| 47  | Approver | Submitted | Review    | Reviewed  |
| 48  | Approver | Submitted | Reject    | Rejected  |
| 49  | Approver | Submitted | Approve   | Approved  |
| 50  | Approver | Reviewed  | Save      | Saved     |
| 51  | Approver | Reviewed  | Submit    | Submitted |
| 52  | Approver | Reviewed  | Review    | Reviewed  |
| 53  | Approver | Reviewed  | Reject    | Rejected  |
| 54  | Approver | Reviewed  | Approve   | Approved  |
| 55  | Approver | Rejected  | Save      | Saved     |
| 56  | Approver | Rejected  | Submit    | Submitted |
| 57  | Approver | Rejected  | Review    | Reviewed  |
| 58  | Approver | Rejected  | Reject    | Rejected  |
| 59  | Approver | Rejected  | Approve   | Approved  |
| 60  | Approver | Approved  | Save      | Saved     |
| 61  | Approver | Approved  | Submit    | Submitted |
| 62  | Approver | Approved  | Review    | Reviewed  |
| 63  | Approver | Approved  | Reject    | Rejected  |
| 64  | Approver | Approved  | Approve   | Approved  |

### Example Workflow Scenario

A typical VAR narrative might move through this workflow as follows: A submitter copies forward the narrative for a given element from the previous period to the current period (row 1). The submitter edits the narrative and saves it (row 5). The submitter submits the narrative without any more editing (row 6). The reviewer rejects the narrative (row 24). The submitter revises the narrative, saves it, and submits it again (rows 9 and 10). The reviewer reviews it (row 23). Finally, the approver gives it the final approval (row 54), and the narrative is finished.

As mentioned, this is the narrative workflow Empower provides as installed. The workflow can be customized to fit the narrative workflow requirements of your organization. Doing so is a topic beyond the scope of this user's manual; please contact Empower Technical Support if you wish to implement a custom workflow. The narrative approval workflow is as follows. The first four steps are start-up steps typically performed once for each contract.

---

## Narrative Approval Workflow Steps

### Start-up Steps (performed once per contract)

1. **Define VAR thresholds.** In this activity you enter the contractually specified thresholds in Empower; this step is described in Section 16.9.12.

2. **Define user roles.** In this step you identify which users will be submitting narratives and which will be reviewing and approving them, who the submitters, reviewers, and approvers will be for each element of each contract, and entering the emails of these users (for use by the email notification system).

3. **Configure the narrative email system.** This is an administrative task; it is described in the technical note "Automating Narrative Workflow Emails with Empower," available on our support website, http://encoreanalyticsllc.freshdesk.com/support/solutions.

4. **Write narrative email templates** (or obtain samples from us, which you can use as is or customize).

(Naturally, you may need to redo some of the above steps from time to time due to changes in contractual threshold requirements or personnel.)

### Workflow Process Steps (repeated for each contract period)

The steps listed below constitute the narrative workflow process proper and are repeated for each period of the contract:

1. Import a new period of data and recalculate. See Sections 16.1 and 16.2.

2. Set manual VARs, if desired. See Section 20.5.

3. Write, review, and approve narratives.

4. View the VAR narrative status using narrative views and prefilters.

5. Notify submitters, reviewers, and approvers of actions they need to take with manual or automated emails.

6. Generate narrative reports and export narratives. See Sections 9.23 and 9.24.

Some of the steps above are not unique to the narrative workflow process and have already been described elsewhere in this User's Manual. The other steps will be described in more detail in the following sections.

---

## 20.2 Define User Roles

We begin by setting the narrative role and email address for each user who will be involved in the narrative workflow. Figure 20.1 shows us doing this with the User Maintenance dialog for user Jones. Note that you can set the narrative role and the action item role for a user. Action item tracking is discussed in Chapter 21. A user can have different roles for narratives and action items, being, for instance, a Submitter for narratives and a Reviewer for action items.

**Figure 20.1: Setting a User's Narrative Role and Email Address**

Next, we are going to assign a submitter, reviewer, and approver to each WBS (and OBS, etc.) element. It is important to realize that any user who is in the submitter role can submit a VAR narrative for an element, even he or she is not the submitter assigned to the element. A user in the submitter role can submit VAR narratives on any element, a user in the reviewer role can review a VAR narrative on any element, and so on. But the user who has been assigned a role for a given element will be the user who gets the nagging email if some action is required for a given element, as described later (see Section 20.8).

Before we assign users as submitters, reviewers, and approvers for the elements, we will need to know the ids of our users. We download the User table for use in the following step. Figure 20.2 shows the User table with the relevant columns: UserID and UserName.

**Figure 20.2: Getting UserIDs from the User Download**

Now we assign a submitter, reviewer, and approver to each WBS element in our contract. We download the Element table. Figure 20.3 shows the Element table with a number of columns hidden. Note that we have put the appropriate user ids in the SubmID and ApprID columns: user 14 (Smith, as we can see from Figure 20.2) is the approver on all elements, Spataro (user id 6) is the reviewer on all elements, and Brown (userid 16) is the submitter for elements 3000 and 3100.

**Figure 20.3: Setting Approver, Reviewer, and Submitter for Each WBS Element**

---

## 20.3 Write and Approve Narratives

Using the Narrative Editor in general is covered in Section 15. Here we focus on how the editor shows the current state of a narrative and allows the user to change the narrative's state, in conformity with the workflow rules.

In Figure 20.4, we see a narrative whose status is Unopened; that is, no actions have been performed on it. The user can edit the narrative, save it, submit it, or copy it forward to the next period, as the Action dropdown list shows.

**Figure 20.4: A VAR Narrative in the Unopened State**

In Figure 20.5, we see a narrative that has been edited and saved. The current user is Zepka (not shown in the figure, but the current user is displayed in the Status Bar). Notice that the Action dropdown list shows the status is Saved, and the actions available are Save and Submit. (This is because the current user Zepka is a submitter, not an approver.)

**Figure 20.5: A VAR Narrative in the Saved State**

In Figure 20.6 we see part of the same narrative from the previous figure (20.6), but this time in the Report Pane. We displayed this report by selecting WBS 3600 in the Sort Window, then choosing Reports > VAR Narrative from the menu.

**Figure 20.6: A VAR Narrative in the Report Pane**

Figure 20.7 shows the same narrative after user Zepka has submitted it. Note that the status has changed to Submitted. If Zepka has second thoughts, they can Save the narrative to change the status back to "Saved."

**Figure 20.7: A Submitted VAR Narrative, Viewed by the Submitting User**

In Figure 20.8 we once again see the same narrative, but now the current user is Jones. Since Jones has the Approver role, the actions available to him are to Approve or Reject the narrative. This illustrates the fact that the actions available to a user for a given narrative depend on the status of the narrative and the role of the user.

This point is worth emphasizing: if you don't see the actions you are expecting in the narrative editor's list of available actions, it probably means that you haven't been assigned the narrative role you think you have or ought to have. For instance, if you try to submit a narrative and find that "Submit" is not one of your options, most likely you haven't been made a narrative submitter. ("Failure" is never an option.)

**Figure 20.8: A Submitted VAR Narrative, Viewed by the Approving User**

Figure 20.9 displays a narrative that has been rejected, as viewed by the submitting user Troop; his options are to edit and save the narrative, or just submit it again unchanged (perhaps hoping that the Reviewer is in a better mood this time).

**Figure 20.9: A Rejected VAR Narrative**

Figure 20.10 displays a narrative that has been approved, as viewed by the submitting user Tideman. Since Tideman is not an Approver, and this narrative has already been approved, there is nothing she can (or needs to) do to it. If she were in the Approver role, she could Reject this Approved narrative, thus beginning the edit/submit/review/approve cycle again.

**Figure 20.10: A VAR Narrative in the Approved State**

---

## 20.4 Copy Forward

This option allows users to copy the text from their VAR for the previous period of data forward to the VAR for the currently selected period. The user can then adjust the text as necessary and save their changes. This can help simplify writing VARs.

---

## 20.5 Set VAR Required

This command allows the user to mark one or more elements as requiring a VAR narrative. You might want to do this if an element does not exceed the threshold, but you have some other requirement to write a narrative for it anyway.

**Figure 20.11: Set VAR Required Dialog**

When an element is marked with this dialog, the chosen VAR flags will appear in the Format 5 column in the Sort Window. The VAR flags in the Format 5 column (called VAR in the Empower Default view) are used to determine which sections will need to be filled out in the VAR Narrative for the corresponding element.

In practice, VARs are treated the same way whether they are calculated or marked manually. For example, an element manually marked with "S" will have the same required sections for Cumulative SV in the VAR Narrative that it would if "S" were a calculated VAR flag. The same applies for Action Item categories.

The dialog offers three ways to chose elements to be marked:

- **Current element** – when you click the Submit, the currently selected element is marked.

- **Top N elements in sort window** — this offers an easy way to select a range of elements: simply choose a sort criterion that will group the desired elements at the top of the Sort Window, adjust the value in the text box as appropriate, then click Submit.

- **All elements in sort window** – just what it says.

The dialog will show checked boxes for all of the VAR flags that are marked for the currently selected element. Clicking Submit will mark the chosen elements with all of the checked VAR flags and remove any flags that have been unchecked.

If you leave the "Restore manually marked items to their calculated value" checkbox unchecked, clicking Submit marks the items meeting the criteria selected in the first section of the dialog. If this checkbox is checked, the selected items will be restored to their calculated value, clearing any VARs that have been set manually.

The calculated values for the currently selected element are marked by an "x" to the left of the VAR flag. For example, in 20.11, the calculated VAR flag is "c", while "S" has been set manually.

The view "VAR Compare" shown in 20.12 shows the values for calculated VAR flags in the column "CVAR" and the currently set VAR flags in the "VAR" column. The column "F5M" will contain a one if CVAR and VAR do not match and a zero if they do. This allows sorting for all elements whose set VAR flags differ from the calculated VAR flags, allowing you to look back at the changes that have been made to the VAR flags for each element.

**Figure 20.12: VAR Compare view**

---

## 20.6 View the VAR Narrative Status

Next we describe Empower's features for managing the narrative workflow.

You can create views that will highlight the status of your VAR narratives. The fields that you might find particularly useful for this purpose are: Approver, Submitter, VarUser, VarUpdate, VarState, VarReject, and Fmt5Var. In the discussion below, we will use a sample VAR Narrative Status view (available upon request).

Figure 20.13 shows the Sort Window with the VAR Narrative Status view applied (We have hidden a few fields to make the figure fit on the page.) The Sort Window has been sorted on the VAR column to bring together all elements that have non-blank Format 5 VAR values. From this view, we see, among other things, that Smith hasn't started on the narrative for WBS 3000, Tideman's required narrative for 3200 has been saved, and Troop's narrative for 3700 has been submitted and approved.

**Figure 20.13: Sort Window with VAR Narrative Status View**

You can also create prefilters to help manage the VAR narrative workflow, using the same fields mentioned above. A sample prefilter, VAR Action Required (Submitter), is used in the discussion below (and is, along with similar prefilters for Reviewers and Approvers, also available upon request).

Figure 20.14 shows the same view with the VAR Action Required (Submitter) prefilter applied. As the name implies, this filters the Sort Window to elements which need action from VAR narrative submitters. (This prefilter passes elements whose Fmt5Var is not null, and whose VarState is not Submitted.) Jones needs to submit the narrative for 1000, Smith needs to start on 3000, and Troop needs to revise the rejected narrative for 3700 and submit it again. Note that the saved narrative for WBS 3200, which appeared in the previous figure (20.13), has been filtered out. Even though this narrative is still in the Saved state, no Submitter action is required since the VAR column is blank for this element. (There is nothing to prevent you from writing a VAR narrative on any element.)

**Figure 20.14: Sort Window with VAR Narrative Status View and VAR Action Required (Submitter) Prefilter**

---

## 20.7 Writing Narrative Email Templates

When you send emails to submitters, reviewers, and approvers of actions they need to take (see Section 20.8), you will be asked to specify a template that will be used to generate the email text.

Narrative email templates are just another type of Empower template. General instructions for writing Empower templates can be found in Appendix C. Here we note special considerations for email templates.

To identify a template as an email template (meaning it will be displayed in the Template listbox on the Send Narrative Emails dialog), you must put the line

```
Default : EMAIL
```

in the template header. The template name is what will be displayed in the Template listbox.

### Available Email Placeholders

Several placeholders are available for use in email templates:

- `(|Submitter|)`, `(|Reviewer|)`, `(|Approver|)`
- `(|Recipient|)`: the display name of the recipient
- `(|User|)`: the current user
- `(|Role|)`: Submitter, Reviewer, or Approver, depending on which was picked in the Recipient listbox
- `(|Note|)`
- `(|State1|)`, `(|State2|)`: The status of the narrative; for this placeholder and those listed below, the trailing 1 is for VAR narratives and 2 for user narratives.
- `(|User1|)`, `(|User2|)`: the last user who changed the status of this narrative
- `(|LastUpdate1|)`, `(|LastUpdate2|)`: date and time of last status change or save.
- `(|RejectReason1|)`, `(|RejectReason2|)`: The reason text entered by the disapproving Approver.

Sample templates are available upon request. We describe most of these placeholders using the sample Submitter template shown below.

Templates can include HTML formatting or be in plain text (which you might prefer if your recipients have an email system that does not handle HTML formatting in emails).

The

```
(|Meta|BeginLoop|ce|SyncSortWnd|$ce$|)
```

and

```
(|Meta|EndLoop|ce|)
```

lines are special codes that loop through all elements in the Sort Window. (You can learn more about looping constructs from the technical note, "Writing Empower Custom Reports," available on our support website (http://encoreanalyticsllc.freshdesk.com/support/solutions).

### Example HTML Email Template

```html
<!-- input template -->
Name : Submitter Email (HTML)
Description : Submitter Email Template (HTML)
Default : EMAIL
<!-- input template -->
<!DOCTYPE html>
<html>
<style>
body.tmpl { font-family:sans-serif; font-size:8; }
table.tmpl { width:100%; border:1px solid silver; border-collapse:collapse; }
td.tdl { border:1px solid silver; border-collapse:collapse; padding:4px; width:10%; white-space:nowrap; }
td.tdr { border:1px solid silver; border-collapse:collapse; padding:4px; }
</style>
<body class="tmpl">
Dear (|Submitter|),
<p>
For Period ending (|EndDate|$ce$|), the following elements have VARs that require attention. (|Meta|Note|)
<p>
Regards,
<p>
(|Meta|User|)
(|Meta|BeginLoop|ce|SyncSortWnd|$ce$|)
<table class="tmpl">
<tr><td class="tdl">Contract</td><td class="tdr">(|ContrName|)</td></tr>
<tr><td class="tdl">WBS</td><td class="tdr">(|WbsNum|$ce$|)</td></tr>
<tr><td class="tdl">Description</td><td class="tdr">(|LongDesc|$ce$|)</td></tr>
<tr><td class="tdl">VAR Flags</td><td class="tdr">(|Fmt5Var|$ce$|)</td></tr>
<tr><td class="tdl">Submitter</td><td class="tdr">(|Submitter|$ce$|)</td></tr>
<tr><td class="tdl">Approver</td><td class="tdr">(|Approver|$ce$|)</td></tr>
<tr><td class="tdl">VAR State</td><td class="tdr">(|State1|$ce$|)</td></tr>
<tr><td class="tdl">Last Updated By</td><td class="tdr">(|User1|$ce$|)</td></tr>
<tr><td class="tdl">Last Updated On</td><td class="tdr">(|LastUpdate1|$ce$|)</td></tr>
<tr><td class="tdl">Reject Reason (if any)</td><td class="tdr">(|RejectReason1|$ce$|)</td></tr>
</table>
<br>
(|Meta|EndLoop|ce|)
</body>
</html>
```

### Example Plain Text Email Template

```
<!-- input template -->
Name : Submitter Email
Description : Submitter Email Template
Default : EMAIL
<!-- input template -->
Dear (|Submitter|),

For Period ending (|EndDate|$ce$|), the following elements have VARs that require attention. (|Meta|Note|)

Regards,

(|Meta|User|)

(|Meta|BeginLoop|ce|SyncSortWnd|$ce$|)

Contract: (|ContrName|)
WBS: (|WbsNum|$ce$|)
Description: (|LongDesc|$ce$|)
VAR Flags: (|Fmt5Var|$ce$|)
Submitter: (|Submitter|$ce$|)
Approver: (|Approver|$ce$|)
VAR State: (|State1|$ce$|)
Last Updated By: (|User1|$ce$|)
Last Updated On: (|LastUpdate1|$ce$|)
Reject Reason (if any): (|RejectReason1|$ce$|)

(|Meta|EndLoop|ce|)
```

---

## 20.8 Notify Submitters, Reviewers, and Approvers of Required Actions

The Admin > Send Email Notifications allows the user to send emails to submitters, reviewers, or approvers who have required actions to perform regarding narratives.

Sending narrative emails can be done manually or as part of an automated process. In this manual, we will describe the manual process. Setting up the automated process is an administrative task; it is described in the technical note "Automating Narrative Workflow Emails with Empower," available on our support website, http://encoreanalyticsllc.freshdesk.com/support/solutions.

The first step is to filter the Sort Window to show just elements for which you wish to send narrative emails. We will do this by applying the VAR Narrative Status view, then the VAR Action Required (Submitter), VAR Action Required (Reviewer), or VAR Action Required (Approver) prefilters (all these available as samples upon request).

Figure 20.15 shows the Send Email Notifications dialog. Under Recipient, the user chooses to send the emails to Submitters or Approvers. Under Template, the user chooses which template to use. (Writing such templates was covered in the previous section.)

**Figure 20.15: Sending Email Notifications to Submitters**

In addition to the text provided as part of the template, the user can enter an optional note that will be added to each generated email. The note can be formatted, as you can see from the formatting toolbar on the dialog. In the figure, we have added some additional encouragement in red, which will no doubt be appreciated. To get your note text to appear as a new paragraph after the text in the email template, you need to enter a blank line in the Note editor, as we have done in the figure.

If you want to do a "dry run" to see what emails will be generated, without actually sending them, check the "Generate emails only (do not send)" checkbox (as we have done in the figure).

When you are ready to send (or to do a dry run), click Submit. The generated emails will be shown in the Status window of the dialog, as you see in Figure 20.16.

**Figure 20.16: Generated Emails**

Below we show an extract of the generated emails. You can see that the subject line and most of the body of the email comes from the template. The recipient's name and email address are filled in appropriately, and the note we wrote is added as well. Then follows a list of all required actions.

In the extract, we see that Smith and Jones each need to submit VAR narratives for one WBS element. If a recipient is on the hook for more than one element, his or her email will list all the such elements. One email will be generated for each recipient, so in our example two emails have been generated. Note that since this listing was generated from a dry run, the transcript of each email ends with (Not) Sending..

### Example Generated Emails

```
Smith (smith@daedalus.com)
--------------------------------------------------
To: smith@daedalus.com
From: empower.vm@encore-analytics.com
Subject: Submitter Smith, you have work to do.
Dear Smith,

For Period ending JAN 04, the following elements have VARs
that require attention.

We were late on submissions last period. Let's be on time
this period!

Regards,
Admin
Contract MOH-2

Wbs 3000

Description PRIME EQUIP
VAR Flags c
Submitter Smith
Approver Jones
VAR State
Last Updated By
Last Updated On
Reject Reason (if any)
--------------------------------------------------
(Not) Sending.. OK

Jones (jones@daedalus.com)
--------------------------------------------------
To: jones@daedalus.com
From: empower.vm@encore-analytics.com
Subject: Submitter Jones, you have work to do.
Dear Jones,

For Period ending JAN 04, the following elements have VARs
that require attention.

We were late on submissions last period. Let's be on time
this period!

Regards,
Admin
Contract MOH-2

Wbs 1000

Description MOH-2
VAR Flags c
Submitter Jones
Approver Jones
VAR State Saved
Last Updated By
Last Updated On 2016-04-18 09:52:50
Reject Reason (if any)
--------------------------------------------------
(Not) Sending.. OK

Generated 2 of 2 emails.
```
