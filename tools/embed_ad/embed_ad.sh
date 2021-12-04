#!/bin/bash

if [ $# -ne 1 ]; then
    echo "Usage: sh embed_ad.sh <src_dir>"
    exit 1
fi

SCRIPT_DIR=$(cd $(dirname $0); pwd)
SRC_DIR=${1}
TMP_DIR=$(mktemp -d)

for file in `find ${SRC_DIR} -name "*.html"`; do
    perl ${SCRIPT_DIR}/embed_ad.pl ${file} ${SCRIPT_DIR}/embed_ad_patterns.ini > ${TMP_DIR}/embed_file.tmp
	cp ${TMP_DIR}/embed_file.tmp  ${file}
done
