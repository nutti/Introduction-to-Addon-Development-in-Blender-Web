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

let mdFilesToCheck = [];
let pngFilesToCheck = [];
let tocFilesToCheck = [];
readdirRecursive(dirToCheck, (p) => {
    let path = p.replace(/\\/g, '/')

    let match = null;
    if ((match = /.*\.md$/.exec(path)) != null) {
        mdFilesToCheck.push(path);
        console.log(`  [Markdown] ${path}`);
    }
    if ((match = /.*\.png$/.exec(path)) != null) {
        pngFilesToCheck.push(path);
        console.log(`  [PNG] ${path}`);
    }
    if ((match = /toc\.json$/.exec(path)) != null) {
      tocFilesToCheck.push(path);
      console.log(`  [TOC] ${path}`);
    }
}, (err) => {
    console.log(`Error: (readdirRecursive) ${err}`)
});

console.log(`Checking...`);

mdFilesToCheck.forEach((file) => {
    let match = null;

    console.log(`  Check ${file} ...`);

    let relativePaths = [];
    mdFilesToCheck.forEach((f) => {
        let rPath = path.relative(file, f).replace(/\\/g, '/');;
        if (rPath === '') {
            return;
        }
        rPath = rPath.replace(/^\.\.\//g, '').replace(/\\/g, '/');
        rPath = rPath.replace(/\.md$/g, '.html');
        relativePaths.push(rPath);
    });
    pngFilesToCheck.forEach((f) => {
        let rPath = path.relative(file, f).replace(/\\/g, '/');;
        if (rPath === '') {
            return;
        }
        rPath = rPath.replace(/^\.\.\/\.\.\//g, '').replace(/\\/g, '/');
        relativePaths.push(rPath);
    });

    let body = fs.readFileSync(file);
    let lines = body.toString().split('\n');
    lines.forEach((l) => {
        let match = null;

        // for HTML link.
        if ((match = /\[.*\]\((.*\.html)\)/.exec(l)) != null) {
            let target = match[1];
            if ((match = /^http/.exec(target)) != null) {
                return;
            }
            if (!relativePaths.includes(target)) {
              console.log(`    Invalid html URL found '${target}'`);
            }
        }

        // for image link.
        if ((match = /!\[.*\]\((.*\.png) ".*"\)/.exec(l)) != null) {
            let target = match[1];
            if ((match = /^http/.exec(target)) != null) {
                return;
            }
            if (!relativePaths.includes(target)) {
              console.log(`    Invalid Image URL found '${target}'`);
            }
        }
    });
});

tocFilesToCheck.forEach((file) => {
    let match = null;

    console.log(`  Check ${file} ...`);

    let relativePaths = [];
    mdFilesToCheck.forEach((f) => {
        let rPath = path.relative(file, f).replace(/\\/g, '/');;
        if (rPath === '') {
            return;
        }
        rPath = rPath.replace(/^\.\.\/\.\.\/markdown\//g, '').replace(/\\/g, '/');
        rPath = rPath.replace(/\.md$/g, '.html');
        relativePaths.push(rPath);
    });

    let body = fs.readFileSync(file);
    let lines = body.toString().split('\n');
    lines.forEach((l) => {
        let match = null;

        // for HTML link.
        if ((match = /: "(.*\.html)"/.exec(l)) != null) {
            let target = match[1];
            if (!relativePaths.includes(target)) {
              console.log(`    Invalid html URL found '${target}'`);
            }
        }
    });
});
