# Introduction to Programming
**Curated list of resources for budding developers**

## Table of contents
[**SEE GITHUB PAGE VIEW**](http://ashleymcnamara.github.io/learn_to_code/)
- [Introduction](#introduction)
    - [Goals](#goals)
    - [Where do I start?](#where-do-i-start)
    - [How this page is organized](#how-this-page-is-organized)
    - [Which resource should I pick?](#which-resource-should-i-pick)
    - [Warning](#warning)
- [General resources](#general-resources)
    - [Links to other big lists](#links-to-other-big-lists)
    - [Online courses](#online-courses)
- [Programming Languages](#programming-languages)
    - [C](#c)
    - [C++](#c-1)
    - [C#](#c-sharp)
    - [Haskell](#haskell)
    - [HTML, CSS, and JavaScript](#html-css-and-javascript)
    - [Lisp (Scheme, Common Lisp, Clojure, etc)](#lisp-scheme-common-lisp-clojure-etc)
    - [Java](#java)
    - [Perl](#perl)
    - [PHP](#php)
    - [Python](#python)
    - [Golang](#golang)
    - [Ruby](#ruby)
    - [Scratch](#scratch)
- [Data](#data)
    - [Neo4j & Graph Databases](#neo4j-and-graph-databases)
    - [MongoDB](#mongodb)
- [Other topics](#other-topics)
    - [Developing on specific platforms](#developing-on-specific-platforms)
        - [Android](#android)
        - [Mac and iOS](#mac-and-ios)
        - [Windows and Windows Phones](#windows-and-windows-phones)
    - [Data structures and algorithms](#data-structures-and-algorithms)
- [Tools](#tools)
    - [Version control](#version-control)
        - [Git](#git)
        - [Mercurial](#mercurial)

## Introduction

### Goals

 Programming and computer science are becoming more popular than ever -- major initiatives like the [Hour of Code](http://hourofcode.com/us) are popularizing learning  programming across the world.

As a consequence, there are an increasingly huge number of resources and tutorials being produced for beginners who want to learn to code, ranging from books to online tutorials to interactive websites to massive open online courses _(MOOCS)_ like [Codecademy](https://www.codecademy.com/) and [Coursera](https://www.coursera.org/).

While this is great, it can also be overwhelming for beginners -- there are almost too _many_ resources available, and it's difficult to figure out where to start.

This page is meant to help solve that problem -- to present a **curated** list of resources for people who are either new to programming, new to a particular topic, or want to advance their skills past the beginner stage. This page doesn't try and list every single resource available, but instead links to resources that are guaranteed to be high-quality.

### Where do I start?

If you know what you want to learn about, great! Jump to that section, start browsing the links, and find something which works for you.

If you're not sure where to start and which language to learn, some good beginner languages are:

- [Golang](#golang) (Go is an attempt to combine the ease of programming of an interpreted, dynamically typed language, with the efficiency and safety of a statically typed, compiled language.)
- [Python](#python) (general-purpose; scientific and mathematical computing)
- [Java](#java) (general-purpose; Android development)
- [HTML/CSS/JavaScript](#html-css-and-javascript) (websites and webapps)
- [Scratch](#scratch) (for younger children)

Python and Java are both languages that are [commonly used](http://www.codingdojo.com/blog/9-most-in-demand-programming-languages-of-2016/) to teach programming to beginners in schools and universities, and there are a wide variety of resources available to help you learn. They're also widely used in the industry which makes them useful languages to have in your toolbelt.

Web development has been very popular lately, so there are many resources for learning HTML, CSS, and JavaScript, also making it suitable for learning. It requires little to no installation and configuration on your computer. All you need is a text editor to write code -- the code will run on your web browser.

[Scratch](https://www.youtube.com/watch?v=4y6J2jXjU34) is a little different from other languages. It was designed from the ground up to be easy to use and learn -- instead of typing text, you drag and connect together "blocks" to form programs, making it a very visual language. As a result, Scratch is a good language especially for younger children _(elementary schoolers, middle school)_ or for people who dislike typing.

### How this page is organized...

This page is subdivided into three parts -- first, a _"General resources"_ section that links to sites that tend to deliver high-quality content about a variety of topics, and a _"Specific resources"_ section that provides resources on specific programming languages or topics.

In general, most resources available will fall between two categories -- online courses, and books + tutorials. Online courses tend to teach using video lectures, try and be more interactive, and try and emulate the structure of a course similar to ones you might take in college. In contrast, books and tutorials teach via written text and allow you to set your own pace.

### Where should I start?

Whether you prefer learning by watching a video or reading text is really a matter of personal preference. _I_ personally prefer visual, but your learning style might be completely different. You may need to explore and browse several different resources before you discover how you best learn.

In addition, you'll find that most links, whether they're online courses, tutorials, or books, tend to focus on either one of three things:

  1. Some resources focus on _programming_, _semantics_, or _computer science theory_ -- in other words, how to use a programming language to write something that works.
  2. Other resources will focus more on _coding_ and _syntax_ -- the particular details and rules about how a programming language works.
  3. Other resources focus on teaching _idioms_ -- teaching best practices specific to that language, the underlying philosophy of that language, or teaching you about the different libraries available to you: the broader ecosystem.

If you're new to programming, the first model will be the best. Programming is all about applied problem solving: being able to take a problem, and break it up into smaller and smaller pieces until they're small enough to translate into computer code. Simply memorizing a collection of rules will not be very useful to you. You also need to learn how to _apply_ those rules.

However, if you already know how to program, then you most likely already know how to do this. In that case, you're going to want to use the second kind since it'll be easier to learn about the differences between the language you're learning and ones you already know.

Once you've moved past the beginning phase, then it would be a good idea to try and move on to the third kind of resource, which will help teach you how to actually use and apply that language on a practical and professional level.

When I say that a resource is _"heavy in theory"_ or _"is rigorous"_, I mean that it leans towards the first category. When I say that a resource _"focuses on syntax"_, I mean that it leans towards the second. And when I say a resource _"focuses on idioms"_ or _"on practical applications"_, I mean that it leans towards the third.

### WARNING!

This page is still a **work-in-progress**! Some sections may currently be incomplete, and some links may not yet be fully vetted.

If you would like to contribute, please see **[CONTRIBUTING.md][contrib]** for details.

  [contrib]: https://github.com/ashleymcnamara/learn_to_code/blob/master/Contributing.md

## General resources

### Links to other big lists

You can find a huge and utterly massive compendium of [list of free programming books and resources on github](https://github.com/EbookFoundation/free-programming-books/blob/main/README.md). (It used to be hosted on StackOverflow, but was moved over to Github on October 2013).

You can also find a meta _"list of programming resources"_ aggregator here: http://resrc.io/


### Online courses

Online courses are an increasingly popular way for universities and professionals to teach programming and computer science in a structured format. As a result, new online courses will pop up all the time, so it's worth checking these resources periodically to see what's new.

- **[Blackbird School](https://blackbird.school)** - offers a web-based platform where you can learn to code from scratch. Geared toward a beginner-friendly experience. Focuses on coding fundamentals rather than specific languages or frameworks, uses JavaScript. Offers a 30-day free trial, but users must enter a credit/debit card.
- **[Codecademy](http://www.codecademy.com/)** - offers free online courses in several different languages. However, Codecademy does have a tendency to teach only basic syntax, so you may need work through more tutorials after finishing Codecademy. Focuses mainly on web development, Ruby, and Python.
- **[Coursera](https://www.coursera.org/)** - offers free online courses in many different fields from several different well-known universities. New courses are added every quarter, and content from old courses is typically archived. Because many courses appear to be new/may be a one-time thing, this page will not link to courses on Coursera unless it appears to be stable.
- **[Springboard](https://www.springboard.com/)** - offers several free programming resources and mentored workshops on data science, UX design and more that can teach you Python, R, data science, and SQL with the help of an expert who works professionally.
- **[Udacity](http://www.udacity.com/)** - offers free computer science courses taught by industry experts. Udacity offers two kinds of courses -- regular courses and nanodegrees. Regular courses are free. Regular courses with one-on-one tutoring/code review requires a monthly fee. Nanodegrees are typically for people with some prior coding experience, and cost more money.
- **[edX](https://www.edx.org/)** - a joint effort between MIT, Harvard, and Berkeley to provide free online versions of some of their courses.
- **[OpenCulture](http://www.openculture.com/computer_science_free_courses)** - similar to all of the above. Video lectures are typically available on iTunes or Youtube. Typically does **not** require you to complete assignments, unlike many other online courses.
- **[MIT OpenCourseWare](http://ocw.mit.edu/index.htm)** - static course materials taught at MIT. Unless otherwise noted, most content from this website tends to be very rigorous and fast-paced.
- **[Khan Academy](https://www.khanacademy.org/)** - contains a few courses on programming and computer science; does contain many more courses on all kinds of topics (especially math).
- **[Stanford Engineering Everywhere](http://see.stanford.edu/see/courses.aspx)** - static course materials taught at Stanford.
- **[Learn Code](https://www.youtube.com/learncodeacademy/)** - offers free online courses hosted on YouTube focusing primarily on greater JavaScript ecosystem. Covers everything from basic JavaScript, front end Web Apps, NodeJS and some of the more popular frameworks. Also covers other topics such as basic Git usage, and SSH.
- **[Do What You Love (DWYL)](https://github.com/dwyl)** - over 150 tutorials in the form of Github repositories, covering languages such as JavaScript, HTML5, Elixir and Elm; platforms like AWS, Digital Ocean, and Azure; other tools like CodeShip and Github; and also covering basics on architecture, security, and test driven design  
- **[Object-Oriented Reengineering Patterns](http://scg.unibe.ch/download/oorp/)** - Object-Oriented Reengineering Patterns collects and distills successful techniques in planning a reengineering project, reverse-engineering, problem detection, migration strategies and software redesign.
- **[Computer Musings (lectures by Donald Knuth)](http://scpd.stanford.edu/free-stuff/engineering-archives/donald-e-knuth-lectures)** - The Stanford Center for Professional Development has digitized more than one hundred tapes of Knuth's musings, lectures, and selected classes and posted them online.
- **[NASA Software Measurement Handbook](https://www.scribd.com/doc/7181362/NASA-Software-Measurement-Guidebook)**
- **[Introduction to Functional Programming (class lectures and slides)](http://www.cl.cam.ac.uk/teaching/Lectures/funprog-jrh-1996/)** - Introduction and Overview Functional and imperative programming: contrast, pros and cons. General structure of the course: how lambda calculus turns out to be a general programming language. Lambda notation: how it clarifies variable binding and provides a general analysis of mathematical notation. Currying. Russell's paradox.
- **[Guide to the Software Engineering Body of Knowledge](https://www.computer.org/portal/web/swebok)** - The Guide to the Software Engineering Body of Knowledge (SWEBOK Guide) describes generally accepted knowledge about software engineering. Its 15 knowledge areas (KAs) summarize basic concepts and include a reference list pointing to more detailed information.
- **[Programming Languages: Application and Interpretation](http://cs.brown.edu/~sk/Publications/Books/ProgLangs/2007-04-26/)** - Programming language ‘‘paradigms’’ are a moribund and tedious legacy of a bygone age. Modern language designers pay them no respect, so why do our courses slavishly adhere to them? This paper argues that we should abandon this method of teaching languages, offers an alternative, reconciles an important split in programming language education, and describes a textbook that explores these matters.
- **[Producing Open Source Software](https://producingoss.com)** - Producing Open Source Software is a book about the human side of open source development. It describes how successful projects operate, the expectations of users and developers, and the culture of free software.
- **[97 Things Every Programmer Should Know](http://programmer.97things.oreilly.com/wiki/index.php/97_Things_Every_Programmer_Should_Know)** - 97 Things Every Programmer Should Know project, pearls of wisdom for programmers collected from leading practitioners. You can read through the Contributions Appearing in the Book plus the Other Edited Contributions, browse Contributions in Progress, view the list of Contributors, and also learn How to Become a Contributor. If you would simply like to comment on a contribution, please also read How to Become a Contributor as some of it applies to you.
- **[Type Theory and Functional Programming](https://www.cs.kent.ac.uk/people/staff/sjt/TTFP/)** - Constructive Type theory has been a topic of research interest to computer scientists, mathematicians, logicians and philosophers for a number of years. For computer scientists it provides a framework which brings together logic and programming languages in a most elegant and fertile way: program development and verification can proceed within a single system.
- **[Operating Systems and Middleware (PDF and LaTeX)](https://gustavus.edu/mcs/max/os-book/)** - Operating Systems and Middleware: Supporting Controlled Interaction by Max Hailperin
- **[Scaler](https://www.scaler.com/topics/)** - Understand how programming works, Learn Python, Java, Data Structure, C/C++ and other popular programming languages with easy to follow tutorials and examples.

The following websites also contain a wide variety of tutorials for many different topics, but require payment and registration before you can access their courses.

- **[Team Treehouse](http://teamtreehouse.com/)** - focuses on web and iOS development.
- **[Lynda](http://www.lynda.com/)** - also includes courses on design, animation, video, business, and more.
- **[PluralSight](http://www.pluralsight.com/)** - similar to Lynda, but with a focus on developer and IT courses.
-  **[General Assembly](https://generalassemb.ly/)** - also includes courses on design, animation, video, business, and more.

In general, edX, OpenCulture, MIT OpenCourseware, and Stanford Engineering Everywhere tend to contain more rigorous, thorough, and demanding courses, whereas Codecademy and Khan Academy tend to focus on giving a more gentle introduction to programming. Coursera and Udacity tend to vary between these two extremes.


## Programming Languages

### C

Note: C can be a difficult-to-teach language. Although the online courses and books are a good starting point and can take you a long way, the general consensus is that the best way to learn is through reading an actual book.

- **Online courses:**
    - MIT Open Courseware has a few:
        - [Practical Programming in C][c-mit-practical]
          For beginners.
        - [Introduction to C Memory Management and C++ Object-Oriented Programming][c-mit-intro]
          Geared towards people with prior experience in a programming language that is not C or C++.
        - [Effective Programming in C and C++][c-mit-effective]
          Similar to the above.
- **Video tutorials:** N/A
- **Interactive tutorials:**
    - [Learn-C][c-learn-c]
      An interactive online guide that teaches you basic C step-by-step.
- **Books and tutorials (online):**
   -  [Learn C The Hard Way][c-lcthw]
      Part of the "Learn X the Hard Way" series. Assumes you have prior programming experience. Currently incomplete, in progress.
   -  [C Programming][c-c-programming]
      One of Wikibooks' featured books. Tends to focus on teaching mainly syntax. A good starting point and reference.
   -  [Build Your Own Lisp][c-lisp]
      Walks you through how to write a Lisp interpreter in C, teaching both languages simultaneously.
    - [More free books][c-more]
- **Books (paper):**
    - [The C Programming Language][c-c-lang]
      The definitive guide to C. Also known as K&R, after the authors.
    - [The Definitive C Book Guide and List][c-so-definitive]
A very well-maintained list of recommended books and resources on StackOverflow. Every book listed on this page is highly-recommended.
- **Exercises:** N/A

  [c-mit-practical]: http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-087-practical-programming-in-c-january-iap-2010/
  [c-mit-intro]: http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-088-introduction-to-c-memory-management-and-c-object-oriented-programming-january-iap-2010/
  [c-mit-effective]: http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-s096-effective-programming-in-c-and-c-january-iap-2014/

  [c-learn-c]: http://learn-c.org
  [c-lcthw]: http://c.learncodethehardway.org/book/
  [c-lisp]: http://www.buildyourownlisp.com/
  [c-c-programming]: http://en.wikibooks.org/wiki/C_Programming
  [c-more]: https://github.com/vhf/free-programming-books/blob/master/free-programming-books.md#c

  [c-c-lang]: http://www.amazon.com/C-Programming-Language-2nd-Edition/dp/0131103628/
  [c-so-definitive]: http://stackoverflow.com/questions/562303/the-definitive-c-book-guide-and-list

### C++

Note: Similar to C, C++ can be a difficult-to-teach language. Although the online courses and books are a good starting point and can take you a long way, the general consensus is that the best way to learn is through reading an actual book.

- **Online courses:**
    - MIT Open Courseware has a few:
        - [Introduction to C++][cpp-mit-intro]
          For beginners, is fast-paced.
        - [Introduction to C Memory Management and C++ Object-Oriented Programming][cpp-mit-intro-2]
          Geared towards people with prior experience in a programming language that is not C or C++.
        - [Effective Programming in C and C++][cpp-mit-effective]
        Similar to the above.
    - **Stanford's 3-part "Introduction to Computer Science" series for beginners.** The first course teaches Java, the latter two teaches C and C++.
        - [Programming Methodology][cpp-stan-methodology]
        - [Programming Abstractions][cpp-stan-abstractions]
        - [Programming Paradigms][cpp-stan-paradigms]
    - Coursera's [C++ for C Programmers][cpp-coursera-c-for-cpp]
      May also be helpful for programmers with prior experience in another language besides C or C++.
- **Interactive tutorials:**
    - [C++ Interactive Exercises][cpp-interactive]
      An introduction to basic C++. Is a cross between an interactive tutorial and an online book.
- **Video tutorials:** N/A
- **Books and tutorials (online):**
    - [How to Think Like a Computer Scientist][cpp-think-cs]
      A good introduction to basic C++.
    - [Learncpp.com][cpp-learn]
      Tends to focus more on syntax, and less on programming. Might be useful for beginners, but as a reference, not a tutorial.
    - [Linear C++][cpp-linear]
      A tutorial on C++ for people with some prior programming experience. Teaches by presenting and explaining a series of programs.
   - [More free books][cpp-more]
- **Books (paper):**
   - [The Definitive C++ Book Guide and List][cpp-so-definitive]
     A very well-maintained list of recommended books and resources on StackOverflow. Every book listed on this page is highly-recommended.
- **Exercises:** N/A

  [cpp-google-class]: https://developers.google.com/edu/c++/
  [cpp-coursera-c-for-cpp]: https://www.coursera.org/course/cplusplus4c
  [cpp-mit-intro]: http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-096-introduction-to-c-january-iap-2011/
  [cpp-mit-intro-2]: http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-088-introduction-to-c-memory-management-and-c-object-oriented-programming-january-iap-2010/
  [cpp-mit-effective]: http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-s096-effective-programming-in-c-and-c-january-iap-2014/
  [cpp-stan-methodology]: http://see.stanford.edu/see/courseinfo.aspx?coll=824a47e1-135f-4508-a5aa-866adcae1111
  [cpp-stan-abstractions]: http://see.stanford.edu/see/courseinfo.aspx?coll=11f4f422-5670-4b4c-889c-008262e09e4e
  [cpp-stan-paradigms]: http://see.stanford.edu/see/courseinfo.aspx?coll=2d712634-2bf1-4b55-9a3a-ca9d470755ee

  [cpp-interactive]: http://nova.umuc.edu/~jarc/sdsd/

  [cpp-think-cs]: http://greenteapress.com/thinkcpp/index.html
  [cpp-learn]: http://www.learncpp.com/
  [cpp-linear]: https://github.com/jesyspa/linear-cpp
  [cpp-more]: https://github.com/vhf/free-programming-books/blob/master/free-programming-books.md#c-1

  [cpp-so-definitive]: http://stackoverflow.com/questions/388242/the-definitive-c-book-guide-and-list

### C-Sharp
 (pronounced as see sharp) is a multi-paradigm programming language encompassing strong typing, imperative, declarative, functional, generic, object-oriented (class-based), and component-oriented programming disciplines.

- **Online courses:**
    - Microsoft Virtual Academy has a few free courses:
      - [C# Fundamentals for Absolute Beginners][csharp-fundamentals]
        A series of videos produced by Microsoft on learning C#. For beginners.
      - [Programming in C# Jump Start][csharp-jump-start]
        Another series of videos produced by Microsoft. Assumes some prior knowledge of C#.
- **Interactive tutorials:** N/A
- **Video tutorials:** N/A
- **Books and tutorials (online):**
    - [C# Programming][csharp-programming]
      One of Wikibook's featured books. For beginners. Tends to focus on syntax, and would also make a good reference.
    - [The C# Yellow Book][csharp-yellow]
      The introductory text used by the University of Hull.
    - [C# Essentials][csharp-essentials]
      An introductory text on C#. Also includes information on Windows Forms, Visual Studios, and making GUIs.
    - [Visual C# resources][csharp-visual]
      Microsoft's official series of tutorials and guides on C# and .NET.
    - [More free books][csharp-more]
- **Books (paper):**
    - [Sam's Teach Yourself C# 5.0 in 24 Hours]() by Scott Dorman
      A good introduction for beginners.
    - [Essential C# 5.0][csharp-essential-book]
      Very comprehensive, and intended more for intermediate programmers/programmings coming from another language.
    - [C# in Depth, 3rd Edition][csharp-in-depth]
      Also very comprehensive, and covers how to write idiomatic and clean C# code. Assumes the reader already knows some C#.
    - [Effective C#][csharp-effective] and [More Effective C#][csharp-more-effective]
      A collection of tips and tricks to improve your C# code. Not for beginners.
- **Exercises:** N/A

  [csharp-fundamentals]: http://channel9.msdn.com/Series/C-Fundamentals-for-Absolute-Beginners
  [csharp-jump-start]: http://www.microsoftvirtualacademy.com/training-courses/developer-training-with-programming-in-c

  [csharp-programming]: http://en.wikibooks.org/wiki/C_Sharp_Programming
  [csharp-yellow]: http://www.csharpcourse.com/
  [csharp-essentials]: http://www.techotopia.com/index.php/C_Sharp_Essentials
  [csharp-visual]: http://msdn.microsoft.com/en-us/vstudio/hh341490
  [csharp-more]: https://github.com/vhf/free-programming-books/blob/master/free-programming-books.md#c-sharp

  [csharp-sam]: http://www.amazon.com/Sams-Teach-Yourself-5-0-Hours/dp/0672336847
  [csharp-essential-book]: http://www.amazon.com/Essential-Edition-Microsoft-Windows-Development/dp/0321877586
  [csharp-in-depth]: http://www.amazon.com/gp/product/161729134X
  [csharp-effective]: http://www.amazon.com/Effective-Specific-Ways-Improve-Your/dp/0321245660
  [csharp-more-effective]: http://www.amazon.com/More-Effective-Specific-Ways-Improve/dp/0321485890

### Haskell
Haskell is a [polymorphically](https://wiki.haskell.org/Polymorphism) [statically typed](https://wiki.haskell.org/Typing), [lazy, purely functional](https://wiki.haskell.org/Lazy_evaluation) language, quite different from most other programming languages. The language is named for [Haskell Brooks Curry](https://wiki.haskell.org/Haskell_Brooks_Curry), whose work in mathematical logic serves as a foundation for functional languages. Haskell is based on the [lambda calculus](https://wiki.haskell.org/Lambda_calculus), hence the lambda they use as a logo.
- **Online courses:**
    - edX's [Introduction to Functional Programming][haskell-intro-func]
      Assumes familiarity with a non-functional programming language (Java, Python, C#, C++, etc). Take a look at [course content][haskell-course-content].
- **Interactive tutorials:**
    - [Try Haskell][haskell-try]
      An interactive guide that teaches basic Haskell.
- **Video tutorials:**
    - [Parallel and Concurrent Haskell][haskell-by-bartosz]
      A series of lectures which cover both basics and advanced concepts.
- **Books and tutorials (online):**
    - [Getting started with Haskell][haskell-getting-started]
      A comprehensive meta-guide that suggests the recommended order for following Haskell tutorials from beginning to advanced.
    - [Learn You a Haskell for Great Good][haskell-great-good]
      A beginner's introduction to Haskell. Tends to focus on syntax.
    - [Haskell][haskell-wikibooks]
      One of Wikibook's featured books. Covers basic to advanced Haskell. Very comprehensive.
    - [Real World Haskell][haskell-real-world]:
      Covers how to use Haskell for practical applications. This is a good second book to read, after completing one of the above tutorials.
    - [More free books][haskell-more]
- **Books (paper):** N/A
- **Exercises:**
    - [H-99][haskell-h-99]
      A collection of 99 problems designed to increase your proficiency in Haskell.

  [haskell-intro-func]: https://www.edx.org/course/introduction-functional-programming-delftx-fp101x-0
  [haskell-course-content]: https://github.com/fptudelft/FP101x-Content-2015

  [haskell-try]: http://tryhaskell.org/
  [haskell-by-bartosz]: https://www.youtube.com/playlist?list=PLbgaMIhjbmEm_51-HWv9BQUXcmHYtl4sw

  [haskell-getting-started]: http://stackoverflow.com/a/1016986/646543
  [haskell-great-good]: http://learnyouahaskell.com/
  [haskell-wikibooks]: http://en.wikibooks.org/wiki/Haskell
  [haskell-real-world]: http://book.realworldhaskell.org/
  [haskell-more]: https://github.com/vhf/free-programming-books/blob/master/free-programming-books.md#haskell

  [haskell-h-99]: http://haskell.org/haskellwiki/H-99:_Ninety-Nine_Haskell_Problems

### HTML, CSS, and JavaScript

Note: HTML, CSS, and JavaScript are the three core technologies that runs on every web browser and makes up every webpage.

HTML is a language used to describe the _structure_ and _content_ of a webpage. CSS is used to describe the _style_ and _appearance_. JavaScript is used to add _behavior_ and _interactivity_.

The recommended learning order is typically to start with HTML and CSS, then move on to learning JavaScript once you feel you've acquired a basic understanding of the previous two.

Also note that HTML and CSS are examples of "markup languages", not "programming languages" and so will feel fairly different from JavaScript. If your goal is to learn just programming, you might want to jump straight ahead to JavaScript (or pick a different programming language!). However, since the main way to actually use JavaScript is through the web browser, you _do_ need to learn HTML and CSS at one point or another.

- **Online courses:**
    - Dash teaches HTML, CSS, and Javascript through fun projects you can do in your browser.
      - [Make a website][general-assembly-make-website]
    - Codecademy has several courses related to web development.
        - [Make a website][webdev-cc-make-website]
        - [Make an interactive website][webdev-cc-make-interactive]
        - [HTML & CSS][webdev-cc-html-css]
        - [JavaScript][webdev-cc-js]
        - [jQuery][webdev-cc-jquery]
    - So does Udacity:
        - [Intro to HTML and CSS][webdev-uda-html-css]
        - [JavaScript Basics][webdev-uda-js]
          Does require some prior programming experience.
    - Open Culture's [Building Dynamic Websites][webdev-open-dynamic]
      Hosted by Harvard, and covers a wide variety of topics.
    - Khan Academy has a series of [three courses][webdev-khan] on introductory Javascript that focuses on drawing graphics and animations, and making games.
    - Team Treehouse has a series of courses on [HTML][webdev-treehouse-js], [CSS][webdev-treehouse-css], and [Javascript][webdev-treehouse-js]
      Allows a free 14-day trial, but later requires payment.
- **Interactive tutorials:**
    - [CSS3, please!][webdev-please]
      An interactive website that lets you dynamically change CSS rules to style an element on-screen. Not for beginners, but is a good way to discover advanced applications of CSS.
- **Video tutorials:** N/A
- **Books and tutorials (online):**
    - [Mozilla Developer Network][webdev-mdn] (MDN)
      A series of tutorials covering HTML, CSS, JavaScript, and more. Some tutorials are appropriate for beginners while other tutorials will be more advanced.
    - [HtmlDog][webdev-htmldog]
      Similar to the above, but targeted more specifically to beginners.
    - [Eloquent JavaScript][webdev-eloquent]
      A book that teaches you how to write idiomatic and clean JavaScript. Assumes prior experience with JavaScript/another programming language.
    - [A Re-introduction to JavaScript][webdev-js-reintroduction]
      A guide which gives a thorough and detailed overview of JavaScript.
    - [JavaScript Frameworks Resources and Tutorials][webdev-js-frameworks]
      Currently features Angular.js, Backbone.js, D3.js, Dojo, Ember.js, Express.js, jQuery, Knockout.js, and Meteor.
    - [JavaScript30][webdev-js-30vanilla]
      30 Day Vanilla JS Coding Challenge. Build 30 things in 30 days with 30 tutorials
    - [JavaScript Tutorial][webdev-js-onevideo]
      Learn JavaScript in one 90 minute Video.
    - More free books:
        - [HTML and CSS][webdev-more-html-css]
        - [JavaScript][webdev-more-js]
- **Books (paper):**
    - [JavaScript: The Good Parts][webdev-the-good-parts]
      A short book that covers the core aspects of JavaScript as well as info on writing idiomatic and clean JavaScript.
    - [JavaScript: The Good Parts Notes][webdev-the-good-parts-notes]
      Notes on the Douglas Crockford's book. Great if you don't have time to get into the detail of the book.
- **Exercises:**
    - [CSS Diner][webdev-css-diner]
      A series of exercises on using CSS selectors effectively.
    - [DevProjects](https://www.codementor.io/projects/javascript)
      DevProjects is a community with free and unique real-world projects in multiple coding languages and tech stacks. The website also includes solutions from other developers and discussion board for all users to participate in.

  [webdev-js-30vanilla]: https://javascript30.com/
  [webdev-js-onevideo]: https://www.youtube.com/watch?v=fju9ii8YsGs
  [webdev-cc-make-website]: http://www.codecademy.com/skills/make-a-website
  [webdev-cc-make-interactive]: http://www.codecademy.com/skills/make-an-interactive-website
  [webdev-cc-html-css]: http://www.codecademy.com/tracks/web
  [webdev-cc-js]: http://www.codecademy.com/tracks/javascript
  [webdev-cc-jquery]: http://www.codecademy.com/tracks/jquery
  [webdev-uda-html-css]: https://www.udacity.com/course/ud304
  [webdev-uda-js]: https://www.udacity.com/course/ud804
  [webdev-open-dynamic]: http://cs75.tv/2010/fall/
  [webdev-khan]: https://www.khanacademy.org/computing/computer-programming
  [webdev-treehouse-html]: http://teamtreehouse.com/features/html
  [webdev-treehouse-css]: http://teamtreehouse.com/features/css
  [webdev-treehouse-js]: http://teamtreehouse.com/features/javascript

  [webdev-please]: http://css3please.com/

  [webdev-mdn]: https://developer.mozilla.org/en-US/docs/Web
  [webdev-htmldog]: http://www.htmldog.com/
  [webdev-eloquent]: http://eloquentjavascript.net/
  [webdev-js-reintroduction]: https://developer.mozilla.org/en-US/docs/Web/JavaScript/A_re-introduction_to_JavaScript
  [webdev-js-frameworks]: http://resrc.io/list/18/javascript-frameworks/
  [webdev-more-html-css]: https://github.com/vhf/free-programming-books/blob/master/free-programming-books.md#html--css
  [webdev-more-js]: https://github.com/vhf/free-programming-books/blob/master/free-programming-books.md#javascript

  [webdev-the-good-parts]: http://www.amazon.com/gp/product/0596517742
  [webdev-the-good-parts-notes]: https://github.com/iteles/Javascript-the-Good-Parts-notes

  [webdev-css-diner]: http://flukeout.github.io/
  [general-assembly-make-website]: https://dash.generalassemb.ly/

### Lisp (Scheme, Common Lisp, Clojure, etc)

- **Online courses:**
  - [Learn Lisp the Hard Way][lisp-course] Brought to you by the Toronto Lisp User Group
- I**nteractive tutorials:**
    - [Try Clojure][lisp-try-clojure]
      An interactive tutorial for basic Clojure.
- **Video tutorials:**
  - [Overview and Introduction to Lisp][mit-course] videos from MIT open courseware
- **Books and tutorials (online):**
    - [The Nature of Lisp][lisp-nature]
      Not really a tutorial on Lisp, but is instead an article on why so many people advocate Lisp and claim it will fundamentally change how you view code. Very good at explaining the philosophy of Lisp.
    - [Structure and Interpretation of Computer Programs][lisp-sicp]
      SICP is the canonical introduction to Lisp, and used to be part of MIT's introduction to CS course (before they switched to Python).
        - [SICP in Clojure][lisp-sicp-clojure]
          An amended version of SICP which uses Clojure instead of Scheme.
    - [How to Design Programs][lisp-htdp]
      A competing book and philosophy of teaching to SICP. SICP tends to focus more on CS theory whereas HTDP tends to focus more on writing how to go about writing programs/analyzing problems.
    - [Build Your Own Lisp][lisp-build]
      Walks you through how to write a Lisp interpreter in C, teaching both languages simultaneously.
    - [Practical Common Lisp][lisp-learn-practical]
      An introductory book on Common Lisp. Covers practical and real-world applications of Common Lisp.
    - [Where to learn how to practically use Common Lisp][lisp-learn-practical]
      An aggregation of books and resources on effectively using Common Lisp for programmers coming from an imperative world.
    - [Learn Clojure][lisp-learn-clojure]
      A website collecting many links related to learning Lisp.
    - More free books:
        - [Clojure][lisp-more-clojure]
        - [Lisp][lisp-more-lisp] in general
        - [Scheme][lisp-more-scheme]
- **Books (paper):**
    - [Land of Lisp][lisp-land]
      A book that teaches Lisp (specifically Common Lisp) via making games. For beginners.
- **Exercises:**
    - [L-99][lisp-l99]
      A series of 99 problems designed to increase your proficiency in Lisp.
    - [4Clojure][lisp-4clojure]
      A series of exercises geared around learning Clojure.

  [lisp-try-clojure]: http://www.tryclj.com/

  [lisp-nature]: http://www.defmacro.org/ramblings/lisp.html
  [lisp-sicp]: http://mitpress.mit.edu/sicp/
  [lisp-sicp-clojure]: http://sicpinclojure.com/
  [lisp-htdp]: http://htdp.org/
  [lisp-build]: http://www.buildyourownlisp.com/
  [lisp-practical]: http://www.gigamonkeys.com/book/
  [lisp-learn-practical]: http://stackoverflow.com/q/7224823/646543
  [lisp-learn-clojure]: http://learn-clojure.com/
  [lisp-more-clojure]: https://github.com/vhf/free-programming-books/blob/master/free-programming-books.md#clojure
  [lisp-more-lisp]: https://github.com/vhf/free-programming-books/blob/master/free-programming-books.md#lisp
  [lisp-more-scheme]: https://github.com/vhf/free-programming-books/blob/master/free-programming-books.md#scheme

  [lisp-land]: http://www.amazon.com/Land-Lisp-Learn-Program-Game/dp/1593272812

  [lisp-l99]: http://www.ic.unicamp.br/~meidanis/courses/mc336/2006s2/funcional/L-99_Ninety-Nine_Lisp_Problems.html
  [lisp-4clojure]: http://4clojure.com
  [mit-course]: http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-001-structure-and-interpretation-of-computer-programs-spring-2005/video-lectures/1a-overview-and-introduction-to-lisp/
  [lisp-course]: http://learnlispthehardway.org/

### Java
Java is a programming language designed to build secure, powerful applications that run across multiple operating systems, including Linux, Mac OS X, and Windows. The Java language is known to be flexible, scalable, and maintainable.

- **Online courses:**
    - Udacity's [Intro to Java Programming][java-uda-intro]
      An objects-first introduction to Java.
    - MIT Open Courseware:
        - [Introduction to Programming in Java][java-mit-intro-to-prog]
        - [Introduction to Computers and Engineering Problem Solving][java-mit-intro-to-computers]
          For beginners, emphasizes practical application of Java.
    - Stanford's 3-part "Introduction to Computer Science" series for beginners. The first course teaches Java, the latter two teaches C and C++.
        - [Programming Methodology][java-methodology]
        - [Programming Abstractions][java-abstractions]
        - [Programming Paradigms][java-paradigms]
    - The University of Helsinki's "Object-Oriented programming with Java" series for beginners.
        - [Part 1][java-helsinki-1]
        - [Part 2][java-helsinki-2]
- **Interactive tutorials:**
    - [Learn Java][java-learn-online]
      An interactive tutorial that teaches basic Java.
- **Video tutorials:** N/A
- **Books and tutorials (online):**
    - [Introduction to Computer Science using Java][java-intro-cs]
      An introductory text on Java. Moves a bit slowly, but covers everything in great detail (including setup).
    - [Learn by Doing][java-doing]
      An introductory text on Java. The tutorial is exercise-driven.
    - [Think Java][java-think]
      Another introductory text on Java. The content is based on the "How to think like a Computer Scientist" series.
    - [Thinking in Java, 3rd edition][java-thinking]
      Note: the fourth edition is the latest one, but currently is not free. The website can also be a little hard to navigate -- the direct download link is [here][java-thinking-direct]. Assumes some basic prior programming experience.
    - [TutorialsPoint's Java Tutorial][java-tutorialspoint]
      An introduction to Java. Tends to focus mainly on syntax. May also make a good reference.
    - [The Java Tutorial][java-oracle]
      The official Java tutorial, produced by Oracle. Tends to focus on language features and syntax.
    - [More free books][java-more]
- **Books (paper):**
    - [Head First Java][java-head]
      A beginner's introduction to Java.
- **Exercises:**
    - [Practice-it][java-practice-it]
      A series of exercises hosted by the University of Washington, starting with basic Java and finishing with data structures and algorithms. Requires (free) registration first before you can view or work on the exercises.
    - [DevProjects](https://www.codementor.io/projects/java)
      A commnuty of free and unique Java projects that focus on both mobile and web apps. Created by Codementor, a paid mentorship platform, DevProjects offer projects, solutions from other developers, and discussion board for all users to participate in.

  [java-uda-intro]: https://www.udacity.com/course/cs046
  [java-mit-intro-to-prog]: http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-092-introduction-to-programming-in-java-january-iap-2010/index.htm
  [java-mit-intro-to-computers]: http://ocw.mit.edu/courses/civil-and-environmental-engineering/1-00-introduction-to-computers-and-engineering-problem-solving-spring-2012/
  [java-methodology]: http://see.stanford.edu/see/courseinfo.aspx?coll=824a47e1-135f-4508-a5aa-866adcae1111
  [java-abstractions]: http://see.stanford.edu/see/courseinfo.aspx?coll=11f4f422-5670-4b4c-889c-008262e09e4e
  [java-paradigms]: http://see.stanford.edu/see/courseinfo.aspx?coll=2d712634-2bf1-4b55-9a3a-ca9d470755ee
  [java-helsinki-1]: http://mooc.fi/courses/2013/programming-part-1/
  [java-helsinki-2]: http://mooc.fi/courses/2013/programming-part-2/

  [java-learn-online]: http://www.learnjavaonline.org/

  [java-doing]: http://programmingbydoing.com/
  [java-think]: http://greenteapress.com/thinkapjava/
  [java-thinking]: http://www.mindview.net/Books/TIJ/
  [java-thinking-direct]: http://www.mindviewinc.com/downloads/TIJ-3rd-edition4.0.zip
  [java-tutorialspoint]: http://www.tutorialspoint.com/java/index.htm
  [java-intro-cs]: http://chortle.ccsu.edu/java5/index.html
  [java-oracle]: http://docs.oracle.com/javase/tutorial/
  [java-more]: https://github.com/vhf/free-programming-books/blob/master/free-programming-books.md#java

  [java-head]: http://www.amazon.com/Head-First-Java-2nd-Edition/dp/0596009208/

  [java-practice-it]: http://practiceit.cs.washington.edu/

### Perl
Businesses talk about Perl 5 when talking Perl, but on a far-far land, beyond deep-thinking island, the design-by-committee tribe is still cooking a hefty slab of Perl 6 (and it's almost ready, with an engine written in Haskell and powered by the tears of the gods)

**Ok, that said, what is Perl 5 used for, today?**

- **legacy web systems / intrawebs** - some just won't die

- **data mining / statistical analysis** - the perl regex engine, even if slightly outdated, (PCRE, a spinned off library, tops it up in any possibile way and it's the default PHP engine) is still good for simple analysis

- **UNIX system administration **- Perl shall always be installed on UNIX.
You can count on it being readily available even on Mac OS X.

- **Network Prototyping **- many core network experts learned Perl when it was all the rage; and they still do their proofs-of-concept with it.

- **Security** - many security experts, too, need fast prototyping. (and fast automated fixes) Perl can, and does, cover for that.

The extensive CPAN collection is very handy, when dealing with prototypes.
(Batteries may not be included, but they're still right there, on the shelf)

**Remember drawbacks, though:**

- Object support in Perl sucks hard, you bless references and do unholy stuff in the name of objects, then wonder why you took all the trouble in the first place.
- Reading other people's Perl is more than a craft, it's science, and a painful one, too.
- Perl is nifty, it makes you think nifty, it makes you feel nifty, you become a programming rockstar. Now, think about getting up, and going to work in a office full of rockstars: it's a "boat that rocks" hard. Expect wild fluctuations.

- **Online courses:** N/A
- **Interactive tutorials:** N/A
- **Video tutorials:** N/A
- **Books and tutorials (online):**
    - [Beginning Perl][perl-beginning]
      A comprehensive and thorough introduction to Perl.
    - [Modern Perl][perl-modern]
      A guide on writing clean and idiomatic Perl code. Very good for teaching the philosophy and fundamentals of Perl. Comprehensive and thorough.
    - [Impatient Perl][perl-impatient]
      An accelerated guide for impatient people or people with prior programming experience.
    - [Learn Perl in about 2 hours 30 minutes][perl-230]
      Another accelerated guide for the impatient. Geared towards people who have prior experience in another programming language.
    - [More free books][perl-more]
    - Perl.org also hosts a [list of recommended books][perl-books], many of which are available online for free.
- **Books (paper):**
    - [Learning Perl][perl-learning]
      An introductory text on Perl. Teaches on focusing syntax/the details of Perl, and not so much on how to program. Pragmatic and practical.
- **Exercises:**
    - [Perl Quiz of the Week][perl-qotw]
      A mailing list which sends out a new quiz/prompt once a week. Archives of past prompts are also available.

  [perl-beginning]: http://www.perl.org/books/beginning-perl/
  [perl-modern]: http://modernperlbooks.com/books/modern_perl_2014/
  [perl-impatient]: http://www.perl.org/books/impatient-perl/
  [perl-230]: http://qntm.org/perl
  [perl-more]: https://github.com/vhf/free-programming-books/blob/master/free-programming-books.md#perl
  [perl-books]: http://www.perl.org/books/library.html

  [perl-learning]: http://www.amazon.com/Learning-Perl-Randal-L-Schwartz/dp/1449303587

  [perl-qotw]: http://perl.plover.com/qotw/

### PHP

Note: while PHP can be very convenient, quick, and easy to use, it's also a language viewed negatively by many programmers. (See [PHP: a fractal of bad design][php-fractal]). If you do decide to learn PHP and adopt it as your language of choice, just be aware of the fact that people will probably make fun of you at one point or another.

Also, it's important to first learn [HTML and CSS](#html-css-and-javascript) before attempting to learn PHP. PHP is a language which attempts to "extend" and work with HTML, so may not fully make sense if you try and learn it before picking up basic web development.

- **Online courses:**
    - Codecademy's [PHP track](http://www.codecademy.com/en/tracks/php)
    - Team Treehouse's [PHP course](http://teamtreehouse.com/features/php) - allows a free 14-day trial, but later requires payment.
- **Interactive resources:**
    - [Learn PHP][php-learn]
      An interactive guide that teaches basic PHP.
- **Exercises:**
    - [DevProjects](https://www.codementor.io/projects/php)
      A growing list of PHP real-world projects that is free for all. Solutions and discussions can be found in most projects. Paid help to complete the project is optional through related product, Codementor.
- **Video tutorials:** N/A
- **Books and tutorials (online):**
    - [PHP Manual][php-manual]
      The official tutorial on PHP. Tends to focus on language features and syntax.
    - [TutorialPoint's PHP Tutorial][php-tutorialspoint]
      An introduction to PHP. Tends to focus on syntax. May make a good reference.
    - [PHP The Right Way][php-right-way]
      A comprehensive guide that covers modern best practices in PHP and attempts to address common flaws, misconceptions, and errors that many beginners (and many tutorials) seem to possess. Assumes some prior knowledge of PHP.
- **Books (paper):**
    - [PHP for Absolute Beginners][php-absolute]
      An introductory text on PHP.
    - [PHP Solutions: Dynamic Web Design Made Easy, 2nd edition][php-solutions]
      An example-driven introduction to PHP.

  [php-learn]: http://www.learn-php.org/

  [php-fractal]: http://eev.ee/blog/2012/04/09/php-a-fractal-of-bad-design/

  [php-manual]: http://php.net/manual/en/index.php
  [php-tutorialspoint]: http://www.tutorialspoint.com/php/
  [php-right-way]: http://www.phptherightway.com/

  [php-absolute]: http://www.amazon.com/PHP-Absolute-Beginners-Jason-Lengstorf/dp/1430268158/ref=dp_ob_title_bk
  [php-solutions]: http://www.amazon.com/PHP-Solutions-Dynamic-Design-Made/dp/1430232498/ref=dp_ob_title_bk


### Python

Note: there are currently two versions of Python that are commonly taught and used -- Python 2, and Python 3. Python 3 is the most recent version, but for a variety of reasons Python 2 still is fairly popular among many developers.

If you're not sure which version to pick, my recommendation would be to pick the resource which looks like the best fit for you, and just use whatever version they're recommending. Luckily, the differences between the two are very minor (at least from the perspective of the beginner), so there's really no difference if you learn using Python 2 vs Python 3.

- **Online courses:**
    - edx's [Introduction to Computer Science and Programming Using Python][python-mit-intro]
      The companion book can be [found here][python-mit-intro-book]. The course is designed for beginners, part of a 2-part series, is self-paced, and has an emphasis on computation and data science.
        -   MIT Open Courseware also offers a gentler "lead-in" course designed for those with no programming background that you can take before taking the above: [Building Programming Experience: A Lead-In to 6.001][python-mit-lead-in].
    - MIT Open Courseware's [A Gentle Introduction to Programming Using Python][python-mit-gentle]
      A gentler version of the above.
    - Coursera's [Programming for Everybody (Python)][python-coursera]
      For beginners; requires registration.
    - Codecademy's [Python track][python-codecademy]
      For beginners; tends to focus primarily on syntax.
    - Udacity's [Programming Foundations with Python][python-udacity]
      Requires some prior programming experience; focuses on object-oriented programming.
    - Team Treehouse's [Python course][python-treehouse]
      Allows a free 14-day trial, but later requires payment.
- **Interactive resources:**
    - [LearnPython][python-learn]
      An interactive online guide that teaches basic Python.
    - [Try Python][python-try]
      Another interactive online guide.
- **Video tutorials:** N/A
- **Books and tutorials (online):**
    - [Learn Python the Hard Way][python-lpthw]
      Part of the "Learn X the Hard Way" series. Despite its name, this is one of the easiest introductions to Python available.
    - [Automate the Boring Stuff with Python][python-automate]
      A book for complete beginners. It is aimed at office workers, students, administrators, and hobbyists who want to learn how to write useful, practical programs rather than necessarily become software engineers. From the [Invent with Python][python-invent] author.
    - How to Think Like a Computer Scientist ([Python 2 version][python-think-cs-2] and [Python 3 version][python-think-cs-3])
      A comprehensive introductory text on Python.
    - [Think Python][python-think]
      Another comprehensive introductory text on Python.
    - The official Python tutorial (for [Python 2][python-official-2] and [Python 3][python-official-3]). Moves a little quickly, but is very comprehensive and thorough.
    - [Problem Solving with Algorithms and Data Structures][python-problem]
      A fantastic introduction to data structures and algorithms and other traditional
      computer science concepts using Python. While it does briefly cover Python syntax,
      it assumes that you already have some basic prior experience.
    - [Dive into Python 3][python-dive]
      An accelerated introduction to Python. Warning: do NOT use "Dive into Python 2". It's very outdated.
    - [Program Arcade Games With Python And Pygame][python-arcade]
      A fantastic and thorough introduction to Python via making games. For beginners.
    - [Invent with Python][python-invent]
      Teaches programming through the creation of computer games with Python and Pygame. For beginners.
    - [The Hitchhiker's Guide to Python][python-hitchhiker]
      A comprehensive introduction to the Python ecosystem. Covers how to properly configure and set up a development environment in Python, best practices, writing idiomatic code, what the best 3rd party libraries are for different tasks, and shipping your code. Useful for both beginners and experts (however, the guide does not actually teach Python itself).
    - [pycrumbs][python-pycrumbs]
      A huge list of many useful articles, tutorials, and snippits on Python, ranging from basic to advanced.
    - [More free books][python-more]
    - [PyMOTW][pymotw]
      A tour of the Python standard library through short examples.
- **Books (paper):**
    - [Import Python][python-import]
      A catalog of Python books (some are free)
- **Exercises:**
    - [Pyschools][python-pyschools]
      Exercises and challenges in Python. Challenges require (free) registration.
    - [DevProjects](https://www.codementor.io/projects/python)
      A list of growing, free Python projects that cater to web development and data analysis.

  [python-codecademy]: http://www.codecademy.com/tracks/python
  [python-udacity]: https://www.udacity.com/course/ud036
  [python-coursera]: https://www.coursera.org/course/pythonlearn
  [python-mit-intro]: https://www.edx.org/course/introduction-computer-science-mitx-6-00-1x-0#.VJw5pv-kAA
  [python-mit-intro-book]:http://mitpress.mit.edu/books/introduction-computation-and-programming-using-python-0
  [python-mit-lead-in]: http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-090-building-programming-experience-a-lead-in-to-6-001-january-iap-2005/
  [python-mit-gentle]: http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-189-a-gentle-introduction-to-programming-using-python-january-iap-2011/
  [python-treehouse]: http://teamtreehouse.com/features/python

  [python-learn]: http://learnpython.org
  [python-try]: http://www.trypython.org/

  [python-automate]: http://automatetheboringstuff.com/
  [python-lpthw]: http://learnpythonthehardway.org/book/
  [python-think-cs-2]: http://www.openbookproject.net/thinkcs/python/english2e/
  [python-think-cs-3]: http://www.openbookproject.net/thinkcs/python/english3e/
  [python-think]: http://www.greenteapress.com/thinkpython/
  [python-official-2]: https://docs.python.org/2/tutorial/
  [python-official-3]: https://docs.python.org/3/tutorial/
  [python-problem]: http://interactivepython.org/runestone/static/pythonds/index.html
  [python-dive]: http://www.diveintopython3.net/
  [python-invent]: http://inventwithpython.com/
  [python-arcade]: http://ProgramArcadeGames.com
  [python-hitchhiker]: https://python-guide.readthedocs.org/en/latest/
  [python-pycrumbs]: http://resrc.io/list/4/pycrumbs/
  [python-more]: https://github.com/vhf/free-programming-books/blob/master/free-programming-books.md#python

  [python-import]: http://importpython.com/books/

  [python-pyschools]: http://www.pyschools.com/
  [pymotw]: http://pymotw.com/

### Golang
The Go programming language is an open source project to make programmers more productive.

Go is expressive, concise, clean, and efficient. Its concurrency mechanisms make it easy to write programs that get the most out of multicore and networked machines, while its novel type system enables flexible and modular program construction. Go compiles quickly to machine code yet has the convenience of garbage collection and the power of run-time reflection. It's a fast, statically typed, compiled language that feels like a dynamically typed, interpreted language.

In addition to the resources available [at golang.org](http://golang.org/doc/#learning) there are a range of community-driven initiatives:

- **Orgs:**
  - [GoBridge](https://golangbridge.org/): Building Bridges That Educate &
Empower Underrepresented Communities
  - [Women Who Go](http://www.womenwhogo.org/): We are women of the Go community.

- **Starter Books:**
  - [The Little Go Book](http://openmymind.net/The-Little-Go-Book/): The Little Go Book is a free introduction to Google's Go programming language. It's aimed at developers who might not be quite comfortable with the idea of pointers and static typing. It's longer than the other Little books, but hopefully still captures that little feeling.
  - [An Introduction to Programming in Go](http://openmymind.net/The-Little-Go-Book/): This book is a short, concise introduction to computer programming using the language Go. Designed by Google, Go is a general purpose programming language with modern features, clean syntax and a robust well-documented common library, making it an ideal language to learn as your first programming language.
  - [Go Bootcamp](http://www.golangbootcamp.com/): This companion book contains material initially written specifically for this event as well as content from Google & the Go team under Creative Commons Attribution 3.0 License and code licensed under a BSD license.
  - [Learning Go](https://www.miek.nl/go/): A online book to start learning Golang. It features numerous exercises (and answers).
  - [Go for Javascript Developers](https://github.com/pazams/go-for-javascript-developers): This book helps Javascripters become Gophers. Outlining the differences between these languages makes it easier to switch back and forth, and can help mitigate potential issues when doing so.
  - [The Go Programming Language](http://www.gopl.io/): The Go Programming Language* is the authoritative resource for any programmer who wants to learn Go. Alan A. A. Donovan and Brian W. Kernighan show you how to write clear and idiomatic Go to solve real-world problems. The book does not assume prior knowledge of Go nor experience with any specific language, so you'll find it accessible whether you're most comfortable with JavaScript, Ruby, Python, Java, or C++. The book features hundreds of interesting and practical examples of idiomatic Go code that cover the whole language, its most important libraries, and a wide range of applications. Source code is freely available for download from the book's companion web site and may be conveniently fetched, built, and installed using the `go get` command.
  - [Go in Action](https://www.manning.com/books/go-in-action): Go in Action introduces the Go language, guiding you from inquisitive developer to Go guru. The book begins by introducing the unique features and concepts of Go. (We assume you're up to speed with another programming language already, so don't expect to spend a lot of time rehearsing stuff you already know.) Then, you'll get hands-on experience writing real-world applications including web sites and network servers, as well as techniques to manipulate and convert data at speeds that will make your friends jealous. In the final chapters, you'll go in-depth with the language and see the tricks and secrets that the Go masters are using to make their applications perform. For example, you'll learn to use Go's powerful reflection libraries and work with real-world examples of integration with C code.
  - [Go Programming Blueprints](https://www.packtpub.com/application-development/go-programming-blueprints): Build real-world, production-ready solutions in Go using cutting-edge technology and techniques. Intended for seasoned Go programmers who want to put their expertise in Go to use to solve big, real-world, modern problems. With a basic understanding of channels and goroutines, you will hone your skills to build tools and programs that are quick and simple. You need not be an expert in distributed systems or technologies in order to deliver solutions capable of great scale. It is assumed that you are familiar with the basic concepts of Go.
  - [Programming in Go: Creating Applications for the 21st Century](http://www.informit.com/store/programming-in-go-creating-applications-for-the-21st-9780321774637): Programming in Go brings together all the knowledge you need to evaluate Go, think in Go, and write high-performance software with Go. Summerfield presents multiple idiom comparisons showing exactly how Go improves upon older languages, calling special attention to Go’s key innovations. Along the way, he explains everything from the absolute basics through Go’s lock-free channel-based concurrency and its flexible and unusual duck-typing type-safe approach to object-orientation.
  - [Introducing Go: Build Reliable, Scalable Programs](http://shop.oreilly.com/product/0636920046516.do):  Perfect for beginners familiar with programming basics, this hands-on guide provides an easy introduction to Go, the general-purpose programming language from Google. Author Caleb Doxsey covers the language's core features with step-by-step instructions and exercises in each chapter to help you practice what you learn.
  - [Learn Go](https://www.manning.com/books/get-programming-with-go?a_aid=nathany&a_bid=53f68821): *Learn Go* is a beginner’s guide to the Go programming language, aimed squarely at hobbyists and new developers. It’s chock-full of exercises that you can tackle with nothing more than a web browser. Move forward each day with succinctly written chapters punctuated by elaborate challenges. By the end you will have cracked ancient ciphers, discovered the wonders of cellular automatons, planned a vacation on Mars, and directed rovers to gather weather data. This is just the beginning. What you build next is up to you.
  - [Go Programming by Example](https://www.amazon.com/Go-Programming-Example-Agus-Kurniawan-ebook/dp/B00TWLZVQQ): Go, commonly referred to as golang, is a programming language initially developed at Google in 2007. This book helps you to get started with Go programming. It describes all the elements of the language and illustrates their use with code examples.

- **Web Development Books:**

  - [Building Web Apps with Go](https://www.gitbook.com/book/codegangsta/building-web-apps-with-go/details): A good resource for start Building Web Apps with Go.
  - [Build Web Application with Golang](https://www.gitbook.com/book/astaxie/build-web-application-with-golang/details): Another awesome book for learning Web Development in Golang.
  - [Mastering Go Web Services](http://shop.oreilly.com/product/9781783981304.do): This book will take you through the most important aspects of designing, building, and deploying a web service utilizing idiomatic REST practices with a focus on speed, security, and flexibility. You will begin by building your first API in Go using the HTTP package. You will look at designing and building your application including popular design structures like Model-View-Controller. You will also understand methods for deploying code to staging and development. Finally, you will see how the security features in Go can be used for protection against SQL injection, and sensitive data compromise.
  - [Level Up Your Web Apps With Go](https://learnable.com/books/level-up-your-web-apps-with-go): This book gives you all you need to use Go in your web applications. You’ll learn the basic concepts — language structures, the standard library, and Go tools — then tackle more advanced features like concurrency concepts, testing methodologies, and package structures. At each step, you’ll get advice for better coding in Go. You’ll see how to structure projects, how to use concurrency effectively, and best practices for testing—as well as many other hints and tips gleaned from real world experience of developing web applications with Go.
  - [Go Web Programming](https://www.manning.com/books/go-web-programming): Go Web Programming teaches you how to build web applications in Go using modern design principles. You'll work through numerous examples that introduce core concepts like processing requests and sending responses, template engines, and data persistence. You'll also dive into more advanced topics, such as concurrency, web application testing and deployment both to barebones servers and PaaS providers.
  - [Build webapps in Go the anti textbook](https://github.com/thewhitetulip/web-dev-golang-anti-textbook): This book was written to teach how to develop web applications in Go for people who know a bit of Go and have basic information about web applications in general. We (you) will build a webapp without using a third party framework and using as few external libraries as possible. The advantage is that you'll learn a lot when you code without a framework.
  - [Cloud Native Go: Building Web Applications and Microservices for the Cloud with Go and React](https://www.amazon.com/Cloud-Native-Applications-Microservices-Developers/dp/0672337797): Today, companies and developers need to respond to changing markets at breakneck speeds. Organizations that aren't built on highly-available, rapidly-evolving software are going the way of the dinosaurs. Cloud Native Go brings together the knowledge developers need to build massive-scale cloud applications that meet the insatiable demands of today's customers and markets.
  - [Web Development with Go: Learn to Create Real World Web Applications using Go](https://gumroad.com/l/web-development-with-go) : Web Development with Go was written to teach both beginners and experts how to create and deploy a real web application. You won't be building a boilerplate TODO list, but will instead be creating and deploying a production ready photo gallery application, similar to Pixieset, from scratch. The book assumes no previous web development experience and covers everything you need to know to successfully build your own web application.
  - [Go: Building Web Applications](https://www.amazon.com/dp/B01LD8K5C0/ref=cm_sw_su_dp): This course is an invaluable resource to help you understand Go's powerful features to build simple, reliable, secure, and efficient web applications.


- **Advanced Go Books:**
  - [Test-driven development with Go](https://leanpub.com/golang-tdd): A short guide to Test-driven development in golang
  - [Network Programming with Go](https://jan.newmarch.name/go/): An e-book on building network applications using the Google Go programming language. Free to
  - [Mastering Concurrency in Go](http://shop.oreilly.com/product/9781783983483.do): This book will take you through the history of concurrency, how Go utilizes it, how Go differs from other languages, and the features and structures of Go's concurrency core. Each step of the way, the book will present real, usable examples with detailed descriptions of the methodologies used. By the end, you will feel comfortable designing a safe, data-consistent, high-performance concurrent application in Go.
  - [Go in Practice](https://www.manning.com/books/go-in-practice): Go in Practice guides you through dozens of real-world techniques in key areas like package management, microservice communication, and more. Following a cookbook-style Problem/Solution/Discussion format, this practical handbook builds on the foundational concepts of the Go language and introduces specific strategies you can use in your day-to-day applications. You'll learn techniques for building web services, using Go in the cloud, testing and debugging, routing, network applications, and much more.
  - [A Go Developer's Notebook](https://leanpub.com/GoNotebook/): A developer's experience in golang.
  - [The Go Programming Language Phrasebook](http://www.informit.com/store/go-programming-language-phrasebook-9780321817143): Tested, easy-to-adapt code examples illuminate every step of Go development, helping you write highly scalable, concurrent software. You’ll master Go-specific idioms for working with strings, collections, arrays, error handling, goroutines, slices, maps, channels, numbers, dates, times, files, networking, web apps, the runtime, and more.


- **Videos:**
  - [Just for Func](https://www.youtube.com/channel/UC_BzFbxG2za3bp5NRRRXJSw)- Series of talk recordings and screencasts mainly about Go and the Google Cloud Platform
  - [Gopher Academy](https://www.youtube.com/channel/UCx9QVEApa5BKLw9r8cnOFEA)- A collection of videos and conference talks for learning Go.
  - [GoingGo.net](http://www.goinggo.net/) - A collection of videos and articles for learning Go.
  - [O'Reilly Go Fundamentals](http://shop.oreilly.com/category/learning-path/go-fundamentals.do) - Video learning path for Go programming.
  - [Learn Go in an Hour](https://www.youtube.com/watch?v=CF9S4QZuV30) Learn the go programming language in one hour.
  - [Learning to Program in Go](https://www.youtube.com/playlist?list=PLei96ZX_m9sVSEXWwZi8uwd2vqCpEm4m6) - a multi-part video training class.
- **Exercises:**
  - [Exercism.io - Go](http://exercism.io/languages/go) - Online code exercises for Go for practice and mentorship.
  - [Outlearn.com](https://www.outlearn.com/search?filter=path&q=golang) - Jump right into Go with a tour, helpful examples, sample app, and common pitfalls.
  - [The Go Bridge Foundry](https://github.com/gobridge) - A member of the [Bridge Foundry](http://bridgefoundry.org/) family, offering a complete set of free Go training materials with the goal of bringing Go to under-served communities.
  - [Go Fragments](http://www.gofragments.net/) - A collection of annotated Go code examples.
  - [Golang Tutorials](http://golangtutorials.blogspot.com/2011/05/table-of-contents.html) - A free online class.
  - [Learn Go in Y minutes](http://learnxinyminutes.com/docs/go/) is a top-to-bottom walk-through of the language.
  - [Go By Example](http://gobyexample.com/) - Go by Example is a hands-on introduction to Go using annotated example programs. Check out the first example or browse the full list below.
  -  [Pluralsight Classes for Go](http://www.pluralsight.com/tag/golang) - A growing collection of (paid) online classes.
- **Workshops:**
  - [Free Go Language Workshop](https://www.frameworktraining.co.uk/go-language-free-training-workshop/) Framework Training is running regular free BYOD workshops in London, UK
  - [Workshop-Go](https://github.com/sendwithus/workshop-go) - Startup Slam Go Workshop - examples and slides.
- **Learning resources for specific topics:**
  - [LearnConcurrency](LearnConcurrency) outlines a course of study of Go's concurrency model and patterns.
  - [LearnErrorHandling](LearnErrorHandling) links to resources about error handling in Go.
  - [LearnTesting](LearnTesting) links to resources about testing in Go.
  - [LearnServerProgramming](LearnServerProgramming) links to resources about server programming in Go.
- **Further reading:**
  - [50 Shades of Go: Traps, Gotchas, Common Mistakes for New Golang Devs](http://devs.cloudimmunity.com/gotchas-and-common-mistakes-in-go-golang/index.html)
  - [Newspaper](http://www.newspaper.io) is a topic based newsfeed for slack. Built on Go

### Ruby

Note: Ruby is a dynamic, reflective, object-oriented, general-purpose programming language. It was designed and developed in the mid-1990s by Yukihiro "Matz" Matsumoto in Japan. According to its creator, Ruby was influenced by Perl, Smalltalk, Eiffel, Ada, and Lisp.

- **Online courses:**
    - Codecademy's [Ruby track][ruby-codecademy]
      For beginners. Tends to focus on syntax.
    - Team Treehouse's [Ruby course][ruby-treehouse]
      Allows a free 14-day trial, but later requires payment.
- **Interactive tutorials:**
    - [RubyMonk][ruby-rubymonk]
      A collection of interactive tutorials to help you learn basic and advanced Ruby.
    - [TryRuby][ruby-try]
      An interactive online guide that teaches you basic Ruby step-by-step.
    - [Learn Ruby][ruby-learn]
      A downloadable set of interactive tutorials.
- **Video tutorials:** N/A
- **Books and tutorials (online):**
    - [Learn Ruby The Hard Way][ruby-lrthw]
      Part of the "Learn X The Hard Way" series. Despite its name, this is one of the easiest introductions to Ruby available.
    - [Why's (Poignant) Guide to Ruby][ruby-poignant]
      A little quirky, but still very good.
    - [More free books][ruby-more]
- **Books (paper):**
    - [The Well-Grounded Rubyist][ruby-grounded]
      A comprehensive and thorough introduction to Ruby. For beginners.
    - [Eloquent Ruby][ruby-eloquent]
      A guide on how to write Ruby idiomatically and cleanly. This book assumes that you already know Ruby or some other programming language.
- **Exercises:**
    - [Ruby Quiz][ruby-quiz]
      A series of exercises on writing programs in Ruby. New exercises are no longer being written, but the existing exercises are still very good.
    - [DevProjects](https://www.codementor.io/projects/ruby)
      A compilation of free and unique Ruby projects for developers of all levels of expertise.

  [ruby-codecademy]: http://www.codecademy.com/tracks/ruby
  [ruby-treehouse]: http://teamtreehouse.com/features/ruby

  [ruby-rubymonk]: http://rubymonk.com/
  [ruby-try]: http://tryruby.org
  [ruby-learn]: http://rubykoans.com/

  [ruby-lrthw]: http://learncodethehardway.org/ruby/
  [ruby-poignant]: http://mislav.uniqpath.com/poignant-guide/
  [ruby-more]: https://github.com/vhf/free-programming-books/blob/master/free-programming-books.md#ruby

  [ruby-grounded]: http://www.amazon.com/The-Well-Grounded-Rubyist-David-Black/dp/1933988657
  [ruby-eloquent]: http://www.amazon.com/Eloquent-Ruby-Addison-Wesley-Professional-Series/dp/0321584104

  [ruby-quiz]: http://rubyquiz.com/


### Scratch

Scratch is a language wherein you create programs by dragging together and connecting "blocks". Unlike other programming languages, Scratch is very visual, making it a very good first programming language, especially for children and younger teens.

Because not many people may be familiar with Scratch, this section will contain resources that are helpful both for _learning_ Scratch, and _teaching_ Scratch.

There are two

- **Online courses:**
    - edX's [Programming in Scratch](https://www.edx.org/course/programming-scratch-harveymuddx-cs002x#.VJw5t_-kAA) - for beginners.
    - edX's [Middle-Years Computer Science](https://www.edx.org/course/middle-years-computer-science-harveymuddx-cs001x#.VJw5rP-kAA) - a course designed to help teachers design an engaging computer science curriculum for middle-schoolers using Scratch.
- **Interactive tutorials:** N/A
- **Video tutorials:**
    - [A Collection of Scratch Videos][scratch-official] from Scratch's website
      A collection of video tutorials on Scratch for absolute beginners. Very comprehensive.
- **Books and tutorials (online):**
    - [Invent with Scratch!][scratch-invent]
      An introductory text on Scratch. For beginners.
    - [Scratch for Budding Computer Scientists][scratch-budding]
      A short tutorial that takes a more formalized approach to teaching Scratch. Best suited for those with some prior experience.
    - [Computer Science Concepts in Scratch][scratch-cs-concepts]
      A thorough introduction to Scratch. For beginners.
    - [Scratch Advanced Topics][scratch-advanced]
      A collection of resources and guides on advanced usage of Scratch. Not for beginners.
    - Reference guides: for [Scratch][scratch-reference] and [Snap/Build Your Own Blocks][scratch-snap-reference] (a variant of Scratch)
      Contains comprehensive descriptions of all language features. The Scratch reference will be useful for all levels, and the Snap reference will be particularly useful for those who are already proficient at programming in another language.
    - [Scratch for Educators][scratch-educators]
      Scratch's official portal and collection of resources for teaching using Scratch.
    - [More free books][scratch-more]
- **Books (paper):**
  - [Scratch Cards](https://scratch.mit.edu/info/cards) - Scratch cards provide a quick way to learn new Scratch code.
  - [Learn to Program with Scratch: A Visual Introduction to Programming with Games, Art, Science, and Math](http://www.amazon.com/Learn-Program-Scratch-Introduction-Programming/dp/1593275439/ref=sr_1_1?ie=UTF8&qid=1460418004&sr=8-1&keywords=scratch+programming) - In Learn to Program with Scratch, author Majed Marji uses Scratch to explain the concepts essential to solving real-world programming problems. The labeled, color-coded blocks plainly show each logical step in a given script, and with a single click, you can even test any part of your script to check your logic.
  - [Super Scratch Programming Adventure! (Covers Version 2): Learn to Program by Making Cool Games](http://www.amazon.com/Scratch-Programming-Adventure-Covers-Version/dp/1593275315/ref=sr_1_5?ie=UTF8&qid=1460418004&sr=8-5&keywords=scratch+programming) - In Super Scratch Programming Adventure!, kids learn programming fundamentals as they make their very own playable video games. They'll create projects inspired by classic arcade games that can be programmed (and played!) in an afternoon. Patient, step-by-step explanations of the code and fun programming challenges will have kids creating their own games in no time.
- **Exercises:**
  - [SHS Programming 1 Exercises](https://scratch.mit.edu/studios/532108/) - LTPWS Studio of Exercises

  [scratch-official]: http://scratch.mit.edu/help/videos/

  [scratch-invent]: http://inventwithscratch.com/about/
  [scratch-budding]: http://cs.harvard.edu/malan/scratch/index.php
  [scratch-cs-concepts]: http://stwww.weizmann.ac.il/g-cs/scratch/scratch_en.html
  [scratch-advanced]: http://wiki.scratch.mit.edu/wiki/Advanced_Topics_%28forum%29
  [scratch-reference]: http://download.scratch.mit.edu/ScratchReferenceGuide14.pdf
  [scratch-snap-reference]: http://snap.berkeley.edu/SnapManual.pdf
  [scratch-educators]: http://scratch.mit.edu/educators/
  [scratch-more]: https://github.com/vhf/free-programming-books/blob/master/free-programming-books.md#scratch

## Data

### Neo4j and Graph Databases

[Neo4j][Neo4j] is an open source NOSQL graph database, implemented in Java. It saves structured data in graphs rather than in tables. Graph databases simplify and speed up access to data that is complex and contains many connections. They use graph structures with nodes, edges, and properties to store and access connected information, and can traverse parts of the data without touching the whole graph.

Neo4j is widely used for:

- Highly connected data
- Recommendation
- Path Finding
- Data First Schema
- Schema Evolution
- A* (Least Cost Path)

- **Online courses:**
    - [Neo4j Training][Neo4j-Training] - free course, completely online
    - [GraphGist][GraphGist] - geek out on real graphs on finance, sports, politics, or even The Hobbit

[Neo4j-Training]: http://message.neotechnology.com/O0005CuN03006GNt0z0ffeO
[GraphGist]: http://message.neotechnology.com/R00NCefOuf003050GuN0A60
[Neo4j]: https://neo4j.com/

### MongoDB

[MongoDB](https://www.mongodb.com/) is an open-source [NoSQL database](https://en.wikipedia.org/wiki/NoSQL) engine built in C++.

It's a document-store database which means it stores data as a "document" inside a collection, with multiple collections inside a database. Multiple databases can exist for each server. The document data is stored as [BSON](https://en.wikipedia.org/wiki/BSON) which is [JSON](http://www.json.org/) (JavaScript Object Notation) in a binary format for performance. The data is [schema-less](https://www.google.com/search?q=schema-less&oq=schema-less&aqs=chrome..69i57j0l5.446j0j4&sourceid=chrome&ie=UTF-8) which means each document can have as many keys and values as you want with no restriction on the type of data.

It's easy to think of documents in collections like rows in a relational database table, except that these documents can have any arbitrary amount of properties (like columns for rows) and they can be different for each document and include lots of nesting like arrays of more properties. This is very powerful way to store complex data and matches up well to the object-oriented nature of most programming languages.

MongoDB runs on both Windows and Linux servers and has lots of documentation and years of production usage now so it's considered a stable and useful database, although there are continuing issues with durability and an overly-complicated replication setup to keep in mind.

- **Online courses:**
    - [MongoDB University][mongodb-university] - Paid course but it comes with a certification

- **Video Tutorials:**
    - [MongoDB Tutorial For Beginners | MongoDB Training][mongo-for-beginners]

- **Books and tutorials (online):**
    - [The Littel MongoDB Book][the-little-mongodb-book]

[mongodb-university]: https://university.mongodb.com/
[mongo-for-beginners]: https://www.youtube.com/watch?v=4ioP11POfZ4
[the-little-mongodb-book]: http://openmymind.net/mongodb.pdf

---

## Other topics

TODO: EXPAND AND POLISH

### Developing on specific platforms

Please see our [FAQ](http://www.reddit.com/r/learnprogramming/wiki/faq#wiki_how_do_i_get_starting_making_mobile_apps.2Fandroid_apps.2Fios_apps.2Fwindows_phone_apps.3F) for more information.

#### Android

- [Spreadsheet of Android resources](http://www.reddit.com/r/learnprogramming/comments/1dy9wj/im_a_cpa_who_learned_java_android_and_published/)
- [List of Android learning resources](http://www.reddit.com/r/learnprogramming/comments/22xlu9/you_want_to_how_to_write_apps_for_android/)
- [Google Code University](https://developers.google.com/university/) - also contains tutorials on other Google technologies.
- [Developing Android Apps](https://www.udacity.com/course/ud853) - via Udacity. Assumes prior programming experience.
- Team Treehouse's [Android course](http://teamtreehouse.com/features/android) - allows a free 14-day trial, but later requires payment.
- [Devprojects](https://www.codementor.io/projects/mobile) - free real-world mobile app projects that can be implemented for both Android and iOS.
- [More free books](https://github.com/vhf/free-programming-books/blob/master/free-programming-books.md#android)

#### Mac and iOS

- [List of iOS learning resources](http://www.reddit.com/r/learnprogramming/comments/22w8sk/you_want_to_know_where_to_start_for_writing_apps/)
- [List of iOS Video Tutorials](http://www.reddit.com/r/learnprogramming/comments/22zkce/want_to_learn_ios_development_best_video/)
- Apple's [iOS Developer Library](https://developer.apple.com/library/ios/navigation/)
- Apple's [Mac Developer Library](https://developer.apple.com/library/mac/navigation/)
- [Intro to iOS App Development with Swift](https://www.udacity.com/course/ud585) - via Udacity. Assumes prior programming experience.
- Team Treehouse's [iOS course](http://teamtreehouse.com/features/ios) - allows a free 14-day trial, but later requires payment.
- [Devprojects](https://www.codementor.io/projects/mobile) - free real-world mobile app projects that can be implemented for both Android and iOS.
- [More free books](https://github.com/vhf/free-programming-books/blob/master/free-programming-books.md#ios)

#### Windows and Windows phones

- Microsoft's [Developer Guides](http://msdn.microsoft.com/en-us/vstudio/cc136611)
- Microsoft's [App Hub](http://create.msdn.com/en-US/education/catalog/) - resources for mobile and XNA game development.
- More free books:
    - [.NET](https://github.com/vhf/free-programming-books/blob/master/free-programming-books.md#net-framework)
    - [Windows 8 and Windows Phone](https://github.com/vhf/free-programming-books/blob/master/free-programming-books.md#windows-8)

TODO: Expand? Don't want to duplicate too much existing content.

### Data structures and algorithms

Unless otherwise noted, all of the resources in this category assume prior programming experience.

- **Online courses:**
    - Udacity's [Intro to Algorithms](https://www.udacity.com/course/cs215) - assumes  proficiency in math up to the Algebra 2 level.
    - [Andrew Ng's Machine Learning course](https://www.coursera.org/learn/machine-learning)
    - [Lynda Data Science Basics](http://www.lynda.com/SharedPlaylist/ff466840b2ba481e82149ecca9a5bdd6) - Explore Data Science with this selection of courses to help you analyze and gain insight on your business data for improved performance and results.
    - [Intro to Data Science](https://www.udacity.com/course/intro-to-data-science--ud359) - The class will focus on breadth and present the topics briefly instead of focusing on a single topic in depth. This will give you the opportunity to sample and apply the basic techniques of data science.
    - Coursera's [Algorithms: Design and Analysis, Part 1](https://www.coursera.org/course/algo) - lectures are archived. Assumes some familarity with proofs.
    - Open Culture has several good video playlists (mostly on YouTube)
        - [Algorithm Design and Analysis](https://www.youtube.com/playlist?list=PL6EF0274BD849A7D5) - hosted by UCDavis (University of California, Davis)
        - [Computer Science 61B (Data structures)](https://www.youtube.com/playlist?list=PL-XXv-cvA_iDXrTvCvDgIkeCWeSIDr4Yh) - hosted by UCBerkeley (University of California, Berkeley).
        - [CS2: Data Structures and Algorithms](https://www.youtube.com/course?feature=edu&list=ECE621E25B3BF8B9D1&category=University%2FScience) - Hosted by the University of New South Wales
    - MIT Open Courseware's [Introduction to Algorithms](http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-006-introduction-to-algorithms-fall-2011/) and [Design and Analysis of Algorithms](http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-046j-design-and-analysis-of-algorithms-spring-2012/)
    - Khan Academy's [Algorithms](https://www.khanacademy.org/computing/computer-science/algorithms)
- **Interactive tutorials:** N/A
- **Exercises:**
    - [Codingbat][algo-codingbat]
      Contains Java and Python exercises. For beginners and intermediate-level programmers.
    - [CodeAbbey][algo-codeabbey]
      Similar to Codingbat.
    - [HackerRank][algo-hackerrank]
      Contains a large collection of exercises, from basic up to the competitive
      level. Good for both beginners and advanced programmers. Also holds their own
      online competition.
    - [TopCoder][algo-topcoder]
      Similar to HackerRank.
    - [UVa Online Judge][algo-uva]
      A collection of programming problems and solutions from multiple programming
      competitions.
    - [Project Euler][algo-euler]
      A collection of programming exercises. The exercises are more math-oriented,
      and are not always CS-oriented.
- **Video tutorials:** N/A
- **Books and tutorials (online):**
    - [Problem Solving with Algorithms and Data Structures][algo-problem]
      A very thorough introduction to data structures and algorithms. Although it uses
      Python, the main concepts taught should be applicable to every language. Starts with
      a quick overview of Python for those unfamiliar to the language.
    - [Algorithms by Robert Sedgewick](http://algs4.cs.princeton.edu/home/) which is in Java and accompanies [these lectures](https://www.coursera.org/course/algs4partI) on Coursera.
    - [The Stony Brook Algorithm Repository](http://www3.cs.stonybrook.edu/~algorith/) - a comprehensive reference of many different data structures and algorithms.
    - [The Big-O Cheat Sheet](http://bigocheatsheet.com/) - a cheat sheet containing links and condensed information about the top most commonly-used/commonly-taught data structures and algorithms.
- **Books (paper):**
    - [Introduction to Algorithms](http://www.amazon.com/Introduction-Algorithms-Thomas-H-Cormen/dp/0262033844) - the canonical guide to algorithms and is very comprehensive. The book is language agnostic, moves at an accelerated pace, and is accompanied by lectures [here](http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-046j-introduction-to-algorithms-sma-5503-fall-2005/index.htm).
    - [The Algorithm Design Manual](http://www.amazon.com/Algorithm-Design-Manual-Steve-Skiena/dp/0387948600) - the first half of the book emphasizes the design and analysis of algorithms, and the second half is a catalog of the 75 most important algorithmic problems for reference.
    - [Machine Learning for Hackers](http://www.amazon.com/Machine-Learning-Hackers-Drew-Conway/dp/1449303714) - If you’re an experienced programmer interested in crunching data, this book will get you started with machine learning.

    - [How can I rebuild my base of algorithms/data structures knowledge?](http://stackoverflow.com/q/1697572/646543) - contains links to various recommended books and suggestions for improvement.
    - [Data Driven:
Creating a Data Culture](http://www.oreilly.com/data/free/data-driven.csp) - Succeeding with data isn’t just a matter of putting Hadoop in your machine room, or hiring some physicists with crazy math skills.

  [algo-problem]: http://interactivepython.org/runestone/static/pythonds/index.html
  [algo-codingbat]: http://codingbat.com/
  [algo-codeabbey]: http://www.codeabbey.com/
  [algo-hackerrank]: https://www.hackerrank.com/
  [algo-topcoder]: http://www.topcoder.com/
  [algo-uva]: http://uva.onlinejudge.org/
  [algo-euler]: https://projecteuler.net/


---

## Tools

### Version control

#### Git

- **Online courses:**
    - [How to Use Git and GitHub](https://www.udacity.com/course/ud775) - via Udacity.
- **Interactive tutorials:**
    - [Learn Git Branching](http://pcottle.github.io/learnGitBranching/) - a very visual interactive tutorial starting from the absolute basics with a high emphasis on understanding the internals/what each git command really means.
    - [Try Git](https://try.github.io/levels/1/challenges/1) - an interactive tutorial that teaches basic Git.
- **Exercises:** N/A
- **Video tutorials:** N/A
- **Books and tutorials (online):**
    - [Learn Version Control with Git](http://www.git-tower.com/learn/ebook/command-line/introduction) - an introduction to Git for the absolute beginner (via git-tower).
    - Git has an [official reference and book](http://git-scm.com/documentation)
    - [More free books](https://github.com/vhf/free-programming-books/blob/master/free-programming-books.md#git)
- **Books (paper):** N/A

#### Mercurial

- **Online courses:** N/A
- **Interactive tutorials:** N/A
- **Exercises:** N/A
- **Video tutorials:** N/A
- **Books and tutorials (online):**
    - [HgInit](http://hginit.com/01.html) - a basic introduction to Mercurial.
    - [Mercurial: The Definitive Guide](http://hgbook.red-bean.com/)
    - [More free books](https://github.com/vhf/free-programming-books/blob/master/free-programming-books.md#mercurial)
- **Books (paper):** N/A

**TODO:** Expand, add info on Subversion
# Introduction to Programming
**Curated list of resources for budding developers**

## Table of contents
[**SEE GITHUB PAGE VIEW**](http://ashleymcnamara.github.io/learn_to_code/)
- [Introduction](#introduction)
    - [Goals](#goals)
    - [Where do I start?](#where-do-i-start)
    - [How this page is organized](#how-this-page-is-organized)
    - [Which resource should I pick?](#which-resource-should-i-pick)
    - [Warning](#warning)
- [General resources](#general-resources)
    - [Links to other big lists](#links-to-other-big-lists)
    - [Online courses](#online-courses)
- [Programming Languages](#programming-languages)
    - [C](#c)
    - [C++](#c-1)
    - [C#](#c-sharp)
    - [Haskell](#haskell)
    - [HTML, CSS, and JavaScript](#html-css-and-javascript)
    - [Lisp (Scheme, Common Lisp, Clojure, etc)](#lisp-scheme-common-lisp-clojure-etc)
    - [Java](#java)
    - [Perl](#perl)
    - [PHP](#php)
    - [Python](#python)
    - [Golang](#golang)
    - [Ruby](#ruby)
    - [Scratch](#scratch)
- [Data](#data)
    - [Neo4j & Graph Databases](#neo4j-and-graph-databases)
    - [MongoDB](#mongodb)
- [Other topics](#other-topics)
    - [Developing on specific platforms](#developing-on-specific-platforms)
        - [Android](#android)
        - [Mac and iOS](#mac-and-ios)
        - [Windows and Windows Phones](#windows-and-windows-phones)
    - [Data structures and algorithms](#data-structures-and-algorithms)
- [Tools](#tools)
    - [Version control](#version-control)
        - [Git](#git)
        - [Mercurial](#mercurial)

## Introduction

### Goals

 Programming and computer science are becoming more popular than ever -- major initiatives like the [Hour of Code](http://hourofcode.com/us) are popularizing learning  programming across the world.

As a consequence, there are an increasingly huge number of resources and tutorials being produced for beginners who want to learn to code, ranging from books to online tutorials to interactive websites to massive open online courses _(MOOCS)_ like [Codecademy](https://www.codecademy.com/) and [Coursera](https://www.coursera.org/).

While this is great, it can also be overwhelming for beginners -- there are almost too _many_ resources available, and it's difficult to figure out where to start.

This page is meant to help solve that problem -- to present a **curated** list of resources for people who are either new to programming, new to a particular topic, or want to advance their skills past the beginner stage. This page doesn't try and list every single resource available, but instead links to resources that are guaranteed to be high-quality.

### Where do I start?

If you know what you want to learn about, great! Jump to that section, start browsing the links, and find something which works for you.

If you're not sure where to start and which language to learn, some good beginner languages are:

- [Golang](#golang) (Go is an attempt to combine the ease of programming of an interpreted, dynamically typed language, with the efficiency and safety of a statically typed, compiled language.)
- [Python](#python) (general-purpose; scientific and mathematical computing)
- [Java](#java) (general-purpose; Android development)
- [HTML/CSS/JavaScript](#html-css-and-javascript) (websites and webapps)
- [Scratch](#scratch) (for younger children)

Python and Java are both languages that are [commonly used](http://www.codingdojo.com/blog/9-most-in-demand-programming-languages-of-2016/) to teach programming to beginners in schools and universities, and there are a wide variety of resources available to help you learn. They're also widely used in the industry which makes them useful languages to have in your toolbelt.

Web development has been very popular lately, so there are many resources for learning HTML, CSS, and JavaScript, also making it suitable for learning. It requires little to no installation and configuration on your computer. All you need is a text editor to write code -- the code will run on your web browser.

[Scratch](https://www.youtube.com/watch?v=4y6J2jXjU34) is a little different from other languages. It was designed from the ground up to be easy to use and learn -- instead of typing text, you drag and connect together "blocks" to form programs, making it a very visual language. As a result, Scratch is a good language especially for younger children _(elementary schoolers, middle school)_ or for people who dislike typing.

### How this page is organized...

This page is subdivided into three parts -- first, a _"General resources"_ section that links to sites that tend to deliver high-quality content about a variety of topics, and a _"Specific resources"_ section that provides resources on specific programming languages or topics.

In general, most resources available will fall between two categories -- online courses, and books + tutorials. Online courses tend to teach using video lectures, try and be more interactive, and try and emulate the structure of a course similar to ones you might take in college. In contrast, books and tutorials teach via written text and allow you to set your own pace.

### Where should I start?

Whether you prefer learning by watching a video or reading text is really a matter of personal preference. _I_ personally prefer visual, but your learning style might be completely different. You may need to explore and browse several different resources before you discover how you best learn.

In addition, you'll find that most links, whether they're online courses, tutorials, or books, tend to focus on either one of three things:

  1. Some resources focus on _programming_, _semantics_, or _computer science theory_ -- in other words, how to use a programming language to write something that works.
  2. Other resources will focus more on _coding_ and _syntax_ -- the particular details and rules about how a programming language works.
  3. Other resources focus on teaching _idioms_ -- teaching best practices specific to that language, the underlying philosophy of that language, or teaching you about the different libraries available to you: the broader ecosystem.

If you're new to programming, the first model will be the best. Programming is all about applied problem solving: being able to take a problem, and break it up into smaller and smaller pieces until they're small enough to translate into computer code. Simply memorizing a collection of rules will not be very useful to you. You also need to learn how to _apply_ those rules.

However, if you already know how to program, then you most likely already know how to do this. In that case, you're going to want to use the second kind since it'll be easier to learn about the differences between the language you're learning and ones you already know.

Once you've moved past the beginning phase, then it would be a good idea to try and move on to the third kind of resource, which will help teach you how to actually use and apply that language on a practical and professional level.

When I say that a resource is _"heavy in theory"_ or _"is rigorous"_, I mean that it leans towards the first category. When I say that a resource _"focuses on syntax"_, I mean that it leans towards the second. And when I say a resource _"focuses on idioms"_ or _"on practical applications"_, I mean that it leans towards the third.

### WARNING!

This page is still a **work-in-progress**! Some sections may currently be incomplete, and some links may not yet be fully vetted.

If you would like to contribute, please see **[CONTRIBUTING.md][contrib]** for details.

  [contrib]: https://github.com/ashleymcnamara/learn_to_code/blob/master/Contributing.md

## General resources

### Links to other big lists

You can find a huge and utterly massive compendium of [list of free programming books and resources on github](https://github.com/vhf/free-programming-books/blob/master/free-programming-books.md). (It used to be hosted on StackOverflow, but was moved over to Github on October 2013).

You can also find a meta _"list of programming resources"_ aggregator here: http://resrc.io/


### Online courses

Online courses are an increasingly popular way for universities and professionals to teach programming and computer science in a structured format. As a result, new online courses will pop up all the time, so it's worth checking these resources periodically to see what's new.

- **[Codecademy](http://www.codecademy.com/)** - offers free online courses in several different languages. However, Codecademy does have a tendency to teach only basic syntax, so you may need work through more tutorials after finishing Codecademy. Focuses mainly on web development, Ruby, and Python.
- **[Coursera](https://www.coursera.org/)** - offers free online courses in many different fields from several different well-known universities. New courses are added every quarter, and content from old courses is typically archived. Because many courses appear to be new/may be a one-time thing, this page will not link to courses on Coursera unless it appears to be stable.
- **[Udacity](http://www.udacity.com/)** - offers free computer science courses taught by industry experts. Udacity offers two kinds of courses -- regular courses and nanodegrees. Regular courses are free. Regular courses with one-on-one tutoring/code review requires a monthly fee. Nanodegrees are typically for people with some prior coding experience, and cost more money.
- **[edX](https://www.edx.org/)** - a joint effort between MIT, Harvard, and Berkeley to provide free online versions of some of their courses.
- **[OpenCulture](http://www.openculture.com/computer_science_free_courses)** - similar to all of the above. Video lectures are typically available on iTunes or Youtube. Typically does **not** require you to complete assignments, unlike many other online courses.
- **[MIT OpenCourseWare](http://ocw.mit.edu/index.htm)** - static course materials taught at MIT. Unless otherwise noted, most content from this website tends to be very rigorous and fast-paced.
- **[Khan Academy](https://www.khanacademy.org/)** - contains a few courses on programming and computer science; does contain many more courses on all kinds of topics (especially math).
- **[Stanford Engineering Everywhere](http://see.stanford.edu/see/courses.aspx)** - static course materials taught at Stanford.
- **[Learn Code](https://www.youtube.com/learncodeacademy/)** - offers free online courses hosted on YouTube focusing primarily on greater JavaScript ecosystem. Covers everything from basic JavaScript, front end Web Apps, NodeJS and some of the more popular frameworks. Also covers other topics such as basic Git usage, and SSH.
- **[Do What You Love (DWYL)](https://github.com/dwyl)** - over 150 tutorials in the form of Github repositories, covering languages such as JavaScript, HTML5, Elixir and Elm; platforms like AWS, Digital Ocean, and Azure; other tools like CodeShip and Github; and also covering basics on architecture, security, and test driven design  

The following websites also contain a wide variety of tutorials for many different topics, but require payment and registration before you can access their courses.

- **[Team Treehouse](http://teamtreehouse.com/)** - focuses on web and iOS development.
- **[Lynda](http://www.lynda.com/)** - also includes courses on design, animation, video, business, and more.
- **[PluralSight](http://www.pluralsight.com/)** - similar to Lynda, but with a focus on developer and IT courses.
-  **[General Assembly](https://generalassemb.ly/)** - also includes courses on design, animation, video, business, and more.

In general, edX, OpenCulture, MIT OpenCourseware, and Stanford Engineering Everywhere tend to contain more rigorous, thorough, and demanding courses, whereas Codecademy and Khan Academy tend to focus on giving a more gentle introduction to programming. Coursera and Udacity tend to vary between these two extremes.


## Programming Languages

### C

Note: C can be a difficult-to-teach language. Although the online courses and books are a good starting point and can take you a long way, the general consensus is that the best way to learn is through reading an actual book.

- **Online courses:**
    - MIT Open Courseware has a few:
        - [Practical Programming in C][c-mit-practical]
          For beginners.
        - [Introduction to C Memory Management and C++ Object-Oriented Programming][c-mit-intro]
          Geared towards people with prior experience in a programming language that is not C or C++.
        - [Effective Programming in C and C++][c-mit-effective]
          Similar to the above.
- **Video tutorials:** N/A
- **Interactive tutorials:**
    - [Learn-C][c-learn-c]
      An interactive online guide that teaches you basic C step-by-step.
- **Books and tutorials (online):**
   -  [Learn C The Hard Way][c-lcthw]
      Part of the "Learn X the Hard Way" series. Assumes you have prior programming experience. Currently incomplete, in progress.
   -  [C Programming][c-c-programming]
      One of Wikibooks' featured books. Tends to focus on teaching mainly syntax. A good starting point and reference.
   -  [Build Your Own Lisp][c-lisp]
      Walks you through how to write a Lisp interpreter in C, teaching both languages simultaneously.
    - [More free books][c-more]
- **Books (paper):**
    - [The C Programming Language][c-c-lang]
      The definitive guide to C. Also known as K&R, after the authors.
    - [The Definitive C Book Guide and List][c-so-definitive]
A very well-maintained list of recommended books and resources on StackOverflow. Every book listed on this page is highly-recommended.
- **Exercises:** N/A

  [c-mit-practical]: http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-087-practical-programming-in-c-january-iap-2010/
  [c-mit-intro]: http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-088-introduction-to-c-memory-management-and-c-object-oriented-programming-january-iap-2010/
  [c-mit-effective]: http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-s096-effective-programming-in-c-and-c-january-iap-2014/

  [c-learn-c]: http://learn-c.org
  [c-lcthw]: http://c.learncodethehardway.org/book/
  [c-lisp]: http://www.buildyourownlisp.com/
  [c-c-programming]: http://en.wikibooks.org/wiki/C_Programming
  [c-more]: https://github.com/vhf/free-programming-books/blob/master/free-programming-books.md#c

  [c-c-lang]: http://www.amazon.com/C-Programming-Language-2nd-Edition/dp/0131103628/
  [c-so-definitive]: http://stackoverflow.com/questions/562303/the-definitive-c-book-guide-and-list

### C++

Note: Similar to C, C++ can be a difficult-to-teach language. Although the online courses and books are a good starting point and can take you a long way, the general consensus is that the best way to learn is through reading an actual book.

- **Online courses:**
    - MIT Open Courseware has a few:
        - [Introduction to C++][cpp-mit-intro]
          For beginners, is fast-paced.
        - [Introduction to C Memory Management and C++ Object-Oriented Programming][cpp-mit-intro-2]
          Geared towards people with prior experience in a programming language that is not C or C++.
        - [Effective Programming in C and C++][cpp-mit-effective]
        Similar to the above.
    - **Stanford's 3-part "Introduction to Computer Science" series for beginners.** The first course teaches Java, the latter two teaches C and C++.
        - [Programming Methodology][cpp-stan-methodology]
        - [Programming Abstractions][cpp-stan-abstractions]
        - [Programming Paradigms][cpp-stan-paradigms]
    - Coursera's [C++ for C Programmers][cpp-coursera-c-for-cpp]
      May also be helpful for programmers with prior experience in another language besides C or C++.
- **Interactive tutorials:**
    - [C++ Interactive Exercises][cpp-interactive]
      An introduction to basic C++. Is a cross between an interactive tutorial and an online book.
- **Video tutorials:** N/A
- **Books and tutorials (online):**
    - [How to Think Like a Computer Scientist][cpp-think-cs]
      A good introduction to basic C++.
    - [Learncpp.com][cpp-learn]
      Tends to focus more on syntax, and less on programming. Might be useful for beginners, but as a reference, not a tutorial.
    - [Linear C++][cpp-linear]
      A tutorial on C++ for people with some prior programming experience. Teaches by presenting and explaining a series of programs.
   - [More free books][cpp-more]
- **Books (paper):**
   - [The Definitive C++ Book Guide and List][cpp-so-definitive]
     A very well-maintained list of recommended books and resources on StackOverflow. Every book listed on this page is highly-recommended.
- **Exercises:** N/A

  [cpp-google-class]: https://developers.google.com/edu/c++/
  [cpp-coursera-c-for-cpp]: https://www.coursera.org/course/cplusplus4c
  [cpp-mit-intro]: http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-096-introduction-to-c-january-iap-2011/
  [cpp-mit-intro-2]: http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-088-introduction-to-c-memory-management-and-c-object-oriented-programming-january-iap-2010/
  [cpp-mit-effective]: http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-s096-effective-programming-in-c-and-c-january-iap-2014/
  [cpp-stan-methodology]: http://see.stanford.edu/see/courseinfo.aspx?coll=824a47e1-135f-4508-a5aa-866adcae1111
  [cpp-stan-abstractions]: http://see.stanford.edu/see/courseinfo.aspx?coll=11f4f422-5670-4b4c-889c-008262e09e4e
  [cpp-stan-paradigms]: http://see.stanford.edu/see/courseinfo.aspx?coll=2d712634-2bf1-4b55-9a3a-ca9d470755ee

  [cpp-interactive]: http://nova.umuc.edu/~jarc/sdsd/

  [cpp-think-cs]: http://greenteapress.com/thinkcpp/index.html
  [cpp-learn]: http://www.learncpp.com/
  [cpp-linear]: https://github.com/jesyspa/linear-cpp
  [cpp-more]: https://github.com/vhf/free-programming-books/blob/master/free-programming-books.md#c-1

  [cpp-so-definitive]: http://stackoverflow.com/questions/388242/the-definitive-c-book-guide-and-list

### C-Sharp
 (pronounced as see sharp) is a multi-paradigm programming language encompassing strong typing, imperative, declarative, functional, generic, object-oriented (class-based), and component-oriented programming disciplines.

- **Online courses:**
    - Microsoft Virtual Academy has a few free courses:
      - [C# Fundamentals for Absolute Beginners][csharp-fundamentals]
        A series of videos produced by Microsoft on learning C#. For beginners.
      - [Programming in C# Jump Start][csharp-jump-start]
        Another series of videos produced by Microsoft. Assumes some prior knowledge of C#.
- **Interactive tutorials:** N/A
- **Video tutorials:** N/A
- **Books and tutorials (online):**
    - [C# Programming][csharp-programming]
      One of Wikibook's featured books. For beginners. Tends to focus on syntax, and would also make a good reference.
    - [The C# Yellow Book][csharp-yellow]
      The introductory text used by the University of Hull.
    - [C# Essentials][csharp-essentials]
      An introductory text on C#. Also includes information on Windows Forms, Visual Studios, and making GUIs.
    - [Visual C# resources][csharp-visual]
      Microsoft's official series of tutorials and guides on C# and .NET.
    - [More free books][csharp-more]
- **Books (paper):**
    - [Sam's Teach Yourself C# 5.0 in 24 Hours]() by Scott Dorman
      A good introduction for beginners.
    - [Essential C# 5.0][csharp-essential-book]
      Very comprehensive, and intended more for intermediate programmers/programmings coming from another language.
    - [C# in Depth, 3rd Edition][csharp-in-depth]
      Also very comprehensive, and covers how to write idiomatic and clean C# code. Assumes the reader already knows some C#.
    - [Effective C#][csharp-effective] and [More Effective C#][csharp-more-effective]
      A collection of tips and tricks to improve your C# code. Not for beginners.
- **Exercises:** N/A

  [csharp-fundamentals]: http://channel9.msdn.com/Series/C-Fundamentals-for-Absolute-Beginners
  [csharp-jump-start]: http://www.microsoftvirtualacademy.com/training-courses/developer-training-with-programming-in-c

  [csharp-programming]: http://en.wikibooks.org/wiki/C_Sharp_Programming
  [csharp-yellow]: http://www.csharpcourse.com/
  [csharp-essentials]: http://www.techotopia.com/index.php/C_Sharp_Essentials
  [csharp-visual]: http://msdn.microsoft.com/en-us/vstudio/hh341490
  [csharp-more]: https://github.com/vhf/free-programming-books/blob/master/free-programming-books.md#c-sharp

  [csharp-sam]: http://www.amazon.com/Sams-Teach-Yourself-5-0-Hours/dp/0672336847
  [csharp-essential-book]: http://www.amazon.com/Essential-Edition-Microsoft-Windows-Development/dp/0321877586
  [csharp-in-depth]: http://www.amazon.com/gp/product/161729134X
  [csharp-effective]: http://www.amazon.com/Effective-Specific-Ways-Improve-Your/dp/0321245660
  [csharp-more-effective]: http://www.amazon.com/More-Effective-Specific-Ways-Improve/dp/0321485890

### Haskell
Haskell is a [polymorphically](https://wiki.haskell.org/Polymorphism) [statically typed](https://wiki.haskell.org/Typing), [lazy, purely functional](https://wiki.haskell.org/Lazy_evaluation) language, quite different from most other programming languages. The language is named for [Haskell Brooks Curry](https://wiki.haskell.org/Haskell_Brooks_Curry), whose work in mathematical logic serves as a foundation for functional languages. Haskell is based on the [lambda calculus](https://wiki.haskell.org/Lambda_calculus), hence the lambda they use as a logo.
- **Online courses:**
    - edX's [Introduction to Functional Programming][haskell-intro-func]
      Assumes familiarity with a non-functional programming language (Java, Python, C#, C++, etc). Take a look at [course content][haskell-course-content].
- **Interactive tutorials:**
    - [Try Haskell][haskell-try]
      An interactive guide that teaches basic Haskell.
- **Video tutorials:**
    - [Parallel and Concurrent Haskell][haskell-by-bartosz]
      A series of lectures which cover both basics and advanced concepts.
- **Books and tutorials (online):**
    - [Getting started with Haskell][haskell-getting-started]
      A comprehensive meta-guide that suggests the recommended order for following Haskell tutorials from beginning to advanced.
    - [Learn You a Haskell for Great Good][haskell-great-good]
      A beginner's introduction to Haskell. Tends to focus on syntax.
    - [Haskell][haskell-wikibooks]
      One of Wikibook's featured books. Covers basic to advanced Haskell. Very comprehensive.
    - [Real World Haskell][haskell-real-world]:
      Covers how to use Haskell for practical applications. This is a good second book to read, after completing one of the above tutorials.
    - [More free books][haskell-more]
- **Books (paper):** N/A
- **Exercises:**
    - [H-99][haskell-h-99]
      A collection of 99 problems designed to increase your proficiency in Haskell.

  [haskell-intro-func]: https://www.edx.org/course/introduction-functional-programming-delftx-fp101x-0
  [haskell-course-content]: https://github.com/fptudelft/FP101x-Content-2015

  [haskell-try]: http://tryhaskell.org/
  [haskell-by-bartosz]: https://www.youtube.com/playlist?list=PLbgaMIhjbmEm_51-HWv9BQUXcmHYtl4sw

  [haskell-getting-started]: http://stackoverflow.com/a/1016986/646543
  [haskell-great-good]: http://learnyouahaskell.com/
  [haskell-wikibooks]: http://en.wikibooks.org/wiki/Haskell
  [haskell-real-world]: http://book.realworldhaskell.org/
  [haskell-more]: https://github.com/vhf/free-programming-books/blob/master/free-programming-books.md#haskell

  [haskell-h-99]: http://haskell.org/haskellwiki/H-99:_Ninety-Nine_Haskell_Problems

### HTML, CSS, and JavaScript

Note: HTML, CSS, and JavaScript are the three core technologies that runs on every web browser and makes up every webpage.

HTML is a language used to describe the _structure_ and _content_ of a webpage. CSS is used to describe the _style_ and _appearance_. JavaScript is used to add _behavior_ and _interactivity_.

The recommended learning order is typically to start with HTML and CSS, then move on to learning JavaScript once you feel you've acquired a basic understanding of the previous two.

Also note that HTML and CSS are examples of "markup languages", not "programming languages" and so will feel fairly different from JavaScript. If your goal is to learn just programming, you might want to jump straight ahead to JavaScript (or pick a different programming language!). However, since the main way to actually use JavaScript is through the web browser, you _do_ need to learn HTML and CSS at one point or another.

- **Online courses:**
    - Dash teaches HTML, CSS, and Javascript through fun projects you can do in your browser.
      - [Make a website][general-assembly-make-website]
    - Codecademy has several courses related to web development.
        - [Make a website][webdev-cc-make-website]
        - [Make an interactive website][webdev-cc-make-interactive]
        - [HTML & CSS][webdev-cc-html-css]
        - [JavaScript][webdev-cc-js]
        - [jQuery][webdev-cc-jquery]
    - So does Udacity:
        - [Intro to HTML and CSS][webdev-uda-html-css]
        - [JavaScript Basics][webdev-uda-js]
          Does require some prior programming experience.
    - Open Culture's [Building Dynamic Websites][webdev-open-dynamic]
      Hosted by Harvard, and covers a wide variety of topics.
    - Khan Academy has a series of [three courses][webdev-khan] on introductory Javascript that focuses on drawing graphics and animations, and making games.
    - Team Treehouse has a series of courses on [HTML][webdev-treehouse-js], [CSS][webdev-treehouse-css], and [Javascript][webdev-treehouse-js]
      Allows a free 14-day trial, but later requires payment.
- **Interactive tutorials:**
    - [CSS3, please!][webdev-please]
      An interactive website that lets you dynamically change CSS rules to style an element on-screen. Not for beginners, but is a good way to discover advanced applications of CSS.
- **Video tutorials:** N/A
- **Books and tutorials (online):**
    - [Mozilla Developer Network][webdev-mdn] (MDN)
      A series of tutorials covering HTML, CSS, JavaScript, and more. Some tutorials are appropriate for beginners while other tutorials will be more advanced.
    - [HtmlDog][webdev-htmldog]
      Similar to the above, but targeted more specifically to beginners.
    - [Eloquent JavaScript][webdev-eloquent]
      A book that teaches you how to write idiomatic and clean JavaScript. Assumes prior experience with JavaScript/another programming language.
    - [A Re-introduction to JavaScript][webdev-js-reintroduction]
      A guide which gives a thorough and detailed overview of JavaScript.
    - [JavaScript Frameworks Resources and Tutorials][webdev-js-frameworks]
      Currently features Angular.js, Backbone.js, D3.js, Dojo, Ember.js, Express.js, jQuery, Knockout.js, and Meteor.
    - [JavaScript30][webdev-js-30vanilla]
      30 Day Vanilla JS Coding Challenge. Build 30 things in 30 days with 30 tutorials
    - [JavaScript Tutorial][webdev-js-onevideo]
      Learn JavaScript in one 90 minute Video.
    - More free books:
        - [HTML and CSS][webdev-more-html-css]
        - [JavaScript][webdev-more-js]
- **Books (paper):**
    - [JavaScript: The Good Parts][webdev-the-good-parts]
      A short book that covers the core aspects of JavaScript as well as info on writing idiomatic and clean JavaScript.
    - [JavaScript: The Good Parts Notes][webdev-the-good-parts-notes]
      Notes on the Douglas Crockford's book. Great if you don't have time to get into the detail of the book.
- **Exercises:**
    - [CSS Diner][webdev-css-diner]
      A series of exercises on using CSS selectors effectively.

  [webdev-js-30vanilla]: https://javascript30.com/
  [webdev-js-onevideo]: https://www.youtube.com/watch?v=fju9ii8YsGs
  [webdev-cc-make-website]: http://www.codecademy.com/skills/make-a-website
  [webdev-cc-make-interactive]: http://www.codecademy.com/skills/make-an-interactive-website
  [webdev-cc-html-css]: http://www.codecademy.com/tracks/web
  [webdev-cc-js]: http://www.codecademy.com/tracks/javascript
  [webdev-cc-jquery]: http://www.codecademy.com/tracks/jquery
  [webdev-uda-html-css]: https://www.udacity.com/course/ud304
  [webdev-uda-js]: https://www.udacity.com/course/ud804
  [webdev-open-dynamic]: http://cs75.tv/2010/fall/
  [webdev-khan]: https://www.khanacademy.org/computing/computer-programming
  [webdev-treehouse-html]: http://teamtreehouse.com/features/html
  [webdev-treehouse-css]: http://teamtreehouse.com/features/css
  [webdev-treehouse-js]: http://teamtreehouse.com/features/javascript

  [webdev-please]: http://css3please.com/

  [webdev-mdn]: https://developer.mozilla.org/en-US/docs/Web
  [webdev-htmldog]: http://www.htmldog.com/
  [webdev-eloquent]: http://eloquentjavascript.net/
  [webdev-js-reintroduction]: https://developer.mozilla.org/en-US/docs/Web/JavaScript/A_re-introduction_to_JavaScript
  [webdev-js-frameworks]: http://resrc.io/list/18/javascript-frameworks/
  [webdev-more-html-css]: https://github.com/vhf/free-programming-books/blob/master/free-programming-books.md#html--css
  [webdev-more-js]: https://github.com/vhf/free-programming-books/blob/master/free-programming-books.md#javascript

  [webdev-the-good-parts]: http://www.amazon.com/gp/product/0596517742
  [webdev-the-good-parts-notes]: https://github.com/iteles/Javascript-the-Good-Parts-notes

  [webdev-css-diner]: http://flukeout.github.io/
  [general-assembly-make-website]: https://dash.generalassemb.ly/

### Lisp (Scheme, Common Lisp, Clojure, etc)

- **Online courses:**
  - [Learn Lisp the Hard Way][lisp-course] Brought to you by the Toronto Lisp User Group
- I**nteractive tutorials:**
    - [Try Clojure][lisp-try-clojure]
      An interactive tutorial for basic Clojure.
- **Video tutorials:**
  - [Overview and Introduction to Lisp][mit-course] videos from MIT open courseware
- **Books and tutorials (online):**
    - [The Nature of Lisp][lisp-nature]
      Not really a tutorial on Lisp, but is instead an article on why so many people advocate Lisp and claim it will fundamentally change how you view code. Very good at explaining the philosophy of Lisp.
    - [Structure and Interpretation of Computer Programs][lisp-sicp]
      SICP is the canonical introduction to Lisp, and used to be part of MIT's introduction to CS course (before they switched to Python).
        - [SICP in Clojure][lisp-sicp-clojure]
          An amended version of SICP which uses Clojure instead of Scheme.
    - [How to Design Programs][lisp-htdp]
      A competing book and philosophy of teaching to SICP. SICP tends to focus more on CS theory whereas HTDP tends to focus more on writing how to go about writing programs/analyzing problems.
    - [Build Your Own Lisp][lisp-build]
      Walks you through how to write a Lisp interpreter in C, teaching both languages simultaneously.
    - [Practical Common Lisp][lisp-learn-practical]
      An introductory book on Common Lisp. Covers practical and real-world applications of Common Lisp.
    - [Where to learn how to practically use Common Lisp][lisp-learn-practical]
      An aggregation of books and resources on effectively using Common Lisp for programmers coming from an imperative world.
    - [Learn Clojure][lisp-learn-clojure]
      A website collecting many links related to learning Lisp.
    - More free books:
        - [Clojure][lisp-more-clojure]
        - [Lisp][lisp-more-lisp] in general
        - [Scheme][lisp-more-scheme]
- **Books (paper):**
    - [Land of Lisp][lisp-land]
      A book that teaches Lisp (specifically Common Lisp) via making games. For beginners.
- **Exercises:**
    - [L-99][lisp-l99]
      A series of 99 problems designed to increase your proficiency in Lisp.
    - [4Clojure][lisp-4clojure]
      A series of exercises geared around learning Clojure.

  [lisp-try-clojure]: http://www.tryclj.com/

  [lisp-nature]: http://www.defmacro.org/ramblings/lisp.html
  [lisp-sicp]: http://mitpress.mit.edu/sicp/
  [lisp-sicp-clojure]: http://sicpinclojure.com/
  [lisp-htdp]: http://htdp.org/
  [lisp-build]: http://www.buildyourownlisp.com/
  [lisp-practical]: http://www.gigamonkeys.com/book/
  [lisp-learn-practical]: http://stackoverflow.com/q/7224823/646543
  [lisp-learn-clojure]: http://learn-clojure.com/
  [lisp-more-clojure]: https://github.com/vhf/free-programming-books/blob/master/free-programming-books.md#clojure
  [lisp-more-lisp]: https://github.com/vhf/free-programming-books/blob/master/free-programming-books.md#lisp
  [lisp-more-scheme]: https://github.com/vhf/free-programming-books/blob/master/free-programming-books.md#scheme

  [lisp-land]: http://www.amazon.com/Land-Lisp-Learn-Program-Game/dp/1593272812

  [lisp-l99]: http://www.ic.unicamp.br/~meidanis/courses/mc336/2006s2/funcional/L-99_Ninety-Nine_Lisp_Problems.html
  [lisp-4clojure]: http://4clojure.com
  [mit-course]: http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-001-structure-and-interpretation-of-computer-programs-spring-2005/video-lectures/1a-overview-and-introduction-to-lisp/
  [lisp-course]: http://learnlispthehardway.org/

### Java
Java is a programming language designed to build secure, powerful applications that run across multiple operating systems, including Linux, Mac OS X, and Windows. The Java language is known to be flexible, scalable, and maintainable.

- **Online courses:**
    - Udacity's [Intro to Java Programming][java-uda-intro]
      An objects-first introduction to Java.
    - MIT Open Courseware:
        - [Introduction to Programming in Java][java-mit-intro-to-prog]
        - [Introduction to Computers and Engineering Problem Solving][java-mit-intro-to-computers]
          For beginners, emphasizes practical application of Java.
    - Stanford's 3-part "Introduction to Computer Science" series for beginners. The first course teaches Java, the latter two teaches C and C++.
        - [Programming Methodology][java-methodology]
        - [Programming Abstractions][java-abstractions]
        - [Programming Paradigms][java-paradigms]
    - The University of Helsinki's "Object-Oriented programming with Java" series for beginners.
        - [Part 1][java-helsinki-1]
        - [Part 2][java-helsinki-2]
- **Interactive tutorials:**
    - [Learn Java][java-learn-online]
      An interactive tutorial that teaches basic Java.
- **Video tutorials:** N/A
- **Books and tutorials (online):**
    - [Introduction to Computer Science using Java][java-intro-cs]
      An introductory text on Java. Moves a bit slowly, but covers everything in great detail (including setup).
    - [Learn by Doing][java-doing]
      An introductory text on Java. The tutorial is exercise-driven.
    - [Think Java][java-think]
      Another introductory text on Java. The content is based on the "How to think like a Computer Scientist" series.
    - [Thinking in Java, 3rd edition][java-thinking]
      Note: the fourth edition is the latest one, but currently is not free. The website can also be a little hard to navigate -- the direct download link is [here][java-thinking-direct]. Assumes some basic prior programming experience.
    - [TutorialsPoint's Java Tutorial][java-tutorialspoint]
      An introduction to Java. Tends to focus mainly on syntax. May also make a good reference.
    - [The Java Tutorial][java-oracle]
      The official Java tutorial, produced by Oracle. Tends to focus on language features and syntax.
    - [More free books][java-more]
- **Books (paper):**
    - [Head First Java][java-head]
      A beginner's introduction to Java.
- **Exercises:**
    - [Practice-it][java-practice-it]
      A series of exercises hosted by the University of Washington, starting with basic Java and finishing with data structures and algorithms. Requires (free) registration first before you can view or work on the exercises.

  [java-uda-intro]: https://www.udacity.com/course/cs046
  [java-mit-intro-to-prog]: http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-092-introduction-to-programming-in-java-january-iap-2010/index.htm
  [java-mit-intro-to-computers]: http://ocw.mit.edu/courses/civil-and-environmental-engineering/1-00-introduction-to-computers-and-engineering-problem-solving-spring-2012/
  [java-methodology]: http://see.stanford.edu/see/courseinfo.aspx?coll=824a47e1-135f-4508-a5aa-866adcae1111
  [java-abstractions]: http://see.stanford.edu/see/courseinfo.aspx?coll=11f4f422-5670-4b4c-889c-008262e09e4e
  [java-paradigms]: http://see.stanford.edu/see/courseinfo.aspx?coll=2d712634-2bf1-4b55-9a3a-ca9d470755ee
  [java-helsinki-1]: http://mooc.fi/courses/2013/programming-part-1/
  [java-helsinki-2]: http://mooc.fi/courses/2013/programming-part-2/

  [java-learn-online]: http://www.learnjavaonline.org/

  [java-doing]: http://programmingbydoing.com/
  [java-think]: http://greenteapress.com/thinkapjava/
  [java-thinking]: http://www.mindview.net/Books/TIJ/
  [java-thinking-direct]: http://www.mindviewinc.com/downloads/TIJ-3rd-edition4.0.zip
  [java-tutorialspoint]: http://www.tutorialspoint.com/java/index.htm
  [java-intro-cs]: http://chortle.ccsu.edu/java5/index.html
  [java-oracle]: http://docs.oracle.com/javase/tutorial/
  [java-more]: https://github.com/vhf/free-programming-books/blob/master/free-programming-books.md#java

  [java-head]: http://www.amazon.com/Head-First-Java-2nd-Edition/dp/0596009208/

  [java-practice-it]: http://practiceit.cs.washington.edu/

### Perl
Businesses talk about Perl 5 when talking Perl, but on a far-far land, beyond deep-thinking island, the design-by-committee tribe is still cooking a hefty slab of Perl 6 (and it's almost ready, with an engine written in Haskell and powered by the tears of the gods)

**Ok, that said, what is Perl 5 used for, today?**

- **legacy web systems / intrawebs** - some just won't die

- **data mining / statistical analysis** - the perl regex engine, even if slightly outdated, (PCRE, a spinned off library, tops it up in any possibile way and it's the default PHP engine) is still good for simple analysis

- **UNIX system administration **- Perl shall always be installed on UNIX.
You can count on it being readily available even on Mac OS X.

- **Network Prototyping **- many core network experts learned Perl when it was all the rage; and they still do their proofs-of-concept with it.

- **Security** - many security experts, too, need fast prototyping. (and fast automated fixes) Perl can, and does, cover for that.

The extensive CPAN collection is very handy, when dealing with prototypes.
(Batteries may not be included, but they're still right there, on the shelf)

**Remember drawbacks, though:**

- Object support in Perl sucks hard, you bless references and do unholy stuff in the name of objects, then wonder why you took all the trouble in the first place.
- Reading other people's Perl is more than a craft, it's science, and a painful one, too.
- Perl is nifty, it makes you think nifty, it makes you feel nifty, you become a programming rockstar. Now, think about getting up, and going to work in a office full of rockstars: it's a "boat that rocks" hard. Expect wild fluctuations.

- **Online courses:** N/A
- **Interactive tutorials:** N/A
- **Video tutorials:** N/A
- **Books and tutorials (online):**
    - [Beginning Perl][perl-beginning]
      A comprehensive and thorough introduction to Perl.
    - [Modern Perl][perl-modern]
      A guide on writing clean and idiomatic Perl code. Very good for teaching the philosophy and fundamentals of Perl. Comprehensive and thorough.
    - [Impatient Perl][perl-impatient]
      An accelerated guide for impatient people or people with prior programming experience.
    - [Learn Perl in about 2 hours 30 minutes][perl-230]
      Another accelerated guide for the impatient. Geared towards people who have prior experience in another programming language.
    - [More free books][perl-more]
    - Perl.org also hosts a [list of recommended books][perl-books], many of which are available online for free.
- **Books (paper):**
    - [Learning Perl][perl-learning]
      An introductory text on Perl. Teaches on focusing syntax/the details of Perl, and not so much on how to program. Pragmatic and practical.
- **Exercises:**
    - [Perl Quiz of the Week][perl-qotw]
      A mailing list which sends out a new quiz/prompt once a week. Archives of past prompts are also available.

  [perl-beginning]: http://www.perl.org/books/beginning-perl/
  [perl-modern]: http://modernperlbooks.com/books/modern_perl_2014/
  [perl-impatient]: http://www.perl.org/books/impatient-perl/
  [perl-230]: http://qntm.org/perl
  [perl-more]: https://github.com/vhf/free-programming-books/blob/master/free-programming-books.md#perl
  [perl-books]: http://www.perl.org/books/library.html

  [perl-learning]: http://www.amazon.com/Learning-Perl-Randal-L-Schwartz/dp/1449303587

  [perl-qotw]: http://perl.plover.com/qotw/

### PHP

Note: while PHP can be very convenient, quick, and easy to use, it's also a language viewed negatively by many programmers. (See [PHP: a fractal of bad design][php-fractal]). If you do decide to learn PHP and adopt it as your language of choice, just be aware of the fact that people will probably make fun of you at one point or another.

Also, it's important to first learn [HTML and CSS](#html-css-and-javascript) before attempting to learn PHP. PHP is a language which attempts to "extend" and work with HTML, so may not fully make sense if you try and learn it before picking up basic web development.

- **Online courses:**
    - Codecademy's [PHP track](http://www.codecademy.com/en/tracks/php)
    - Team Treehouse's [PHP course](http://teamtreehouse.com/features/php) - allows a free 14-day trial, but later requires payment.
- **Interactive resources:**
    - [Learn PHP][php-learn]
      An interactive guide that teaches basic PHP.
- **Exercises:**
- **Video tutorials:** N/A
- **Books and tutorials (online):**
    - [PHP Manual][php-manual]
      The official tutorial on PHP. Tends to focus on language features and syntax.
    - [TutorialPoint's PHP Tutorial][php-tutorialspoint]
      An introduction to PHP. Tends to focus on syntax. May make a good reference.
    - [PHP The Right Way][php-right-way]
      A comprehensive guide that covers modern best practices in PHP and attempts to address common flaws, misconceptions, and errors that many beginners (and many tutorials) seem to possess. Assumes some prior knowledge of PHP.
- **Books (paper):**
    - [PHP for Absolute Beginners][php-absolute]
      An introductory text on PHP.
    - [PHP Solutions: Dynamic Web Design Made Easy, 2nd edition][php-solutions]
      An example-driven introduction to PHP.

  [php-learn]: http://www.learn-php.org/

  [php-fractal]: http://eev.ee/blog/2012/04/09/php-a-fractal-of-bad-design/

  [php-manual]: http://php.net/manual/en/index.php
  [php-tutorialspoint]: http://www.tutorialspoint.com/php/
  [php-right-way]: http://www.phptherightway.com/

  [php-absolute]: http://www.amazon.com/PHP-Absolute-Beginners-Jason-Lengstorf/dp/1430268158/ref=dp_ob_title_bk
  [php-solutions]: http://www.amazon.com/PHP-Solutions-Dynamic-Design-Made/dp/1430232498/ref=dp_ob_title_bk


### Python

Note: there are currently two versions of Python that are commonly taught and used -- Python 2, and Python 3. Python 3 is the most recent version, but for a variety of reasons Python 2 still is fairly popular among many developers.

If you're not sure which version to pick, my recommendation would be to pick the resource which looks like the best fit for you, and just use whatever version they're recommending. Luckily, the differences between the two are very minor (at least from the perspective of the beginner), so there's really no difference if you learn using Python 2 vs Python 3.

- **Online courses:**
    - edx's [Introduction to Computer Science and Programming Using Python][python-mit-intro]
      The companion book can be [found here][python-mit-intro-book]. The course is designed for beginners, part of a 2-part series, is self-paced, and has an emphasis on computation and data science.
        -   MIT Open Courseware also offers a gentler "lead-in" course designed for those with no programming background that you can take before taking the above: [Building Programming Experience: A Lead-In to 6.001][python-mit-lead-in].
    - MIT Open Courseware's [A Gentle Introduction to Programming Using Python][python-mit-gentle]
      A gentler version of the above.
    - Coursera's [Programming for Everybody (Python)][python-coursera]
      For beginners; requires registration.
    - Codecademy's [Python track][python-codecademy]
      For beginners; tends to focus primarily on syntax.
    - Udacity's [Programming Foundations with Python][python-udacity]
      Requires some prior programming experience; focuses on object-oriented programming.
    - Team Treehouse's [Python course][python-treehouse]
      Allows a free 14-day trial, but later requires payment.
- **Interactive resources:**
    - [LearnPython][python-learn]
      An interactive online guide that teaches basic Python.
    - [Try Python][python-try]
      Another interactive online guide.
- **Video tutorials:** N/A
- **Books and tutorials (online):**
    - [Learn Python the Hard Way][python-lpthw]
      Part of the "Learn X the Hard Way" series. Despite its name, this is one of the easiest introductions to Python available.
    - [Automate the Boring Stuff with Python][python-automate]
      A book for complete beginners. It is aimed at office workers, students, administrators, and hobbyists who want to learn how to write useful, practical programs rather than necessarily become software engineers. From the [Invent with Python][python-invent] author.
    - How to Think Like a Computer Scientist ([Python 2 version][python-think-cs-2] and [Python 3 version][python-think-cs-3])
      A comprehensive introductory text on Python.
    - [Think Python][python-think]
      Another comprehensive introductory text on Python.
    - The official Python tutorial (for [Python 2][python-official-2] and [Python 3][python-official-3]). Moves a little quickly, but is very comprehensive and thorough.
    - [Problem Solving with Algorithms and Data Structures][python-problem]
      A fantastic introduction to data structures and algorithms and other traditional
      computer science concepts using Python. While it does briefly cover Python syntax,
      it assumes that you already have some basic prior experience.
    - [Dive into Python 3][python-dive]
      An accelerated introduction to Python. Warning: do NOT use "Dive into Python 2". It's very outdated.
    - [Program Arcade Games With Python And Pygame][python-arcade]
      A fantastic and thorough introduction to Python via making games. For beginners.
    - [Invent with Python][python-invent]
      Teaches programming through the creation of computer games with Python and Pygame. For beginners.
    - [The Hitchhiker's Guide to Python][python-hitchhiker]
      A comprehensive introduction to the Python ecosystem. Covers how to properly configure and set up a development environment in Python, best practices, writing idiomatic code, what the best 3rd party libraries are for different tasks, and shipping your code. Useful for both beginners and experts (however, the guide does not actually teach Python itself).
    - [pycrumbs][python-pycrumbs]
      A huge list of many useful articles, tutorials, and snippits on Python, ranging from basic to advanced.
    - [More free books][python-more]
    - [PyMOTW][pymotw]
      A tour of the Python standard library through short examples.
- **Books (paper):**
    - [Import Python][python-import]
      A catalog of Python books (some are free)
- **Exercises:**
    - [Pyschools][python-pyschools]
      Exercises and challenges in Python. Challenges require (free) registration.

  [python-codecademy]: http://www.codecademy.com/tracks/python
  [python-udacity]: https://www.udacity.com/course/ud036
  [python-coursera]: https://www.coursera.org/course/pythonlearn
  [python-mit-intro]: https://www.edx.org/course/introduction-computer-science-mitx-6-00-1x-0#.VJw5pv-kAA
  [python-mit-intro-book]:http://mitpress.mit.edu/books/introduction-computation-and-programming-using-python-0
  [python-mit-lead-in]: http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-090-building-programming-experience-a-lead-in-to-6-001-january-iap-2005/
  [python-mit-gentle]: http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-189-a-gentle-introduction-to-programming-using-python-january-iap-2011/
  [python-treehouse]: http://teamtreehouse.com/features/python

  [python-learn]: http://learnpython.org
  [python-try]: http://www.trypython.org/

  [python-automate]: http://automatetheboringstuff.com/
  [python-lpthw]: http://learnpythonthehardway.org/book/
  [python-think-cs-2]: http://www.openbookproject.net/thinkcs/python/english2e/
  [python-think-cs-3]: http://www.openbookproject.net/thinkcs/python/english3e/
  [python-think]: http://www.greenteapress.com/thinkpython/
  [python-official-2]: https://docs.python.org/2/tutorial/
  [python-official-3]: https://docs.python.org/3/tutorial/
  [python-problem]: http://interactivepython.org/runestone/static/pythonds/index.html
  [python-dive]: http://www.diveintopython3.net/
  [python-invent]: http://inventwithpython.com/
  [python-arcade]: http://ProgramArcadeGames.com
  [python-hitchhiker]: https://python-guide.readthedocs.org/en/latest/
  [python-pycrumbs]: http://resrc.io/list/4/pycrumbs/
  [python-more]: https://github.com/vhf/free-programming-books/blob/master/free-programming-books.md#python

  [python-import]: http://importpython.com/books/

  [python-pyschools]: http://www.pyschools.com/
  [pymotw]: http://pymotw.com/

### Golang
The Go programming language is an open source project to make programmers more productive.

Go is expressive, concise, clean, and efficient. Its concurrency mechanisms make it easy to write programs that get the most out of multicore and networked machines, while its novel type system enables flexible and modular program construction. Go compiles quickly to machine code yet has the convenience of garbage collection and the power of run-time reflection. It's a fast, statically typed, compiled language that feels like a dynamically typed, interpreted language.

In addition to the resources available [at golang.org](http://golang.org/doc/#learning) there are a range of community-driven initiatives:

- **Books (online):**
  - [The Little Go Book](http://openmymind.net/The-Little-Go-Book/) The Little Go Book is a free introduction to Google's Go programming language. It's aimed at developers who might not be quite comfortable with the idea of pointers and static typing. It's longer than the other Little books, but hopefully still captures that little feeling.
- **Books (paper):**
  - [Go in Action](http://www.amazon.com/Go-Action-William-Kennedy/dp/1617291781/ref=sr_1_2?ie=UTF8&qid=1460415974&sr=8-2&keywords=golang): Go in Action introduces the Go language, guiding you from inquisitive developer to Go guru. The book begins by introducing the unique features and concepts of Go. Then, you'll get hands-on experience writing real-world applications including websites and network servers, as well as techniques to manipulate and convert data at speeds that will make your friends jealous.
  - [The Way to Go: A Thorough Introduction to the Go Programming Language](http://www.amazon.com/Way-Go-Thorough-Introduction-Programming-ebook/dp/B0083RVAJW/ref=sr_1_9?ie=UTF8&qid=1460415974&sr=8-9&keywords=golang): Pros - Book is very relevant and up-to-date, well-structured (maybe too well-structured at times), covers virtually everything in Go language, has a myriad of useful code examples. Cons - Author is not a native speaker and it shows. At times it is a bit hard to understand his writing - proofreading was definitely needed.
  - [Introducing Go: Build Reliable, Scalable Programs](http://www.amazon.com/Introducing-Go-Reliable-Scalable-Programs/dp/1491941952/ref=sr_1_6?ie=UTF8&qid=1460415974&sr=8-6&keywords=golang): Perfect for beginners familiar with programming basics, this hands-on guide provides an easy introduction to Go, the general-purpose programming language from Google. Author Caleb Doxsey covers the language’s core features with step-by-step instructions and exercises in each chapter to help you practice what you learn.
  - [The Go Programming Language](http://www.amazon.com/Programming-Language-Addison-Wesley-Professional-Computing/dp/0134190440/ref=sr_1_1?ie=UTF8&qid=1460415974&sr=8-1&keywords=golang): The Go Programming Language is the authoritative resource for any programmer who wants to learn Go. It shows how to write clear and idiomatic Go to solve real-world problems. The book does not assume prior knowledge of Go nor experience with any specific language, so you’ll find it accessible whether you’re most comfortable with JavaScript, Ruby, Python, Java, or C++.
- **Videos**
  - [GoingGo.net](http://www.goinggo.net/) - A collection of videos and articles for learning Go.
  - [O'Reilly Go Fundamentals](http://shop.oreilly.com/category/learning-path/go-fundamentals.do) - Video learning path for Go programming.
  - [Learn Go in an Hour](https://www.youtube.com/watch?v=CF9S4QZuV30) Learn the go programming language in one hour.
  - [Learning to Program in Go](https://www.youtube.com/playlist?list=PLei96ZX_m9sVSEXWwZi8uwd2vqCpEm4m6) - a multi-part video training class.
- **Exercises:**
  - [Exercism.io - Go](http://exercism.io/languages/go) - Online code exercises for Go for practice and mentorship.
  - [Outlearn.com](https://www.outlearn.com/search?filter=path&q=golang) - Jump right into Go with a tour, helpful examples, sample app, and common pitfalls.
  - [The Go Bridge Foundry](https://github.com/gobridge) - A member of the [Bridge Foundry](http://bridgefoundry.org/) family, offering a complete set of free Go training materials with the goal of bringing Go to under-served communities.
  - [Go Fragments](http://www.gofragments.net/) - A collection of annotated Go code examples.
  - [Golang Tutorials](http://golangtutorials.blogspot.com/2011/05/table-of-contents.html) - A free online class.
  - [Learn Go in Y minutes](http://learnxinyminutes.com/docs/go/) is a top-to-bottom walk-through of the language.
  - [Go By Example](http://gobyexample.com/) - Go by Example is a hands-on introduction to Go using annotated example programs. Check out the first example or browse the full list below.
  -  [Pluralsight Classes for Go](http://www.pluralsight.com/tag/golang) - A growing collection of (paid) online classes.
- **Workshops:**
  - [Free Go Language Workshop](https://www.frameworktraining.co.uk/go-language-free-training-workshop/) Framework Training is running regular free BYOD workshops in London, UK
  - [Workshop-Go](https://github.com/sendwithus/workshop-go) - Startup Slam Go Workshop - examples and slides.
- **Learning resources for specific topics:**
  - [LearnConcurrency](LearnConcurrency) outlines a course of study of Go's concurrency model and patterns.
  - [LearnErrorHandling](LearnErrorHandling) links to resources about error handling in Go.
  - [LearnTesting](LearnTesting) links to resources about testing in Go.
  - [LearnServerProgramming](LearnServerProgramming) links to resources about server programming in Go.
- **Further reading:**
  - [50 Shades of Go: Traps, Gotchas, Common Mistakes for New Golang Devs](http://devs.cloudimmunity.com/gotchas-and-common-mistakes-in-go-golang/index.html)
  - [Newspaper](http://www.newspaper.io) is a topic based newsfeed for slack. Built on Go

### Ruby

Note: Ruby is a dynamic, reflective, object-oriented, general-purpose programming language. It was designed and developed in the mid-1990s by Yukihiro "Matz" Matsumoto in Japan. According to its creator, Ruby was influenced by Perl, Smalltalk, Eiffel, Ada, and Lisp.

- **Online courses:**
    - Codecademy's [Ruby track][ruby-codecademy]
      For beginners. Tends to focus on syntax.
    - Team Treehouse's [Ruby course][ruby-treehouse]
      Allows a free 14-day trial, but later requires payment.
- **Interactive tutorials:**
    - [RubyMonk][ruby-rubymonk]
      A collection of interactive tutorials to help you learn basic and advanced Ruby.
    - [TryRuby][ruby-try]
      An interactive online guide that teaches you basic Ruby step-by-step.
    - [Learn Ruby][ruby-learn]
      A downloadable set of interactive tutorials.
- **Video tutorials:** N/A
- **Books and tutorials (online):**
    - [Learn Ruby The Hard Way][ruby-lrthw]
      Part of the "Learn X The Hard Way" series. Despite its name, this is one of the easiest introductions to Ruby available.
    - [Why's (Poignant) Guide to Ruby][ruby-poignant]
      A little quirky, but still very good.
    - [More free books][ruby-more]
- **Books (paper):**
    - [The Well-Grounded Rubyist][ruby-grounded]
      A comprehensive and thorough introduction to Ruby. For beginners.
    - [Eloquent Ruby][ruby-eloquent]
      A guide on how to write Ruby idiomatically and cleanly. This book assumes that you already know Ruby or some other programming language.
- **Exercises:**
    - [Ruby Quiz][ruby-quiz]
      A series of exercises on writing programs in Ruby. New exercises are no longer being written, but the existing exercises are still very good.

  [ruby-codecademy]: http://www.codecademy.com/tracks/ruby
  [ruby-treehouse]: http://teamtreehouse.com/features/ruby

  [ruby-rubymonk]: http://rubymonk.com/
  [ruby-try]: http://tryruby.org
  [ruby-learn]: http://rubykoans.com/

  [ruby-lrthw]: http://learncodethehardway.org/ruby/
  [ruby-poignant]: http://mislav.uniqpath.com/poignant-guide/
  [ruby-more]: https://github.com/vhf/free-programming-books/blob/master/free-programming-books.md#ruby

  [ruby-grounded]: http://www.amazon.com/The-Well-Grounded-Rubyist-David-Black/dp/1933988657
  [ruby-eloquent]: http://www.amazon.com/Eloquent-Ruby-Addison-Wesley-Professional-Series/dp/0321584104

  [ruby-quiz]: http://rubyquiz.com/


### Scratch

Scratch is a language wherein you create programs by dragging together and connecting "blocks". Unlike other programming languages, Scratch is very visual, making it a very good first programming language, especially for children and younger teens.

Because not many people may be familiar with Scratch, this section will contain resources that are helpful both for _learning_ Scratch, and _teaching_ Scratch.

There are two

- **Online courses:**
    - edX's [Programming in Scratch](https://www.edx.org/course/programming-scratch-harveymuddx-cs002x#.VJw5t_-kAA) - for beginners.
    - edX's [Middle-Years Computer Science](https://www.edx.org/course/middle-years-computer-science-harveymuddx-cs001x#.VJw5rP-kAA) - a course designed to help teachers design an engaging computer science curriculum for middle-schoolers using Scratch.
- **Interactive tutorials:** N/A
- **Video tutorials:**
    - [A Collection of Scratch Videos][scratch-official] from Scratch's website
      A collection of video tutorials on Scratch for absolute beginners. Very comprehensive.
- **Books and tutorials (online):**
    - [Invent with Scratch!][scratch-invent]
      An introductory text on Scratch. For beginners.
    - [Scratch for Budding Computer Scientists][scratch-budding]
      A short tutorial that takes a more formalized approach to teaching Scratch. Best suited for those with some prior experience.
    - [Computer Science Concepts in Scratch][scratch-cs-concepts]
      A thorough introduction to Scratch. For beginners.
    - [Scratch Advanced Topics][scratch-advanced]
      A collection of resources and guides on advanced usage of Scratch. Not for beginners.
    - Reference guides: for [Scratch][scratch-reference] and [Snap/Build Your Own Blocks][scratch-snap-reference] (a variant of Scratch)
      Contains comprehensive descriptions of all language features. The Scratch reference will be useful for all levels, and the Snap reference will be particularly useful for those who are already proficient at programming in another language.
    - [Scratch for Educators][scratch-educators]
      Scratch's official portal and collection of resources for teaching using Scratch.
    - [More free books][scratch-more]
- **Books (paper):**
  - [Scratch Cards](https://scratch.mit.edu/info/cards) - Scratch cards provide a quick way to learn new Scratch code.
  - [Learn to Program with Scratch: A Visual Introduction to Programming with Games, Art, Science, and Math](http://www.amazon.com/Learn-Program-Scratch-Introduction-Programming/dp/1593275439/ref=sr_1_1?ie=UTF8&qid=1460418004&sr=8-1&keywords=scratch+programming) - In Learn to Program with Scratch, author Majed Marji uses Scratch to explain the concepts essential to solving real-world programming problems. The labeled, color-coded blocks plainly show each logical step in a given script, and with a single click, you can even test any part of your script to check your logic.
  - [Super Scratch Programming Adventure! (Covers Version 2): Learn to Program by Making Cool Games](http://www.amazon.com/Scratch-Programming-Adventure-Covers-Version/dp/1593275315/ref=sr_1_5?ie=UTF8&qid=1460418004&sr=8-5&keywords=scratch+programming) - In Super Scratch Programming Adventure!, kids learn programming fundamentals as they make their very own playable video games. They'll create projects inspired by classic arcade games that can be programmed (and played!) in an afternoon. Patient, step-by-step explanations of the code and fun programming challenges will have kids creating their own games in no time.
- **Exercises:**
  - [SHS Programming 1 Exercises](https://scratch.mit.edu/studios/532108/) - LTPWS Studio of Exercises

  [scratch-official]: http://scratch.mit.edu/help/videos/

  [scratch-invent]: http://inventwithscratch.com/about/
  [scratch-budding]: http://cs.harvard.edu/malan/scratch/index.php
  [scratch-cs-concepts]: http://stwww.weizmann.ac.il/g-cs/scratch/scratch_en.html
  [scratch-advanced]: http://wiki.scratch.mit.edu/wiki/Advanced_Topics_%28forum%29
  [scratch-reference]: http://download.scratch.mit.edu/ScratchReferenceGuide14.pdf
  [scratch-snap-reference]: http://snap.berkeley.edu/SnapManual.pdf
  [scratch-educators]: http://scratch.mit.edu/educators/
  [scratch-more]: https://github.com/vhf/free-programming-books/blob/master/free-programming-books.md#scratch

## Data

### Neo4j and Graph Databases

[Neo4j][Neo4j] is an open source NOSQL graph database, implemented in Java. It saves structured data in graphs rather than in tables. Graph databases simplify and speed up access to data that is complex and contains many connections. They use graph structures with nodes, edges, and properties to store and access connected information, and can traverse parts of the data without touching the whole graph.

Neo4j is widely used for:

- Highly connected data
- Recommendation
- Path Finding
- Data First Schema
- Schema Evolution
- A* (Least Cost Path)

- **Online courses:**
    - [Neo4j Training][Neo4j-Training] - free course, completely online
    - [GraphGist][GraphGist] - geek out on real graphs on finance, sports, politics, or even The Hobbit

[Neo4j-Training]: http://message.neotechnology.com/O0005CuN03006GNt0z0ffeO
[GraphGist]: http://message.neotechnology.com/R00NCefOuf003050GuN0A60
[Neo4j]: https://neo4j.com/

### MongoDB

[MongoDB](https://www.mongodb.com/) is an open-source [NoSQL database](https://en.wikipedia.org/wiki/NoSQL) engine built in C++.

It's a document-store database which means it stores data as a "document" inside a collection, with multiple collections inside a database. Multiple databases can exist for each server. The document data is stored as [BSON](https://en.wikipedia.org/wiki/BSON) which is [JSON](http://www.json.org/) (JavaScript Object Notation) in a binary format for performance. The data is [schema-less](https://www.google.com/search?q=schema-less&oq=schema-less&aqs=chrome..69i57j0l5.446j0j4&sourceid=chrome&ie=UTF-8) which means each document can have as many keys and values as you want with no restriction on the type of data.

It's easy to think of documents in collections like rows in a relational database table, except that these documents can have any arbitrary amount of properties (like columns for rows) and they can be different for each document and include lots of nesting like arrays of more properties. This is very powerful way to store complex data and matches up well to the object-oriented nature of most programming languages.

MongoDB runs on both Windows and Linux servers and has lots of documentation and years of production usage now so it's considered a stable and useful database, although there are continuing issues with durability and an overly-complicated replication setup to keep in mind.

- **Online courses:**
    - [MongoDB University][mongodb-university] - Paid course but it comes with a certification

- **Video Tutorials:**
    - [MongoDB Tutorial For Beginners | MongoDB Training][mongo-for-beginners]

- **Books and tutorials (online):**
    - [The Littel MongoDB Book][the-little-mongodb-book]

[mongodb-university]: https://university.mongodb.com/
[mongo-for-beginners]: https://www.youtube.com/watch?v=4ioP11POfZ4
[the-little-mongodb-book]: http://openmymind.net/mongodb.pdf

---

## Other topics

TODO: EXPAND AND POLISH

### Developing on specific platforms

Please see our [FAQ](http://www.reddit.com/r/learnprogramming/wiki/faq#wiki_how_do_i_get_starting_making_mobile_apps.2Fandroid_apps.2Fios_apps.2Fwindows_phone_apps.3F) for more information.

#### Android

- [Spreadsheet of Android resources](http://www.reddit.com/r/learnprogramming/comments/1dy9wj/im_a_cpa_who_learned_java_android_and_published/)
- [List of Android learning resources](http://www.reddit.com/r/learnprogramming/comments/22xlu9/you_want_to_how_to_write_apps_for_android/)
- [Google Code University](https://developers.google.com/university/) - also contains tutorials on other Google technologies.
- [Developing Android Apps](https://www.udacity.com/course/ud853) - via Udacity. Assumes prior programming experience.
- Team Treehouse's [Android course](http://teamtreehouse.com/features/android) - allows a free 14-day trial, but later requires payment.
- [More free books](https://github.com/vhf/free-programming-books/blob/master/free-programming-books.md#android)

#### Mac and iOS

- [List of iOS learning resources](http://www.reddit.com/r/learnprogramming/comments/22w8sk/you_want_to_know_where_to_start_for_writing_apps/)
- [List of iOS Video Tutorials](http://www.reddit.com/r/learnprogramming/comments/22zkce/want_to_learn_ios_development_best_video/)
- Apple's [iOS Developer Library](https://developer.apple.com/library/ios/navigation/)
- Apple's [Mac Developer Library](https://developer.apple.com/library/mac/navigation/)
- [Intro to iOS App Development with Swift](https://www.udacity.com/course/ud585) - via Udacity. Assumes prior programming experience.
- Team Treehouse's [iOS course](http://teamtreehouse.com/features/ios) - allows a free 14-day trial, but later requires payment.
- [More free books](https://github.com/vhf/free-programming-books/blob/master/free-programming-books.md#ios)

#### Windows and Windows phones

- Microsoft's [Developer Guides](http://msdn.microsoft.com/en-us/vstudio/cc136611)
- Microsoft's [App Hub](http://create.msdn.com/en-US/education/catalog/) - resources for mobile and XNA game development.
- More free books:
    - [.NET](https://github.com/vhf/free-programming-books/blob/master/free-programming-books.md#net-framework)
    - [Windows 8 and Windows Phone](https://github.com/vhf/free-programming-books/blob/master/free-programming-books.md#windows-8)

TODO: Expand? Don't want to duplicate too much existing content.

### Data structures and algorithms

Unless otherwise noted, all of the resources in this category assume prior programming experience.

- **Online courses:**
    - Udacity's [Intro to Algorithms](https://www.udacity.com/course/cs215) - assumes  proficiency in math up to the Algebra 2 level.
    - [Andrew Ng's Machine Learning course](https://www.coursera.org/learn/machine-learning)
    - [Lynda Data Science Basics](http://www.lynda.com/SharedPlaylist/ff466840b2ba481e82149ecca9a5bdd6) - Explore Data Science with this selection of courses to help you analyze and gain insight on your business data for improved performance and results.
    - [Intro to Data Science](https://www.udacity.com/course/intro-to-data-science--ud359) - The class will focus on breadth and present the topics briefly instead of focusing on a single topic in depth. This will give you the opportunity to sample and apply the basic techniques of data science.
    - Coursera's [Algorithms: Design and Analysis, Part 1](https://www.coursera.org/course/algo) - lectures are archived. Assumes some familarity with proofs.
    - Open Culture has several good video playlists (mostly on YouTube)
        - [Algorithm Design and Analysis](https://www.youtube.com/playlist?list=PL6EF0274BD849A7D5) - hosted by UCDavis (University of California, Davis)
        - [Computer Science 61B (Data structures)](https://www.youtube.com/playlist?list=PL-XXv-cvA_iDXrTvCvDgIkeCWeSIDr4Yh) - hosted by UCBerkeley (University of California, Berkeley).
        - [CS2: Data Structures and Algorithms](https://www.youtube.com/course?feature=edu&list=ECE621E25B3BF8B9D1&category=University%2FScience) - Hosted by the University of New South Wales
    - MIT Open Courseware's [Introduction to Algorithms](http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-006-introduction-to-algorithms-fall-2011/) and [Design and Analysis of Algorithms](http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-046j-design-and-analysis-of-algorithms-spring-2012/)
    - Khan Academy's [Algorithms](https://www.khanacademy.org/computing/computer-science/algorithms)
- **Interactive tutorials:** N/A
- **Exercises:**
    - [Codingbat][algo-codingbat]
      Contains Java and Python exercises. For beginners and intermediate-level programmers.
    - [CodeAbbey][algo-codeabbey]
      Similar to Codingbat.
    - [HackerRank][algo-hackerrank]
      Contains a large collection of exercises, from basic up to the competitive
      level. Good for both beginners and advanced programmers. Also holds their own
      online competition.
    - [TopCoder][algo-topcoder]
      Similar to HackerRank.
    - [UVa Online Judge][algo-uva]
      A collection of programming problems and solutions from multiple programming
      competitions.
    - [Project Euler][algo-euler]
      A collection of programming exercises. The exercises are more math-oriented,
      and are not always CS-oriented.
- **Video tutorials:** N/A
- **Books and tutorials (online):**
    - [Problem Solving with Algorithms and Data Structures][algo-problem]
      A very thorough introduction to data structures and algorithms. Although it uses
      Python, the main concepts taught should be applicable to every language. Starts with
      a quick overview of Python for those unfamiliar to the language.
    - [Algorithms by Robert Sedgewick](http://algs4.cs.princeton.edu/home/) which is in Java and accompanies [these lectures](https://www.coursera.org/course/algs4partI) on Coursera.
    - [The Stony Brook Algorithm Repository](http://www3.cs.stonybrook.edu/~algorith/) - a comprehensive reference of many different data structures and algorithms.
    - [The Big-O Cheat Sheet](http://bigocheatsheet.com/) - a cheat sheet containing links and condensed information about the top most commonly-used/commonly-taught data structures and algorithms.
- **Books (paper):**
    - [Introduction to Algorithms](http://www.amazon.com/Introduction-Algorithms-Thomas-H-Cormen/dp/0262033844) - the canonical guide to algorithms and is very comprehensive. The book is language agnostic, moves at an accelerated pace, and is accompanied by lectures [here](http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-046j-introduction-to-algorithms-sma-5503-fall-2005/index.htm).
    - [The Algorithm Design Manual](http://www.amazon.com/Algorithm-Design-Manual-Steve-Skiena/dp/0387948600) - the first half of the book emphasizes the design and analysis of algorithms, and the second half is a catalog of the 75 most important algorithmic problems for reference.
    - [Machine Learning for Hackers](http://www.amazon.com/Machine-Learning-Hackers-Drew-Conway/dp/1449303714) - If you’re an experienced programmer interested in crunching data, this book will get you started with machine learning.

    - [How can I rebuild my base of algorithms/data structures knowledge?](http://stackoverflow.com/q/1697572/646543) - contains links to various recommended books and suggestions for improvement.
    - [Data Driven:
Creating a Data Culture](http://www.oreilly.com/data/free/data-driven.csp) - Succeeding with data isn’t just a matter of putting Hadoop in your machine room, or hiring some physicists with crazy math skills.

  [algo-problem]: http://interactivepython.org/runestone/static/pythonds/index.html
  [algo-codingbat]: http://codingbat.com/
  [algo-codeabbey]: http://www.codeabbey.com/
  [algo-hackerrank]: https://www.hackerrank.com/
  [algo-topcoder]: http://www.topcoder.com/
  [algo-uva]: http://uva.onlinejudge.org/
  [algo-euler]: https://projecteuler.net/


---

## Tools

### Version control

#### Git

- **Online courses:**
    - [How to Use Git and GitHub](https://www.udacity.com/course/ud775) - via Udacity.
- **Interactive tutorials:**
    - [Learn Git Branching](http://pcottle.github.io/learnGitBranching/) - a very visual interactive tutorial starting from the absolute basics with a high emphasis on understanding the internals/what each git command really means.
    - [Try Git](https://try.github.io/levels/1/challenges/1) - an interactive tutorial that teaches basic Git.
- **Exercises:** N/A
- **Video tutorials:** N/A
- **Books and tutorials (online):**
    - [Learn Version Control with Git](http://www.git-tower.com/learn/ebook/command-line/introduction) - an introduction to Git for the absolute beginner (via git-tower).
    - Git has an [official reference and book](http://git-scm.com/documentation)
    - [More free books](https://github.com/vhf/free-programming-books/blob/master/free-programming-books.md#git)
- **Books (paper):** N/A

#### Mercurial

- **Online courses:** N/A
- **Interactive tutorials:** N/A
- **Exercises:** N/A
- **Video tutorials:** N/A
- **Books and tutorials (online):**
    - [HgInit](http://hginit.com/01.html) - a basic introduction to Mercurial.
    - [Mercurial: The Definitive Guide](http://hgbook.red-bean.com/)
    - [More free books](https://github.com/vhf/free-programming-books/blob/master/free-programming-books.md#mercurial)
- **Books (paper):** N/A

**TODO:** Expand, add info on Subversion
