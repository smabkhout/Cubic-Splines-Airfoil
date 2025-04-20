
.PHONY: clean rapport


all: rapport

rapport:
	pdflatex rapport/rapport.tex
	pdflatex rapport/rapport.tex
	evince rapport.pdf&

clean:
	find . -name "*.log" -delete
	find . -name "*.aux" -delete
	find . -name "*~" -delete
	find . -name "*.pdf" -delete
	find . -name "*.out" -delete
