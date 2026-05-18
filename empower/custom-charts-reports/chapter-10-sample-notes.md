# Chapter 10: Sample Notes

*From TN-CustomChartsReports*

---

## Overview

This chapter describes several example reports and charts that demonstrate key patterns and best practices for custom report development.

## Key Examples

### Banded EOC Report

The Banded EOC report is an example using multiple queries. The first query gets EOC units, the second gets Element information, the third gets the associated EV data. Lookup tables are built in memory in the Javascript code to tie everything together.

### BAC by CAM Report

The BAC by CAM report is intended to be reused – results from any query can be presented in tabular form by modifying the args object alone; the JavaScript should work without change.

### Cross-Contract Sample Report

The Cross-Contract Sample report was created in just this way. It illustrates some of the subtleties of cross-contract reports and provides a good template for experimenting with formatting numbers and dates. It also shows what happens to a delete query (in a word, nothing), though you'll need to fiddle to see this.

For best results, at least one contract in your database should have different `Contract.DateFmt`, `ContrUnit.DisplayScale`, and `ContrUnit.DisplayDecimal` values than the rest.

### Chart Examples

The BAC by CAM chart and Target Price vs. Forecasts are examples of pie and line charts, respectively.

Both make a call to `scale_chart_data()`, a function defined in `chrp-min.js` that scales data the way built-in charts do. The interested user can view this file by clicking the link created to it in JSFiddle. A JavaScript beautifier (e.g., [jsbeautifier.org](http://jsbeautifier.org)) will help.

Of course, any function defined in `chrp-min.js` is available for use in user-defined custom charts and reports.

## SQL Conventions

### Table Names and Capitalization

When table names are required, the SQL in the samples follow these conventions:

**Preferred approach** (full table names with matching Empower schema capitalization):
```sql
SELECT Element.ElemID, Bac
FROM EarnedValue
INNER JOIN Element ON Element.ElemID = EarnedValue.ElemID
WHERE Element.ElemID = ce_id
```

**Alternative approaches to avoid:**

Using aliases and `USING` construct:
```sql
SELECT e.ElemID, Bac
FROM EarnedValue ev
INNER JOIN Element e ON e.ElemID = ev.ElemID
WHERE e.ElemID = ce_id
```

Using `USING` clause without aliases:
```sql
SELECT ElemID, Bac
FROM EarnedValue
INNER JOIN Element USING (ElemID)
WHERE ElemID = ce_id
```

### Rationale for Conventions

- **Avoid `USING` construct**: SQL Server does not support it
- **Match schema capitalization**: Prevents errors in SQL Server databases created with case-sensitive collation
- **Use full table names**: Allows SQL from the Column table to be inserted without change

## Best Practices Summary

When writing custom charts and reports:

1. Use full table names with proper capitalization from the Empower schema
2. Avoid SQL Server unsupported constructs like `USING`
3. Use explicit `INNER JOIN ... ON` syntax instead of aliases and `USING`
4. This ensures compatibility across different database configurations and allows reuse of SQL fragments
