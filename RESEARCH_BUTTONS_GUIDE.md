# Research Download Buttons Setup

## ✅ What's Been Implemented

### Enhanced Research Display
Your research tab now features professional download buttons for:
- **Download Paper** (blue button with PDF icon)
- **Download Slides** (light blue button with PowerPoint icon) 
- **BibTeX** (gray button with quote icon)

### Visual Improvements
- **Research badges**: "Working Paper" and "Work in Progress" labels
- **Tags display**: Shows research keywords
- **Better spacing**: Clean separation between research items
- **Mobile responsive**: Buttons stack on small screens

## 📁 Required File Structure

### Research Front Matter
Each research file needs these fields for download buttons:

```yaml
---
title: "Your Paper Title"
collection: research
category: working_paper  # or work_in_progress
permalink: /research/2025-08-05-paper-name
excerpt: 'Brief description'
date: 2025-08-05
paperurl: 'http://SonWoohun.github.io/files/paper.pdf'        # Optional
slidesurl: 'http://SonWoohun.github.io/files/slides.pdf'      # Optional
bibtexurl: 'http://SonWoohun.github.io/files/citation.bib'    # Optional
tags:
  - tag1
  - tag2
---
```

### File Upload Location
Upload your files to the `files/` directory:
```
files/
├── AttBlurAds_draft2025Mar30.pdf
├── NCL_slides2025Apr7.pdf
├── ads_main.bib
├── IdentUnobsBudg2025Jul14.pdf
├── UnobsBudget_draft2025Aug1.pdf
└── main.bib
```

## 🎨 Button Styling

### Button Colors
- **Download Paper**: Blue (#3f51b5) - Primary action
- **Download Slides**: Light Blue (#2196f3) - Secondary action  
- **BibTeX**: Gray (#6c757d) - Utility action

### Icons
- **Paper**: PDF icon (`fa-file-pdf-o`)
- **Slides**: PowerPoint icon (`fa-file-powerpoint-o`)
- **BibTeX**: Quote icon (`fa-quote-left`)

## ✨ Features

### Automatic Display
Buttons only appear when the corresponding URL is provided:
- No `paperurl` = no paper button
- No `slidesurl` = no slides button
- No `bibtexurl` = no BibTeX button

### Target Blank
All download links open in new tabs/windows for better user experience.

### Research Categories
- **Working Papers**: Green "Working Paper" badge
- **Work in Progress**: Yellow "Work in Progress" badge

### Tags
Research tags appear below the download buttons as small gray labels.

## 🔧 Customization

### To Change Button Colors
Edit `_sass/custom-research.scss`:
```scss
.archive__item-links .btn--info {
  background-color: #your-color;
}
```

### To Add New Button Types
1. Add new field to research file front matter
2. Add button logic to `_includes/archive-single-research.html`
3. Add styling to `_sass/custom-research.scss`

## 📱 Mobile Responsive
On mobile devices:
- Buttons stack vertically
- Full width for easy tapping
- Tags display as blocks

Your research tab now provides a professional presentation of your academic work with easy access to papers, slides, and citations!
