Title: Paying for Open Source
Date: 2019-11-26 06:40
Category: Other
Slug: paying-for-open-source
Authors: Ben Hoff
Summary: Exploring methods for promoting Open Source

I think the first time I saw an Open Source project that was well funded and was using that funding to promote development was NeoVim. NeoVim was a fork of the popular Vim project, focused on reducing the cruft of the project and bringing best practices back in. Whoever was running the project was a marketing genius. He got a ton of press outlining the issues with the Vim project. But the key difference between him and a thousand of other people complaining about projects is that he launched an alternative *and asked for money*. This is how I got introduced to [BountySource](https://www.bountysource.com/).

The BountySource idea is simple. Give money against (typically) GitHub issues to promote development for fixes. Bounties can be pooled so that interested individuals can pool money together. Some of the bounties are quite large, in the $5K realm and IBM has awarded $470,000+ dollars on the platform. Now these two data points are by far the outliers. The platform itself hasn't really caught on in a substantial way. There are 5-8 projects in the $5K realm which are deeply technical lifts, and the next largest businesses are Ripple coin and Elementary with $37K and $27K respectively.

NeoVim itself looks like it's focused on funding an individual developer or project maintenance over funding individual issues. I seem to remember in the early days that they were funding individual issues. I'm guessing the lag between putting money down and actual implementations was too large. Especially for bug fixes, this seems like an unwise strategy.

For my own personal use, I've been interested in throwing some small cash sums around to get a feel for different approaches. My pet project lately has been [OpenCV's CVAT](https://benhoff.net/developing-cvat.html). Because CVAT has been blending in Machine Learning into the user interface, it's a cool sell. You can show people the platform itself and the neat things it can do.

I wanted to continue to increase the magicalness of the platform, so I put [$100 on BountySource](https://www.bountysource.com/issues/70724425-intelligent-scissors) against some [intelligent scissors](https://github.com/opencv/cvat/issues/336).

Nobody has bitten off on the project. I'm guessing there's a couple of issues, one of which is that the dollar value is low for the platform. The other of which is I haven't done any marketing. BountySource doesn't seem like a large enough of a platform to drive implementations for that low of a price point. And at least for United States development labor, the cost is probably a bit low. I would guess that patch would take somewhere between 4-32 hours to implement, depending on the developer. That's probably not costing time for setting up a development environment with a new project. Assuming $50/hour, it's quick to see the price delta.
