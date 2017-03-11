#!/bin/bash

if [ $# -ne 1 ]; then
    echo "Usage: install_sample.sh <target>"
fi


package=("te")

find ./sample -type f | while read file
do
    if [ `echo "${file}" | grep '__init__.py'` ]; then
        path=${file%/*}
        echo ${path}
        package+=("1")
    fi
done

echo ${package[@]}
#
# for pkg in ${package[@]}; do
#     echo "${pkg}"
# done
