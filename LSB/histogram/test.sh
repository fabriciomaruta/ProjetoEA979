#!/bin/bash

cc=python
file_py=histogram.py
dir_cover=../imgs/imgs-cover

for file in $dir_cover/*; do
    $cc $histogram $file_py $file ${file//cover/steg}
done