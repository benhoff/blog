Blog Tech Stack
###############

:date: 2017-06-12 08:34
:category: blog
:slug: blog-tech-stack
:authors: Ben Hoff
:summary: Reviewing the tech stack and hosting services I'm using for the blog.

As I'm looking to start up a mailing service I thought it be interesting to talk about the services I'm using for hosting this blog. I'll do it in cronological order. Kind of.

+---------------------------+---------------------------------------------------+
| Service Type              | Provider                                          | 
+===========================+===================================================+
| Static Site Generator     | `Pelcian <https://blog.getpelican.com/>`_         |
+---------------------------+---------------------------------------------------+
| Static Site Host          | `Github Pages <https://pages.github.com/>`_       |
+---------------------------+---------------------------------------------------+
| Comments/Forum            | `Discourse <https://www.discourse.org/>`_         |
+---------------------------+---------------------------------------------------+
| Dynamic Content Host [1]_ | `Digital Ocean <https://m.do.co/c/2fdf30b46683>`_ |
+---------------------------+---------------------------------------------------+
| Domain Registration/DNS   | `Google Domains <https://domains.google/#/>`_     |
+---------------------------+---------------------------------------------------+
| Transactional Email [2]_  | `Mailgun <https://www.mailgun.com/>`_             |
+---------------------------+---------------------------------------------------+
| Mailing List             | `Mailchimp <https://mailchimp.com/>`_             |
+---------------------------+---------------------------------------------------+

I'll try to add here as things change.

.. [1] Used for hosting the discourse instance
.. [2] Transactional email is, according to `Mailchimp's Docs <https://blog.mailchimp.com/what-is-transactional-email/>`_, an email sent to an individual based on some action. Discourse uses it for signups, which is why I needed it.
