# Chapter 2: QuickStart

*From the Empower User Manual*

---

## Chapter 2: Quick Start

This chapter gives the user a quick overview of Empower's features; later chapters drill down and provide more detail.

## 2.1 Standalone Startup

Empower can be installed as a client-server system, where the Empower program and its database reside on one or more servers connected by a network to the user's computer (the client), or as a standalone, where the Empower program is installed on the user's computer, either directly or using Docker.

Most of the time this difference between standalone and client-server installation is transparent to the user. However, users of the Docker installation of Empower need to remember to start Docker unless Docker is configured to start up on boot-up.

## 2.2 Starting, Logging in, and Stopping Empower

Empower is a web application. This means that the user runs Empower by opening one of the supported browsers (see Section 22.4 for a list) and entering something like http://[servername]/empower or http://[servername]:5000/index.html in the browser's address bar, where [servername] will be the name of the server on which Empower is installed at your site. This name will vary from site to site; contact your local system administrator for more information. (For standalone Empower, the server name is localhost by default.)

What happens next depends on whether or not single sign-on (SSO) has been implemented at your site.

If single sign-on is not in effect, you will then see the login screen in Figure 2.1. Note that this screen also shows a dropdown list to select a data source. This is the name for a Empower database. An Empower installation can have any number of databases, so if the default choice is not the one you want, use the dropdown list to find your desired database. In the figure shown, an SQL Server database is available.

**Figure 2.1: Choose Database and Login Screen**

Next you enter your credentials (username and password) and press the OK button. If authentication is successful, then you will then see the Empower main screen (shown in Figure 2.2) and you can begin using the application.

If your site has implemented SSO, you will usually not be prompted for your Empower username and password; you will be sent straight to Empower's main screen.

If your site has implemented SSO, and Empower asks for your credentials anyway, what has most likely happened is that your OS credentials (those that you supplied when you did the SSO) and your Empower credentials have not been synchronized. If this happens, go ahead and enter your Empower credentials. Empower will automatically synchronize your credentials with the OS credentials, and you won't be asked to login to Empower again.

What happens if you log on using SSO, but there is more than one Empower database available? Since SSO bypasses the screen that allows you to choose the database, it might seem that SSO prevents you from using a different database. In fact, if there is more than one database available when you log in with integrated authentication, the default database will be selected. If you wish to change to a different database, you need to logout (see Section 3.2.1.7). Then the login screen will be presented (Figure 2.1), and you can choose a different database with the dropdown list. You do not, however, have to enter a username and password provided that your username and password are set up in the datasource that you're selecting (remember, the point of SSO is that the operating system and all SSO-enabled applications already know who you are). You just chose the data source and click OK.

Since Empower is a web-based application, you can exit the application by closing the browser tab in which Empower is running, closing the entire browser, or by logging out from Empower's File menu.

## 2.3 Overview of the Screen

Figure 2.2 shows Empower running in the Internet Explorer (IE) browser. If you are using Firefox, Chrome, Safari or any other browser, your screen may look slightly different. Also, you may have additional toolbars displayed in your browser depending upon optional settings in your browser.

**Figure 2.2: Screen Overview**

In Figure 2.2, the IE browser is displaying the server URL (the top row). The second row is the Empower Menu Bar. On the Empower menu bar you will find: File, View, Charts, Reports, Inputs, and so on. Clicking on the major heading on the Menu Bar will open sub-menus. For example, selecting the Charts menu will provide a list of all charts available in the tool. These items will be discussed in more detail later. Just below the Empower Menu Bar is the Empower Toolbar.

The most commonly used functions are included in the Empower Toolbar. The Toolbar is dynamic, meaning that it will change depending on what is selected in the lower Chart and Report windows. For example, you will notice that the Toolbar is different in Figure 2.2 than it is in Figure 1.1. This is because the Schedule Gantt Chart is open in Figure 2.2, which causes the Toolbar to display buttons for functions related to the Gantt chart (Filter, Scale, Links, Critical, Milestone, and SIB). The Status Bar also shows information related to the Gantt chart: it shows that 42 tasks are displayed in the chart. The "[RC]" tells us that the chart is being filtered for Red tasks (R) and tasks that are on the critical path (C). These filters were set with the Filter and Critical buttons on the ToolBar.

Each item on the Empower Toolbar will be discussed later.

### 2.3.1 The Tripane Layout: Sort, Chart, and Report Windows

Empower presents information in three primary windows, called the Sort, Chart, and Report Windows. The Sort Window is at the top of the Empower window, with the Chart Window and Report Window side by side and below the Sort Window. This layout of the three primary windows is called the "Tripane" layout. Currently it is the only layout of the three windows available.

Below the Empower Toolbar is the Sort Window. The Sort Window has powerful tools for filtering and sorting, and is used to select accounts for further analysis. The Sort Window can be filtered on multiple columns to limit the rows to specific problem accounts, and can be sorted to bring worst or best performers to the top of the window. You may add or delete columns in the Sort Window and change the order of the columns using a drag-and-drop technique. Note that vertical and horizontal scroll bars will appear in the various windows as required depending upon the amount of data contained in the window. You may also use gestures to scroll, but if the Sort Window has the Freeze WBS/Desc option selected, make sure that your gestures are to the right of the frozen columns.

Selecting an element in the Sort Window will update the open chart, report and input windows. If an input window is open and the text has changed, you will be prompted to save or discard the changes. If for any reason you don't like the layout of your windows, you can use the Layout button on the Toolbar ribbon to restore them to the default size and arrangement.

### 2.3.2 Menu Bar

The Menu Bar provides access to the main Empower features. Figure 2.3 displays the Menu Bar. Selecting an item from the Menu Bar produces a sub-menu with more options.

**Figure 2.3: Menu Bar**

### 2.3.3 Toolbar

The Toolbar is used for quick access to commonly used functions. Figure 2.4 shows the Empower Toolbar.

**Figure 2.4: Toolbar**

### 2.3.4 Status Bar

The Status Bar is located at the bottom of the application and provides key information regarding the status of selections including the contract, active element, sort parameter, prefilter applied, and filters applied. In Figure 2.5, for example, the Status Bar shows:

- the current user is Admin,
- the open contract is MOH-2,
- the period being displayed is JAN04,
- the structure being displayed is WBS (as opposed to OBS or IPT),
- the units are Dollars (as opposed to labor hours, etc.),
- the selected element is "3200:Communications",
- the rows in the Sort Window are sorted by CV ascending (worst to best),
- and the currently applied filter results in the display of 8 of 28 total elements in the dataset. Furthermore, the filtered columns included Lowest Level (LL), % Complete and CPI.

**Figure 2.5: Status Bar**

Filters will be discussed in Chapter 4. When the Gantt chart is active, additional items will be displayed in the Status Bar. These are discussed later in the Gantt Toolbar section (7.17.1). When using "Task Mode" note that the number of "Elements" displayed in the Status Bar is really the number of Tasks displayed in the sort window.

## 2.4 Opening Datasets

After logging in, the next thing the user will want to do is open a Dataset. This will populate the Sort Window with data. A Dataset is comprised of a contract (sometimes called a project), period of data, structure (WBS, OBS, IPT, etc.) and unit of measure (Dollars, Hours, etc.). To open a Dataset, choose the Dataset button from the Toolbar, or select File > Open Dataset from the Menu Bar. The Open Dataset dialog will appear (Figure 2.6). As you select different contracts, the list of periods, structures (WBS, OBS, IPT, etc.), and units will change to reflect the items actually available for that contract. So, for instance, if you only have a WBS defined for a contract, only "WBS" will appear in the structures list box when that contract is selected. Likewise, if the selected contract only uses Dollars, Hours, and EQP, only those three units will appear in the list box of units.

**Figure 2.6: Open Dataset Dialog**

Note that you can leave the Dataset dialog box open and move it around the screen or close it by selecting the X in the upper right hand corner. Repeat this process to open a different Dataset.

The dialog also has a checkbox that you can mark if you want the dialog to close after you click "OK" to open a dataset, or uncheck if you want the dialog to stay open. This checkbox defaults to the value specified for your install, see the tech note titled "The Empower Configuration File" for more details.

### 2.4.1 Dataset Prefilters

Note in Figure 2.6 the select box with the text "(All Elements)." This is a prefilter select box. Prefilters are a way of filtering or limiting the data rows (elements) that are shown in the Sort Window. Prefilters are discussed more fully in Chapter 6; here we briefly note that a prefilter is a logical expression that is applied on the server side and limits the elements of a contract that are sent over the network to the client's computer. This is in distinction from interactive filters or views, which are applied on the client's computer and do not limit the number of rows sent down over the network from the server to the client's computer. Allowing the user to choose and apply a prefilter when opening a dataset with a very large number of rows will reduce network traffic and can significantly improve the responsiveness of the Empower application. For instance, if a contract had 10,000 elements, and the user applied a prefilter that filtered out all but 100 elements, only those 100 would be sent over the network. By contrast, if the user didn't apply a prefilter when opening the dataset, but used an equivalent interactive filter (Chapter 4) or view (Chapter 5), all 10,000 elements would be downloaded, then the relevant 100 records would be displayed in the Sort Window.

To apply a prefilter when opening a dataset, click on the prefilter select box; a list of prefilter choices will appear, as shown in Figure 2.7. Click on the desired choice. Some, such as "CAM/IPT" or "WBS Contains," will then display a prompt box to get a necessary parameter. For instance, selecting "CAM/IPT" will lead to a prompt box in which the user will enter the name of the person. If the user enters "Price," then only elements with Price as the CAM will be downloaded over the network from the server and displayed in the Sort Window.

**Figure 2.7: Open Dataset Dialog**

When a prefilter has been chosen, the Open Dataset dialog will look like Figure 2.8 below.

**Figure 2.8: Open Dataset Dialog**

At this point, the user selects the contract, period, structure, and units as before, and presses the OK button to open the dataset.

Empower will display the text "Loading..." in the status bar while it is loading the dataset. Depending on speed of your computer and the size of your dataset, the dataset may be loaded before you even see this status message. For really large datasets, however, this message assures you that Empower is working on your request.

### 2.4.2 Cross-Contract Datasets

It is also possible to open all contracts. This is known as creating a "cross-contract query". Note in the figure below that the first entry in the Contract list box is "(All Contracts)". Note also how the Periods list box displays "CUR-0", "CUR-1", "CUR-2" and so on. "CUR" here means "most recent in the contract", "CUR-1" means "the period prior to the most recent in the contract", and so on. (The figure also shows that we are opening the dataset with a prefilter, in this case showing only level 1 elements, as there is little point in opening all contracts without some filtering.)

**Figure 2.9: Open Dataset Dialog**

When you choose a cross-contract query, the title in the Sort Window will, as always, reflect your choice of contract, period, structure, units (with display scaling), and the view. The figure below shows the contract is "(All Contracts)" and the period selected was "CUR-2" (two periods before the most recent period in each contract).

**Figure 2.10: Sort Window Title with All Contracts Opened**

### 2.4.3 Dataset Portfolios

Note in Figure 2.6 the select box with the text "(All Portfolios)." This is a portfolio select box. Portfolios are sets of Contracts that are grouped together.

**Figure 2.11: Open Dataset Dialog**

Selecting a portfolio will filter the datasets displayed to those in the selected portfolio.

**Figure 2.12: Open Dataset Dialog Portfolio Selected**

Selecting "(All Contracts)" with a portfolio selected allows you to open a dataset with all of the contracts in that portfolio.

**Figure 2.13: Open Dataset Dialog All Contracts in Portfolio**

Portfolios can be created and assigned contracts via the "Portfolios" Data Download found in Admin > Download Data File.

**Figure 2.14: Portfolio Data Download**

The resulting Excel file will have multiple tabs. The first tab will list all of the existing portfolios in the database. New portfolios can be added as usual via data upload of this file.

**Figure 2.15: Portfolio Data Download: First Tab**

The following tabs will list the contracts assigned to each portfolio.

**Figure 2.16: Portfolio Data Download: Second Tab**

### 2.4.4 Dataset Calendars

Depending on your server configuration, your "Open Dataset" dialog may also have a select box with the text "(All Calendars)." This option is not enabled by default. For information on how to enable this option at the server level see the tech note titled "The Empower Configuration File." This select box allows you to select a calendar as a data filter.

**Figure 2.17: Open Dataset Dialog Calendars Dropdown**

When using this dropdown, only contracts that use the selected calendar will be displayed.

Notice that when "(All Contracts)" is selected with a calendar selected, the Period section of the dialog does not use the "CUR-0" syntax discussed earlier in this chapter. This is because the behavior of the Period section is slightly different when a calendar is selected.

When "(All Contracts)" or multiple contracts are selected when a calendar has been selected, only data with an EndDate that matches the EndDate for the selected Period in the calendar will be opened.

**Figure 2.18: Open Dataset Dialog Calendar Selected**

For example, if you selected the "(Default)" calendar, then selected "MOH-2" and "Alpha" as your contracts, then selected the "JUN17" Period, only data for "Alpha" would be displayed in the sort window because "MOH-2" does not have a period with the JUN17 EndDate, even though both contracts share the same calendar.

## 2.5 Managing the Sort Window

The browser window in which the Empower application is running can be resized by using the standard window resizing procedure for your operating system.

The user can also customize the size and arrangement of the sub-windows that display various parts of the Empower application. Recall that in the standard layout (called "Tripane View"), the top pane is the Sort Window, taking up the full width of the browser window. The space below the Sort Window is equally divided between the Chart and Report Windows, arranged side-by-side.

The three panes can be minimized or restored by clicking on the carets at the upper right of their respective borders.

For example, clicking on the caret at the top right of the Report Window minimizes (hides) the Report Window and the Chart Window grows to fill the space previously occupied by the Report Window. You will now see an arrow bar on the right side with a left-pointing caret indicating that the Report Window has been minimized. Clicking on this left-pointing caret will restore the Report Window to its previous size. Likewise, the Sort Window can be minimized by clicking on the upward-pointing caret. In response, the lower windows (Chart and Report) will expand upwards to fill the space vacated by the Sort Window. Clicking the downward-pointing caret restores the Sort Window.

These are all-or-nothing resizes. The user can also obtain finer control over the sizes of the windows by hovering the mouse over the borders between windows until the double-headed mouse cursor appears, then dragging the border until the windows are the desired size. This procedure is just like resizing main windows in your operating system.

To reset the default Tripane view, with the default sizes of the Sort, Chart, and Report Windows, choose the Layout button from the Toolbar. The default view shows all three windows, makes the Chart and Report Windows of equal width, and makes the Sort Window of equal height to the Chart and Report Windows.

The state of the tripane layout (that is, the size of the Sort, Chart, and Report windows, and whether each is expanded or collapsed) is saved automatically, so the next time you run Empower, the layout will be as you left it last time.

### 2.5.1 Sorting Rows

The user can sort the rows by clicking on the column header for the field to use as a sort key. For example, to sort by CAM, click the header labeled "CAM", and the rows will be sorted. A small arrow will appear in the column header to indicate that the sort windows is being sorted by the CAM column; the direction (up or down) of the arrow indicates whether the rows are being sorted in ascending or descending order. See Figure 2.19 to see what the CAM header looks like when sorting in ascending order. To sort in descending order, just click on the header again. The rows will be resorted, and the arrow will now point down. If you are done sorting by whatever column you had been using for a sort key, just click on another header to sort by that field (HIER — hierarchy — is a good choice, since it is the default sort order).

**Figure 2.19: CAM Header, Sorted Ascending**

### 2.5.2 Reordering Columns

Empower presents many fields (columns) of information about each contract element, usually many more than can fit on a screen. The user can reorder columns to bring more frequently used columns to the left, where they will be more likely to fit on the screen. Or the user may just want to bring certain columns closer to one another for the sake of convenience. Empower makes it easy to reorder columns. Simply click on the header of the column you wish to move, hold down the mouse, and drag the column to the desired location and release the mouse button.

Empower also allows the user to delete columns from the view, or add columns that are not present in the default view. For more on creating, modifying, and saving Views, see Chapter 5.

### 2.5.3 Filtering Rows

Empower makes it easy to filter the rows that appear in the Sort Window. Just below the row of column headers is the filter Bar (see Figure 2.20).

**Figure 2.20: Filter Bar**

The user types in a filtering condition, and the Sort Window will display just the rows meeting the condition. In the example shown below in Figure 2.21, the user is filtering to show just elements where the CAM is Brown. For more on filtering, see Chapter 4.

**Figure 2.21: Filter Row, Showing Filtering by CAM="Brown"**

### 2.5.4 Selecting Elements

Selecting an element will typically change what is shown in the Chart or Report Windows. To select an element, just click anywhere on the element's row. To indicate that the element has been selected, the background of the selected row will be darker than the other rows, as illustrated in Figure 2.22 below.

**Figure 2.22: Selected Row in Sort Window**

## 2.6 Charts

Empower displays a rich variety of charts to assist in Earned Value analysis. Figure 2.23 shows a Current Variance Chart as an example. For more on charts, see Chapter 7.

**Figure 2.23: Current Variance Chart**

## 2.7 Reports

Empower can produce many reports to assist in presenting the results of Earned Value analysis. For example, an AIN Narrative Report is shown in Figure 2.24 below. For more on reports, see Chapter 9.

**Figure 2.24: AIN Narrative Report**
