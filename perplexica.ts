#!/usr/bin/env node

import yargs from 'yargs';
import { hideBin } from 'yargs/helpers';
import inquirer from 'inquirer';
import axios from 'axios';
import ora from 'ora';
import chalk from 'chalk';

interface SearchResponse {
  answer: string;
  sources: Array<{
    title: string;
    url: string;
  }>;
}

const focusModes = [
  'webSearch',
  'academicSearch',
  'newsSearch',
  'codeSearch',
  'patentSearch'
] as const;

type FocusMode = typeof focusModes[number];

const optimizationModes = ['speed', 'balanced'] as const;
type OptimizationMode = typeof optimizationModes[number];

async function performSearch(
  query: string, 
  focusMode: FocusMode,
  optimizationMode: OptimizationMode
): Promise<SearchResponse> {
  const spinner = ora('Searching...').start();
  
  try {
    const response = await axios.post('http://100.71.229.63:3001/api/search', {
      query,
      focusMode,
      optimizationMode,
      history: []
    });

    spinner.succeed('Search completed');
    return response.data;
  } catch (error) {
    spinner.fail('Search failed');
    if (axios.isAxiosError(error)) {
      throw new Error(`Search failed: ${error.message}`);
    }
    throw error;
  }
}

async function main() {
  const argv = await yargs(hideBin(process.argv))
    .option('query', {
      alias: 'q',
      describe: 'Search query',
      type: 'string'
    })
    .option('focus', {
      alias: 'f',
      describe: 'Focus mode',
      choices: focusModes,
      type: 'string'
    })
    .option('optimization', {
      alias: 'o',
      describe: 'Optimization mode',
      choices: optimizationModes,
      default: 'balanced' as OptimizationMode,
      type: 'string'
    })
    .help()
    .argv;

  let query = argv.query;
  let focusMode = argv.focus as FocusMode;
  const optimizationMode = argv.optimization as OptimizationMode;

  if (!query || !focusMode) {
    const answers = await inquirer.prompt([
      {
        type: 'input',
        name: 'query',
        message: 'Enter your search query:',
        when: !query
      },
      {
        type: 'list',
        name: 'focusMode',
        message: 'Select focus mode:',
        choices: focusModes,
        when: !focusMode
      }
    ]);

    query = query || answers.query;
    focusMode = focusMode || answers.focusMode;
  }

  try {
    const result = await performSearch(query, focusMode, optimizationMode);
    
    console.log('\n' + chalk.bold('Answer:'));
    console.log(result.answer);
    
    if (result.sources && result.sources.length > 0) {
      console.log('\n' + chalk.bold('Sources:'));
      result.sources.forEach((source, index) => {
        console.log(`${index + 1}. ${chalk.blue(source.title)}`);
        console.log(`   ${chalk.gray(source.url)}`);
      });
    }
  } catch (error) {
    console.error(chalk.red(error instanceof Error ? error.message : 'An unknown error occurred'));
    process.exit(1);
  }
}

main().catch(error => {
  console.error(chalk.red('Fatal error:', error));
  process.exit(1);
});
