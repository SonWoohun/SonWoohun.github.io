# SEO Setup Guide for Your Academic Website

## Quick Setup Checklist

### ✅ Completed Automatically:
- [x] Robots.txt file created
- [x] Structured data (JSON-LD) for academic profile
- [x] Enhanced sitemap
- [x] Social media meta tags
- [x] SEO-optimized About page
- [x] Research and Publications pages optimized

### 🔧 Manual Setup Required:

## 1. Google Search Console Setup

1. **Go to** [Google Search Console](https://search.google.com/search-console)
2. **Add your property**: `https://SonWoohun.github.io`
3. **Choose verification method**: HTML tag method
4. **Copy the verification code** (looks like: `google1234567890abcdef.html`)
5. **Add to _config.yml**:
   ```yaml
   google_site_verification: "your-verification-code-here"
   ```

## 2. Submit Your Sitemap

After verification:
1. In Google Search Console, go to **Sitemaps**
2. Submit: `https://SonWoohun.github.io/sitemap.xml`

## 3. Google Scholar Profile

1. **Create** [Google Scholar profile](https://scholar.google.com/citations)
2. **Add your papers** as they become available
3. **Update _config.yml**:
   ```yaml
   googlescholar: "https://scholar.google.com/citations?user=YOUR_ID"
   ```

## 4. ORCID Setup

1. **Register** at [ORCID.org](https://orcid.org)
2. **Add your works** and education
3. **Update _config.yml**:
   ```yaml
   orcid: "http://orcid.org/0000-0000-0000-0000"
   ```

## 5. Content SEO Best Practices

### Research Papers:
- Use descriptive titles with keywords
- Include detailed abstracts
- Add relevant tags and categories
- Link to paper PDFs when available

### Regular Content Updates:
- Add new research regularly
- Update CV and publications
- Write about your research progress
- Share conference presentations

## 6. Monitor Your SEO

### Tools to Use:
- **Google Search Console**: Track search performance
- **Google Analytics**: Monitor website traffic  
- **PageSpeed Insights**: Check site speed
- **Google Scholar**: Track citations

### Key Metrics:
- Search impressions and clicks
- Average position in search results
- Pages indexed by Google
- Site loading speed

## 7. Academic Keywords to Target

Based on your research, target these keywords:
- "Industrial organization economics"
- "Limited attention consumer behavior"
- "Discrete choice models budget constraints"
- "Applied econometrics Ohio State"
- "Decision theory research"
- "Advertising economics attention"

## Expected Timeline

- **Week 1**: Google Search Console verification and sitemap submission
- **Weeks 2-4**: Initial indexing of your pages
- **Month 2-3**: Start appearing in search results for your name
- **Month 3-6**: Ranking for academic keywords as you add more content

## Advanced Tips

1. **Internal Linking**: Link between your research papers and CV
2. **External Links**: Link to your university profile and co-authors
3. **Mobile Optimization**: Your site is already mobile-friendly
4. **Loading Speed**: GitHub Pages is already fast
5. **Content Freshness**: Update regularly with new research

Your website is now optimized for search engines with proper structured data, meta tags, and academic-focused content!
