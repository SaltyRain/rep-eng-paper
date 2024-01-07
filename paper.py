import subprocess
import os

# Define the paths to your .tex and .bib files
tex_file = 'paper.tex'
bib_file = 'literature.bib'

# Define the output directory
output_dir = './output'

# Ensure the output directory exists
os.makedirs(output_dir, exist_ok=True)

# Compile the .tex file into a PDF
# This often needs to be run multiple times to resolve references,
# especially when using .bib files for bibliography

# Run pdflatex or xelatex or lualatex depending on your document
subprocess.run(['pdflatex', '-output-directory', output_dir, tex_file])
# Run biber
subprocess.run(['biber', os.path.splitext(os.path.basename(tex_file))[0]], cwd=output_dir)
# Run pdflatex again to update document references and citations
subprocess.run(['pdflatex', '-output-directory', output_dir, tex_file])
# Run pdflatex again to ensure all references are updated
subprocess.run(['pdflatex', '-output-directory', output_dir, tex_file])

print("Compilation done. Check the output directory for the PDF.")
