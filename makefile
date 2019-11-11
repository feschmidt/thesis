.PHONY: all

SHELL=/bin/bash

all: 
	bash src/compile.sh
	bash src/compress.sh

compile:
	bash src/compile.sh

view:
	xdg-open dissertation.pdf

view2:
	xdg-open dissertation.out.pdf

compress:
	bash src/compress.sh

clean:
	bash src/cleanup.sh