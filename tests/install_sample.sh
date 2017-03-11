#!/bin/bash

if [ $# -ne 1 ]; then
    echo "Usage: install_sample.sh <target>"
fi


# search package
package=()
files=()
for file in `\find ./sample -type f -name '*.py'`; do
    if [ `echo "${file}" | grep '__init__.py'` ]; then
        path=${file%/*}
        package+=("${path}")
        
    fi
    files+=("${file}")
done

# remove package
module=()
for file in ${files[@]}; do
    found=0
    for pkg in ${package[@]}; do
        if [ `echo "${file}" | grep "${pkg}"` ]; then
            found=1
        fi
    done
    if [ ${found} -ne 1 ]; then
        module+=("${file}")
    fi
done

echo "pa"
echo ${package[@]}
echo "mo"
echo ${module[@]}

