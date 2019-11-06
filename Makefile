
.PHONY : all clean

all : dissertation.pdf

view :
	xdg-open dissertation.pdf

dissertation.pdf : dissertation.tex dissertation.bib
	pdflatex --interaction=batchmode dissertation.tex
	bibtex dissertation.aux
	bibtex chapter-introduction/introduction.aux
	bibtex chapter-theory/theory.aux
	bibtex chapter-experimental-methods/experiment.aux
	bibtex chapter-gJJ/gJJ.aux
	bibtex chapter-MoRe/moredna.aux
	bibtex chapter-AlJJ/AlJJ.aux
	bibtex chapter-currentdetection/currentdetection.aux
	pdflatex --interaction=batchmode dissertation.tex
	pdflatex --interaction=batchmode dissertation.tex

propositions.pdf :
	xelatex --interaction=batchmode propositions
	xelatex --interaction=batchmode propositions


clean :
	rm -f *.pdf *.out *aux *bbl *blg *log *toc *.ptb *.tod *.fls *.fdb_latexmk *.lof
