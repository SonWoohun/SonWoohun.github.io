# Research Tab Setup - Complete Configuration

## ✅ What Has Been Fixed

### 1. **Collection Configuration**
Added `research` collection to `_config.yml`:
```yaml
collections:
  research:
    output: true
    permalink: /:collection/:path/
```

### 2. **Default Settings**
Added research collection defaults to `_config.yml`:
```yaml
# _research
- scope:
    path: ""
    type: research
  values:
    layout: single
    author_profile: true
    share: true
    comments: true
```

### 3. **Research Categories**
Already defined in `_config.yml`:
```yaml
research_category:
  working_paper:
    title: 'Working Papers'
  work_in_progress:
    title: 'Work in Progress'
```

### 4. **Research Page**
Updated `_pages/research.html`:
- Changed title from "Working Papers" to "Research"
- Changed permalink from `/research/working_papers/` to `/research/`
- Uses the same categorization logic as publications

### 5. **Navigation**
Already correctly set up in `_data/navigation.yml`:
```yaml
- title: "Researches"
  url: /research/
```

## 📁 File Structure

### Research Files in `_research/` folder:
```
_research/
├── 2025-08-05-unobs-budget.md (working_paper)
└── 2025-08-06-attention-positioning.md (work_in_progress)
```

### Required Front Matter Format:
```yaml
---
title: "Your Paper Title"
collection: research
category: working_paper  # or work_in_progress
permalink: /research/2025-08-05-paper-name
excerpt: 'Brief description of the paper'
date: 2025-08-05
---
```

## 🎯 How It Works

### Categories Display:
1. **Working Papers** - Research papers that are complete drafts
2. **Work in Progress** - Research in early stages

### Same as Publications:
- Uses identical categorization system
- Same archive layout and styling
- Same front matter structure
- Same navigation pattern

## 🚀 Adding New Research

### For Working Papers:
```yaml
---
title: "Your Working Paper Title"
collection: research
category: working_paper
permalink: /research/2025-MM-DD-short-name
excerpt: 'Brief description'
date: 2025-MM-DD
---
```

### For Work in Progress:
```yaml
---
title: "Your Work in Progress Title"
collection: research
category: work_in_progress
permalink: /research/2025-MM-DD-short-name
excerpt: 'Brief description'
date: 2025-MM-DD
---
```

## 📋 Next Steps

1. **Test the site**: Your research tab should now work exactly like publications
2. **Add your real research**: Replace the sample files with your actual research
3. **Customize categories**: You can modify the category names in `_config.yml` if needed

## 🔧 Troubleshooting

If research items don't appear:
1. Check that front matter uses `collection: research`
2. Verify category matches one in `research_category`
3. Ensure files are in `_research/` folder
4. Restart Jekyll server after config changes

Your research tab should now function identically to your publications tab with proper categorization!
