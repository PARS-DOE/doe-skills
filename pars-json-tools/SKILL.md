---
name: pars-json-tools
description: Tools and utilities for working with PARS CPP JSON files - validation, conversion to Excel, schema reference, and DIQ definition lookup. Use when asked to validate, convert, or analyze PARS JSON data, when the user needs information about PARS CPP data format or schema, or when looking up a specific DIQ (Data Integrity and Quality) check.
---

# PARS JSON Tools

## Overview

PARS (Project Assessment and Reporting System) uses a structured JSON format for Capital Project Planning (CPP) data. This skill provides tools for working with PARS CPP JSON files.

## When to Use This Skill

- User asks to validate a PARS JSON file
- User wants to convert PARS JSON to Excel
- User needs information about PARS JSON structure
- User asks about PARS CPP data format or schema
- User asks about a specific DIQ check or data integrity rule

## Available Tools

### 1. JSON Validation

**Tool**: `validate-pars-json.ts`

**Purpose**: Validate PARS CPP JSON files against the official v5.0.3 schema using the exact configuration PARS uses in production.

**Usage**:
```bash
bun run skills/pars-json-tools/validate-pars-json.ts <json-file-path>
```

**Output**:
- Exit code 0: Valid JSON
- Exit code 1: Validation errors (with detailed error messages)
- Exit code 2: File not found or parse error

**Example**:
```bash
# Validate a PARS JSON file
bun run skills/pars-json-tools/validate-pars-json.ts project-data.json

# Check exit code in bash
if [ $? -eq 0 ]; then
  echo "Valid"
else
  echo "Invalid"
fi
```

### 2. JSON to Excel Conversion

**Tool**: `json-to-excel.ts`

**Purpose**: Convert PARS CPP JSON files to Excel workbooks with each top-level array as a separate sheet. Supports both single JSON files and ZIP archives containing multiple JSON files.

**Usage**:
```bash
# Convert JSON to Excel (auto-generates output filename)
bun run skills/pars-json-tools/json-to-excel.ts <input-file.json>

# Convert with custom output filename
bun run skills/pars-json-tools/json-to-excel.ts <input-file.json> <output-file.xlsx>

# Convert ZIP archive containing JSON files
bun run skills/pars-json-tools/json-to-excel.ts <input-file.zip>
```

**Output**:
- Excel workbook (.xlsx) with one sheet per dataset
- Each dataset (top-level array in JSON) becomes a separate sheet
- Exit code 0 on success

**Example**:
```bash
# Convert PARS JSON to Excel
bun run skills/pars-json-tools/json-to-excel.ts project-data.json

# This creates project-data.xlsx with sheets for each dataset
# Common datasets: Projects, ActivitiesWBS, Resources, etc.
```

### 3. DIQ Definition Lookup

**Tool**: `get-diq-definition.py`

**Purpose**: Retrieve a PARS Data Integrity and Quality (DIQ) check definition from the public [PARS Wiki](https://wiki.pars.doe.gov/en/DIQs). Returns clean markdown with the check's basic information, error causes, rationale, and SQL logic. DIQs are quality rules applied to PARS CPP JSON uploads after schema validation; each DIQ has a 7-digit ID and belongs to a dataset (DS00-DS21).

**Usage**:
```bash
# Number-only form: dataset inferred from digits 2-3 (9070365 -> DS07)
python3 skills/pars-json-tools/get-diq-definition.py 9070365

# Explicit DS{NN}/{number} form
python3 skills/pars-json-tools/get-diq-definition.py DS07/9070365

# Or fetch any wiki.pars.doe.gov page directly
python3 skills/pars-json-tools/get-diq-definition.py --url https://wiki.pars.doe.gov/en/DIQs
```

**Output**:
- Markdown to stdout with the page title, source URL, basic information table, what causes the error, why we check this, and (where present) the SQL function used to evaluate the check.
- Exit code 0 on success, 1 if the page is missing or unreachable, 2 if the DIQ ID is malformed.

**DIQ ID format**:
- The first digit is `1` for single-dataset DIQs or `9` for DIQs that touch multiple datasets.
- Digits 2-3 are the dataset number: `01`=DS01 (WBS), `02`=DS02, `03`=DS03 (EVT), `04`=DS04 (Schedule), `05`=DS05 (Schedule Logic), `06`=DS06 (Resources), `07`=DS07 (IPMR), `08`=DS08 (WAD), `09`=DS09 (CC Log), `10`=DS10 (CC Log Detail), `11`-`15`=DS11-DS15, `16`=DS16, `17`=DS17 (WBS EU), `18`=DS18 (Schedule EU), `19`=DS19 (Schedule Logic EU), `20`=DS20 (Sched CAL EU), `21`=DS21 (Rates EU). `00`=DS00 (metadata-level checks).

**Example**:
```bash
# Look up "12 Months Since OTB-OTS Without BCP" (DS07/9070365)
python3 skills/pars-json-tools/get-diq-definition.py 9070365

# Browse the full index of DIQs (groups all checks by dataset)
python3 skills/pars-json-tools/get-diq-definition.py --url https://wiki.pars.doe.gov/en/DIQs
```

**Notes**:
- Uses the Python standard library only; no extra packages required.
- DIQs are the second phase of PARS data validation, applied after JSON schema validation. Each DIQ documents the check's severity (CRITICAL / MAJOR / MINOR), the table it runs against, the failure condition, and the SQL function that implements it.
- The wiki is public, so this tool needs no credentials.

## Schema Information

### Compact Reference

**File**: `pars-cpp-compact-reference.md`

**Purpose**: AI-friendly, human-readable description of the PARS CPP JSON schema structure. This is MUCH easier to read than the full JSON schema.

**When to use**:
- User asks "what fields are in PARS JSON?"
- User needs to understand PARS data structure
- You need to know what data is available

**How to use**:
```bash
# Read the compact reference
cat skills/pars-json-tools/pars-cpp-compact-reference.md
```

**Note**: Read this file when you need to understand PARS structure. It's designed to be readable by AI and humans.

### Full JSON Schema

**File**: `pars-cpp-json-schema-v5-0-3.json`

**Purpose**: Machine-readable JSON Schema for PARS CPP v5.0.3 (official schema from json.pars.doe.gov).

**When to use**:
- When the validation script needs it (automatic)
- When you need precise type definitions
- DO NOT read this file unless absolutely necessary (2751 lines)

**Important**: The compact reference is almost always sufficient. Only use the full schema if you need exact JSON Schema syntax.

## Common Workflows

### Validate and Convert PARS JSON

```bash
# Step 1: Validate
bun run skills/pars-json-tools/validate-pars-json.ts project-data.json

# Step 2: If valid, convert to Excel
if [ $? -eq 0 ]; then
  bun run skills/pars-json-tools/json-to-excel.ts project-data.json
  echo "Created project-data.xlsx"
else
  echo "Fix validation errors first"
fi
```

### Analyze PARS JSON Structure

```bash
# Quick overview using jq
jq 'keys' project-data.json

# Count records in each dataset
jq 'to_entries | map({key: .key, count: (.value | length)})' project-data.json

# Extract specific dataset
jq '.Projects' project-data.json

# Filter projects by criteria
jq '.Projects[] | select(.TotalProjectCost > 1000000)' project-data.json
```

### Check What Fields Are Available

```bash
# Read the compact reference to see all available fields
cat skills/pars-json-tools/pars-cpp-compact-reference.md

# Or use jq to see actual fields in a file
jq '.Projects[0] | keys' project-data.json
```

## Tips for Working with PARS JSON

1. **Validation first**: Always validate before processing PARS JSON files
2. **Use compact reference**: Read `pars-cpp-compact-reference.md` to understand structure
3. **Use jq for queries**: jq is perfect for quick JSON analysis and filtering
4. **Excel for exploration**: Convert to Excel when users want to browse data visually
5. **Check datasets**: Common datasets include Projects, ActivitiesWBS, Resources, Milestones

## File Locations

All PARS tools are in `skills/pars-json-tools/`:
- `validate-pars-json.ts` - Validation script
- `json-to-excel.ts` - Excel conversion script
- `get-diq-definition.py` - DIQ definition lookup against the PARS Wiki
- `pars-cpp-compact-reference.md` - AI-friendly schema documentation
- `pars-cpp-json-schema-v5-0-3.json` - Full JSON schema (use sparingly)

## Visual Verification Loop (RECOMMENDED)

For Excel conversions from PARS JSON, verify output quality:

1. **Convert to PDF/PNG**: `soffice --headless --convert-to pdf output.xlsx && pdftoppm -jpeg -r 150 output.pdf sheet`
2. **Inspect images** for: clipped data, readable headers, consistent formatting
3. **Fix and regenerate** if issues found

## Quality Checklists

### JSON Validation Quality
- [ ] JSON syntax is valid (proper braces, quotes, commas)
- [ ] All required fields are present
- [ ] Date formats are ISO 8601 (YYYY-MM-DDTHH:MM:SSZ)
- [ ] No validation errors from schema check

### Excel Output Quality
- [ ] All JSON data is represented
- [ ] Column widths accommodate content
- [ ] Headers are bold and distinct from data

## Citation Standards

When presenting PARS-derived data:
```
Source: PARS [Database/Export]
Date Extracted: [Date]
Records: [Count]
```

## Common Issues & Solutions

| Issue | Solution |
|-------|----------|
| JSON validation error | Check syntax (quotes, brackets, commas) |
| Date format error | Convert to ISO 8601: YYYY-MM-DDTHH:MM:SSZ |
| Column clipping in Excel | Autofit or manually widen after conversion |
| Enum value unrecognized | Verify against compact reference |

## Dependencies

These scripts require:
- **Bun** runtime (for `validate-pars-json.ts` and `json-to-excel.ts`)
- **ajv** and **ajv-formats** packages (for validation)
- **xlsx** package (for Excel conversion)
- **adm-zip** package (for ZIP file handling)
- **Python 3.9+** with network access (for `get-diq-definition.py` — standard library only)
