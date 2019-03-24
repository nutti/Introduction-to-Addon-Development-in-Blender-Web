#!/bin/bash

if [ $# -ne 2 ]; then
    echo "Usage: bash pre_process.sh <in_file> <out_file>"
    exit 1
fi

in_file=${1}
out_file=${2}
cur_dir=`dirname ${0}`

cp ${in_file} ${out_file}-tmp-0

pass=0
for rb_file in `find ${cur_dir}/pre_process -type f -name "*.rb" | sort`; do
    next_pass=$(( pass + 1 ))
    ruby ${rb_file} ${out_file}-tmp-${pass} ${out_file}-tmp-${next_pass}
    if [ $? -ne 0 ]; then
        echo "Pre-process Pass ${pass}:${rb_file} is Failed"
        exit 1
    fi
    echo "Adapted Pre-process Pass ${pass}:${rb_file}"
    pass=${next_pass}
done

cp ${out_file}-tmp-${pass} ${out_file}

exit 0
