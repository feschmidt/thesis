#!/bin/bash
pdflatex --interaction=batchmode dissertation
bash src/dobib.sh
pdflatex --interaction=batchmode dissertation
pdflatex --interaction=batchmode dissertation
