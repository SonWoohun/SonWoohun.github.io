---
layout: archive
title: "Sitemap"
permalink: /sitemap/
author_profile: true
---

{% include base_path %}

A list of all the main pages on this website. For you robots out there, there is an [XML version]({{ base_path }}/sitemap.xml) available for digesting as well.

## Main Navigation

* [Researches]({{ base_path }}/research/)
* [Curriculum Vitae (CV)]({{ base_path }}/cv-json/)
* [Talks]({{ base_path }}/talks/)
* [Teaching]({{ base_path }}/teaching/)

## Other Pages

* [About]({{ base_path }}/about/)
* [Home]({{ base_path }}/)
* [Terms of Use]({{ base_path }}/terms/)

## Research Papers

{% for post in site.research %}
  {% include archive-single-sitemap.html %}
{% endfor %}
