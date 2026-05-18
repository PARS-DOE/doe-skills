#!/usr/bin/env bun

/**
 * PARS CPP JSON Schema Validator
 *
 * Validates PARS CPP JSON files against the official schema using the exact
 * configuration that PARS uses in production.
 *
 * Usage:
 *   bun run validate-pars-json.ts <json-file-path>
 *
 * Exit codes:
 *   0 - Valid JSON
 *   1 - Validation errors
 *   2 - File not found or parse error
 */

import { readFileSync } from 'node:fs';
import { dirname, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';
import Ajv2020 from 'ajv/dist/2020';
import addFormats from 'ajv-formats';

const __dirname = dirname(fileURLToPath(import.meta.url));

// Load schema
const schemaPath = resolve(__dirname, 'pars-cpp-json-schema-v5-0-3.json');
const schema = JSON.parse(readFileSync(schemaPath, 'utf-8'));

// Configure AJV exactly as PARS does
const ajv = new Ajv2020({
  allErrors: true,
  verbose: true,
  multipleOfPrecision: 2,
  coerceTypes: false,
});

addFormats(ajv);
ajv.addKeyword('key');
ajv.addKeyword('notes');

const validate = ajv.compile(schema);

// Parse command-line arguments
const args = process.argv.slice(2);
if (args.length === 0) {
  console.error('Error: No file specified');
  console.error('Usage: bun run validate-pars-json.ts <json-file-path>');
  process.exit(2);
}

const jsonFilePath = resolve(args[0]);

try {
  // Read and parse JSON file
  const jsonContent = readFileSync(jsonFilePath, 'utf-8');
  const data = JSON.parse(jsonContent);

  // Validate
  const valid = validate(data);

  if (valid) {
    console.log('✓ Valid PARS CPP JSON');
    process.exit(0);
  } else {
    console.error('✗ Validation failed\n');

    if (validate.errors) {
      for (const error of validate.errors) {
        const path = error.instancePath || '/';
        const keyword = error.keyword;
        const message = error.message;
        const params = JSON.stringify(error.params);

        console.error(`  ${path}`);
        console.error(`    ${keyword}: ${message}`);
        if (error.params && Object.keys(error.params).length > 0) {
          console.error(`    params: ${params}`);
        }
        console.error('');
      }

      console.error(`Total errors: ${validate.errors.length}`);
    }

    process.exit(1);
  }
} catch (error) {
  if (error instanceof Error) {
    if ('code' in error && error.code === 'ENOENT') {
      console.error(`Error: File not found: ${jsonFilePath}`);
    } else if (error instanceof SyntaxError) {
      console.error(`Error: Invalid JSON: ${error.message}`);
    } else {
      console.error(`Error: ${error.message}`);
    }
  } else {
    const errorStr = typeof error === 'object' ? JSON.stringify(error, null, 2) : String(error);
    console.error(`Error: ${errorStr}`);
  }
  process.exit(2);
}
