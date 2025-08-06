# CV Generation System

This repository includes an automated system to generate LaTeX and PDF versions of your CV from the JSON data in `_data/cv.json`.

## Files

- `_data/cv.json` - Your CV data in JSON format
- `scripts/generate_cv_tex.py` - Python script to generate LaTeX from JSON
- `scripts/generate_cv_pdf.py` - Python script to generate PDF locally
- `scripts/generate_cv_pdf.bat` - Windows batch script for easy PDF generation
- `files/cv.tex` - Generated LaTeX file
- `files/cv.pdf` - Generated PDF file (auto-created)
- `.github/workflows/generate-cv.yml` - GitHub Action for automatic PDF generation

## Automatic Generation (GitHub Actions)

The system automatically generates a new PDF whenever you:
1. Push changes to `_data/cv.json`
2. Push changes to the generation scripts
3. Manually trigger the workflow

The GitHub Action will:
1. Generate the LaTeX file from your JSON data
2. Compile it to PDF using LaTeX
3. Commit the updated files back to the repository

## Local Generation

### Prerequisites

For local PDF generation, you need:
1. Python 3.x
2. LaTeX distribution (pdflatex):
   - **Windows**: Install [MiKTeX](https://miktex.org/) or [TeX Live](https://www.tug.org/texlive/)
   - **macOS**: Install [MacTeX](https://www.tug.org/mactex/)
   - **Linux**: `sudo apt-get install texlive-latex-extra texlive-fonts-recommended`

### Generate LaTeX only

```bash
cd scripts
python generate_cv_tex.py
```

### Generate PDF locally

```bash
cd scripts
python generate_cv_pdf.py
```

Or on Windows, double-click `generate_cv_pdf.bat`

## Customizing the CV

### Editing Content

Edit `_data/cv.json` to update your CV content. The file follows the [JSON Resume](https://jsonresume.org/) schema.

### Customizing LaTeX Template

Modify `scripts/generate_cv_tex.py` to:
- Change the LaTeX document class or packages
- Modify the CV layout and styling
- Add or remove sections
- Change formatting

### Available ModernCV Styles

You can change the CV style by modifying the `\moderncvstyle{}` line in the generator:
- `classic` - Traditional CV style
- `casual` - More relaxed style
- `oldstyle` - Conservative style
- `banking` - Professional banking style

### Available Colors

Change `\moderncvcolor{}` to:
- `blue`, `orange`, `green`, `red`, `purple`, `grey`, `black`

## Troubleshooting

### LaTeX Compilation Errors

If you get LaTeX errors:
1. Check that all special characters in your JSON are properly formatted
2. Ensure dates are in a consistent format
3. Look at the generated `.log` file in the `files/` directory for detailed error messages

### GitHub Action Fails

If the GitHub Action fails:
1. Check the Actions tab for detailed error logs
2. Ensure your JSON syntax is valid
3. Check that you haven't exceeded GitHub's usage limits

### Missing Packages

If you get "package not found" errors, install additional LaTeX packages:
```bash
# Ubuntu/Debian
sudo apt-get install texlive-full

# Or specific packages
sudo apt-get install texlive-latex-extra texlive-fonts-recommended
```

## Examples

### Adding a New Publication

Add to the `publications` array in `cv.json`:
```json
{
  "name": "Paper Title",
  "publisher": "Journal Name",
  "releaseDate": "2023",
  "website": "https://doi.org/...",
  "summary": "Brief description"
}
```

### Adding Awards

Replace the empty `awards` object:
```json
"awards": [
  {
    "title": "Best Paper Award",
    "date": "2023",
    "awarder": "Conference Name",
    "summary": "Description of the award"
  }
]
```

## LaTeX Output

The generated LaTeX uses the `moderncv` class, which creates professional-looking academic CVs. The output includes:

- Personal information header
- Education (reverse chronological)
- Work experience with highlights
- Teaching experience
- Publications (if any)
- Awards (if any)
- Languages

The PDF is automatically formatted and ready for professional use.
