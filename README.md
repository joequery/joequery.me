joequery.me source mirror
=========================

This repo holds the source of the site [http://joequery.me][0].  The site is
written in Python2.7 with the aid of the [Flask][1] framework.

About this repo: notes on quality
---------------------------------

This repo reflects my ideal workflow. The way I like to go about creating
articles, storing metadata, or anything else could be completely different than
your preferences. My system is not perfect, but it is perfect *for me*. The code
may be of mediocre quality, simply because I would rather spend time writing
articles than work on the thing that lets me write articles.

Site features
-------------

* Easy to create static pages
* File based blogging platform
    + Markdown
    + Static home page/category index pages for speed
    + Automatic sitemap.xml generation
    + Automatic rss feed generation
* Code snippets can be pulled into articles from files
    + Links to raw snippet sources automatically generated ([See example][2])

Requirements
------------

* Python2.7
* virtualenv
* libxml2-dev
* libxslt-dev


How to use the site
-------------------

### Installation

    $ git://github.com/joequery/joequery.me.git
    $ cd joequery.me
    $ virtualenv env
    $ . env/bin/activate
    (env) $ pip install -r requirements.txt

If you recieve any errors during the installation of PyQuery, ensure that
libxml2-dev and libxslt-dev are installed on your system.

Now generate the blog index pages and the home page (we explain this later)

    (env) $ python genfeed.py
    Generated rss.txt
    Generated static rss feed
    Generated static blog pages
    Generated sample posts for the home page
    Generated xml sitemap
    Generated related posts.txt files
    Generated tag index pages
    Generated series index pages
    (env) $ python runserver.py
    * Running on http://0.0.0.0:5000/
    * Restarting with reloader

Now head to http://localhost:5000


### Creating articles

Posts are located in `joequery/blog/posts/`. To create an article, copy the
template located at `joequery/blog/posts/template` to one of the article
categories (currently code, math, or screencast), and rename it to be the post
slug. For example,

    $ cd joequery/blog/posts
    $ cp -r template code/how-to-use-javascript

You can then visit http://localhost:5000/code/how-to-use-javascript and you 
will see a generic article. You will not see this newly created article appear
on the home page yet, but we will get to that later.

Move to the newly copied directory and examine the `meta.txt` file.

    $ cd code/how-to-use-javascript
    $ cat meta.txt
    [post]
    title: Post Title
    description: Post description
    time: 2012-12-07 Fri 09:53 PM

The \[post] tag must remain on top of the `meta.txt` file. The title is the post
title, the description is the excerpt that will be displayed on the home page
and blog index pages. Note: If you want your description to span multiple
lines, every line after the first needs to be indented: [Example][3]. The time
is the publish time, and the time format you see above is the *required* format.
If you're a vim user, you can place the following in your `~/.vimrc` to have the
F3 key generate a timestamp for you:

    " Insert timestamp
    nmap <F3> a<C-R>=strftime("%Y-%m-%d %a %I:%M %p")<CR><Esc>
    imap <F3> <C-R>=strftime("%Y-%m-%d %a %I:%M %p")<CR>

If you examine the `body.html` file of the directory we created, you'll see

    {% from "macros" import img, blogimg, snippet %} {% set p = post %}
    {% extends "templates/post.html" %} {% block post %} {% filter markdown %}

    {% endfilter %} {% endblock post %}

You start writing your article in the line left blank. For example, 

    {% from "macros" import img, blogimg, snippet %} {% set p = post %}
    {% extends "templates/post.html" %} {% block post %} {% filter markdown %}

    Headline level 2
    ----------------

    This is some content.

    ### Headline level 3

    More content

    {% endfilter %} {% endblock post %}

### Generating the home page and blog index pages

Since I didn't feel like using a database for the site, I needed a way to have
the home page and blog index pages display the most recent articles without
reading through the file system every time the home page is requested. My
solution was to create a script I would run after

* Creating a new artile
* Adding tags/series to an article (will explain soon)
* Editing a publish time of an article

This script is called `genfeed.py`, and it's located in the top level directory
of the project. To use it, simply make sure the virtualenv is activated and run

    (env) $ python genfeed.py

`genfeed.py` also creates an XML sitemap which can be reached at
http://localhost:5000/sitemap as well as an RSS feed which can be reached at
http://localhost:5000/feed 

### Series and tags

Posts can have multiple tags separated by commas specified in their meta.txt
files. Currently, tags can only be **one word long**, but dashes and underscores
are okay. For example,

    [post]
    title: Debugging failed compilations with apt-file
    description: A quick tutorial on using apt-file on Ubuntu to solve failed make
        compilations due to missing files.
    time: 2012-12-28 Fri 07:05 PM
    tags: ubuntu, utilities

The `ubuntu` and `utilities` directories need to exist in the 
`/joequery/blog/posts/tags/` directory. We need these directories to be
versioned, so I add a `.gitkeep` file to the tag directories and commit them.

    $ cd joequery/blog/posts/tags
    $ mkdir ubuntu
    $ touch ubuntu/.gitkeep

Posts with tags will automatically list the tags at the bottom of the article.
Additionally, every tag has its own index page generated by `genfeed.py`, such
as http://localhost:5000/tag/ubuntu

These tag index pages have the most recent articles on top.

A series is like a tag except a post can only have one series and the series
page is ordered with the oldest articles on top. This is useful if you're
writing related tutorials that are to be read in a specific order.

A post can have a series and have tags. For example, 

    [post]
    title: Programming Language Design Issues
    description: We begin studying programming language design and implementations
        by examining the history of programming languages, the role of programming
        languages, and the details on programming environments.
    time: 2013-02-14 Thu 11:22 PM
    series: programming-languages-4th-edition
    tags: computer-science

For this example, it's necessary to have the directory
`joequery/blog/posts/series/programming-languages-4th-edition` exist, versioned
with a `.gitkeep` file.

### Blog images

Suppose we have an article `easy-math` in the `math` category. So the path to
our article would be `joequery/blog/posts/math/easy-math`. If we want to include
images in our article, we would do the following:

    $ cd joequery
    $ cd static/images
    $ mkdir -p math/easy-math

Now we can place images in the `static/math/easy-math` directory. Suppose we
have "img1.png", "hello.jpg" in the directory, and now we want to have those
images appear in our post.

Somewhere in the `joequery/blog/posts/math/easy-math/body.html` file, we would
write

    {{blogimg(g,p, "img1.png")|safe}}

This would produce the image tag

    <img src="/static/images/math/easy-math/img1.png />

#### How it works (if you care)

The above is a bit cryptic, so I'll explain what it does. `blogimg` is what's
known as a macro in Jinja2, the default templating system used by Flask. The
purpose of this custom macro is to generate an img tag. Jinja2 forces us to
declare the returned string of a macro safe to render as html, hence the `safe`
at the end.  The first argument, `g`, represents Flask's global object that
we're free to populate with anything. In my case, I populated it with a property
called `assets`. That way I can specify different places for Flask to look for
images and static files on production, such as Amazon S3 (Currently I have
`g.assets` set to the `joequery/static` directory both on development and
production, but you can see the `joequery/settings.py` file where that can
easily be changed). The second parameter, `p`, is a dictionary holding a lot of
information about the current post. The last parameter is the name of the file.

### Code snippets

What I believe is the most useful feature of my site is the ability to easily
embed source files into a post. Very simple code snippets can be written
directly to the post just by indenting four spaces. However, when you want to
create complex programming examples, it gets cumbersome to extract code you've
written on your article, go compile it, edit it, paste it back, and repeat as
you find issues. Here was my solution:

Suppose you're working on an article in `joequery/blog/posts/code/learn-python`.
You make an example python file, say `learn-lists.py`. Place that in the post
directory, and then you can call that source file into the post via

    {{ snippet(p, "learn-lists.py")|safe}}

Additionally, a link to a plain-text version of the source file (similar to
Github's Raw) is automatically generated for you and linked to in the source.
This is extremely convenient for people who wish to `wget` your code snippet
onto a server.

In order to avoid worrying about cleaning up .o or .pyc files, an extension
whitelist is located in the `display_raw_source_file()` function in the 
`joequery/blog/routes.py` file. I do recommend adding any type of
object/bytecode file to your `.gitignore`, though.

### Notes on genfeed.py

No files generated by genfeed.py are versioned. If you're pushing your repo to a
production server, be sure to have genfeed.py run afterwards.

[0]: http://joequery.me
[1]: http://flask.pocoo.org/
[2]: http://joequery.me/code/environment-variable-c/
[3]: https://github.com/joequery/joequery.me/blob/master/joequery/blog/posts/code/minify-js-commandline/meta.txt
