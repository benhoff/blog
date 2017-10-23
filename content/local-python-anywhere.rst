###########################
Self Hosted Python Anywhere
###########################


:date: 2017-10-16 07:22
:category: Random
:slug: local-python-anywhere
:summary: Working around aggressive workplace firewalls


I have a great job, but it doesn't always fully employ me. Such is life. I still like to be productive, and having a programming hobbies and an office job seems like a match made in heaven.

Oh, you don't have enough things for me to do? But you still want me to be here in case something comes up? No worries team, I gotcha. Totally self entertaining.

The problem has been that my office's aggressive firewall has prevented me from doing anything that doesn't come over port 80 or 443. Which I totally get. But c'mon man. I can only read Reddit so many hours of the day.

But then I found `Python Anywhere`_. The basic premise is that all you need is a web browser and you can be up and coding in no time. I immediately signed up. This was exactly what I was looking for! Up until the point I realized that I can't bind to ports. With my main project using zmq, which requires binding to ports, I was super bummed.

It did however get me thinking that maybe I could use the same program. They had a full fledged terminal in the browser! There was no way that the website author made that program himself. It was too slick. It had to be open sourced.

After lots of googling I found it. `hterm`_, the xterm-compatible terminal emulator. A terminal emulator itself didn't help me though. I need to have it hosted and hooked into a server somewhere. Enter `wetty`_, the full bound service.

So now that I had a terminal as a service, I still needed to work with my office's firewall. Luckily for me, I have this blog. Or more specifically, I have the comments of the blog that I'm hosting myself using nginx. Using a `reverse proxy`_ feature in nginx, I was able to link up my new 'terminal as a service' to the ip address of my blog comments which has already been white listed in my organizations firewall.

Sweet. My organization gets a much more motivated/attentive employee during lull periods and I get to be more productive. Win-win.


.. _`Python Anywhere`: https://www.pythonanywhere.com/
.. _`hterm`: https://github.com/macton/hterm
.. _`wetty`: https://github.com/krishnasrinivas/wetty
.. _`reverse proxy`: https://en.wikipedia.org/wiki/Reverse_proxy

