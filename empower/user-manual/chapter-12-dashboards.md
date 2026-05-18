# Chapter 12: Dashboards

*From the Empower User Manual*

---

## Overview

Empower's user interface is highly configurable. You can, for example, set views and filters to show just the data you want to see, sort it so it appears in the order you want, choose which charts and reports you want to work with and how they are sized within Empower's main window, and whether you want any charts or reports showing in external windows, and if so, where on your screen you want those external windows to appear.

You might find you set up your Empower user interface in a certain way for a given task, then configure the user interface differently for a different task, and you might wish you had an easy way to save your setup and recall it on demand. This is where dashboards come in; an Empower dashboard gathers your user interface configuration in a single place, so you can open a dashboard and have your Empower environment set up just the way you want it.

A dashboard stores the state of your Empower panes (Sort, Chart, and Report windows) — the size of each and whether or not they are minimized, and which chart and report is selected; chart options (line style, colors); the current view, prefilter, and sort settings; the size of the main window; and the size, location, and contents of any external chart or report windows, etc.

### Important Considerations

There are a couple of things to be aware of when you use dashboards:

1. Browsers aren't consistent in the way they report window size/position, so positioning external windows exactly might require trial and error
2. Some browsers do not allow the position of the main window to be set programmatically, so the main window position might not be retained

### Dashboards Menu

Figure 12.1 shows the Dashboards menu.

Dashboards are user items, and are imported and exported like other user items; see Sections 3.2.1.4 and 3.2.1.5. As in the case of other user items, there are Global dashboards (dashboards loaded by the Admin user which are available to all users and which can appear on the Global submenu), and User items (dashboards loaded by a non-admin user which appear on the User submenu and are only available to the owning user).

---

## 12.1 Save Current and Save Current As

To create a dashboard, simply arrange your Empower user interface the way you want it. Do any combination of the following:

- Choose a view
- Open a report and a chart (or minimize the chart or report window)
- Select the Sum button
- Set chart options
- Apply a prefilter
- Set up the sort order
- Open and position external windows for reports and/or charts

When you have the user interface set up, issue the command **Save Current As**. You will see the dialog box shown in Figure 12.2, which prompts you for a name for your dashboard.

### Dashboard Name Display

The name of your dashboard will be shown in the title of the Sort Window, as shown in Figure 12.3:

This tells us that in this case we are using the dashboard named "Bob-Schedule" (and the view named "IMSDQI").

### Updating Current Dashboard

If you make changes to the arrangement of your user interface while you have a dashboard applied, and you want to save these changes to the currently open dashboard, issue the command **Save Current**.

---

## 12.2 Apply/Edit

One way to apply a dashboard that has already been created is to pick it from the Global or User menus. Another way is to issue the **Apply/Edit** command. This brings up the dialog shown in Figure 12.4.

This dialog lists all the dashboards. As with other custom items, you might not see all available dashboards in the Global or User submenus, either because those submenus might already be filled to their limit, or because the "Show in Menu" property has been unchecked — more about that below. But the Apply/Edit dialog will always show all the dashboards.

Also following the pattern of other user items, User dashboards are shown with a prefixed "+" sign, while Global dashboards don't have the plus sign, and dashboards that have "Show in Menu" unchecked will have their name enclosed in square brackets.

### Applying a Dashboard

To apply a dashboard from this dialog, select the dashboard in the list and press the **Apply** button.

### Editing a Dashboard

To edit a dashboard, select it in the list and press **Edit**; you will then see the dialog shown in Figure 12.5.

You can do two things to edit a dashboard:

1. **Change its name** — Use the text box next to the 'Name:' label
2. **Control menu visibility** — Choose whether or not to show this dashboard in the Global or User submenu by checking or unchecking the "Show in Menu" checkbox

Note that to edit the contents of the dashboard, i.e., the arrangement of the user interface, you modify said arrangement and save the dashboard.

---

## 12.3 Delete/Reorder

This command allows you to delete any of your own dashboards, or to change the order in which these dashboards appear in the Global or User submenus. Ordinary users can only delete or reorder their own dashboards; the Admin user can delete and reorder Global dashboards.

Figure 12.6 shows the dialog box that appears when the user selects the Dashboards > Delete/Reorder command.

### Deleting a Dashboard

In this case, the current user is Bob, so the list does not include the Global dashboards (Dash-1 and Default) we saw in Figure 12.4. (Since users can only delete or reorder their own dashboards, the list does not show the plus signs elsewhere used to differentiate Global and User items.)

To delete a dashboard, select the dashboard you want to delete, then press the **Delete** button.

### Reordering Dashboards

To reorder a dashboard, select the dashboard you wish to reorder and move it up or down in the list of dashboards using the up and down arrow buttons. When you have the dashboard where you want it, press the **Reorder** button to finalize your change.
