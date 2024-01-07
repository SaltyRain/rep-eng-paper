.PHONY: all clean
JOB = paper

all: $(JOB).pdf

$(JOB).pdf: $(JOB).tex literature.bib paper.py
	python3 paper.py

clean:
	rm -rfv $(JOB).pdf *.log *.aux *.bbl *.bcf *.blg *.out *.run.xml *.tex
