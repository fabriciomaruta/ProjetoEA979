#!/bin/bash

cc=python
file_py=steganographyHash.py
function_merge=merge
function_unmerge=unmerge
dir_cover=../imgs/imgs-cover
dir_secret=../imgs/imgs-secret
dir_steg=../imgs/imgs-steg

for file in $dir_cover/*; do
    $cc $file_py $function_merge --img1=$file --img2=${file//cover/secret} --output=${file//cover/steg}
    $cc $file_py $function_unmerge --img=${file//cover/steg} --output=${file//cover/un}
done
