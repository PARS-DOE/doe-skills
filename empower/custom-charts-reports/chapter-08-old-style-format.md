# Chapter 8: Old-Style Format

*From TN-CustomChartsReports*

---

## Overview

If your local policy prevents you from running `eval` in your browser, new-style custom charts and reports will not display properly in Empower. In this situation, you can instead use old-style custom charts and reports.

The disadvantage of using the old-style format is that you will need to have access to the Empower server in order to make changes to the custom chart or report.

The old-style format uses two pieces:
1. A text document that will be imported into Empower
2. A JavaScript function that will be added to a `js` file on the Empower server

## 8.1 Import File

You can create the text file to import into Empower using the text editor of your choosing. This file should contain valid JSON and should be similar to the `args` section of a new-style chart or report. This file should have any custom SQL that will be used, the type of user item, the name of the function that will contain the JavaScript for this user item, etc.

### Example: Recalc Status Report

Here is an import file for the "Recalc Status" custom report:

```json
{
  "type": "report",
  "title": "Recalc Status",
  "func": "rp_recalc_status",
  "L1": "1",
  "header": "This report displays any running recalcs in the current data source. Click on any element to update status.",
  "sql": [
    "select ContrName, RecalcLock, UserName from Userr inner join Contract on Contract.RecalcID = Userr.UserID where RecalcLock is not null"
  ],
  "cols": ["CONTRACT", "LAUNCHED", "BY"],
  "align": ["l", "l", "l"]
}
```

### Key Points

- The `"func"` entry indicates the name of the JavaScript function that will be used for this custom report.
- This file does **not** begin with `args =` and does **not** end with a semicolon.

## 8.2 JavaScript Function

For this style of chart or report, you will need to add a JavaScript function for your chart or report to the `cust.js` file on the Empower server. This file can be found in the `empower/www` directory.

The JavaScript function should have the same name as the `"func"` entry in your import file. The `cust.js` file begins with this line:

```javascript
/* jshint -W098, -W003, bitwise: false */
```

You can add your function below this line. You can add multiple functions to this file for different user items.

### Example: Recalc Status Function

Here is the function for the "Recalc Status" report:

```javascript
function rp_recalc_status(args) {
  "use strict";

  var em = [], extra = args.extra,
      td_h = "rpt ral rcgr1 rtb",
      td_c = "rpt ra",
      arr = [],
      s, i, ilen, j, jlen, vals, val;

  em.push('<div class="rpt">');
  em.push('<div class="rtitle">');

  s = args.title + '<br/>' + 'Data Source: ' + extra.dsn;
  em.push(s);
  em.push('</div>');

  s = args.header;
  em.push('<br/>');
  em.push(s);
  em.push('<p>');

  em.push('<table class="rpt">');
  em.push('<tr>');

  for (i = 0, ilen = args.cols ? args.cols.length : 0; i < ilen; i++) {
    s = args.cols[i];
    em.push('<td class="' + td_h + '">' + s + '</td>');
  }

  em.push('</tr>');

  arr = args.sql[0];

  for (i = 0, ilen = arr.length; i < ilen; i++) {
    em.push('<tr>');
    vals = arr[i];

    if (args.sync) {
      vals.shift();
    }

    for (j = 0, jlen = vals.length; j < jlen; j++) {
      val = vals[j];
      s = args.align ? args.align[j] : 'l';
      em.push('<td class="' + td_c + s + '">' + val + '</td>');
    }

    em.push('</tr>');
  }

  em.push('</table>');
  em.push('</div>');

  return em.join('');
}
```

### Key Points

Notice that we have defined the `"extra"` variable with `extra = args.extra`. If you want to use items from the `extra` variable, such as a preformatted title, you will need to add this to your JavaScript code for your chart or report.
