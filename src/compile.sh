#!/bin/bash
pdflatex --interaction=batchmode dissertation
bibtex dissertation
bibtex chapter-introduction/introduction
bibtex chapter-theory/theory
bibtex chapter-experimental-methods/experiment
bibtex chapter-gJJ/gJJ
bibtex chapter-MoRe/moredna
bibtex chapter-AlJJ/AlJJ
bibtex chapter-currentdetection/currentdetection
pdflatex --interaction=batchmode dissertation
pdflatex --interaction=batchmode dissertation