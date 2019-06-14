#!/usr/bin/env bash
seq 1 1000 | awk -v seed="${RANDOM}" 'BEGIN{srand(seed)}{print int(rand()*100)}'