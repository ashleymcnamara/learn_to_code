# Maintenance Guide

This repo should stay useful because it is curated, reviewed, and honest about
cost. A smaller current guide is better than a huge stale guide.

## Review Cadence

- Monthly: fix reported broken links and obvious outdated notes.
- Quarterly: review one major section, such as AI, web, Python, or university
  OpenCourseWare.
- Quarterly: review the high-priority starter resources in
  [resources.yml](resources.yml).
- Yearly: do a broad research pass and update the README's "Last major research
  pass" date.

## Review Checklist

When reviewing a resource, check:

- Does the link still work?
- Is the material still free, free-audit, or accurately labeled?
- Has the course moved, archived, or become paywalled?
- For books, is the linked edition official or otherwise legitimate?
- If a paid book is included, is it still widely recommended and worth the cost?
- Are prerequisites clear?
- Is the content still technically current?
- Does it overlap with a better listed resource?
- Would a beginner know why to choose it?
- Would a career switcher with no technical background know where to start?
- Does the description sound like a human recommendation rather than marketing
  copy or unedited AI text?
- Does it have surprise costs, such as API usage, cloud compute, or paid
  certificates?
- Is the submission promotional, affiliated, or selling a paid course rather
  than helping learners?
- For YouTube, is the suggested item educational on its own, or mainly a funnel
  into a paid product?
- If this is a starter resource, is [resources.yml](resources.yml) updated?

## Stale Resource Signals

Consider replacing or annotating a resource when:

- the last visible update is many years old and the topic changes quickly
- install steps no longer work
- the resource teaches unsupported versions by default
- links have moved to an archive
- the free tier has been removed
- the resource now pushes learners toward a paid subscription before teaching
  the core material
- the submitter appears to be using the repo for course, bootcamp, coaching,
  newsletter, app, community, or subscription marketing
- a YouTube channel shifts from educational videos to mostly promotional funnel
  content
- the README entry becomes vague, inflated, or generic enough that it no longer
  helps a learner choose
- an unofficial PDF is being used for a book that is not legally free

Do not remove classic books or courses only because they are old. Fundamentals
resources can age well. Add context instead.

## Section Priorities

Fast-changing sections:

- AI and Machine Learning
- Web Development
- Developer Tools
- Data Engineering
- Career and Community

Slower-changing sections:

- Books and Textbooks
- Discrete Math
- Algorithms and Data Structures
- Operating Systems
- Compilers
- Programming Language Theory

## Adding University Courses

Prefer course pages that include at least two of:

- lecture notes or slides
- video lectures
- assignments or projects
- readings
- exams or practice problems
- public textbook or companion site

Clearly label courses where current materials require student login but older
public materials are still useful.

## Adding AI Resources

AI resources should be reviewed more often than most sections. Prefer official
docs and open-source curricula from credible organizations. Always note when a
resource may require:

- API keys
- paid model usage
- cloud credits
- GPUs
- account signup
- uploading private data

For AI coding assistants, emphasize that learners should understand, test, and
explain generated code.

## Link Checking

Run the local structural check:

```bash
python scripts/check_links.py --include-resources
```

Run the online link check:

```bash
python scripts/check_links.py --online --include-resources
```

The GitHub Actions workflow in `.github/workflows/link-check.yml` runs the
online check on pull requests, on demand, and monthly. A few sites are
browser-verified but block command-line checks; keep those in the script's
`BROWSER_ONLY_URLS` allowlist only when you have manually verified them.
