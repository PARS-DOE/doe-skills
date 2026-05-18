# Chapter 2: New-Style Format

*From TN-CustomChartsReports*

---

## 2.1 Custom Report Format

Writing a custom report for Empower can be broken down into two tasks:

1. Specifying the data you want to show in your report
2. Specifying how you want your report to look (the layout of the report)

These tasks will be discussed in detail in the following chapters.

### Skeleton Custom Report File

```javascript
var args = {
  "title": "BAC Delta",
  // ... data and codes to get data go here ...
};

(function () {
  // ... JavaScript statements to generate your report as a HTML string ...
})();
```

---

## 2.2 Custom Chart Format

A "new-style" custom chart uses an anonymous JavaScript function to create and return a JSON object in the format expected by Empower's Chart pane. That format, in turn, is defined by the Highcharts charting tool that Empower uses. See https://highcharts.com/demo for many examples.

### Skeleton Custom Chart File

```javascript
var args = {
  "type": "chart",
  "title": "Target Price vs. Forecasts",
  // ... data and codes to get data go here ...
};

(function () {
  // ... JavaScript statements to generate the "options" object,
  // which will be passed to the Empower charting tool ...
})();
```

### Understanding the Structure

The first section, beginning `var args = {`, defines a JSON structure that should be familiar from writing custom reports. The first entry, `"type":"chart"`, identifies this as a chart. (If omitted, the object is treated as a report.)

**Note:** Notice the consistent use of double-quotes around text elements in the JSON. This is required for charts and reports containing user-defined SQL (due to an intermediate JSON-decode) and should be adopted as a best-practice for all future charts and reports.

The remainder of the JSON uses placeholder syntax to gather data for the chart. The second section, the anonymous JavaScript function, takes the data and populates and returns the options object. The details of the options object are defined by Highcharts according to chart type, and are best learned by experimenting with their demos.

### Sample: BAC by CAM Chart

Consider the "BAC by CAM" sample chart. (Download with File > Export User Items.)

The `"type":"chart"` entry identifies this as a chart. The `"L1"` entry is used as a flag to select (or not) a title that doesn't change unless a new dataset is selected. In the function, notice the different character of the options object returned, reflecting differences between line and pie charts.

**Windows-Specific Note:** For sites hosting Empower on a Windows machine, you may encounter a Windows-specific bug with the JSON::XS Perl module related to encoding true/false values. The workaround for this issue is to use `"1"` instead of `"true"` for the `"L1"` entry.

Example:
```javascript
"L1": "1"
```

### Excerpt of "BAC by CAM" Chart

```javascript
var args = {
  "type": "chart",
  "title": "BAC by CAM",
  "L1": "1",
  // ... data configuration ...
};

(function () {
  options = {
    "series": [{
      "data": [],
      "type": "pie"
    }],
    "tooltip": false,
    "plotOptions": {
      "pie": {
        "allowPointSelect": true,
        "dataLabels": {
          "format": "{ point.name }: {point.percentage:.1f}% = {point.s}",
          "enabled": true
        },
        "cursor": "pointer"
      },
      "series": {
        "animation": false
      }
    }
    // ... additional configuration ...
  };

  return options;
})();
```
