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
    name = escape_latex(basics.get('name', ''))
    email = escape_latex(basics.get('email', ''))
    website = escape_latex(basics.get('website', ''))
    location = basics.get('location', {})
    city = escape_latex(location.get('city', ''))
    region = escape_latex(location.get('region', ''))
    phone = escape_latex(basics.get('phone', ''))
    
    # Get GitHub profile
    github_url = ""
    profiles = basics.get('profiles', [])
    for profile in profiles:
        if profile.get('network') == 'GitHub' and profile.get('url'):
            github_url = escape_latex(profile.get('url', ''))
            break
    
    latex_content = r"""% LaTeX Curriculum Vitae Template
% Based on Jason Blevins' CV template
% Adapted for automated generation from JSON data

\documentclass[letterpaper]{article}

\usepackage{hyperref}
\usepackage{geometry}

% Use Palatino font for a professional look
\usepackage[T1]{fontenc}
\usepackage[sc,osf]{mathpazo}

% Set your name here
\def\name{""" + name + r"""}

% Set footer link
\def\footerlink{""" + website + r"""}

% PDF metadata
\hypersetup{
  colorlinks = true,
  urlcolor = black,
  pdfauthor = {\name},
  pdfkeywords = {economics, research, academic},
  pdftitle = {\name: Curriculum Vitae},
  pdfsubject = {Curriculum Vitae},
  pdfpagemode = UseNone
}

% Page geometry
\geometry{
  body={6.5in, 8.5in},
  left=1.0in,
  top=1.25in
}

% Customize page headers
\pagestyle{myheadings}
\markright{\name}
\thispagestyle{empty}

% Custom section fonts
\usepackage{sectsty}
\sectionfont{\rmfamily\mdseries\Large}
\subsectionfont{\rmfamily\mdseries\itshape\large}

% Don't indent paragraphs
\setlength\parindent{0em}

% Make lists without bullets
\renewenvironment{itemize}{
  \begin{list}{}{
    \setlength{\leftmargin}{1.5em}
  }
}{
  \end{list}
}

\begin{document}

% Place name at left
{\huge \name}

\vspace{0.25in}

\begin{minipage}{0.45\linewidth}"""

    # Add current institution (first education entry or first work entry)
    education = cv_data.get('education', [])
    work = cv_data.get('work', [])
    
    if education:
        current_institution = escape_latex(education[0].get('institution', ''))
        latex_content += f"\n  {current_institution} \\\\"
        
        # Try to extract department/area info
        area = escape_latex(education[0].get('area', ''))
        if area:
            latex_content += f"\n  {area} \\\\"
    elif work:
        current_institution = escape_latex(work[0].get('company', ''))
        latex_content += f"\n  {current_institution} \\\\"
    
    # Add location info
    if city and region:
        latex_content += f"\n  {city}, {region}"
    
    latex_content += r"""
\end{minipage}
\begin{minipage}{0.45\linewidth}
  \begin{tabular}{ll}"""

    # Add contact information
    if phone:
        latex_content += f"\n    Phone: & {phone} \\\\"
    
    if email:
        latex_content += f"\n    Email: & \\href{{mailto:{email}}}{{\\tt {email}}} \\\\"
    
    if website:
        latex_content += f"\n    Homepage: & \\href{{{website}}}{{\\tt {website}}} \\\\"
    
    if github_url:
        latex_content += f"\n    GitHub: & \\href{{{github_url}}}{{\\tt {github_url}}} \\\\"

    latex_content += r"""
  \end{tabular}
\end{minipage}

"""

    # Education section
    education = cv_data.get('education', [])
    if education:
        latex_content += r"""
\section*{Education}

\begin{itemize}
"""
        for edu in education:
            institution = escape_latex(edu.get('institution', ''))
            area = escape_latex(edu.get('area', ''))
            end_date = escape_latex(edu.get('endDate', ''))
            
            if area and institution and end_date:
                latex_content += f"  \\item {area}, {institution}, {end_date}.\n"
            elif area and institution:
                latex_content += f"  \\item {area}, {institution}.\n"
            elif institution:
                latex_content += f"  \\item {institution}.\n"
        
        latex_content += r"""\end{itemize}

"""

    # Work Experience section
    work = cv_data.get('work', [])
    if work:
        latex_content += r"""
\section*{Employment}

\begin{itemize}
"""
        for job in work:
            company = escape_latex(job.get('company', ''))
            position = escape_latex(job.get('position', ''))
            start_date = escape_latex(job.get('startDate', ''))
            end_date = escape_latex(job.get('endDate', ''))
            
            # Format date range
            if start_date and end_date:
                date_str = f"{start_date}--{end_date}"
            elif start_date:
                date_str = f"{start_date}--Present"
            elif end_date:
                date_str = end_date
            else:
                date_str = ""
            
            if position and company and date_str:
                latex_content += f"\\item {position}, {company}, {date_str}.\n"
            elif position and company:
                latex_content += f"\\item {position}, {company}.\n"
            elif company:
                latex_content += f"\\item {company}.\n"
        
        latex_content += r"""\end{itemize}

"""

    # Teaching section
    teaching = cv_data.get('teaching', [])
    if teaching:
        latex_content += r"""
\section*{Teaching}

\begin{itemize}
"""
        for teach in teaching:
            course = escape_latex(teach.get('course', ''))
            institution = escape_latex(teach.get('institution', ''))
            role = escape_latex(teach.get('role', ''))
            description = escape_latex(teach.get('description', ''))
            
            if course and role and description:
                latex_content += f"\\item {role}, {course}, {description}.\n"
            elif course and role:
                latex_content += f"\\item {role}, {course}.\n"
            elif course:
                latex_content += f"\\item {course}.\n"
        
        latex_content += r"""\end{itemize}

"""

    # Publications section (if any)
    publications = cv_data.get('publications', [])
    if publications:
        latex_content += r"""
\section*{Publications}

\subsection*{Journal Articles}

\begin{itemize}
"""
        for pub in publications:
            name = escape_latex(pub.get('name', ''))
            publisher = escape_latex(pub.get('publisher', ''))
            release_date = escape_latex(pub.get('releaseDate', ''))
            summary = escape_latex(pub.get('summary', ''))
            
            if name and publisher and release_date:
                latex_content += f"\\item {name}, {release_date}, {{\\it {publisher}}}.\n"
            elif name and publisher:
                latex_content += f"\\item {name}, {{\\it {publisher}}}.\n"
            elif name:
                latex_content += f"\\item {name}.\n"
        
        latex_content += r"""\end{itemize}

"""

    # Awards section (if any)
    awards = cv_data.get('awards', [])
    if awards and any(award for award in awards if award):  # Check if awards has non-empty entries
        latex_content += r"""
\section*{Awards and Honors}

\begin{itemize}
"""
        for award in awards:
            if award:  # Skip empty award objects
                title = escape_latex(award.get('title', ''))
                date = escape_latex(award.get('date', ''))
                awarder = escape_latex(award.get('awarder', ''))
                
                if title and date and awarder:
                    latex_content += f"\\item {title}, {awarder}, {date}.\n"
                elif title and date:
                    latex_content += f"\\item {title}, {date}.\n"
                elif title:
                    latex_content += f"\\item {title}.\n"
        
        latex_content += r"""\end{itemize}

"""

    # Languages section
    languages = cv_data.get('languages', [])
    if languages:
        latex_content += r"""
\section*{Languages}

\begin{itemize}
"""
        for lang in languages:
            name = escape_latex(lang.get('name', ''))
            fluency = escape_latex(lang.get('fluency', ''))
            
            if name and fluency:
                latex_content += f"\\item {name} ({fluency}).\n"
            elif name:
                latex_content += f"\\item {name}.\n"
        
        latex_content += r"""\end{itemize}

"""

    # Footer
    latex_content += r"""
\bigskip

% Footer
\begin{center}
  \begin{footnotesize}
    Last updated: \today \\
    \href{\footerlink}{\texttt{\footerlink}}
  \end{footnotesize}
\end{center}

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
