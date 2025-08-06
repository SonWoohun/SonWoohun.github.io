#!/usr/bin/env python3
"""
Generate CV PDF locally (requires LaTeX installation)
"""
import os
import subprocess
import sys

def run_command(cmd, cwd=None):
    """Run a shell command and return success status"""
    try:
        result = subprocess.run(cmd, shell=True, cwd=cwd, check=True, 
                              capture_output=True, text=True)
        print(f"✓ {cmd}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"✗ {cmd}")
        print(f"Error: {e.stderr}")
        return False

def main():
    """Main function"""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    repo_root = os.path.dirname(script_dir)
    files_dir = os.path.join(repo_root, 'files')
    
    print("Generating CV PDF...")
    
    # Step 1: Generate LaTeX from JSON
    print("\n1. Generating LaTeX from CV JSON...")
    if not run_command("python generate_cv_tex.py", cwd=script_dir):
        print("Failed to generate LaTeX file")
        return 1
    
    # Step 2: Check if LaTeX is installed
    print("\n2. Checking LaTeX installation...")
    if not run_command("pdflatex --version"):
        print("LaTeX (pdflatex) not found. Please install LaTeX:")
        print("- Windows: Install MiKTeX or TeX Live")
        print("- macOS: Install MacTeX")
        print("- Linux: sudo apt-get install texlive-latex-extra")
        return 1
    
    # Step 3: Compile LaTeX to PDF
    print("\n3. Compiling LaTeX to PDF...")
    tex_file = os.path.join(files_dir, 'cv.tex')
    
    if not os.path.exists(tex_file):
        print(f"LaTeX file not found: {tex_file}")
        return 1
    
    # Run pdflatex twice for proper formatting
    if not run_command("pdflatex cv.tex", cwd=files_dir):
        print("Failed to compile LaTeX to PDF")
        return 1
    
    if not run_command("pdflatex cv.tex", cwd=files_dir):
        print("Failed to compile LaTeX to PDF (second pass)")
        return 1
    
    # Step 4: Clean up auxiliary files
    print("\n4. Cleaning up auxiliary files...")
    aux_extensions = ['.aux', '.log', '.out', '.toc', '.nav', '.snm']
    for ext in aux_extensions:
        aux_file = os.path.join(files_dir, f'cv{ext}')
        if os.path.exists(aux_file):
            os.remove(aux_file)
            print(f"Removed {aux_file}")
    
    # Step 5: Check result
    pdf_file = os.path.join(files_dir, 'cv.pdf')
    if os.path.exists(pdf_file):
        print(f"\n✓ CV PDF generated successfully: {pdf_file}")
        return 0
    else:
        print("\n✗ PDF file was not created")
        return 1

if __name__ == "__main__":
    exit(main())
