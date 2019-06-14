#!/usr/bin/env bash
seq 1 1000 | awk -v seed="${RANDOM}" 'BEGIN{srand(seed)}{if(rand() >= 0.05){print $1}else{print ""}}'