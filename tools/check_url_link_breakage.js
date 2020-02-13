'use strict';

let fs = require('fs');
let path = require('path');

let dirToCheck = '';

function printUsage() {
    console.log('Usage: check_url_link_breakage.js --dir=<dir_to_check>');
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

for (let i = 2; i < process.argv.length; i++) {
    let match = null;
    if ((match = /--dir=(\S+)/.exec(process.argv[i])) != null) {
        dirToCheck = match[1];
    }
}

if (dirToCheck === '') {
    printUsage();
    process.exit(1);
}

console.log(`Directory to check URL link breakage: ${dirToCheck}`);

let filesToCheck = [];
readdirRecursive(dirToCheck, (path) => {
    filesToCheck.push(path.replace(/\\/g, '/'));
    console.log(`  ${path}`);
}, (err) => {
    console.log(`Error: (readdirRecursive) ${err}`)
});

console.log(`Checking...`);

filesToCheck.forEach((file) => {
    console.log(`  Check ${file} ...`);

    let relativePaths = [];
    filesToCheck.forEach((f) => {
        let rPath = path.relative(file, f).replace(/\\/g, '/');;
        if (rPath !== '') {
            rPath = rPath.replace(/^\.\.\//g, '').replace(/\\/g, '/');
        }
        rPath = rPath.replace(/\.md$/g, '.html');
        relativePaths.push(rPath);
    });

    let body = fs.readFileSync(file);
    let lines = body.toString().split('\n');
    lines.forEach((l) => {
        let match = null;
        if ((match = /\[.*\]\((.*\.html)\)/.exec(l)) != null) {
            let target = match[1];
            if (!relativePaths.includes(target)) {
              console.log(`    Invalid target found '${target}'`);
            }
        }
    });
})
