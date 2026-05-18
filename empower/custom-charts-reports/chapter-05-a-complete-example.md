# Chapter 5: A Complete Example

*From TN-CustomChartsReports*

---

## 5.1 Getting the Data

Here we present a complete annotated example using the BAC Delta report. We want the report to look like Figure 5.1 (BAC Delta Report - partial).

The first step is declaring a JavaScript variable named `args`, which is set to a JSON string:

```javascript
var args = {
  'title': 'BAC Delta',
  'cd': [
    (|Meta|BeginLoop|ord|PerOrd|0|5|)
    '(|EndDate|(-ord)|)',
    (|Meta|EndLoop|ord|)
  ],
  'ce': [
    (|Meta|BeginLoop|ce|SyncSortWnd|)
    {
      'wbs': '(|WbsNum|$ce$|)',
      'lvl': '(|ElemLevel|$ce$|)',
      'll': '(|Lowest|$ce$|)',
      'desc': '(|ElemDesc|$ce$|)',
      'delta': [
        (|Meta|BeginLoop|ord|PerOrd|0|5|)
        (|BacDelta|$ce$|(-ord)|[n5]|),
        (|Meta|EndLoop|ord|)
      ]
    },
    (|Meta|EndLoop|ce|)
  ]
};
```

You can name this variable anything you want, though `args` is customary.

In the JSON string, the `title` key is set to "BAC Delta", which we will use later as the report title.

The next two keys, `cd` and `ce`, are more interesting—they demonstrate how to specify the data you want from Empower's database for use in the report.

### The `cd` Key (Period Data)

The `cd` key represents the period ID (Empower's internal variable). However, there is no relationship between the key name `cd` and Empower's internal variable—we could have named it anything (e.g., `periods` or `fred`).

The placeholder for data assigned to the `cd` key uses a loop to get the `EndDate` for the current period and the previous five periods, as the `ord` value ranges from 0 to 5. Note that Empower uses `(-ord)` to identify the period:
- `(-0)` = current period
- `(-1)` = one period before the current period
- And so on...

When Empower replaces the placeholder with actual data, the first part of the `args` variable will look like this:

```javascript
var args = {
  'title': 'BAC Delta',
  'cd': ['JAN 17', 'DEC 16', 'NOV 16', 'OCT 16', 'SEP 16', 'AUG 16'],
  ...
}
```

Note that the loop construct in the report file has been replaced by the specified data values from the database. The value associated with the `cd` key is an array of period end dates, formatted as short month names and short years.

### The `ce` Key (Element Data)

Now let's look at the code to get the rest of the data:

```javascript
'ce': [
  (|Meta|BeginLoop|ce|SyncSortWnd|)
  {
    'wbs': '(|WbsNum|$ce$|)',
    'lvl': '(|ElemLevel|$ce$|)',
    'll': '(|Lowest|$ce$|)',
    'desc': '(|ElemDesc|$ce$|)',
    'delta': [
      (|Meta|BeginLoop|ord|PerOrd|0|5|)
      (|BacDelta|$ce$|(-ord)|[n5]|),
      (|Meta|EndLoop|ord|)
    ]
  },
  (|Meta|EndLoop|ce|)
]
```

The data associated with the `ce` key represents Empower's internal name for the element ID selected in the sort window. We have two nested loops here:

1. **Outer loop**: Empower loops through all elements in the Sort Window (`SyncSortWnd` token), with `ce` as the loop variable. The `$` token specifies the element ID.
2. **Inner loop**: After gathering WbsNum, ElemLevel, and so on, Empower runs through the inner loop, retrieving the BacDelta for six periods, beginning with the current period and working backwards.

Below is a partial example of the data Empower returns for this placeholder:

```javascript
var args = {
  // ...
  'ce': [{
    'wbs': '1000',
    'lvl': '1',
    'll': ' ',
    'desc': 'MOH-2',
    'delta': [719.80000, 2274.40000, 597.00000, 0.00000, 0.00000, 0.00000]
  }, {
    'wbs': '2000',
    'lvl': '2',
    'll': ' ',
    'desc': 'PROJ MANAGEMENT',
    'delta': [47.40000, 85.20000, -344.00000, 0.00000, 0.00000, 0.00000]
  },
  // ...
]
```

Note how the `wbs`, `lvl`, `ll`, and `desc` keys are assigned the values we would expect for the first two elements in the Sort Window. Note also how the `delta` key was assigned an array of BacDelta values for the last six periods.

---

## 5.2 Laying Out the Report

Now let's turn our attention to laying out the data for our report. We do this with a JavaScript function which, for all its apparent complexity, just returns a string containing your report in HTML:

```javascript
(function () {
  'use strict';

  var em = [],
      ce = args.ce,
      cd = args.cd,
      ndates = cd.length,
      decpl = extra.scale.dd,
      stxt = extra.scale.text,
      i, j, len, n, r, s, d, o;
```

Here we declare the function and the variables we'll use:

- **`em`**: An array of strings; we build our report by adding bits of HTML as elements of this array. (The variable name is short for "emitter.") At the end of this function, we join all elements of the array into one long string and return it. Empower renders this HTML string in its Report Pane to display your report.
- **`args`**: Our function has access to the `args` variable defined in the first part of our report file.

### Building the Report Header

```javascript
em.push('<div class="rpt">');
em.push('<div class="rtitle">');
s = extra.title;
n = s.indexOf(' [');
em.push(s.substr(0, n));
em.push('<br>');
s = 'BAC Delta';
if (stxt.length) {
  s += (' (' + stxt + ')');
}
em.push(s + '<p>');
em.push('</div>');
```

These lines begin the HTML of the report with `<div class="rpt">`. This sets styles that apply to the whole report (unless overridden later): sans-serif font family, 11 pt font, and a 10-pixel margin.

The `<div class="rtitle">` gives us a 12-point bold font for the report title with centered text and a 20-pixel margin at the top.

### Checking for Data

```javascript
while (cd[ndates - 1] === '&nbsp;') {
  --ndates;
}

if (ndates === 0) {
  em.push('<p>No data.');
  em.push('</div>');
  return em.join('');
}
```

Here we skip through blanks in the array of period end dates. We've asked for six periods; if there aren't that many periods in our dataset, there will be one or more blanks at the beginning of the array. If after removing blanks there are no dates left, we return "No data." and we're done.

### Building the Table Header

```javascript
em.push('<table class="rpt">');
em.push('<tr>');
em.push('<td class="rpt ral rcgr1 rtb">WBS</td>');
em.push('<td class="rpt ral rcgr1 rtb">DESCRIPTION</td>');
em.push('<td class="rpt rac rcgr1 rtb">LL</td>');
em.push('<td class="rpt rar rcgr1 rtb">LVL</td>');

for (j = ndates; j > 0; j--) {
  em.push('<td class="rpt rar rcgr1 rtb">' +
    cd[j - 1] + '</td>');
}

em.push('</tr>');
```

Our report is in tabular form, so we emit the HTML to set up a table and its headings. We then loop through the array of period end dates (`cd`) and put them in the next row of the table.

The styles used are:
- **`rpt`**: Basic table style
- **`rcgr1`**: Light gray background
- **`rtb`**: 1-pixel solid light gray cell borders (the "collapse" value means borders of adjacent cells are collapsed to single-border width)

We align the column headings differently:
- **`ral`** (left align) for WBS and DESCRIPTION
- **`rac`** (centered) for the lowest level indicator LL
- **`rar`** (right align) for LVL value and period end date

### Filling Out the Table Rows

```javascript
for (i = 0, len = ce.length; i < len; i++) {
  em.push('<tr>');
  o = ce[i];
  em.push('<td class="rpt">' + o.wbs + '</td>');
  em.push('<td class="rpt">' + o.desc + '</td>');
  em.push('<td class="rpt rac">' + o.ll + '</td>');
  em.push('<td class="rpt rar">' + o.lvl + '</td>');

  d = o.delta;
  for (j = ndates; j > 0; j--) {
    n = d[j - 1];
    r = n === null ? '' : n < 0 ? 'rcr0 ' :
        n > 0 ? 'rcg0 ' : '';
    s = n !== null ? dtostr(n, decpl) :
        '&nbsp;';
    em.push('<td class="rpt rar ' + r +
      '">' + s + '</td>');
  }

  em.push('</tr>');
}

em.push('</table>');
em.push('</div>');

return em.join('');
})()
```

In this section, we fill out our table with the data, one row per trip through the loop. Every row begins with the WBS, description, lowest level flag, and the level. Then come the BAC delta values for each period, so we have an inner loop over the number of dates.

The interesting part is the color coding based on value:
- **White background**: No value (null)
- **Red (`rcr0`)**: Negative value
- **Green (`rcg0`)**: Positive value

We set the variable `r` to the appropriate color style. We also format our numerical values with the function `dtostr`, specifying the number of decimal places (`decpl`), which we obtained from `extra.scale.dd`.

Finally, we join all the elements of the `em` array into one string and return it.
