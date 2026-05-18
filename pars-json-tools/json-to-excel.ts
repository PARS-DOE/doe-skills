#!/usr/bin/env bun

/**
 * PARS JSON to Excel Converter (Non-Interactive)
 *
 * Converts PARS CPP JSON files to Excel workbooks without user prompts.
 * Based on the PARS-DOE/jsonToExcel tool adapted for CLI automation.
 *
 * Usage:
 *   bun run json-to-excel.ts <input-file.json> [output-file.xlsx]
 *   bun run json-to-excel.ts <input-file.zip> [output-file.xlsx]
 *
 * If output file is not specified, generates name from input file.
 *
 * Exit codes:
 *   0 - Success
 *   1 - Conversion error
 *   2 - File not found or invalid arguments
 */

import { readFileSync } from 'node:fs';
import { basename, extname, resolve } from 'node:path';
import AdmZip from 'adm-zip';
import * as XLSX from 'xlsx';

type ParsedData = {
  [key: string]: unknown;
};

function readJsonFile<T>(filePath: string): T {
  const content = readFileSync(filePath, 'utf-8');
  return JSON.parse(content) as T;
}

/**
 * Process ZIP files one entry at a time to minimize memory usage.
 * For large ZIP files (100MB+), this processes each JSON file serially
 * instead of loading all files into memory simultaneously.
 */
function createWorkbookFromZip(zipPath: string): XLSX.WorkBook {
  const zip = new AdmZip(zipPath);
  const zipEntries = zip.getEntries();
  const workbook = XLSX.utils.book_new();

  // Map to accumulate data for each dataset across multiple JSON files
  const datasetMap = new Map<string, unknown[]>();

  console.log(`Processing ZIP with ${zipEntries.length} entries...`);

  for (const entry of zipEntries) {
    if (entry.entryName.endsWith('.json') && !entry.isDirectory) {
      try {
        console.log(`  Processing ${entry.entryName}...`);

        // Load and parse ONE file at a time
        const content = entry.getData().toString('utf-8');
        const data = JSON.parse(content) as ParsedData;

        // Extract datasets from this file and add to accumulated data
        for (const [key, value] of Object.entries(data)) {
          if (Array.isArray(value) && value.length > 0) {
            if (!datasetMap.has(key)) {
              datasetMap.set(key, []);
            }
            datasetMap.get(key)?.push(...value);
          }
        }

        // File is now out of scope and can be garbage collected
        console.log(`    Added ${Object.keys(data).length} dataset(s) from ${entry.entryName}`);
      } catch (error) {
        console.error(`Warning: Could not parse ${entry.entryName}:`, error);
      }
    }
  }

  // Create Excel sheets from accumulated data
  console.log(`\nCreating Excel sheets for ${datasetMap.size} dataset(s)...`);
  for (const [datasetName, datasetRows] of Array.from(datasetMap.entries())) {
    console.log(`  ${datasetName}: ${datasetRows.length} rows`);
    const worksheet = XLSX.utils.json_to_sheet(datasetRows);
    XLSX.utils.book_append_sheet(workbook, worksheet, datasetName);
  }

  return workbook;
}

function createWorkbookFromSingleJson(jsonData: ParsedData): XLSX.WorkBook {
  const workbook = XLSX.utils.book_new();

  for (const [key, value] of Object.entries(jsonData)) {
    if (Array.isArray(value) && value.length > 0) {
      const worksheet = XLSX.utils.json_to_sheet(value);
      XLSX.utils.book_append_sheet(workbook, worksheet, key);
    }
  }

  return workbook;
}

function generateOutputFileName(inputFile: string, outputFile?: string): string {
  if (outputFile) {
    return outputFile;
  }

  const base = basename(inputFile, extname(inputFile));
  return `${base}.xlsx`;
}

// Parse command-line arguments
const args = process.argv.slice(2);
if (args.length === 0) {
  console.error('Error: No file specified');
  console.error('Usage: bun run json-to-excel.ts <input-file.json|zip> [output-file.xlsx]');
  process.exit(2);
}

const inputFile = resolve(args[0]);
const outputFile = args[1] ? resolve(args[1]) : undefined;

try {
  console.log(`Processing: ${inputFile}`);

  let workbook: XLSX.WorkBook;

  // Check file extension and process accordingly
  if (inputFile.endsWith('.zip')) {
    // Process ZIP entries one at a time (memory efficient for large files)
    workbook = createWorkbookFromZip(inputFile);
  } else if (inputFile.endsWith('.json')) {
    // Process single JSON file
    const jsonData = readJsonFile<ParsedData>(inputFile);
    workbook = createWorkbookFromSingleJson(jsonData);
  } else {
    console.error('Error: Input file must be .json or .zip');
    process.exit(2);
  }

  if (workbook.SheetNames.length === 0) {
    console.error('Error: No datasets found in file(s)');
    console.error('Expected arrays in top-level keys of JSON');
    process.exit(1);
  }

  const outputFileName = generateOutputFileName(inputFile, outputFile);

  console.log(`\nWriting Excel file...`);
  XLSX.writeFile(workbook, outputFileName);

  console.log(`✓ Excel file created: ${outputFileName}`);
  console.log(`  Sheets: ${workbook.SheetNames.join(', ')}`);
  process.exit(0);
} catch (error) {
  if (error instanceof Error) {
    if ('code' in error && error.code === 'ENOENT') {
      console.error(`Error: File not found: ${inputFile}`);
    } else if (error instanceof SyntaxError) {
      console.error(`Error: Invalid JSON: ${error.message}`);
    } else {
      console.error(`Error: ${error.message}`);
    }
  } else {
    console.error(`Error: ${String(error)}`);
  }
  process.exit(1);
}
