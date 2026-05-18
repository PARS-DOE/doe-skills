# Chapter 1: Introduction

*From TN-CustomChartsReports*

---

## Overview

This document describes how to write "new-style" custom charts and reports for Empower. These new-style custom charts and reports are handled differently beginning with Empower version 3.3.9.39, so even if you are experienced at writing custom reports for previous versions of Empower, you will find this document helpful. (Empower continues to support the older style of custom reports.)

Custom charts and reports written according to the instructions in this document will appear in Empower's report or chart pane. That is, they won't be external charts and reports, though they can be opened in a separate browser window, like other reports and charts, if the user presses a special key when opening the report.¹

Such reports can also be imported into other applications that can render HTML, such as Word and Excel, via Empower's Export Report HTML command. Such an import of old-style reports might not import successfully into Word or Excel since they often contain JavaScript which the displaying browser must execute to complete the report; but applications such as Word and Excel can't execute JavaScript. Another problem with importing old-style custom reports into Excel and Word is that they cannot import style sheets or handle multiple styles (e.g., the `<td class="rpt rar">...</td>` construct). With reports written according to this document, the report is pure HTML when exported with "Export Report HTML."

## Key Changes from Previous Versions

A few words for those who have written custom reports for earlier versions of Empower:

### 1. The `cust.js` File

The file `cust.js` is not used by new-style reports. Previously, to write a custom report that would appear in the Report Pane, you had to put the JavaScript portion of your report in the `cust.js` file on the Empower server. This meant you couldn't deploy such a report without access to the server, which was typically limited to the IT staff.

In the new way of writing custom reports, everything (the code that specifies the data and the JavaScript that generates the formatted report) resides in the same text file, which can be imported by any user (like the Legacy Reports of old). The file `cust.js` is still present and used if necessary by older reports, though it is deprecated.

### 2. The `cust.css` File

Likewise, the file `cust.css` is not used by new-style reports. This file often contains CSS style definitions used by authors of older custom reports. Now we provide a standard set of consistent styles, which should meet all, or nearly all, of your styling needs.

By using these standard styles, you ensure that your reports have a consistent look and feel with the rest of Empower. Like `cust.js`, `cust.css` still exists and is used if necessary by older reports, though it is deprecated.

## Technical Requirements

To write custom reports, you will need to be familiar with:
- **JavaScript** - The programming language for report logic
- **JSON** - Javascript Object Notation for data structure
- **HTML** - HyperText Markup Language for content
- **CSS styles** - For formatting and appearance

Your report code will be written in JavaScript with JSON; this code will generate the actual report as a bunch of HTML with CSS styles.

## Custom Charts

Custom charts can be generated in a manner analogous to "new-style" custom reports. Where custom reports define an anonymous function that returns HTML in the format expected by Empower's Report pane, custom charts define an anonymous function that returns a JSON object in the format expected by Empower's Chart pane (e.g., the BAC by CAM chart and Target Price vs. Forecast chart).

## File Format and Storage

An Empower custom chart or report is a plain text file; you can edit it with the text editor of your choice. If you use Word for your editor, be sure to save it as a plain text file, and not with any formatting. Chart and report files end by convention with the `.txt` extension, though this is not necessary.

## Importing and Exporting

To import or export a new-style custom chart or report, you simply use the:
- `File > Import User Items` command (to import custom reports)
- `File > Export User Items` command (to export custom reports)

As already mentioned, you don't need to put a separate JavaScript file on the server, since the new style of writing reports includes everything in one file.

---

¹ Control, Shift, or Alt/Option (Alt on Windows, Option on Macs).
