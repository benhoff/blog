Blog Initial Tech Stack Thoughts
################################

:date: 2017-06-04 20:30
:modified: 2017-06-04 20:35
:tags: blog, tech, stack
:category: blog
:slug: blog-tech-stack-thoughts
:authors: Ben Hoff
:summary: Walking through the intial tech stack considerations for a new blog.

Ok, let's start a blog.

First of all, we need a tech stack. My inital thoughts are to use a static site generator. None of the blog code needs to be dynamic, and I can import a javascript comment system (such as discus) later. Probably end up using google analytics as well.

I'll be using either markdown or restructured text so that I can track the blog configuration using git.

Perfect, so we've got a static site generator, mardown/restructured text, third party analytics and commenting... now on to hosting. Since I don't feel like taking on the hosting thing for now, and the domain name isn't important, let's just stick with github pages. I'm pretty sure it's free.

The only other things that I would like would be some responsive desing (I primarily read using my smart phone) and some way to embed a jupyter notebbook directly in the page.

I'll save the responsive design for another day (and a more complicated folder directory as well), but the desire for jupyter notebook means I'll probably be using some sort of python stack instead of the (likely more popular) Github incarnation of Jekyll.

A quick google search shows that Pelican is likely the largest/most supported python static site generator. Looks like it can work with either markdown or restructured text (I'll probably stick with restructured text since I've written some README's with it). Perfect. Another quick search shows there's a plugin that allows for Jupyter-Notebooks to be in embedded. We're cooking with fire now. So let's review our tech.

- Git (version control)
- Resturctured Text (text markup)
- Github Pages (website hosting/Domain)
- Pelican (static site generator)

Tech to be implemented later (third party and potentially hard)

- Discourse (comments)
- Google Analytics (analytics)

Aweomse, let's start implementing.
