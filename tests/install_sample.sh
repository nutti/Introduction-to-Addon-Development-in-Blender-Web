#!/bin/bash

if [ $# -ne 2 ]; then
    echo "Usage: install_sample.sh <source> <target>"
fi

src=${1}
tgt=${2}

# search package
packages=()
files=()
for file in `\find ${src} -type f -name '*.py'`; do
    if [ `echo "${file}" | grep '__init__.py'` ]; then
        path=${file%/*}
        packages+=("${path}")

    fi
    files+=("${file}")
done

# remove package
modules=()
for file in ${files[@]}; do
    found=0
    for pkg in ${packages[@]}; do
        if [ `echo "${file}" | grep "${pkg}"` ]; then
            found=1
        fi
    done
    if [ ${found} -ne 1 ]; then
        modules+=("${file}")
    fi
done

# copy packages to target
for pkg in ${packages[@]}; do
    cp -r ${pkg} ${tgt}
    echo "Copied "${pkg}" to "${tgt}
done

# copy modules to target
for mod in ${modules[@]}; do
    cp ${mod} ${tgt}
    echo "Copied "${mod}" to "${tgt}
done
