---
title: "Updates"
permalink: /updates/
excerpt: "Published research and public updates from the Salsbury Computational Molecular Biophysics Group."
author_profile: true
---

Research publications, student achievements, public talks, teaching, and editorial activity will appear here when they are ready for public release. Confidential and unpublished project details are not included.

<div class="publication-list update-list">
{% for post in site.categories.updates %}
  <article class="publication-item">
    <p class="publication-meta"><time datetime="{{ post.date | date_to_xmlschema }}">{{ post.date | date: "%B %-d, %Y" }}</time></p>
    <h2><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h2>
    <p>{{ post.excerpt | strip_html | strip_newlines }}</p>
    <p class="publication-links"><a href="{{ post.url | relative_url }}">Read update</a></p>
  </article>
{% endfor %}
</div>

<div class="callout-band callout-band--small">
  <div>
    <p class="eyebrow">Stay connected</p>
    <h2>Follow public research and journal news</h2>
    <p>Group updates also appear through Freddie Salsbury's professional profile, while JBSD announcements are published through the journal's page.</p>
  </div>
  <div class="button-stack">
    <a class="text-link" href="https://www.linkedin.com/in/fred-salsbury-b4114a3/">Freddie Salsbury on LinkedIn <span aria-hidden="true">↗</span></a>
    <a class="text-link" href="https://www.linkedin.com/company/jbsd-journal/">JBSD on LinkedIn <span aria-hidden="true">↗</span></a>
  </div>
</div>
