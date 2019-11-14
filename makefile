
.PHONY: force-build

all: dissertation.pdf

force-build:

dissertation.pdf: force-build
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

propositions.pdf: force-build
	xelatex propositions
	xelatex propositions


view:
	xdg-open dissertation.pdf

view2:
	xdg-open dissertation.out.pdf

compress:
	bash src/compress.sh

clean:
	bash src/cleanup.sh