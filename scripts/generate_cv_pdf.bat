@echo off
echo Generating CV PDF...
cd /d "%~dp0"
py generate_cv_pdf.py
pause
