#!/usr/bin/env node

import fs from "node:fs";
import path from "node:path";
import process from "node:process";
import { fileURLToPath } from "node:url";

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const packagePath = path.join(root, "package.json");
const pluginPath = path.join(root, ".claude-plugin", "plugin.json");
const packageJson = JSON.parse(fs.readFileSync(packagePath, "utf8"));
const pluginJson = JSON.parse(fs.readFileSync(pluginPath, "utf8"));
const checkOnly = process.argv.includes("--check");

if (checkOnly) {
  if (packageJson.version !== pluginJson.version) {
    console.error(`FAIL: package ${packageJson.version} != plugin ${pluginJson.version}`);
    process.exit(1);
  }
  console.log(`PASS: plugin version ${pluginJson.version}`);
} else {
  pluginJson.version = packageJson.version;
  fs.writeFileSync(pluginPath, `${JSON.stringify(pluginJson, null, 2)}\n`, "utf8");
  console.log(`Updated ${path.relative(root, pluginPath)} to ${packageJson.version}`);
}
