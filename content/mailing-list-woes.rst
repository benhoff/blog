Mailing List Woes
#################

:date: 2017-06-12 16:01
:category: Blog
:slug: mailing-list-woes
:summary: Figuring out how to add a mailing list.


All right, let's add a mailing list.

So I know I've got Mailgun_ use for Discourse_ (used for forum comments). Looking into the Mailgun documentation, I can see that there's an actual API_ for a mailing list. However the documentation shows Mailgun's implementation is more of a backend deal. Which would be fine if I had a dynamic application, but since I'm dealing with static pages, this is a major hangup.

So my next option is to search for a look for either an already existing solution or host my own. 

This is a mailing list. I could build one with sqlite and python in like 5 minutes. And it would be awful.

Let's start by looking to see what I can host myself.

After some google searching, it looks like the only open source version is Mailman_.

I've got a confession to make. I've tried to get Mailman up and running before. It didn't go very well. Mailman is a mailing list manager. It provides a way to see past emails, navigate replies, and search. Mailman does not provide a way to actually send emails. You have to hook either Postfix or something else up to actually get it up and running.

Also the other thing is, I've already got a full up forum with Discord. And right now, that forum is consuming 1 of 1 gigabytes of data that the Digital Ocean instance provides me. And I don't want to upsize the instance.

So now I'm back to using a hosted service. A couple of blogs recommended using Aweber_, who I've never heard of, but I'm going to stick with Mailchimp_, mostly because I've heard of them actually.

So signed up, started building a mailing list, got the html code to put into the site's template. Which is perfect. I'll eventually work towards sending out weekly "round-up" emails. Just a simple email that lays out all the articles so you don't have to visit the site to see what I'm writing about. 

But there's some pieces I need to figure out. Since I've got my own domain and a transactional mailing agent with Mailgun, I should be able to actually receive emails at the domain. As in: ben@benhoff.net

I set up a few referral rules at Mailgun, but it's a little dicey currently. I've gotten a few emails, but not all of them. I'm not sure what's wrong, but I think it has something to do with the DNS records.

If you have ever experienced or might now what's going on, feel free to comment below and point me in some resources. Otherwise, I'll dive into it later and post another article detailing the fix.

.. _API: https://documentation.mailgun.com/en/latest/api-mailinglists.html
.. _Aweber: https://www.aweber.com/
.. _Discourse: http://benhoff.net/adding-discourse-comments.html
.. _Mailgun: https://www.mailgun.com
.. _Mailman: https://www.gnu.org/software/mailman/
.. _Mailchimp: https://mailchimp.com/


