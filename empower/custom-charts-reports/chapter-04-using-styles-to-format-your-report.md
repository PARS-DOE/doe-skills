# Chapter 4: Using Styles to Format Your Report

*From TN-CustomChartsReports*

---

## 4.1 Standard Styles

The file containing all available styles is `report.css`. The contents of this file are listed in sections here for your convenience.

### 4.1.1 Text alignment options

```css
.ral {
  text-align: left;
}

.rar {
  text-align: right;
}

.rac {
  text-align: center;
}
```

### 4.1.2 Background colors

```css
.rcr0 {
  background-color: #ffdddd;
}

.rcr1 {
  background-color: red;
}

.rcy0 {
  background-color: #ffffdd;
}

.rcy1 {
  background-color: yellow;
}

.rcg0 {
  background-color: #ddffdd;
}

.rcb0 {
  background-color: #edf3fd;
}

.rcgrw {
  background-color: white;
}

.rcgr0 {
  background-color: #f5f5f5;
}

.rcgr1 {
  background-color: #ebebeb;
}

.rcgr2 {
  background-color: #dfdfdf;
}

.rcgr3 {
  background-color: #c0c0c0;
}
```

### 4.1.3 Widths

```css
.rw75 {
  width: 75%;
}

.rw60 {
  width: 60%;
}

.rw50 {
  width: 50%;
}

.rw40 {
  width: 40%;
}

.rw30 {
  width: 30%;
}

.rw25 {
  width: 25%;
}

.rw20 {
  width: 20%;
}

.rw15 {
  width: 15%;
}

.rw10 {
  width: 10%;
}

.rw5 {
  width: 5%;
  white-space: nowrap;
}
```

### 4.1.4 Other text options

```css
.rtw1 {
  color: white;
}

.rtb {
  font-weight: bold;
}

.rnw {
  white-space: nowrap;
}
```

### 4.1.5 Standard table and div style groups

```css
div.rpt {
  font-family: sans-serif;
  font-size: 11pt;
  margin: 10px;
}

div.rtitle {
  font-size: 12pt;
  font-weight: bold;
  text-align: center;
  margin-top: 20px;
}

table.rpt {
  font-size: 10pt;
  width: 100%;
  border-collapse: collapse;
}

th.rpt {
  border: 1px solid lightgray;
  padding: 5px;
  background-color: #eee;
}

td.rpt {
  border: 1px solid lightgray;
  padding: 5px;
}

td.sep {
  border: 0px;
  padding: 4px;
}

table.tmpl {
  width: 100%;
  border: 1px solid silver;
  border-collapse: collapse;
}

td.tmpl {
  border: 1px solid silver;
  border-collapse: collapse;
  padding: 4px;
}

body {
  font-family: sans-serif;
  font-size: 11pt;
}

td.tb, span.tb, th.tb {
  font-weight: bold;
}

td.tr {
  text-align: left;
}

td.tc {
  text-align: left;
}
```

### 4.1.6 Style groups for sticky headers and columns

```css
.freeze-row {
  position: -webkit-sticky;
  position: sticky;
  z-index: 8;
  border: 0.5px solid lightgray;
}

.tiny-row {
  top: 42px;
}

.short-row {
  top: 62px;
}

.freeze-row2 {
  top: 63px;
}

.tall-row {
  top: 82px;
}

.extra-tall-row {
  top: 122px;
}

.freeze-topcol {
  position: -webkit-sticky;
  position: sticky;
  left: 0px;
  z-index: 9;
}

.freeze-col {
  position: -webkit-sticky;
  position: sticky;
  left: 0px;
  z-index: 2;
}

.titlefreeze {
  position: -webkit-sticky;
  position: sticky;
  top: 0;
  z-index: 9;
  border: 0.5px solid white;
  padding: 1px;
}

.tiny-title {
  height: 40px;
  max-height: 40px;
}

.short-title {
  height: 60px;
  max-height: 60px;
}

.tall-title {
  height: 80px;
  max-height: 80px;
}

.extra-tall-title {
  height: 120px;
  max-height: 120px;
}

table.freeze {
  font-size: 10pt;
  width: 100%;
  border-collapse: separate;
  border-spacing: 0px;
}

td.rpt-fr {
  border: 0.5px solid lightgray;
  padding: 5px;
}

th.rpt-fr {
  border: 0.5px solid lightgray;
  padding: 5px;
}

th.rtitle {
  font-size: 12pt;
  font-weight: bold;
  text-align: center;
  margin-top: 20px;
}

p.subtitle {
  font-size: 10pt;
  text-align: center;
  font-weight: normal;
}
```

Styles with a leading period only do one thing, and are meant to be concatenated with other styles.

Styles with "freeze" included in the name are designed for use with sticky titles and table headers. See our sample reports for examples of how to use these styles. In particular, note that "sticky" rows or columns must have background colors and either "top" or "left" values in order to display correctly.

## 4.2 Combining Styles

You can combine styles to get the effect you want. For example, in the BAC Delta report (described in the next section), we want a table header row with 10 point text in boldface, a light gray background, and cell borders 1 pixel wide in solid light gray. We add this line of HTML to our report (line 58 in the listing in the next section):

```html
<td class="rpt ral rcgr1 rbt">WBS</td>
```

There are several things to note about this line:

- Empower requires the class attribute to be the first attribute in the tag, and the class style must be enclosed in double quotes.
- You may add additional attributes after the class attribute if you like, and use single or double quotes, or no quotes at all, for the attribute values (e.g., `colspan='2'`, `colspan="2"`, or `colspan=2`).
- You can put multiple styles in the class attribute, separated by spaces.
- Sharp-eyed readers will have noted that we are using the `td` HTML tag for table header cells instead of the usual `th` tag. This is because Excel doesn't support the `th` tag, and we want to be able to export our report's HTML into Excel and keep the formatting. You can get the standard `th` look in Excel with `td class="rpt rac rcgr1 rtb"`, meaning light-gray border with a 5 pixel margin, centered text in boldface, and a silver background.
- For this cell, we are right aligning the text (ral).
