# Chapter 8: Custom Charts

*From the Empower User Manual*

---

## Custom Charts

In addition to the rich set of standard charts, Empower allows users to create their own custom charts as well as import custom charts developed by others (see Section 3.2.1.4).

The figure below shows an example of a custom chart:

**Figure 8.1: A Custom Chart**

All the features of the standard charts are, in general, available for custom charts. This includes features such as zooming, printing, downloading to image files, hovering over data points to bring up a floating display of the numerical values, showing or hiding selected data series, and using the Chart button on the Toolbar to cycle through chart styles and (where applicable) showing or hiding color bands.

Custom Charts are created, edited, reordered, and deleted in very similar ways to Views and Prefilters. One difference you may notice is that Custom Charts have no equivalent to the Edit Current command for Views and Prefilters.

## 8.1 Global and User Charts

Custom chart functionality is accessed via the Charts > Custom Charts menu command, shown below:

**Figure 8.2: Custom Charts Menu**

Recall that Empower has the notion of Global and User items, where the items can be views, custom charts, custom reports, and prefilters. Also, items are stored under a user's ID, even when that user is a member of a group. (See Section 5.2.)

On the Custom Charts submenu, the first option will always be Global, which brings up a submenu of Global charts. If the current user is not the Admin user there will also be an option called User which, naturally, brings up a submenu of User charts. Clicking on the chart name (whether under Global or User) will open the selected chart in the Chart Window. (The Admin user cannot create User charts by definition, since all charts created by Admin are Global.)

## 8.2 Open/Edit

This command allows the user to open the selected chart, edit the selected chart (possibly saving the edited version as a new chart), or create a new chart from scratch (that is, not based on an existing chart).

**Figure 8.3: Chart Open/Edit Dialog**

This dialog lists both custom and standard charts. Standard charts cannot be edited or exported as user items, but can be opened from this dialog. The checkboxes on the side of the dialog allow you to filter which types of charts are listed. The dropdown at the top of the dialog allows you to change which type of user item you want to see in the dialog. (e.g. Charts, Reports, Prefilters)

### 8.2.1 Opening Charts

We said earlier that the number of charts displayed on the Global and User submenus is limited to twenty. If you have more than twenty charts in one or the other of those categories, they won't all be displayed, and thus you won't be able to open some of them via the submenu. However, the Open/Edit command displays all the available custom charts, both Global and User, so you can always open a custom chart with this command. The figure below shows the Open/Edit Chart dialog for a user:

**Figure 8.4: Open/Edit List Box**

In the list, we see some global custom charts (e.g. "BAC by CAM" and "Target Price vs. Forecasts"). At the bottom we see "+ Fred-Pct Cmp/Sch". The plus sign (+) means that this is a User chart (think of User charts as charts "added" — plus — to the standard set of Global charts). This chart was visible on the User submenu, and could have been opened by clicking on its name there.

Now notice the chart named "[Fred-4]." The brackets around the chart name indicate that this chart is not shown in the User or Global commands; thus only way to open this chart is through this dialog. (And we can see that it is a User chart by the prefixed "+".)

Recall that to open the selected chart in an external window or tab, instead of in Empower's Chart Window, click the Open key while holding down one of these three modifier keys: Control, Shift, or Alt/Option. (See Section 7.1.)

### 8.2.2 Editing Charts

The second functionality available on the Apply/Edit dialog is the ability to modify an existing chart, using the powerful Edit Chart dialog box (see Figure 8.5).

**Figure 8.5: Edit Chart Dialog Box**

Here we have opened the Global chart "Variance vs. Index". We are logged on as the Administrator, so we could save this chart (thus changing it for everybody), or save it as another chart.

At the top of the dialog, we can change the chart name. This is what will be displayed as the chart name in the menus and on the chart itself.

Next to the Chart name is the checkbox that indicates whether this chart should be shown in the Global or User menu. You would normally uncheck this if you had more than twenty custom charts and you decided that you didn't want this chart to be in that top twenty (perhaps because it wasn't going to be used very frequently).

Available columns (fields) are shown on the left side of the dialog box. The Column Group selector is used to filter the Columns selector by the type of column (Primary, Percent, Index, or Audit Tests) to make column selection easier. Further, a short description of the selected column is shown below the column selector to aid in selecting the correct column.

To add a column to the existing chart, select the desired column from the Columns box and press the Add > button. The new column will be added above the currently selected column in the Chart Lines box. To remove a column from the chart, press the < Remove button.

To relocate a column in the Chart Lines list box, use the up and down arrows to the right of the Chart Lines box. The lines are drawn in the order they appear in the list box, from top to bottom. This can affect the appearance of your chart. For instance, if you draw a data series as a line first, then draw another data series as columns, the columns, as the last-added data series, will cover up any lines or points from the first series, which is probably not what you want (see below).

**Figure 8.6: Columns Drawn on Top of Lines**

Drawing the columns first, then the lines, will put the lines and their points on top of the columns, as in the next figure:

**Figure 8.7: Lines Drawn on Top of Columns**

Back in the chart editor, you'll notice in the Chart Lines list that each chart line is prefixed by a "L" or a "R". This indicates whether the axis for that chart line will be displayed on the left or right of the chart. This allows you to have two different kinds of data on one chart, say one or more chart lines showing dollar values, and one or more chart lines showing indexes. The dollar axis (with its numeric labels) will be on one side and the index axis (with its labels) will be on the other side. (Only the tick values will be shown on the left axis; the name of the data will not be shown to conserve real estate. The name of the data on the left axis will be inferred from a well-chosen chart name.)

(Recall that the kinds of data are the entries in the Column Group list.)

You are not allowed to have more than two different kinds of data displayed on a chart. In our example, we have CvCum and SvCum (measured in dollars) on the left axis, and CpiCum and SpiCum (indexes) on the right axis. If we selected "Percent" in the Column Group list box, we would see that the Columns list box is empty. This is because we have already used our allotment of two different kinds of values, and Percent would be a third kind. We could add more "Primary" chart lines or more "Index" chart lines, but none of the other kinds. If we removed all of the chart lines of a given type (say, CpiCum and SpiCum), we would find that we were now able to add Percent-type chart lines.

Below the Chart Lines list box are a number of controls allowing us to customize each chart line. The legend is shown at the bottom of the chart, indicating the color and type (line, column, or gauge) for each chart line, just as in the standard charts. The color dropdown list, naturally, allows the user to choose the color used for drawing the selected line or column (bar); the color names ending in "2" are lighter versions of the standard colors. The style dropdown list allows the user to choose the style of line used for the selected line (solid, dots, dashes, etc.).

Note: Charts with gauges are somewhat different that charts that use lines or columns. See Section 8.2.4 for more details.

The Axis dropdown list allows the user to specify whether the axis for the selected chart line will appear on the left or right. Recall that all chart lines with the same kind of data go on the same axis. Furthermore, an axis can display only one kind of data. This has two consequences. First, if you change the axis side for a given chart line, all chart lines of the same kind will also have their axis side changed. So, in the figure above, if we change CpiCum to have its axis on the left side, the axis for SpiCum will automatically be shifted to the left side as well. Second, since an axis can only have one kind of data, if we put CpiCum (index data) on the left side, the dollar data (CvCum and SvCum) that was already on the left side will be moved automatically to the right side.

Another thing to keep in mind: the left axis is the privileged axis. This means that if you only have one kind of data, its axis will have to be on the left side. So, back to our example: say we have CvCum and SvCum on the right, and CpiCum and SpiCum on the left. If we remove the latter two, leaving just CvCum and SvCum, we will see them automatically reassigned to the left axis, since it was vacated by the removal of CpiCum and SpiCum.

Another consequence of the left axis being the privileged one is that the color threshold display applies to the chart line whose axis is on the left. So in our example, with CvCum and SvCum on the left axis and CpiCum and SpiCum on the right, the color bands are for the variance data.

**Figure 8.8: Color Bands for Variance Data**

If you were to hide both variance data series (by clicking on their names in the legend), you will see the index display but the color bands will not be shown, as they belong to the (hidden) variance:

**Figure 8.9: Variance Chart Lines Hidden**

If we swap the two kinds of data, so that the indexes are on the left axis and the variances on the right, and show the color bands, the color bands will be those applying to the index data, as shown below:

**Figure 8.10: Color Bands for Index Data**

### 8.2.3 Charts With Future Data

Future data can be added to some custom charts by using the "FutureBcws", "FutureEtc", "FutureBcwsCum", and "FutureEtcCum" columns. These columns are listed at the bottom of the "Primary" column group.

**Figure 8.11: Creating a Custom Chart with Future Data**

Notice that we have added the "FutureEtc" and "FutureBcws" columns to our chart. These lines will display future period data in our chart.

If we open this chart, we'll see a chart like Figure 8.12

**Figure 8.12: Custom Chart with Future Data**

Notice that we now have data past JAN 17 (our current selected period), and we now have a dotted red vertical line. This red line indicates "time now", or the currently selected period, and is only present on charts that have future data.

If you plan to use future data in your charts, there are a few things to note:

1. Recall that the left axis is the privileged one. Because of this, the x-axis "buckets" are based on the left axis data. As a result, future data MUST be on the left axis. Attempting to put a future field on the right axis will result in the following message:

**Figure 8.13: Future Data on Right Axis Message**

2. Future data fields cannot be the only fields on the left axis. In other words, you must have at least one non-future field on the left axis in order to add a future field. If you attempt to save a chart that only has future fields on the left axis you will see this message:

**Figure 8.14: Future Data Without Other Fields Message**

You will not be able to save your chart until you have either removed the future field(s) or added a non-future field to the left axis. This also means that you cannot have a chart that ONLY has future fields.

### 8.2.4 Gauge Charts

As noted earlier, Empower also allows the creation of charts with gauges to display the data. Up to nine data series may be shown on a gauge chart. If one data series in a chart uses a gauge, all other data must also be displayed with gauges.

Here's how to create a custom chart with gauges. Begin by opening the chart editor (Charts > Custom Charts > Open/Edit > New). As usual, give your chart a name ("GaugeChartDemo" in this example). We're going to show the cumulative CPI and SPI, so select "Index" in the Column Group list box, then "CpiCum" in the Columns list box. Click Add > to include CpiCum in the Chart Lines list box. Then choose "Gauge" in the Type selection box. Add SpiCum in the same way. Note that for gauge charts, the Color and Axis values are ignored. When you are finished, the chart editor should look like this:

**Figure 8.15: Creating a Custom Chart with Gauges**

Now save your chart. Your chart will appear in the Chart Window, and will look like this:

**Figure 8.16: A Custom Chart with Two Gauges**

The gauges will be displayed in the order that the column names appear in the Chart Lines list box and will appear in the chart ordered left to right, and top to bottom. Note that in our example the two gauges are staggered. Empower will arrange the gauges for the maximum size and legibility.

### 8.2.5 The Chart Button with Custom Charts

Now, a few words about how the Chart button works with custom charts. Recall that the Chart button can be used to cycle the way data series are presented: clicking successively on the button toggles the style from lines to vertical bars to horizontal bars and back to lines. This will happen with custom charts as well, as long as the chart lines on the left axis are set to "Lines". So the chart below was created in the editor with the BAC and EAC chart lines on the left axis and the line type as "lines".

**Figure 8.17: All Chart Lines as Lines**

If you press the Chart button or select the vertical bars option from that button, you will see the chart below. Note that since the left axis is the privileged axis, its data (BAC and EAC in this case) is the data affected by the Chart button, and its data is now presented as vertical bars (columns). The data on the right axis (the percent completed and percent spent) remains displayed as lines.

**Figure 8.18: Chart with Vertical Bars**

And another press of the Chart button shows the BAC and EAC data as horizontal bars.

**Figure 8.19: Chart with Horizontal Bars**

If, however, the data on the left axis was formatted as columns in the chart editor, the Chart button will not change the display of that data. The idea is that if users select "Columns" for a chart line in the editor, they don't want it changed.

The Save button saves the chart being edited and exits the dialog.

The Save As button saves the chart being edited as a chart different from the one you started with, and exits the dialog.

The Reset button undoes all the changes you made and resets the chart to the state it was in when you opened the chart editor.

The third functionality available through the Open/Edit dialog is to create a new chart from scratch; that is, it will open the chart editor with a title of "New Chart" and no chart lines selected.

## 8.3 Delete/Reorder

This command allows the user to delete User charts or to change the order in which User charts appear in the User menu. (The Empower administrator can also change the order of Global custom charts.) Figure 8.20 shows the dialog. Note that charts that have not been selected for display in the User menu are shown with square brackets around their names.

**Figure 8.20: Delete/Reorder Dialog**

To reorder a chart, click on the chart, then click on the up arrow or down arrow buttons to shift the chart by one position. When you have the charts ordered to your satisfaction, click the Reorder button, then close the dialog by clicking on the X in the upper-right hand corner of the dialog. Note: if you reorder the charts in the list with the up and down arrows, and then close the dialog without clicking the Reorder button, your changes will not take effect.

To delete a chart, click on the chart, then click the Delete button. Repeat until you've finished deleting all the charts you want to get rid of, then close the dialog as described above.
