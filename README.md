# Source code for [sglavoie.com](https://www.sglavoie.com/)

This repository contains the source code for my personal website, which is a blog describing my learning path in all things related to computer science. For more details, you can visit the [GitHub repository](https://github.com/sglavoie/sglavoie.github.io) with the actual content of the website.

Please feel free to reuse all the code that you might need!

# How was it done?

It is all generated with the help of **[Pelican](https://github.com/getpelican/pelican)**, a static website generator that uses **[Python](https://www.python.org/)**. The content of the website is written in Markdown format and is rendered automatically as HTML and CSS with some bits of JavaScript here and there.

Here are the main reasons why this approach felt right:

-   It is very easy to maintain. Once the design is done, you simply write in Markdown and you are good to go. It is also easy to modify a theme or have a collection of themes stored in a directory with a bunch of HTML, CSS, JavaScript and image files.
-   It is super quick to deploy anywhere without having any kind of specific server requirements such as PHP, Python, SSL, MySQL, Apache, etc. Everything is static and can be uploaded almost everywhere!
-   It's also quite secure in the end as there is no need to perform updates, no need to authenticate users or deal with a database.
