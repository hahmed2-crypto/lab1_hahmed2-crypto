#!/bin/bash

if [ ! -f "grades.csv" ]; then
    echo "Error: grades.csv not found. Nothing to archive."
    exit 1
fi

if [ ! -d "archive" ]; then
    mkdir archive
fi

timestamp=$(date +"%Y%m%d-%H%M%S")
new_filename="grades_${timestamp}.csv"

mv grades.csv "archive/${new_filename}"

touch grades.csv

echo "${timestamp} - Archived: grades.csv -> archive/${new_filename}" >> organizer.log

echo "Archiving complete. New grades.csv is ready."
