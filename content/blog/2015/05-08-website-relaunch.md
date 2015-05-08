Title: Website relaunch
date: 2015-05-08 23:40
author: mrwonko
tags: this website, Programming, Internship
category: Programming
type: blog
slug: website-relaunch
summary: Look at this glorious new website!

If you've visited my website before you'll have noticed that it has a new look. Now with mobile support. Yay!

Last October to December I did an internship at a local web developer and learned that PHP and MySQL aren't exactly state of the art any more, web development can actually be fun! So I've moved from my web host to a Linux virtual machine where I can basically do anything.

But in the end it actually mostly does less. Instead of generating each page dynamically like I previously did with Wordpress, I now generate HTML pages offline with [Pelican](http://getpelican.com/). That makes most requests super easy: just serve a static page. Eventually I'll set it up to automatically regenerate them whenever I push new articles to the repo, but for now I just manually start a script on the server.

The only dynamic content so far are the comments (and download counts), which use a Python backend running [Twisted](http://twistedmatrix.com/) with [AngularJS](http://angularjs.org/) in the frontend. I used Angular during my internship and once you've learned how it works it's pleasantly simple and fast. The download frontend could still be improved somewhat; it could do with some sorting, searching and filtering and the download count isn't displayed anywhere yet, but I don't really have the time for that at the moment.

All in all I'm quite happy with the new site. I quite like writing my content in Markdown and there's not a bit of PHP left, which [is for the best](http://eev.ee/blog/2012/04/09/php-a-fractal-of-bad-design/).

Expect some more updates in the immediate future (though not necessarily regularly after that), I have quite some experiences to tell you about and a couple of opinions to share.

So long

Willi
