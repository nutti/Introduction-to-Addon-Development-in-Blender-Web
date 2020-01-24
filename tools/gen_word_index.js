'use strict';

let fs = require('fs');
let path = require('path');

let srcDir = '';
let destFile = 'word_index.md';

function printUsage() {
    console.log('Usage: gen_word_index.js --src-dir=<source_dir> [--dest-file=<dest_file>]');
}

function readdirRecursive(p, fileCallback, errCallback) {
    let files = fs.readdirSync(p);
    files.forEach((f) => {
        let fullpath = path.join(p, f);
        if (fs.statSync(fullpath).isDirectory()) {
            readdirRecursive(fullpath, fileCallback, errCallback);
        } else {
            fileCallback(fullpath);
        }
    });
}

for (let i = 2; i <process.argv.length; i++) {
    let match = null;
    if ((match = /--src-dir=(\S+)/.exec(process.argv[i])) != null) {
        srcDir = match[1];
    }
    if ((match = /--dest-file=(\S+)/.exec(process.argv[i])) != null) {
        destFile = match[1];
    }
}

if (srcDir === '') {
    printUsage();
    process.exit(1);
}

console.log(`Source directory: ${srcDir}`);
console.log(`Destination File: ${destFile}`);

let filesToParse = [];
readdirRecursive(srcDir, (path) => {
    filesToParse.push(path.replace(/\\/g, '/'));
}, (err) => {
    console.log(`Error: (readdirRecursive) ${err}`)
});

console.log('Start parse file...');
let wordIndices = [];
filesToParse.forEach((file) => {
    console.log(`  ${file}`);
    let match = null;
    if ((match = /chapter_([0-9]+)\/([0-9]+)_(.*)\.md/.exec(file)) == null) {
        console.log('    ...Skipped (Invalid file name)');
        return;
    }
    let chapterText = match[1];
    let sectionText = match[2];
    let sectionNameText = match[3];
    let chapter = parseInt(chapterText, 10);
    let section = parseInt(sectionText, 10);
    if (chapter <= 0 || chapter >= 99) {
        console.log(`    ...Skipped (Chapter ${chapterText})`);
        return;
    }
    if (section <= 0 || section >= 99) {
        console.log(`    ...Skipped (Section ${sectionText})`);
        return;
    }

    let body = fs.readFileSync(file);
    let lines = body.toString().split('\n');
    lines.forEach((l) => {
        if ((match = /\*\*(.*)\*\*/.exec(l)) != null) {
            let word = match[1];
            // [word, section, relative_path]
            wordIndices.push([
                word,
                `${chapter}-${section}`,
                `../chapter_${chapterText}/${sectionText}_${sectionNameText}.html`
            ]);
        }
    });
});

console.log("Start writing file...");
let linesToWrite = [];
linesToWrite.push("---");
linesToWrite.push("pagetitle: 索引");
linesToWrite.push("subtitle: 索引");
linesToWrite.push("---");
linesToWrite.push("");
linesToWrite.push("");
linesToWrite.push("|用語|節|");
linesToWrite.push("|---|---|");
wordIndices.forEach((wi) => {
    linesToWrite.push(`|${wi[0]}|[${wi[1]}](${wi[2]})|`);
});

let textToWrite = linesToWrite.join("\n");
fs.writeFileSync(destFile, textToWrite);

console.log("Finished");
