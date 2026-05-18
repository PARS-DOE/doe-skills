# Chapter 7: Charts

*From the Empower User Manual*

---

## Chapter 7: Charts

Empower supports the most common charts for earned value analytics and also provides an integrated display of the Gantt schedule view. Empower includes historical trend charts, as well as charts that display the time-phased future period data for BCWS and ETC. This chapter begins with sections describing some advanced features available to the various charts. The chapter then continues with a more detailed description of some charts whose use may be less self-explanatory. Figure 7.1 shows the Charts menu. Custom charts, which also appear in the Charts menu shown here, will be discussed in the next chapter.

**Figure 7.1: Charts Menu**

---

## 7.1 Opening Charts in External Windows

Usually, charts are opened in Empower's Chart Window. However, you can choose to open any chart in an external window. You might want to do this to gain more screen real estate for a densely populated chart. (You can open reports in external windows too; everything in this section applies to reports as well.)

To open a chart in an external window, press and hold a modifier key (to be described in a moment), then click on the chart name.

Different browsers treat the modifier keys in different ways; some browsers will co-opt a given modifier key to perform some browser function, meaning that the key is not available to be used by an application. Empower handles that by recognizing any of the following three as the key to open a chart externally: Control, Shift, or Alt/Option (Alt on Windows, Option on Macs). If one of those keys doesn't open charts externally on your browser, try the next in the list until you find one that works, and then use it all the time.

You can have multiple external windows open. Each time you open a chart or report externally, Empower opens a new chart or report window (unless the chart or report is already open, in which case it just updates in place).

(Tip for Chrome users: Chrome normally opens external charts and reports in a new tab in the current browser window. To move such a chart or report to a new browser window, press and hold down the mouse pointer on the tab you want to move, then drag the tab away and release the mouse.)

Clicking a row in the Sort Window saves the size and position of external windows, and if you close a window, you should click a row to save that change. Empower keeps track of the windows' sizes and positions, and reuses them. So, suppose you have three windows stacked vertically, and you want to put a different chart in the middle position. You'd close the middle window, click a row, then Shift-click the new chart (assuming Shift is the key you use to open charts externally). The new chart will open in the middle position. Chart and report window positions are managed separately.

Many reports can also be opened externally, as described in Section 9.1.

---

## 7.2 Chart Style

The Chart Style button on the Toolbar changes the appearance of some charts in two different ways. First, it controls whether the chart is presented as a line chart, or a bar chart with either horizontal or vertical bars. Second, it controls whether colored backgrounds are drawn on charts to indicate the thresholds between the red, yellow, and green ranges of SPI, CPI, and TCPI (when applicable). Figure 7.2 shows the dropdown menu that is displayed when the Chart Style Toolbar button is pressed.

**Figure 7.2: Chart Style Menu**

The top three items control how the chart data is presented; the bottom two turn on and off the color coding of the chart background to indicate the various CPI and SPI thresholds (to be explained below).

The Chart Style button is a hybrid button: the arrow at the right side invokes a dropdown menu, as described above. But it also can function as a toggle button. If you use the dropdown menu to select the line style, the appearance of the button changes to show a tiny line chart. If now you click on the button again, the style cycles to the next option, vertical bars, and the button's appearance changes accordingly. Another click on the button and the current style becomes horizontal bars, and the button's appearance changes again.

But if you use the dropdown menu to turn thresholds on, the appearance of the button changes accordingly. Note that the image now indicates the threshold state, not the data display type. Another click, and the button's appearance reflects the state change.

In other words, the appearance of the button shows which of the two types of styles (Line/Vertical Bars/Horizontal Bars or Show/Hide Thresholds) will be toggled.

If the button is set to toggle the data display type, and you want to change the threshold display, you have to use the dropdown menu functionality.

The next two sections explain the chart styles in greater detail.

---

### 7.2.1 Chart Style: Lines, Vertical Bars, Horizontal Bars

Where it makes sense, charts can be displayed as lines, vertical bars, or horizontal bars. (Pie charts and the Bull's Eye charts would be obvious exceptions.) These choices are controlled by the Chart Style button. As described on page 129, this button acts as a toggle, with each press of the button cycling the chart style to the next choice. It also allows the user to select the chart style directly by means of the dropdown list (indicated by the down arrow at the right end of the button).

The appearance of the button changes with each push, showing a tiny chart in the selected style (line, vertical bar, horizontal bar).

**Figure 7.3: Current Variance Chart with Line Style**

When the vertical bars style is selected, the same chart will look like Figure 7.4:

**Figure 7.4: Current Variance Chart with Vertical Bars Style**

Finally, Figure 7.5 shows the same chart with Horizontal Bars selected:

**Figure 7.5: Current Variance Chart with Horizontal Bars Style**

---

### 7.2.2 Show Thresholds

A number of charts can be drawn with colored zones indicating how close a SPI, CPI, or TCPI value is to the nominal value of 1. These zones are colored red, yellow, and green, with red indicating the most problematic. The lower two items on the Chart Style menu turn on and off the display of the thresholds.

These threshold values can be set on a per-contract basis (see Section 16.9.4); for the sample MOH-2 contract appearing throughout this manual, red is set at −10 percent, yellow at −5 percent, and green at 10 percent. So if Show Thresholds is turned on, the region of the chart with SPI < 0.9 will be drawn with a red background, the region where SPI is between 0.9 and 0.95 will be colored yellow, and the region where SPI is between 0.95 and 1.1 will be colored green; similarly for CPI. What about the region where CPI or SPI is above 1.1? This will be colored blue as an indication that the numbers are perhaps too good to be true.

The thresholds can be shown on the following charts:

- Cumulative Variance
- Cumulative Variance %
- Current Variance
- Current Variance %
- SPI/CPI
- CPI/TCPI
- Bull's Eye
- Bull's Eye Bubble

**Figure 7.6: Current Variance % Chart with Show Thresholds Option On**

**Figure 7.7: Bull's Eye Chart with Show Thresholds Option On**

Later in this chapter there are also examples of Bull's Eye charts with the thresholds turned on.

The Options > Show Thresholds command brings up a dialog showing the colors and the numerical values for each color, as shown in Figure 7.8:

**Figure 7.8: Show Thresholds Dialog**

Section 16.9.4 describes how to set the threshold values for a contract.

---

## 7.3 Tool Tips

Hovering over any data point will generate a Tool Tip that displays the date and related performance data/metric for each item shown on the chart. Note that Figure 7.9 displays the CPI/TCPI chart with Tool Tips displayed for Dec 03.

**Figure 7.9: Chart Tool Tips**

---

## 7.4 Turn Data Plots On/Off

You can turn off selected data series by clicking on the name of the data item in the legend. Figure 7.10 shows the SPI/CPI chart with both of the SPI data series turned off. Note that they are grayed out in the legend.

**Figure 7.10: Turn On/Off Chart Data Plots**

---

## 7.5 Show/Hide Legend Data

For certain charts, numerical data for the current period can be shown in the legend. This is an option which is toggled on and off by the menu command Options > Show/Hide Legend Data.

**Figure 7.11: Chart with Legend Data not Displayed**

**Figure 7.12: Chart with Legend Data Displayed**

Note how the values for the current period (JAN04) are displayed in the legend at the bottom of the chart. (This figure also shows the popup you get when hovering over any data point. We did this to show that the numbers you see in the legend are the same as what you would see by hovering over the current period.)

---

## 7.6 Downloading and Printing Charts

To download a chart to a file on your computer or to print a chart, click the context menu icon in the upper-right corner of the chart. This icon is a little square with three horizontal bars; it and the context menu it activates is shown in Figure 7.13.

**Figure 7.13: Chart Context Menu**

To print the chart, click on "Print Chart" on the context menu. The standard print file dialog used by your browser/operating system combination will then appear; continue as you normally would to print a file from your browser.

The context menu also offers the choice of downloading the chart to a file in a number of graphics file formats. Currently, the options are Portable Document Format (PDF), Portable Network Graphics (PNG), or Scalable Vector Graphics (SVG). Once you choose a format, depending upon your browser, Empower will either directly download the chart to your download folder or open another browser window/tab where you can choose the download destination for the chart graphics file.

---

## 7.7 Zooming in Charts

There are two distinct methods of zooming for charts: by using the Zoom button on the Toolbar, and by using the mouse.

In the nature of the case, no zooming is available for the pie charts (Element of Cost).

1. **Zoom button**: For charts where the horizontal (x) axis displays the period, the Zoom button toggles between showing all periods and showing the last twelve periods only. For Bull's Eye and Bull's Eye Bubble charts, the Zoom button re-scales the axes to place the bull's eye rectangle in the center of the chart.

2. **Using the Mouse**: For any chart (except the pie charts) the user can zoom in both the horizontal and vertical (x and y) directions by selecting a rectangle with the mouse (sometimes called "rubber-banding"). The chart will be redrawn to the limits of the selected rectangle.

Each of these methods is described in more detail in the following sections.

The Gantt chart has its own set of Toolbar buttons to adjust the timescale. The use of these buttons will be described in Section 7.17.1.2.

---

### 7.7.1 Zooming with the Zoom Button

For charts where the independent variable is time (periods), the Zoom button on the main Toolbar will toggle between all periods or the last twelve periods in the open chart (assuming that there are at least twelve periods of data). When a chart is zoomed out to all periods, the Zoom button will change appearance. Historical trend charts default to the last twelve months. Charts that contain future period data (i.e., Cum Element Performance) default to the last three months of history and the next nine months of future data. If there are twelve or less periods of data, the Zoom button will not change the chart.

**Figure 7.14: Un-zoomed Chart**

**Figure 7.15: Zoomed Chart**

Note that zooming with the Zoom button in this situation means zooming out.

For the Bull's Eye and Bull's Eye Bubble charts, the Zoom button essentially centers the bull's eye rectangle. In Figure 7.16, note how the bull's eye rectangle is off to the right. This is because the default way to draw the chart is to draw it around the extremes of data.

**Figure 7.16: Bull's Eye Chart, Unzoomed**

However, some people prefer their bull's eye charts to have the bull's eye in the center, even if most or all of the data is on one side of the chart. Pressing the Zoom button will redraw the chart in this fashion, as shown in Figure 7.17.

**Figure 7.17: Bull's Eye Chart, Zoomed**

---

### 7.7.2 Zooming with the Mouse

In contrast to using the Zoom button, this method involves zooming in.

Selecting a region to zoom in on is just like the rubber banding rectangular selection process you may be familiar with from a graphics editor like Paint. To select a region to zoom in on, move the mouse to one corner of the desired rectangular region. Press and hold down the left mouse button, then drag the cursor to the diagonally opposite corner of the desired region. A shaded rectangle will appear, changing size as the mouse cursor moves. When the selected region is the size you want it, release the left mouse button, and the chart will be redrawn so that the selected region fills the chart area.

In Figure 7.18, we have chosen a region to zoom in on. We haven't let the mouse button up yet.

**Figure 7.18: Choosing a Region to Zoom**

Now we release the mouse button to accept the selected region, and the chart will look like Figure 7.19.

**Figure 7.19: Chart after Zooming**

(Note that the chart is sometimes not drawn with precisely the same limits as the region selected by the mouse. This is because charts are drawn with automatic axis scaling that chooses "nice" values for the axis extrema.)

As before, to return to the default chart display, press the Reset zoom button located in the upper right-hand corner of the chart.

Zooming a Bull's Eye chart works in exactly the same way. Figure 7.20 shows a Bull's Eye chart before zooming:

**Figure 7.20: Bull's Eye Chart Before Zooming**

Figure 7.21 shows a region to be zoomed-in on (that is, blown up) has been selected (note the shaded rectangle), but the mouse button has not been released yet.

**Figure 7.21: Bull's Eye Chart, Zoom Selected But Not Yet Applied**

And in Figure 7.22 we see the mouse button has been released and the zoom has been applied. Note that, as in the other examples, the Reset zoom button has appeared which allows the user quickly to restore the chart to its default limits.

**Figure 7.22: Bull's Eye Chart Zoomed**

---

## 7.8 Summary of Chart Features

All charts support download and print; other features are available as shown in the table below.

**Table 7.1: Summary of Chart Features**

| Chart | Zoom | Download | Color Threshold | Tooltip | Legend Data |
|-------|------|----------|-----------------|---------|------------|
| Cumulative Variance | ✓ | ✓ | ✓ | ✓ | ✓ |
| Cumulative Variance % | ✓ | ✓ | ✓ | ✓ | ✓ |
| Current Variance | ✓ | ✓ | ✓ | ✓ | ✓ |
| Current Variance % | ✓ | ✓ | ✓ | ✓ | ✓ |
| SPI/CPI | ✓ | ✓ | ✓ | ✓ | ✓ |
| CPI/TCPI | ✓ | ✓ | ✓ | ✓ | ✓ |
| EAC | ✓ | ✓ | ✓ | ✓ | — |
| EAC Realism | — | ✓ | ✓ | ✓ | — |
| Bull's Eye | — | ✓ | ✓ | ✓ | — |
| Bull's Eye Bubble | — | ✓ | ✓ | ✓ | — |
| Performance vs. Percent Complete | ✓ | ✓ | ✓ | ✓ | — |
| Cost Variance vs. Percent Complete | ✓ | ✓ | ✓ | — | — |
| Cost Per 1 Percent Complete | ✓ | ✓ | ✓ | — | — |
| Cost/Schedule Variance Trends | ✓ | ✓ | ✓ | ✓ | ✓ |
| Element of Cost: BAC by EOC | ✓ | — | — | — | — |
| Element of Cost: EAC by EOC | ✓ | — | — | — | — |
| Element of Cost: Cum CV by EOC | ✓ | ✓ | — | — | — |
| Element of Cost: Cur CV by EOC | ✓ | ✓ | — | — | — |
| Format 3 Baseline: Changes | ✓ | — | — | — | — |
| Format 3 Baseline: History | ✓ | ✓ | ✓ | — | — |
| Format 3 Baseline: Delta | ✓ | ✓ | ✓ | — | — |
| Format 4 Staffing: Staffing | ✓ | ✓ | ✓ | — | — |
| Format 4 Staffing: Staffing History | ✓ | ✓ | ✓ | — | — |
| Format 4 Staffing: Staffing Delta | ✓ | ✓ | ✓ | — | — |
| Format 4 Staffing: Staffing Detail | ✓ | — | — | — | — |
| Cumulative Staffing | ✓ | ✓ | ✓ | ✓ | — |
| Current Period Staffing | ✓ | ✓ | ✓ | ✓ | — |
| Budget Staffing Detail | ✓ | ✓ | — | — | — |
| Forecast Staffing Detail | ✓ | ✓ | — | — | — |
| Contract Performance | ✓ | ✓ | ✓ | — | — |
| MR/UB Trends | ✓ | ✓ | ✓ | ✓ | — |
| Cum Element Performance | ✓ | ✓ | ✓ | ✓ | — |
| Cur Element Performance | ✓ | ✓ | ✓ | ✓ | — |
| Execution Indexes | ✓ | ✓ | ✓ | ✓ | — |
| Total Float | ✓ | ✓ | ✓ | ✓ | — |
| Constraints | — | ✓ | — | — | — |
| Schedule Work-Off | ✓ | ✓ | — | — | — |
| Schedule DQI | ✓ | ✓ | ✓ | ✓ | — |
| Schedule DQI % | ✓ | ✓ | ✓ | ✓ | — |
| Baseline Realism Index | ✓ | ✓ | ✓ | ✓ | — |
| Workoff Burden | ✓ | ✓ | ✓ | ✓ | — |
| Forecast Realism Index | ✓ | ✓ | ✓ | ✓ | — |
| OTB SPA | ✓ | ✓ | ✓ | — | — |
| Total Contract Variance | ✓ | ✓ | ✓ | — | — |

---

## 7.9 Bull's Eye Chart

The Bull's Eye chart gives a view of the Cost Performance Index (CPI) and Schedule Performance Index (SPI) for a contract element from period to period, in a graphical display vaguely reminiscent of a dartboard. Figure 7.23 shows a Bull's Eye Chart for element 2300. Each period is plotted as a point with SPI and CPI as the coordinates. A box is drawn indicating the area where both SPI and CPI are within 10 percent of the nominal values of SPI = 1 and CPI = 1. This box gives a measure of whether key SPI and CPI metrics are within tolerance and gives the chart its name. The first point in the time sequence is shown as a downward-pointing triangle; the last is an upward-pointing triangle. The rest of the points are shown as dots.

**Figure 7.23: Bull's Eye Chart**

When the cursor hovers over a point, a tool tip appears, showing the name of the period and the numeric values of CPI and SPI at that period. Figure 7.24 shows such a tool tip. From this figure, one can see that element 2300 was outside the bull's eye for the first two periods, in the bull's eye for the next four, out again, then back in the bull's eye for the most recent three periods.

**Figure 7.24: Bull's Eye Chart with Date Tool Tip**

Note that the Zoom feature works with Bull's Eye charts. Simply use the mouse to indicate a rectangular region within the chart and the chart will be zoomed to that region.

If the user turns on the "Show Thresholds" menu option (see Section 7.2.2), the background of the chart will be colored red, yellow, and green to indicate the relative "goodness" at each period. So, for instance, the first point (APR 03), though it is outside the box, is in the green because SPI is exactly on track at 1, and CPI is better than on track, 1.143. (Unlike real darts, one prefers to miss high and to the right in EVM.) However, in May of 2003, this element was well in the red because the SPI was 0.773.

**Figure 7.25: Bull's Eye Chart with Thresholds Shown in Color**

---

## 7.10 Bull's Eye Bubble Chart

A bubble chart displays three dimensions of data. The first two variables are shown on the horizontal and vertical axes of the chart, where the bubble (circle) is drawn, while the third dimension is represented by the area of the bubble.

Empower's Bull's Eye Bubble Chart shows the SPI and CPI values for an element (and its children, if any) just as with the regular Bull's Eye Chart, with SPI on the horizontal axis and CPI on the vertical, with a rectangular box indicating the "target" area. Then it draws a bubble at the point with coordinates (SPI, CPI), with the area of the bubble indicating the EAC for the given element.

Figure 7.26 shows a chart for element 2000. Note that since element 2000 has three children (as you can verify in the Sort Window), three bubbles are drawn, while the parent element itself is not drawn. The relative sizes of the three bubbles gives you an immediate sense of how much each child element contributes to the EAC value of its parent. In this case, you can also see that all three children are within the target bull's eye, though one element is on the verge of dropping below the 90 percent threshold for CPI. (You can have Empower create a bubble chart of a lowest level element; it will show just the one bubble and won't be as interesting.)

**Figure 7.26: Bull's Eye Bubble Chart**

How do you know which bubble corresponds to which element? Hover the mouse over a bubble, and a tool tip will appear, as shown in Figure 7.27. This will show you the WBS number and name of the element, and the numerical values for SPI, CPI, and EAC. In addition, it will tell you how much this element contributes to its parent element's EAC, as a percentage. So in this example, Functional Integration (element 2300) makes up 36.2 percent of Project Management's (element 2000) EAC.

**Figure 7.27: Bull's Eye Chart with Tool Tip**

Note that the Zoom feature works with Bull's Eye Bubble charts.

The option to display thresholds in color also works with this chart, as shown in Figure 7.28.

**Figure 7.28: Bull's Eye Chart with Thresholds Shown in Color**

---

## 7.11 Cost/Schedule Variance Trends

An example of this chart is shown in Figure 7.29. A notable feature of this chart is the colored region marked as "10 % Threshold". This region shows 10% of BCWP at each period.

**Figure 7.29: Cost/Schedule Variance Trends**

---

## 7.12 Performance vs. Percent Complete Charts

The menu choice Performance vs. % Complete opens a submenu, as shown in Figure 7.30. This submenu offers charts of cumulative CPI against percent complete, where the CPI can be for the current period, or a 3- or 6-period average, as well as cumulative CV against percent complete.

**Figure 7.30: Performance vs. % Complete Submenu**

Figure 7.31 shows the CPI vs. percent complete chart for a 3-month average. Note how the chart title indicates how many periods the CPI is based on.

Something else to note about the figure is the period in the data popup. Normally, as time advances, the percent complete of a job increases (or at least stays the same), so that as you follow the points on the curve in these charts from left to right, time increases. However, if the BAC increases during a project, the percent complete can actually decrease as time increases. (More work may have been done, but the denominator — BAC — for the percent complete calculation has grown, possibly making the fraction smaller.) If the CPI for a point is not what you expect, checking the period in the popup will probably resolve your perplexity.

**Figure 7.31: Three Period Cumulative CPI vs. Percent Complete Chart**

---

## 7.13 Contract Performance Chart

The Contract Performance Chart (Figure 7.32) displays information about the performance of the contract as a whole, so it looks the same no matter which element is currently selected. (It is just like the Executive Summary Report in that respect.)

**Figure 7.32: Contract Performance Chart**

---

## 7.14 EQP Staffing Charts

A few charts based on EQP unit data are grouped under the submenu shown below:

**Figure 7.33: EQP Staffing Charts Sub-Menu**

---

### 7.14.1 Cumulative Staffing

This chart displays cumulative BCWS, BCWP, and ACWP data in EQP units over time.

**Figure 7.34: Cumulative Staffing**

---

### 7.14.2 Current Period Staffing

This chart displays current BCWS, BCWP, and ACWP data in EQP units over time.

**Figure 7.35: Current Staffing**

---

### 7.14.3 Budget Staffing Detail

This chart displays BCWS data in EQP units for the direct children of the selected element. For lowest level elements, the chart will display data for the selected element. For sum button elements, the chart displays data for any elements in the sort window. Note that there is a limit to the number of lines displayed in this chart; for performance reasons the chart will only plot data for up to 50 elements. Also notice that the tooltip will display a total for you when you hover over a period on the chart.

**Figure 7.36: Budget Staffing Detail**

---

### 7.14.4 Forecast Staffing Detail

This chart displays ACWP data in EQP units for the direct children of the selected element. The notes from the "Budget Staffing Detail" chart described in the previous section apply to this chart as well.

**Figure 7.37: Forecast Staffing Detail**

---

## 7.15 OTB Charts

A few charts that show OTB data are grouped together in the submenu shown below:

**Figure 7.38: OTB Charts Sub-Menu**

---

### 7.15.1 OTB Single Point Adjustment

This chart shows adjusted CV and SV values based on the cumulative CV and SV and the Reprogramming Cost of the selected element. At level one, the chart will also display adjusted MR values. The tooltip for this chart will display both adjusted and non-adjusted values for CV and SV. The chart also plots lines displaying when new OTBs begin and end when applicable.

**Figure 7.39: OTB Single Point Adjustment**

---

### 7.15.2 OTB Total Contract Variance

This chart shows adjusted CV, SV, and VAC values based on cumulative CV, SV, VAC and the Reprogramming Cost, Schedule and Budget values for the selected element.

**Figure 7.40: OTB Total Contract Variance**

---

## 7.16 Schedule Analysis Charts

Several charts for schedule analysis are grouped together in the submenu shown below:

**Figure 7.41: Schedule Analysis Charts Sub-Menu**

---

### 7.16.1 Schedule Execution Indexes

This chart shows the SPI, Baseline Execution Index (BEI), Current Execution Index (CEI), and Completion Index (CI) for the selected element.

**Figure 7.42: Schedule Execution Indexes**

---

### 7.16.2 Total Float

This chart shows the total float for the selected element.

**Figure 7.43: Total Float**

---

### 7.16.3 Constraints

This chart shows the number of constraints (MSON, MFON, etc.) attached to the selected element and all its child elements. Elements that don't have any constraints are shown in the chart as "ASAP".

**Figure 7.44: Constraints**

Here are the abbreviations used in the Constraints Chart for Microsoft Project:

| Abbr. | Constraint Type |
|-------|-----------------|
| ALAP | As Late As Possible |
| ASAP | As Soon As Possible |
| FNET | Finish No Earlier Than (finish on or after) |
| FNLT | Finish No Less Than (finish on or before) |
| MFON | Must Finish ON (mandatory finish) |
| MSON | Must Start ON (mandatory start) |
| SNET | Start No Earlier Than (start on or after) |
| SNLT | Start No Less Than (start on or before) |

These constraint abbreviations will be familiar to those familiar with Microsoft Project or the UN/CEFACT XML Schema for IPMR Format 6; Primavera P6 names constraints somewhat differently.

---

### 7.16.4 Schedule Work-Off

This chart displays counts of schedule finishes over the periods of the contract alongside ACWP and BCWS in EQP for each period. For future periods, the chart displays ETC in EQP for each future period. This chart also calculates the average task completion over the six periods up to time now, as well as the average over the six periods after time now.

**Figure 7.45: Schedule Work-Off**

---

### 7.16.5 Schedule Execution Metrics

This chart displays counts of schedule finishes over the periods of the contract, alongside the calculated current Baseline Realism Index (BRI) and percent of finishes for each period that are more than 30 days late.

**Figure 7.46: Schedule Execution Metrics**

---

### 7.16.6 Schedule DQI

This chart shows the number of tasks breaching one or more DQI metrics for the selected element and all its child elements.

**Figure 7.47: Schedule DQI**

---

### 7.16.7 Schedule DQI Percent

This chart shows the number of tasks that have breached one or more DQI metrics for an element and all its child elements, in terms of percent (tasks breaching a DQI metric divided by the total number of incomplete tasks for the element).

**Figure 7.48: Schedule DQI %**

---

### 7.16.8 Baseline Realism Index

This chart shows the six month average baseline realism index for the current selected element. The BRI On Plan Threshold value is 0.65, and the BRI Warning Threshold is 0.2.

**Figure 7.49: Baseline Realism Index**

---

### 7.16.9 Workoff Burden

This chart shows the six month average Workoff Burden for the current selected element. The Schedule Workoff Warning Threshold value is 0.8, and the Schedule Workoff On Plan Threshold is 0.32.

**Figure 7.50: Workoff Burden**

---

### 7.16.10 Forecast Realism Index

This chart shows the six month average forecast realism index for the current selected element. Note that the "Forecast Realism Index" is called "CEI" in the Columns download. The FRI threshold value is 0.67.

**Figure 7.51: Forecast Realism Index**

---

## 7.17 Gantt Chart

The Gantt chart is more complicated than the other charts in Empower, and allows more user interaction. Tasks are shown in a customizable table embedded in the chart; these tasks can be sorted and the information presented with each task can be customized by adding or deleting columns.

To sort rows, click the column header of the column you want to sort by. Arrows will appear in the column header, allowing you to sort in either ascending or descending order. Figure 7.52 shows the Gantt chart sorted by Name in ascending order.

**Figure 7.52: Gantt Chart sorted by Name**

To show or hide columns, right click a column header in the Gantt chart. Hovering over the "Show columns" option will show a checklist of all of the columns in the Gantt view. To change whether a column is displayed, click on the column, which will toggle the display on and off. See Figure 7.53.

**Figure 7.53: Gantt Chart with Table dropdown List**

Figure 7.54 shows a checklist of all of the columns shown in the "Empower Gantt" view.

**Figure 7.54: Gantt Chart, Show or Hide Columns**

The Gantt chart will display tasks for the selected element and all its child elements. If you add the "Hier" column to the Gantt table display, you'll see a value that will identify which element the task is associated with. For example, in the MOH-2 sample contract, element 3000 has 97 associated tasks. (You can see this number by adding the column "Linked Tasks" to the Sort Window, using the Views > Add Column(s) command). None of these tasks are actually attached to element 3000 itself; they are all attached to 3000's child elements. For instance, element 3200 has 49 tasks. Element 3200's Hier value is 122 (see the Hier column at the far left of the Sort Window). Glancing at the Gantt Chart's table, you'll see 49 tasks with the value 122 in the Hier column. Scrolling down in this table, you'll eventually come to tasks whose Hier value is 124. Going back to the Sort Window, you'll find that value is associated with Element 3400. If you select element 3400 in the Sort Window, you'll see just the 25 tasks that are associated with that element, and all the Hier values will be 124.

---

### 7.17.1 Gantt Toolbar

When the Gantt chart is open, the Gantt Toolbar will display at the right end of the main Toolbar.

**Figure 7.55: Gantt Toolbar**

Figure 7.55 displays the Gantt Toolbar buttons. The Gantt Toolbar is only visible when the Gantt chart is displayed. Note that the Filter and Scale buttons have dropdown lists for quick access to the various options.

---

#### 7.17.1.1 Gantt Filter Button

The Gantt Filter button is used to filter the schedule activities based upon the Red, Yellow, Green and White criteria built into Empower. (See Section 16.9 to learn how to change these criteria.) You can select the Filter button to toggle between the last color selected and "None," or use the dropdown list to jump directly to your selection. Figure 7.56 shows the filter choices available in the dropdown list.

**Figure 7.56: Gantt Filter Dropdown Choices**

The Gantt Filter button will display the active Gantt Filter color. The Status Bar will also provide an indicator as to the active Gantt Filter and the number of filtered tasks versus total Tasks. In Figure 7.57, a Status Bar is displayed with a red box added to the figure to draw attention to the schedule task-related information. (The red box does not appear in Empower.) There are 51 tasks associated with account 3200. The Yellow [Y] filter is applied. The Yellow filter returned 5 of the 51 Tasks.

**Figure 7.57: Status Bar with Gantt chart information**

---

#### 7.17.1.2 Gantt Scale Button

The Gantt Scale button changes the time-scale in the Gantt chart between quarters, months, or weeks. Clicking on the button will toggle through the various options or you can use the dropdown list to jump directly to your selection. Figure 7.58 shows the dropdown list.

**Figure 7.58: Gantt Scale Drop Down Menu**

---

#### 7.17.1.3 Gantt Mode Button

The Gantt Mode button changes the mode used for determining which tasks are displayed in the Gantt Chart. The options available will depend on whether you are using this option in cost mode or task mode. (For more information on "Task Mode" see section 5.8)

In "Cost Mode," the options are:

**Figure 7.59: Gantt Mode Drop Down Menu**

In "Task Mode," the options are:

**Figure 7.60: Gantt Mode Drop Down Menu: Task Mode**

To summarize the options:

- **Relationships**: In "Task Mode" display predecessors and successors of the selected task. In "Cost Mode" display tasks linked to the selected element along with their predecessors and successors.
- **Siblings**: In "Task Mode" display all tasks tied to the same element as the selected task. In "Cost Mode" display tasks linked to the selected element.
- **Trace Back**: Display tasks prior to the selected task.
- **Trace Forward**: Display tasks after the selected task.

The status bar will indicate which selection is active: REL for Relationships, SIB for Siblings, TRB for Trace Back, and TRF for Trace Forward.

**Figure 7.61: Status Bar with Relationships Selected**

Similarly, the text of this toolbar button will also update depending on which selection is active.

---

#### 7.17.1.4 Gantt Links Button

The Gantt Links button turns on or off the display of logical connections between activities. Note that the relationships between tasks will not display unless both tasks are shown in the view. This is consistent with how Microsoft Project displays relationships. (Primavera P6 does this somewhat differently.)

Figure 7.62 shows the activity Tool Tip that displays when you hover over an activity bar in the Gantt chart. Note that the yellow bar represents the baseline, the blue bar the current plan for non-critical tasks, the red bar the current plan for critical tasks, and the shaded center of the blue/red bars shows progress. Task relationships can be toggled on or off via the Gantt Toolbar Links button. Relationships are not displayed unless both activities are visible in the chart.

**Figure 7.62: Activity Bar Pop-up**

---

#### 7.17.1.5 Gantt Critical Tasks Filter

Clicking the Gantt Critical button will filter the Gantt chart to tasks for which the "Critical" flag is set to "T". The status bar will change to reflect this. For instance, the figure below shows the status bar when element 3200 of contract MOH-2 is selected. This element has 50 tasks, and all 50 are displayed.

**Figure 7.63: Gantt Toolbar Showing All Tasks**

Clicking the Critical button limits the number of tasks shown, and the status bar, shown below, reflects this. Only 32 of the 50 tasks are marked "Critical" ("32/50"), and the "[C]" indicates that the Critical button has been toggled on. (The button's background will also change appearance depending on your browser when it is toggled on.)

**Figure 7.64: Gantt Toolbar Showing Only Critical Tasks**

---

#### 7.17.1.6 Gantt Milestone Filter

Clicking the Gantt Milestone button will filter the Gantt chart to show just milestones. The status bar will change to reflect this; note that only 4 of the 50 tasks are shown, and the "[M]" indicates that the Milestone button has been toggled on. (The button's background will also change appearance depending on your browser when it is toggled on.)

**Figure 7.65: Gantt Toolbar Showing Only Milestones**

---

#### 7.17.1.7 Gantt Detail Button

Clicking the Gantt Detail button will filter the Gantt chart so that it does not show summary level tasks. The status bar will change to reflect this; note that only 496 of the 691 tasks are shown, and the "[D]" indicates that the Detail button has been toggled on. (The button's background will also change appearance depending on your browser when it is toggled on.)

**Figure 7.66: Gantt Toolbar Showing Only non-summary level tasks**
