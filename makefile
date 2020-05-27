
.PHONY: force-build

all: diss props

force-build:

diss: dissertation.pdf
	pdflatex dissertation.tex
	bibtex dissertation.aux
	pdflatex --interaction=batchmode dissertation.tex
	pdflatex dissertation.tex
	make viewdiss

props: propositions.pdf
	pdflatex propositions.tex
	make viewprops

viewall: viewdiss viewprops

viewdiss:
	open dissertation.pdf &

viewprops:
	open propositions.pdf &

compress:
	bash src/compress.sh

clean:
	bash src/cleanup.sh

testdiss: dissertation.pdf
	pdflatex --interaction=batchmode dissertation.tex
	bibtex dissertation.aux