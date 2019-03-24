#!/bin/bash

BODY_DIR="body"
RELEASE_DIR="release"
TMP_DIR="tmp"
TEMPLATE_FILE="templates/html5_template.html"
CSS_FILE="style.css"

cur_dir=`dirname ${0}`

echo "Making Temporary Directories ..."

# make temporary directories
for dir in `find ${BODY_DIR} -type d | sort`; do
    dirname=${TMP_DIR}${dir#${BODY_DIR}}
    mkdir -p ${dirname}
    echo "  Created ${dirname}"
done

echo "Pre-processing Markdown files ..."

# pre-process markdown files
for md_file in `find ${BODY_DIR} -type f -name "*.md" | sort`; do
    fpath=${md_file#${BODY_DIR}}
    tmp_md_file=${TMP_DIR}${fpath%.md}-tmp.md
    bash ${cur_dir}/tools/pre_process.sh ${md_file} ${tmp_md_file}
    if [ $? -ne 0 ]; then
        echo "ERROR: Failed to pre-process ${md_file}"
        exit 1
    fi
    echo "  Pre-processed ${md_file} -> ${tmp_md_file}"
done

echo "Making Release Directories ..."

# make release directories
for dir in `find ${TMP_DIR} -type d | sort`; do
    dirname=${RELEASE_DIR}${dir#${TMP_DIR}}
    mkdir -p ${dirname}
    echo "  Created ${dirname}"
done

echo "Compiling Scss files ..."

sass scss/style.scss:${RELEASE_DIR}/${CSS_FILE}

echo "Generating HTML files ..."

# generate html files from markdown files
for file in `find ${TMP_DIR} -type f -name "*.md" | sort`; do
    fpath=${file#${TMP_DIR}}
    filename=${RELEASE_DIR}${fpath%-tmp.md}.html
    pandoc -f markdown -t html5 --template=${TEMPLATE_FILE} -c ../../${CSS_FILE} ${file} -o ${filename} metadata.yaml
    if [ $? -ne 0 ]; then
        echo "ERROR: Failed to generate ${filename}"
    fi
    echo "  Generated ${filename}"
done

# cleanup
rm -rf ${TMP_DIR}

echo "Done!"
