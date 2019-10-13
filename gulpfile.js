let gulp = require('gulp');
let plumber = require('gulp-plumber');
let compass = require('gulp-compass');
let rename = require('gulp-rename');

let path = require('path');
let through = require('through2');
let execSync = require('child_process').execSync;
let fs = require('fs');

let srcDir = './src';
let destDir = './build';
let tmpDir = './tmp';

let srcFontDir = srcDir + '/fonts';
let srcImageDir = srcDir + '/images';
let srcScssDir = srcDir + '/scss';
let srcMarkdownDir = srcDir + '/markdown';
let srcSampleDir = srcDir + '/sample';
let destFontDir = destDir + '/fonts';
let destImageDir = destDir + '/images';
let destScssDir = destDir + '/css';
let destMarkdownDir = destDir;

let htmlTemplatePath = srcDir + '/templates/html5_template.html';
let metadataPath = srcDir + '/templates/metadata.yaml';
let tocPath = srcDir + '/templates/toc.json';

gulp.task('copy-font', (done) => {
    gulp.src([srcFontDir + '/**/*.ttf', srcFontDir + '/**/*.woff'])
        .pipe(gulp.dest(destFontDir));
    done();
});

gulp.task('copy-image', (done) => {
    gulp.src([srcImageDir + '/**/*.png', srcImageDir + '/**/*.jpg'])
        .pipe(gulp.dest(destImageDir));
    done();
});

gulp.task('compass', (done) => {
    gulp.src(srcScssDir + '/**/*.scss')
        .pipe(plumber())
        .pipe(compass({
            config_file: './config/compass.rb',
            comments: false,
            css: destScssDir,
            sass: srcScssDir
        }));
    done();
});


function includeCode(input, passCount) {
    let output = [];

    input.forEach((line) => {
        if ((match = /^\s*\[@include-source\s+.*]/.exec(line)) === null) {
            output.push(line);
            return;
        }

        let embedPattern = null;
        if ((match = /pattern="(full|partial)"/.exec(line)) !== null) {
            embedPattern = match[1];
        } else {
            throw new Error(`Not found item "pattern". (line: ${line})`);
        }

        let embedFilepath = null;
        let embedExtension = null;
        if ((match = /filepath="([\.\w_\/]+)"/.exec(line)) !== null) {
            embedFilepath = path.resolve(srcSampleDir + '/' + match[1]);
            embedExtension = path.extname(embedFilepath);
        } else {
            throw new Error(`Not found item "filepath". (line: ${line})`);
        }

        let embedBlock = null;
        if ((match = /block="([\w_]+)"/.exec(line)) !== null) {
            embedBlock = match[1];
        } else {
            if (embedPattern === 'partial') {
                throw new Error(`Not fuond item "block". (line: ${line})`);
            }
        }

        switch (embedExtension) {
            case '.py':
                output.push('```python');
                break;
            case '.yml':
                output.push('```yaml');
                break;
            default:
                throw new Error(`Not supported extension. (extension: ${embedExtension})`);
        }

        if (embedPattern === 'full') {
            let embedInput = fs.readFileSync(embedFilepath, 'utf-8').split('\n');
            embedInput.forEach((embedLine) => {
                if (/^\s*#\s*@include-source\s*start\s*\[.*\]/.exec(embedLine) !== null) {
                    return;
                }
                if (/^\s*#\s*@include-source\s*end\s*\[.*\]/.exec(embedLine) !== null) {
                    return;
                }
                output.push(embedLine);
            });
        } else if (embedPattern == 'partial') {
            let embedInput = fs.readFileSync(embedFilepath, 'utf-8').split('\n');
            let inPartial = false;
            embedInput.forEach((embedLine) => {
                if ((match = /^\s*#\s*@include-source\s*start\s*\[(.*)\]/.exec(embedLine)) !== null) {
                    if (match[1] === embedBlock) {
                        inPartial = true;
                    }
                    return;
                }
                if ((match = /^\s*#\s*@include-source\s*end\s*\[(.*)\]/.exec(embedLine)) !== null) {
                    if (match[1] === embedBlock) {
                        inPartial = false;
                    }
                    return;
                }
                if (inPartial === true) {
                    output.push(embedLine);
                }
            });
            if (inPartial === true) {
                throw new Error('"# @include-source end" not found');
            }
        } else {
            throw new Error(`Not supported pattern ${embedPattern}`);
        }

        output.push('```');
    });

    console.log(`    [Pass ${passCount}] Include Code`);

    return output;
}


function preProcess(filepath) {
    let input = fs.readFileSync(filepath, 'utf-8').split('\n');
    let output = input;
    let passPipeline = [includeCode];
    let passCount = 0;

    passPipeline.forEach((pass) => {
        output = pass(output, passCount);
        passCount++;
    });

    return output;
}


function includeToc(input, passCount, destHtmlPath) {
    let output = [];
    let toc = require(tocPath);

    input.forEach((line) => {
        if (/<!--\s+@include-toc\s+-->/.exec(line) === null) {
            output.push(line);
            return;
        }

        // @pre
        output.push('<ul>');
        if ('@pre' in toc) {
            output.push('  <ul>');
            let chapterBody = toc['@pre'];
            for (let section in chapterBody) {
                let sectionBody = section;
                let url = chapterBody[section];
                let relativeUrl = path.relative(destHtmlPath, url).replace(/\\/g, '/');
                if (relativeUrl !== '') {
                    relativeUrl = relativeUrl.replace(/^\.\.\//g, '').replace(/\\/g, '/');
                }
                if ((match = /@[0-9]+:(.+)/.exec(section)) !== null) {
                    sectionBody = match[1];
                }
                output.push(`    <li><a href="${relativeUrl}">${sectionBody}</a></li>`);
            }
            output.push('  </ul>');
        }
        output.push('</ul>');

        // body
        output.push('<ul>');
        for (let chapter in toc) {
            if (chapter === '@pre' || chapter === '@post') {
                continue;
            }
            if ('@title' in toc[chapter]) {
                let url = toc[chapter]['@title'];
                let relativeUrl = path.relative(destHtmlPath, url).replace(/\\/g, '/');
                if (relativeUrl !== '') {
                    relativeUrl = relativeUrl.replace(/^\.\.\//g, '').replace(/\\/g, '/');
                }
                output.push(`    <li><a href="${relativeUrl}">${chapter}</a></li>`);
            } else {
                output.push(`    <li>${chapter}</li>`);
            }
            output.push('  <ul>');
            let chapterBody = toc[chapter];
            for (let section in toc[chapter]) {
                if (section === '@title') {
                    continue;
                }
                let sectionBody = section;
                let url = chapterBody[section];
                let relativeUrl = path.relative(destHtmlPath, url).replace(/\\/g, '/');
                if (relativeUrl !== '') {
                    relativeUrl = relativeUrl.replace(/^\.\.\//g, '').replace(/\\/g, '/');
                }
                if ((match = /@[0-9]+:(.+)/.exec(section)) !== null) {
                    sectionBody = match[1];
                }
                output.push(`    <li><a href="${relativeUrl}">${sectionBody}</a></li>`);
            }
            output.push('  </ul>');
        }
        output.push('</ul>');

        // @post
        if ('@post' in toc) {
            output.push('  <ul>');
            let chapterBody = toc['@post'];
            for (let section in chapterBody) {
                let sectionBody = section;
                let url = chapterBody[section];
                let relativeUrl = path.relative(destHtmlPath, url).replace(/\\/g, '/');
                if (relativeUrl !== '') {
                    relativeUrl = relativeUrl.replace(/^\.\.\//g, '').replace(/\\/g, '/');
                }
                if ((match = /@[0-9]+:(.+)/.exec(section)) !== null) {
                    sectionBody = match[1];
                }
                output.push(`    <li><a href="${relativeUrl}">${sectionBody}</a></li>`);
            }
            output.push('  </ul>');
        }
        output.push('</ul>');

    });

    console.log(`    [Pass ${passCount}] Include TOC`);

    return output;
}


function replaceOwnUrl(input, passCount, destHtmlPath) {
    let output = [];
    let ownUrl = destHtmlPath;

    input.forEach((line) => {
        output.push(line.replace(/<!--\s+@replace-own-url\s+-->/g, ownUrl));
    });

    console.log(`    [Pass ${passCount}] Replace Own URL`);

    return output;
}


function getOrderedToc(toc) {
    let output = [];
    
    // @pre
    if ('@pre' in toc) {
        for (let section in toc['@pre']) {
            let sectionBody = section;
            if ((match = /@[0-9]+:(.+)/.exec(section)) !== null) {
                sectionBody = match[1];
            }
            output.push({'title': sectionBody, 'url': toc['@pre'][section]});
        }
    }

    // body
    for (let chapter in toc) {
        if (chapter === '@pre' || chapter === '@post') {
            continue;
        }

        // @title
        if ('@title' in toc[chapter]) {
            let url = toc[chapter]['@title'];
            output.push({'title': chapter, 'url': toc[chapter]['@title']});
        }

        let chapterBody = toc[chapter];
        for (let section in chapterBody) {
            if (section === '@title') {
                continue;
            }
            let sectionBody = section;
            if ((match = /@[0-9]+:(.+)/.exec(section)) !== null) {
                sectionBody = match[1];
            }
            output.push({'title': sectionBody, 'url': chapterBody[section]})
        }
    }

    // @post
    if ('@post' in toc) {
        for (let section in toc['@post']) {
            let sectionBody = section;
            if ((match = /@[0-9]+:(.+)/.exec(section)) !== null) {
                sectionBody = match[1];
            }
            output.push({'title': sectionBody, 'url': toc['@post'][section]});
        }
    }

    return output;
}


function includePrevNextUrl(input, passCount, destHtmlPath) {
    let output = [];
    let ownUrl = destHtmlPath;
    let toc = require(tocPath);
    let orderedToc = getOrderedToc(toc);

    let prevEntry = null;
    let nextEntry = null;
    for (let i = 0; i < orderedToc.length; i++) {
        let entry = orderedToc[i];
        if (entry['url'] === ownUrl) {
            if (i != 0) {
                prevEntry = orderedToc[i - 1];
            }
            if (i != (orderedToc.length - 1)) {
                nextEntry = orderedToc[i + 1];
            }
            break;
        }
    }

    input.forEach((line) => {
        if (/<!--\s+@include-prev-url\s+-->/.exec(line) !== null) {
            if (prevEntry !== null) {
                let title = prevEntry['title'];
                let url = prevEntry['url'];
                let relativeUrl = path.relative(destHtmlPath, url).replace(/\\/g, '/');
                if (relativeUrl !== '') {
                    relativeUrl = relativeUrl.replace(/^\.\.\//g, '').replace(/\\/g, '/');
                }
                let body = `<a href="${relativeUrl}">${title}</a>`;
                output.push(line.replace(/<!--\s+@include-prev-url\s+-->/g, body));
            }
        }
        if (/<!--\s+@include-next-url\s+-->/.exec(line) !== null) {
            if (nextEntry !== null) {
                let title = nextEntry['title'];
                let url = nextEntry['url'];
                let relativeUrl = path.relative(destHtmlPath, url).replace(/\\/g, '/');
                if (relativeUrl !== '') {
                    relativeUrl = relativeUrl.replace(/^\.\.\//g, '').replace(/\\/g, '/');
                }
                let body = `<a href="${relativeUrl}">${title}</a>`;
                output.push(line.replace(/<!--\s+@include-next-url\s+-->/g, body));
            }
        }

        output.push(line);
    });

    console.log(`    [Pass ${passCount}] Include Prev Next URL`);

    return output;
}


function postProcess(input, destHtmlPath) {
    let output = input;
    let passPipeline = [includeToc, replaceOwnUrl, includePrevNextUrl];
    let passCount = 0;

    passPipeline.forEach((pass) => {
        output = pass(output, passCount, destHtmlPath);
        passCount++;
    });

    return output;
}


gulp.task('pandoc', (done) => {
    gulp.src(srcMarkdownDir + '/**/*.md')
        .pipe(through.obj((file, enc, cb) => {
            let mdFilePath = file.path.replace(/\\/g, '/');
            let mdInput = preProcess(mdFilePath).join('\n');
            let destHtmlPath = path.relative(srcMarkdownDir, file.path).replace(/\\/g, '/').replace(/.md$/g, '.html');
            let destHtmlFullPath = destDir + '/' + destHtmlPath;
            let destCssPath = path.relative(destHtmlFullPath, path.resolve(destScssDir + '/style.css')).replace(/\\/g, '/').replace(/^\.\.\//g, '').replace(/\\/g, '/');
            
            if (!fs.existsSync(tmpDir)) {
                fs.mkdirSync(tmpDir, {recursive: true});
            }

            let tmpFilePath = `${tmpDir}/tmp.md`;
            fs.writeFileSync(tmpFilePath, mdInput);
            let cmd = `pandoc -f markdown -t html5 --template=${htmlTemplatePath} -c ${destCssPath} ${tmpFilePath} ${metadataPath}`;
            let result;
            try {
                result = execSync(cmd);
            } catch(error) {
                let error_msg = `Failed to Execute Pandoc command. (Status: ${error.status}})`;
                throw new Error(error_msg);
            }
            fs.unlinkSync(tmpFilePath);

            let htmlOutput = postProcess(result.toString().split('\n'), destHtmlPath).join('\n');


            file.contents = Buffer.from(htmlOutput);

            cb(null, file);
        }))
        .pipe(rename({extname: '.html'}))
        .pipe(gulp.dest(destMarkdownDir));
    done();
});

gulp.task('build', gulp.series(gulp.parallel(
    'copy-font', 'copy-image', 'compass', 'pandoc')));
