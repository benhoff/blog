#########################
Adding Discourse Comments
#########################

:date: 2017-06-10 14:25
:category: Blog
:slug: adding-discourse-comments
:summary: Working through adding Discourse Comments to the blog.

Alright, here we go. Let's add comments to my static site. I waited until the weekend because I knew it was going to be a pain.

So following the directions, I created a digital ocean droplet, and copied the github repo over.

This was relatively easy for me. Had some issue with path wrangling, but got it figured out eventually. Github wants to ask for your github username weirdly when doing a git clone if you do it incorrectly. Eventually I just changed into the directory I wanted the repo and did the clone from there. Feel like I shouldn't have to do that, but whatever.

Ok, so now I need email. Damn.

Well let's stick with mailgun, since that sounds familiar.

So I signed up for mailgun, but now I need a domain and a DNS provider.

So I signed up for a domain on Google. `benhoff.net`. Old school. Perfect.

Just remembered that a domain and a DNS provider are different. Wonder if google will act as a DNS provider. I'm swimming in unknown territory now.

Ok, I need to add DNS records for sending according to mailgun.

Uhh, I don't know what I'm doing. Luckily there's this blogpost. http://www.curtismlarson.com/blog/2015/04/12/github-pages-google-domains/
What an annoying pop up page.

Ok, I followed the directions to add the custom resource records from my google name to my google domain. According to the blog, it should take about a day to resolve.

I don't think this solves my mailgun issue though.

A little google fu: https://stackoverflow.com/questions/37864807/setting-up-google-domains-dns-to-work-with-mailgun-mx-records

Looks like I need to add a subdomain as a MX record.

So under Custom Resource records, I'm going to add the name `mg`, with the type `MX` and add the `mxa.mailgun.org` and `mxb.mailgun.org`. Looks like google automagically adds a 10 and a period to the end of that.

Cool, so now that I've done that, I've added the domain `mg.benhoff.net` to the mailgun side.

Now I need to add everything else.

From this site: http://code.krister.ee/mailgun-digitalocean/

Looks like I just keep adding these to the custom resource records.

I added email.mg CNAME to point to mailgun.org, and a krs._domainkey.mg to point to a really long string. By clicking the authorize, looks like everything worked.

All right, back to the discourse setup.

I'll launch the setup tool. Setup wants to create a 2 gig swap file. Fine by me. Following the defaults for mailgun set by: https://github.com/discourse/discourse/blob/master/docs/INSTALL-email.md

Now it asks for let's encrypt account email? Hmm, let's set that up real quick.

Just enter an email and press enter, and everything will be encrypted.

Discourse is now updating which is fine.

I lost internet, but looks like everything worked fine. Perfect.

I'll add the CNAME to the custom resource records. Whoops, looks that's not how to do that.

I need to add it as a 'A' resource and fix the domain name in my setup and rebuild the app using `./launch rebuild app`

Sick. I'll add in some other fancy stuff, like Facebook, Google, Twitter, and Github logins.

Now onto embedding. I'm following this: https://meta.discourse.org/t/embedding-discourse-comments-via-javascript/31963

The admin tab has a customize section. From there to embedding. Add the domain name and I've got some html. Adding it to the theme of the article template and I should be set.

Fingers crossed.
