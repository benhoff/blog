Fixing My Issue With Github Stars
#################################

:date: 2017-06-09 08:11
:category: random
:slug: remembering-github-stars
:authors: Ben Hoff
:summary: How I fixed a long term issue with how I star repositories on Github

I’ve got this weird problem.

I don’t remember why I’ve starred the things I’ve starred on Github. It’s gotten so bad in fact, that I’ll often be browsing an interesting Github repo on a topic I’m interested in, go to bookmark it, and realize that I already have.

Doh!

The real issue is that the reason I bookmark repo’s is for a very specific purpose. For example, a lot of the bot code that I follow is because I’m interested in how different bots parse and handle incoming messages or events.

I mean, in my head, it’s probably something as simple as pushing it onto a queue and then using a worker thread to work through the tasks. But what if it’s different?

Part of the reason I started working on Vexbot was because I was interested in a universal interface to anything. I wanted to take and plug into random services (Youtube, Irc, etc) and have them all run through a common parsing/bot system. So far, I’ve created the only bot that I’ve seen that uses subproccesses for each individual adapter.

But I’m always curious about what others have done to tackle this problem, so I bookmark other bots to go check out how they do it.
Except I never do. And then browsing through my list of stars (which I rarely do) I can never remember why I bookmarked it.

So let’s fix it.

I’ll create a github repo targeted at remembering why I starred the things I stared. By using a Readme file, I’ll only have to visit the main repo page. Plus very thing is version controlled and nice. Something that would be nice would be to create a bot that periodically polls my starred list and creates an issue or a pull request so that I don’t get lazy, but let’s not get ahead of ourselves.

So hold my beer. Here I go.
