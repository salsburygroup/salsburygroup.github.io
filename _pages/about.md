---
permalink: /
title: "Computational Molecular Biophysics Group"
excerpt: "Physics-based simulation and data-driven analysis of biomolecular structure, dynamics, and function at Wake Forest University."
author_profile: true
redirect_from:
  - /about/
  - /about.html
---

<div class="site-hero site-hero--with-visual">
  <div class="site-hero__content">
    <p class="eyebrow">Wake Forest University · Department of Physics</p>
    <p class="hero-lede">We use molecular simulation, statistical analysis, and machine learning to understand how biomolecules move—and how those motions shape recognition, regulation, and disease.</p>
    <div class="button-row">
      <a class="btn btn--accent" href="/research/">Explore our research</a>
      <a class="btn btn--quiet" href="/people/#opportunities">Join the group</a>
      <a class="btn btn--quiet" href="/shared-resource/">Collaborate</a>
    </div>
  </div>
  <div class="site-hero__visual" aria-hidden="true"></div>
</div>

## From molecular motion to biological mechanism

The Salsbury Group develops and applies physics-based computational methods to proteins, nucleic acids, and small molecules. Our work connects atomistic molecular dynamics with rigorous statistical analysis to identify meaningful motions, allosteric communication, and molecular interactions.

We work at the boundary of molecular physics, biophysics, and data science, often in collaboration with experimental scientists. The goal is not simply to produce simulations, but to turn complex molecular trajectories into testable physical insight.

<div class="feature-grid">
  <article class="feature-card">
    <span class="card-number">01</span>
    <h3>Molecular dynamics</h3>
    <p>Atomistic simulations of biomolecular structure, flexibility, interactions, and rare conformational change.</p>
  </article>
  <article class="feature-card">
    <span class="card-number">02</span>
    <h3>Allostery & regulation</h3>
    <p>How local binding or mutation reshapes communication across proteins and molecular complexes.</p>
  </article>
  <article class="feature-card">
    <span class="card-number">03</span>
    <h3>Data-driven biophysics</h3>
    <p>Statistical and machine-learning approaches for separating robust signals from high-dimensional simulation data.</p>
  </article>
  <article class="feature-card">
    <span class="card-number">04</span>
    <h3>Molecular discovery</h3>
    <p>Computational studies that support drug discovery and mechanistic questions in cancer and other diseases.</p>
  </article>
</div>

<div class="callout-band">
  <div>
    <p class="eyebrow">A collaborative group</p>
    <h2>Physics, computation, and biology in conversation</h2>
    <p>Our projects bring together quantitative modeling and experimental context. We contribute computational expertise to interdisciplinary research and train students to build careful, reproducible analyses.</p>
  </div>
  <a class="text-link" href="/shared-resource/">Shared Resource <span aria-hidden="true">→</span></a>
</div>

## For students, researchers, and collaborators

<div class="feature-grid">
  <article class="feature-card">
    <p class="eyebrow">Join</p>
    <h3><a href="/people/">People & opportunities</a></h3>
    <p>Learn about the group's leadership, training environment, and current public recruiting status.</p>
  </article>
  <article class="feature-card">
    <p class="eyebrow">Collaborate</p>
    <h3><a href="/shared-resource/">Structural biology & drug discovery</a></h3>
    <p>See how computational modeling and simulation connect with the Cancer Center's Shared Resource.</p>
  </article>
  <article class="feature-card">
    <p class="eyebrow">Plan</p>
    <h3><a href="/advising/">Graduate & pre-health advising</a></h3>
    <p>Find official Wake Forest resources and prepare for an advising conversation.</p>
  </article>
  <article class="feature-card">
    <p class="eyebrow">Editorial leadership</p>
    <h3><a href="/jbsd/">Journal of Biomolecular Structure and Dynamics</a></h3>
    <p>Learn about JBSD's scope and Freddie Salsbury's service as Editor-in-Chief.</p>
  </article>
</div>

<div class="social-band">
  <div>
    <p class="eyebrow">Follow our work</p>
    <h2>Research, people, teaching, and journal updates</h2>
  </div>
  <div class="button-row">
    <a class="btn btn--quiet" href="https://www.linkedin.com/in/fred-salsbury-b4114a3/">Freddie Salsbury on LinkedIn <span aria-hidden="true">↗</span></a>
    <a class="btn btn--quiet" href="https://www.linkedin.com/company/jbsd-journal/">JBSD on LinkedIn <span aria-hidden="true">↗</span></a>
  </div>
</div>

## Latest updates

<div class="publication-list update-list update-list--home">
{% for post in site.categories.updates limit:3 %}
  <article class="publication-item update-card update-card--compact">
    <a class="update-card__image" href="{{ post.url | relative_url }}" tabindex="-1" aria-hidden="true">
      <img src="{{ '/images/' | append: post.header.teaser | relative_url }}" alt="" width="1200" height="675" loading="lazy">
    </a>
    <div class="update-card__body">
      <p class="publication-meta"><time datetime="{{ post.date | date_to_xmlschema }}">{{ post.date | date: "%B %-d, %Y" }}</time></p>
      <h3><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h3>
      <p>{{ post.excerpt | strip_html | strip_newlines }}</p>
    </div>
  </article>
{% endfor %}
</div>

<p class="section-link"><a href="/updates/">View all updates <span aria-hidden="true">→</span></a></p>

## Recent and representative work

<div class="publication-list publication-list--compact">
  <article class="publication-item">
    <p class="publication-meta">Journal of Biomolecular Structure and Dynamics</p>
    <h3><a href="https://pubmed.ncbi.nlm.nih.gov/40999894/">K294E Change in the Rotavirus Factory Forming Protein NSP2 Stabilizes a Rare C-Terminal Conformation</a></h3>
  </article>
  <article class="publication-item">
    <p class="publication-meta">The Journal of Physical Chemistry B</p>
    <h3><a href="https://pubmed.ncbi.nlm.nih.gov/39945395/">Impact of Amidation on Aβ25–35 Aggregation</a></h3>
  </article>
  <article class="publication-item">
    <p class="publication-meta">ACS Omega</p>
    <h3><a href="https://pubmed.ncbi.nlm.nih.gov/38826540/">Allosteric Modulation of Thrombin by Thrombomodulin: Insights from Logistic Regression and Statistical Analysis of Molecular Dynamics Simulations</a></h3>
  </article>
</div>

<p class="section-link"><a href="/publications/">View selected publications <span aria-hidden="true">→</span></a></p>
