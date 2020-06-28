#!/bin/bash
find . -type f -name '*.aux' -delete
find . -type f -name '*.bbl' -delete
find . -type f -name '*.fdb_latexmk' -delete
find . -type f -name '*.fls' -delete
find . -type f -name '*.blg' -delete
find . -type f -name '*.log' -delete
find . -type f -name '*.toc' -delete
find . -type f -name '*.out' -delete
#find . -type f -name 'dissertation.pdf' -delete
#find . -type f -name 'dissertation.out.pdf' -delete
#find . -type f -name 'propositions.pdf' -delete
#find . -type f -name '*.out.pdf' -delete
