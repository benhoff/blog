##############################
Keeping Track of Past Research
##############################

:date: 2017-06-27 17:07
:category: Random
:slug: keeping-track-of-past-research
:summary: Reviewing multiple methods of keeping track of past research

I've got a very specific problem.

While I was doing research as part of my `Learning Python Data Analysis`_ series, I stumbled across a slideshare that showed the different types of analysis that you can do using Twitter data. I think the author ended up deep diving into building a network diagram showing the different connections between tweets. I want to deep dive into a different aspect of Twitter data analysis, following on the trend of doing live analysis that I did in my aforementioned video series is.

My problem is that I can't find that slideshare.

Now I admittedly have done very little research to re-find it. I actually don't feel like doing any research though. I would like for it to be served to me on a silver platter, since I already spent probably 10+ hours Google searching.

So I went looking for a better way.

There's a couple of different ways I've found.

- Mind maps
- Note cards
- Wiki's
- Blogs

Mind Maps
---------

Mind maps work by showing the connections between different pieces.

.. image:: https://upload.wikimedia.org/wikipedia/commons/1/1a/Tennis-mindmap.png
  :width: 400
  :height: 282

I've been aware of mind maps before, but I was recently reminded of them by an interactive mind map I saw on Github, promising/labeled "Learn Anything". Here's the repo_ and here's the website_ if you want to take a look.

I'll be upfront, I don't really see the use in mind maps... or at least not software generated ones. The Learn Anything site seems to be more a link map, which I can kind of buy for usefulness? Kinda?

Note Cards
----------

This is a method I was thought while I was in school, and is apparently still in use today. The basic gist is to record the idea or information along with the original source on note cards. So you might pull the idea of "Elephants can hear in the infrasonic region" out of a certain book. The useful point of note cards is not to record the idea, but the actual source. That way, when you were writing a research paper you could form a coherent paper/thought process without worrying about keeping track of the sources, as they were a standalone product.

Microsoft Word has a version of this feature that I have [ab]used to write reports before. There are also standalone products that do a version of this as well. The challenge is that webpages, unlike books, do not fit well within this format. `Link rot`_ is also a concern with this method.

Wiki's
------

I've been interested in the idea of creating wiki's for a long time. My interests are diverse, and the idea of hooking a wiki site up to a search engine is very, very appealing. `This Blog post`_ explores in depth a particular research methodology the author recommends as key to enabling his research.

.. _`This Blog post`: http://calnewport.com/blog/2009/05/11/how-to-build-a-paper-research-wiki/

However, according to Wikipedia, a wiki is a website where users collaboratively edit articles. In this case, keeping track of individual lines of research isn't really a collaborative effort. Wikipedia also mentions that wiki's are basically Content Management Systems (CMS's), which is a pretty well worn software model. It would likely be possible to explore a open source CMS for this solution. Or you know, maybe a blog....

Blogs
-----

Blogs at the end of the day are just content and can say anything. One of my favorite posts so far has been the `Beaglebone Black`_ post, where I walked through the steps and frustrations of flashing a Beaglebone black. While I was originally trying to install OpenVPN on the Beaglebone and ended up not doing that, the post serves as a reference point when I (invariably) reflash another one. But I've got some interesting tidbits and posts that should save me some time... next time.

.. _`Beaglebone Black`: {filename}/flashing-beaglebone.rst

Closing Thoughts
----------------

The truth of the matter is there's likely no single model or silver bullet software that is going to make this easy for me. My use case falls somewhere between `Knowledge Transfer`_ and individual research. 

Committing to a research methodology or note taking process would be the main piece. Since I've enjoyed writing up blog posts and linking them to death with outside sources, I'll likely keep that approach until further notice.

On the software side, I would like to figure out a way to keep track of interesting links and download/index the page contents to stave off the issues associated with link rot. Hooking this up to a search engine, (likely elastic search) combined with the aforementioned blog posts I and my video series transcript would scratch the 80% solution. If you know of an easy way to do that, drop me a line.



.. _`Knowledge Transfer`: https://en.wikipedia.org/wiki/Knowledge_transfer

.. _repo: https://github.com/nikitavoloboev/learn-anything
.. _website: https://learn-anything.xyz/
.. _`Learning Python Data Analysis`: https://www.packtpub.com/big-data-and-business-intelligence/learning-python-data-analysis-video
.. _`Link rot`: https://en.wikipedia.org/wiki/Link_rot
