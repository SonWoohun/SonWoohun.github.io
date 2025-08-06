#!/usr/bin/env python3
"""
Generate LaTeX CV from cv.json data
"""
import json
import os
from datetime import datetime

def load_cv_data():
    """Load CV data from JSON file"""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    cv_path = os.path.join(script_dir, '..', '_data', 'cv.json')
    
    with open(cv_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def escape_latex(text):
    """Escape special LaTeX characters"""
    if not text:
        return ""
    
    # Replace special characters
    replacements = {
        '&': r'\&',
        '%': r'\%',
        '$': r'\$',
        '#': r'\#',
        '^': r'\textasciicircum{}',
        '_': r'\_',
        '{': r'\{',
        '}': r'\}',
        '~': r'\textasciitilde{}',
        '\\': r'\textbackslash{}'
    }
    
    for char, replacement in replacements.items():
        text = text.replace(char, replacement)
    
    return text

def format_date_range(start_date, end_date):
    """Format date range for display"""
    if not start_date and not end_date:
        return ""
    
    start_str = start_date if start_date else ""
    end_str = end_date if end_date else "Present"
    
    if start_str and end_str:
        return f"{start_str} -- {end_str}"
    elif end_str:
        return end_str
    else:
        return start_str

def generate_latex_cv(cv_data):
    """Generate LaTeX content from CV data"""
    
    basics = cv_data.get('basics', {})
    
    latex_content = r"""
\documentclass[11pt,a4paper,sans]{moderncv}

% ModernCV themes
\moderncvstyle{classic}
\moderncvcolor{blue}

% Character encoding
\usepackage[utf8]{inputenc}

% Adjust page margins
\usepackage[scale=0.75]{geometry}

% Personal data
\name{""" + escape_latex(basics.get('name', '')) + r"""}{}
\title{""" + escape_latex(basics.get('summary', '')) + r"""}
\address{""" + escape_latex(basics.get('location', {}).get('city', '')) + r"""}{""" + escape_latex(basics.get('location', {}).get('region', '')) + r"""}{""" + escape_latex(basics.get('location', {}).get('countryCode', '')) + r"""}
\phone[mobile]{""" + escape_latex(basics.get('phone', '')) + r"""}
\email{""" + escape_latex(basics.get('email', '')) + r"""}
\homepage{""" + escape_latex(basics.get('website', '')) + r"""}
"""

    # Add GitHub profile if available
    profiles = basics.get('profiles', [])
    for profile in profiles:
        if profile.get('network') == 'GitHub' and profile.get('url'):
            latex_content += r"\social[github]{" + escape_latex(profile.get('username', '')) + r"}"
            break

    latex_content += r"""

\begin{document}
\makecvtitle

"""

    # Education section
    education = cv_data.get('education', [])
    if education:
        latex_content += r"""
\section{Education}
"""
        for edu in education:
            institution = escape_latex(edu.get('institution', ''))
            area = escape_latex(edu.get('area', ''))
            date_range = format_date_range(edu.get('startDate', ''), edu.get('endDate', ''))
            
            latex_content += r"\cventry{" + escape_latex(date_range) + r"}{" + area + r"}{" + institution + r"}{}{}{}" + "\n"

    # Work Experience section
    work = cv_data.get('work', [])
    if work:
        latex_content += r"""
\section{Experience}
"""
        for job in work:
            company = escape_latex(job.get('company', ''))
            position = escape_latex(job.get('position', ''))
            date_range = format_date_range(job.get('startDate', ''), job.get('endDate', ''))
            summary = escape_latex(job.get('summary', ''))
            
            highlights = job.get('highlights', [])
            highlights_str = ""
            if highlights:
                highlights_str = r"\begin{itemize}" + "\n"
                for highlight in highlights:
                    highlights_str += r"\item " + escape_latex(highlight) + "\n"
                highlights_str += r"\end{itemize}"
            
            latex_content += r"\cventry{" + escape_latex(date_range) + r"}{" + position + r"}{" + company + r"}{}{" + summary + r"}{" + highlights_str + r"}" + "\n"

    # Teaching section
    teaching = cv_data.get('teaching', [])
    if teaching:
        latex_content += r"""
\section{Teaching Experience}
"""
        for teach in teaching:
            course = escape_latex(teach.get('course', ''))
            institution = escape_latex(teach.get('institution', ''))
            role = escape_latex(teach.get('role', ''))
            date = escape_latex(teach.get('date', ''))
            description = escape_latex(teach.get('description', ''))
            
            latex_content += r"\cventry{" + date + r"}{" + role + r"}{" + course + r"}{" + institution + r"}{}{" + description + r"}" + "\n"

    # Languages section
    languages = cv_data.get('languages', [])
    if languages:
        latex_content += r"""
\section{Languages}
"""
        for lang in languages:
            name = escape_latex(lang.get('name', ''))
            fluency = escape_latex(lang.get('fluency', ''))
            latex_content += r"\cvitemwithcomment{" + name + r"}{" + fluency + r"}{}" + "\n"

    latex_content += r"""
\end{document}
"""
    
    return latex_content

def main():
    """Main function"""
    try:
        # Load CV data
        cv_data = load_cv_data()
        
        # Generate LaTeX content
        latex_content = generate_latex_cv(cv_data)
        
        # Write to files directory
        script_dir = os.path.dirname(os.path.abspath(__file__))
        output_path = os.path.join(script_dir, '..', 'files', 'cv.tex')
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(latex_content)
        
        print(f"LaTeX CV generated successfully: {output_path}")
        
    except Exception as e:
        print(f"Error generating LaTeX CV: {e}")
        return 1
    
    return 0

if __name__ == "__main__":
    exit(main())
