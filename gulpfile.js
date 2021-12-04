'use strict';

let gulp = require('gulp');
let plumber = require('gulp-plumber');
let compass = require('gulp-compass');
let rename = require('gulp-rename');

let path = require('path');
let through = require('through2');
let execSync = require('child_process').execSync;
let fs = require('fs');

let currentDate = new Date();


function parseOptions() {
    let options = {};

    for (let i = 2; i < process.argv.length; i++) {
        let match = '';
        if ((match = /--dest-dir=([-_/.a-zA-Z0-9]+)/.exec(process.argv[i])) != null) {
            options['destDir'] = match[1];
        }
        else if ((match = /--blender-version=([0-9.]+)/.exec(process.argv[i])) != null) {
            options['blenderVersion'] = match[1];
        }
        else if ((match = /--debug/.exec(process.argv[i])) != null) {
            options['debug'] = true;
        }
    }

    if (!('destDir' in options)) {
        options['destDir'] = './build';
    }
    if (!('blenderVersion' in options)) {
	    console.log('Could not find --blender-version option.');
        process.exit(1);
    }
    if (!('debug' in options)) {
        options['debug'] = false;
    }

    return options;
}


let options = parseOptions();


function debugLog(text) {
    if (options['debug']) {
        console.log(text);
    }
}


debugLog(`Target Blender Version: ${options["blenderVersion"]}`)

let srcDir = './src/' + options["blenderVersion"];
let destDir = options["destDir"];
let tmpDir = './tmp';

let srcFontDir = srcDir + '/fonts';
let srcImageDir = srcDir + '/images';
let srcScssDir = srcDir + '/scss';
let srcMarkdownDir = srcDir + '/markdown';
let srcSampleDir = srcDir + '/sample';
let srcJSDir = srcDir + '/js';

let destFontDir = destDir + '/fonts';
let destImageDir = destDir + '/images';
let destScssDir = destDir + '/css';
let destMarkdownDir = destDir;
let destJSDir = destDir + '/js';

let htmlTemplatePath = srcDir + '/templates/html5_template.html';
let metadataPath = srcDir + '/templates/metadata.yaml';
let tocPath = srcDir + '/templates/toc.json';

let fontFiles = [srcFontDir + '/**/*.ttf', srcFontDir + '/**/*.woff'];
let imageFiles = [srcImageDir + '/**/*.png', srcImageDir + '/**/*.jpg'];
let jsFiles = [srcJSDir + '/**/*.js'];
let scssFiles = [srcScssDir + '/**/*.scss'];
let markdownFiles = [srcMarkdownDir + '/**/*.md'];


gulp.task('copy-font', (done) => {
    gulp.src(fontFiles)
        .pipe(gulp.dest(destFontDir));
    done();
});

gulp.task('copy-image', (done) => {
    gulp.src(imageFiles)
        .pipe(gulp.dest(destImageDir));
    done();
});

gulp.task('copy-js', (done) => {
    gulp.src(jsFiles)
        .pipe(gulp.dest(destJSDir));
    done();
});

gulp.task('compass', (done) => {
    gulp.src(scssFiles)
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
    let match = null;

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
        if ((match = /filepath="([-\.\w_\/]+)"/.exec(line)) !== null) {
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

        let embedUnindent = false;
        if ((match = /unindent="True"/.exec(line)) !== null) {
            embedUnindent = true
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

        let outputEmbedLines = []
        if (embedPattern === 'full') {
            let embedInput = fs.readFileSync(embedFilepath, 'utf-8').split('\n');
            embedInput.forEach((embedLine) => {
                if (/^\s*#\s*@include-source\s*start\s*\[.*\]/.exec(embedLine) !== null) {
                    return;
                }
                if (/^\s*#\s*@include-source\s*end\s*\[.*\]/.exec(embedLine) !== null) {
                    return;
                }
                outputEmbedLines.push(embedLine);
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
                    outputEmbedLines.push(embedLine);
                }
            });
            if (inPartial === true) {
                throw new Error('"# @include-source end" not found');
            }
        } else {
            throw new Error(`Not supported pattern ${embedPattern}`);
        }

        let processedOutputEmbedLines = [];
        if (outputEmbedLines.length > 0) {
            if (embedUnindent) {
                let minSpaces = 9999;
                outputEmbedLines.forEach((line) => {
                    if (line === '') { return; }
                    if ((match = /^( *).*/.exec(line)) !== null) {
                        minSpaces = match[1].length < minSpaces ? match[1].length : minSpaces
                    }
                });
                outputEmbedLines.forEach((line) => {
                    if (line === '') {
                        processedOutputEmbedLines.push(line);
                    } else {
                        let regexp = new RegExp(`^[ ]{${minSpaces}}`);
                        processedOutputEmbedLines.push(line.replace(regexp, ''));
                    }
                });
            } else {
                processedOutputEmbedLines = outputEmbedLines;
            }
        }

        if (processedOutputEmbedLines.length > 0) {
            processedOutputEmbedLines.forEach((line) => {
                output.push(line);
            });
        }

        output.push('```');
    });

    debugLog(`    [Pass ${passCount}] Include Code`);

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


function includeToc(input, passCount, destHtmlPath, tocMetadata) {
    let output = [];
    let toc = require(tocPath);
    let match = null;

    input.forEach((line) => {
        if (/<!--\s+@include-toc\s+-->/.exec(line) === null) {
            output.push(line);
            return;
        }

        // @pre
        output.push('<ul>');
        if ('@pre' in toc) {
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
                let meta = tocMetadata[url];
                output.push(`  <li toc-chapter="${meta['chapter']}" toc-section="${meta['section']}"><a href="${relativeUrl}">${sectionBody}</a></li>`);
            }
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
                let meta = tocMetadata[url];
                output.push(`    <li toc-chapter="${meta['chapter']}" toc-section="${meta['section']}"><a href="${relativeUrl}">${chapter}</a></li>`);
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
                let meta = tocMetadata[url];
                output.push(`    <li toc-chapter="${meta['chapter']}" toc-section="${meta['section']}"><a href="${relativeUrl}">${sectionBody}</a></li>`);
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
                let meta = tocMetadata[url];
                output.push(`    <li toc-chapter="${meta['chapter']}" toc-section="${meta['section']}"><a href="${relativeUrl}">${sectionBody}</a></li>`);
            }
            output.push('  </ul>');
        }
        output.push('</ul>');

    });

    debugLog(`    [Pass ${passCount}] Include TOC`);

    return output;
}


function replaceOwnUrl(input, passCount, destHtmlPath, tocMetadata) {
    let output = [];
    let ownUrl = destHtmlPath;

    input.forEach((line) => {
        output.push(line.replace(/<!--\s+@replace-own-url\s+-->/g, ownUrl));
    });

    debugLog(`    [Pass ${passCount}] Replace Own URL`);

    return output;
}


function getOrderedToc(toc) {
    let output = [];
    let match = null;

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


function includePrevNextUrl(input, passCount, destHtmlPath, tocMetadata) {
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
        } else if (/<!--\s+@include-next-url\s+-->/.exec(line) !== null) {
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
        } else {
            output.push(line);
        }
    });

    debugLog(`    [Pass ${passCount}] Include Prev Next URL`);

    return output;
}


function appendTocParamsToUrl(input, passCount, destHtmlPath, tocMetadata)
{
    let output = [];
    let rootdir = __dirname;
    let dirname = path.dirname(destHtmlPath);
    input.forEach((line) => {
        let pattern = /<a\s+href="(?!http[s]*:\/\/)([^\s]+.html)">/;
        let regexp = new RegExp(pattern, 'g');
        let originals = line.match(regexp);
        if (originals != undefined) {
            originals = Array.from(new Set(originals));

            let replacePatterns = {};
            for (let i = 0; i < originals.length; ++i) {
                let orig = originals[i];
                let match;
                regexp = new RegExp(pattern);
                if ((match = orig.match(regexp)) != undefined) {
                    let url = match[1];
                    let key = path.relative(rootdir, path.resolve(dirname, url));
                    let meta = tocMetadata[key];
                    let replace = `<a href="${match[1]}?toc-chapter=${meta['chapter']}&toc-section=${meta['section']}">`;
                    replacePatterns[orig] = replace;
                }
            }

            for (let original in replacePatterns) {
                let replace = replacePatterns[original];
                regexp = new RegExp(original, 'g');
                line = line.replace(regexp, replace);
            }
        }

        output.push(line);
    });

    debugLog(`    [Pass ${passCount}] Append TOC Params to URL`);

    return output;
}


function includeDate(input, passCount) {
    let output = [];

    let year = currentDate.getFullYear();
    let month = currentDate.getMonth() + 1;
    let day = currentDate.getDate();
    let replace = `${year}.${month}.${day}`;

    input.forEach((line) => {
        let pattern = /<!--\s+@include-date\s+-->/;
        let regexp = new RegExp(pattern, 'g');

        line = line.replace(regexp, replace);

        output.push(line);
    });

    debugLog(`    [Pass ${passCount}] Include Date`);

    return output;
}


function postProcess(input, destHtmlPath, tocMetadata) {
    let output = input;
    let passPipeline = [includeToc, replaceOwnUrl, includePrevNextUrl, appendTocParamsToUrl, includeDate];
    let passCount = 0;

    passPipeline.forEach((pass) => {
        output = pass(output, passCount, destHtmlPath, tocMetadata);
        passCount++;
    });

    return output;
}


function setupTocMetadata() {
    let toc = require(tocPath);
    
    let metadata = {};
    for (let chapter in toc) {
        for (let section in toc[chapter]) {
            metadata[toc[chapter][section]] = {
                "chapter": chapter,
                "section": section
            }
        }
    }

    return metadata;
}


gulp.task('pandoc', (done) => {
    gulp.src(markdownFiles)
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

            let tocMetadata = setupTocMetadata();
            let htmlOutput = postProcess(result.toString().split('\n'), destHtmlPath, tocMetadata).join('\n');

            file.contents = Buffer.from(htmlOutput);

            cb(null, file);
        }))
        .pipe(rename({extname: '.html'}))
        .pipe(gulp.dest(destMarkdownDir));
    done();
});

gulp.task('watch', (done) => {
    gulp.watch(fontFiles, gulp.series('copy-font'));
    gulp.watch(imageFiles, gulp.series('copy-image'));
    gulp.watch(jsFiles, gulp.series('copy-js'));
    gulp.watch(scssFiles, gulp.series('compass'));
    gulp.watch(markdownFiles.concat([srcMarkdownDir + '/**/*.html']), gulp.series('pandoc'));
    done();
});

gulp.task('default', gulp.series(
    gulp.parallel(
        'copy-font', 'copy-image', 'copy-js', 'compass', 'pandoc'
    ),
    gulp.series(
        'watch'
    )
));

gulp.task('build', gulp.series(gulp.parallel(
    'copy-font', 'copy-image', 'copy-js', 'compass', 'pandoc'
)));
