#!/bin/bash
pdflatex dissertation #--interaction=batchmode
bibtex dissertation #bash src/dobib.sh
pdflatex dissertation
pdflatex dissertation
