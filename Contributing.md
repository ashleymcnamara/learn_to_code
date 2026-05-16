# Contributing

Thank you for helping improve Learn to Code.

This project is a curated, free-first guide for people learning programming,
computer science, AI, and developer tools. It is not meant to be a complete
directory of every course, book, video, or tutorial.

Please write like a person helping another person choose a path. Short, specific
descriptions are better than polished marketing copy.

It is also not an advertising channel. Please do not submit paid courses,
bootcamps, coaching programs, newsletters, communities, apps, or subscription
products that you sell or market. Courses and tutorials should be free, or free
to audit in a way that gives learners access to the core material without
payment.

Free YouTube videos, playlists, and full courses are welcome when they are
education-first. Normal platform ads or occasional sponsorships are okay, but do
not submit videos that mainly funnel learners into a paid course, bootcamp,
private community, or subscription.

Books are the main paid exception. Highly regarded books that must be purchased
can be included when they are clearly labeled and linked to official author or
publisher pages.

## Good Contributions

Good pull requests usually do one of these things:

- add one high-quality free or free-audit resource
- add one high-quality free video course, lecture series, or YouTube playlist
- add one high-quality free book, open textbook, or highly regarded paid book
- replace an outdated resource with a better current one
- update a resource's cost, maintenance, or prerequisite note
- improve wording for clarity, accuracy, or accessibility
- reorganize a section so beginners can make better decisions
- fix spelling, formatting, duplicate entries, or broken links
- update [resources.yml](resources.yml) for high-priority starter resources

## Resource Guidelines

Before adding a resource, check that it is:

- free-first, or clearly labeled if payment is required
- beginner-friendly, or clearly labeled as intermediate or advanced
- actively maintained or still technically relevant
- practical enough to help learners build projects
- not redundant with a stronger resource already listed
- accessible without requiring a large payment up front
- focused on durable fundamentals rather than a narrow framework trend
- safe for beginners to use without surprise billing or unclear licensing
- clear enough that a learner with no technical background can tell whether it
  is a good next step for them

Free and open resources are preferred. Courses, tutorials, videos, playlists,
curricula, communities, and tools should be free or genuinely free to audit.
Highly regarded paid books are welcome when they are durable, widely
recommended, and clearly worth buying or borrowing.

For books, prefer official publisher/author pages, open textbook projects, or
legitimate web editions. Do not link to unauthorized PDFs of paid books.

If you have any financial, employment, affiliate, or marketing relationship with
a resource, disclose it clearly. Promotional PRs, affiliate links, referral
links, coupon campaigns, and paid-course submissions will be declined.

Please do not paste AI-generated blurbs into the README. AI tools can help you
draft, but the final description should be checked, specific, and written in
your own words. Avoid empty phrases like "comprehensive resource" unless you
explain what makes it useful.

## Cost Labels

Use the README cost labels when adding or editing entries:

- **Free** - core material is available without payment
- **Free audit** - course can be taken for free, but certificates or grading may
  cost money
- **Free materials** - notes, videos, assignments, or public course pages are
  available, but support/grading may not be
- **Mixed** - useful free material exists, but the platform also has paid tiers
- **Compute may cost** - the course is free, but cloud, GPU, or API usage can
  cost money
- **Library/Paid** - worth borrowing or buying, but not freely available from
  the publisher

## AI Resource Guidelines

AI resources change quickly. For AI, ML, LLM, prompt engineering, and agent
resources, please prefer:

- official course pages, docs, or GitHub repositories
- clear prerequisites
- examples that can run locally or on a free tier where possible
- explicit warnings when API keys, credits, GPUs, or cloud services may cost
  money
- resources that teach evaluation, limitations, privacy, and responsible use

Avoid low-quality generated tutorials, copied prompt packs, and resources that
encourage learners to paste secrets or assignments into tools without
understanding the risk.

## Pull Request Checklist

Before opening a pull request:

- Keep the change focused.
- Add a concise description for every new resource.
- Use HTTPS links when available.
- Avoid link-only entries.
- Link to official book pages or legitimate free editions.
- For YouTube, prefer a specific playlist, course, or lecture series over a
  general channel unless the whole channel is consistently useful.
- Write descriptions in your own words, not marketing copy or unedited AI text.
- If you add or replace a high-priority starter resource, update
  [resources.yml](resources.yml).
- Check that headings and table-of-contents anchors still work.
- Label cost and prerequisites honestly.
- Say who the resource is for: absolute beginner, career switcher,
  intermediate learner, teacher, parent, or advanced learner.
- Explain why the resource should be included.

## What Usually Does Not Fit

These contributions are less likely to be accepted:

- long unannotated lists
- affiliate links
- referral links, coupon codes, or campaign links
- paid courses, bootcamps, coaching programs, newsletters, communities, apps, or
  subscriptions submitted for promotion
- YouTube videos or channels that mainly advertise paid courses, bootcamps,
  coaching, private communities, apps, or subscriptions
- resources locked entirely behind a paywall
- narrow framework tutorials unless they belong in an existing path
- low-quality AI-generated tutorials
- duplicates of resources already listed
- resources that require surprise subscriptions or unclear free trials

If you are not sure whether a resource fits, open an issue first and describe
who it helps, what it teaches, why it is better than nearby alternatives, and
whether it is free.

## Local Checks

Run this before opening a larger pull request:

```bash
python scripts/check_links.py --include-resources
```

Maintainers can run the online link check when reviewing resource-heavy changes:

```bash
python scripts/check_links.py --online --include-resources
```
