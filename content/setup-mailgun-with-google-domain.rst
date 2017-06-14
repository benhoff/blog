Setup Mailgun with Google Domain
################################

:date: 2017-06-12 20:20
:category: random
:slug: setup-mailgun-with-google-domain
:authors: Ben Hoff
:summary: Setting up the DNS configuration of Mailgun for Google Domain
:status: draft

Right, let's setup Mailgun. I'm using Mailgun for my Discourse install.

The first step is to add your domain.

Mailgun is going to recommend that you use a subdomain, such as *mg.mydomain.com*
Whether you want to do that or not is up to you, the steps will be similar. I'm not going to. So for the sake of argument here, the domain that we are setting up is *mydomain.com*

Mailgun is going to give you 4 steps. We will need to go `Google Domains`_. Click the *Manage My Domains*, and then click the *DNS* button on the domain of interest.

OK, we're on a new page. Scroll all the way down to the section that is titled *Custom resource records*. Here's where we make the money.

Under Step 2, *Add DNS Records For Sending* on the **Mailgun** site, there are three resources we need to add: ``TXT``, ``MX``, and a second ``MX``.

Let's add the ``TXT`` first.

.. figure:: {filename}/images/google-domain-1.png

The far left column


.. _`Google Domains`: https://domains.google/#/
