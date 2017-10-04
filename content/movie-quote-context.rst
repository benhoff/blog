#################################################
Creating a Bot that Quotes Pop Culture in Context
#################################################


:date: 2017-10-04 06:15
:category: Random
:slug: movie-quotes-in-context
:summary: Working with Reddit comments and machine learning to get movie quote context


So I'm interested in creating a bot that could quote movie quotes back to your in a context that makes sense. I don't know how your conversations with your buddies go, but 70% of our everyday conversation is quoting things in new and different contexts, so I was interested to see if I could collect enough data to do this with some common quotes.

The first part of any good machine learning project is to collect data. I read `that OpenAI was using Reddit comments`_ to learn language, so I figured I'd use Reddit as a source. Live data seemed to be the most interesting way to pull data out.

The problem is that I've vastly overestimated (apparently) how much people quote famous movie quotes. I left the program running overnight and instead of having 100's of matches, I only had one. So I'll have to figure out a different way to get data out.

From a technology standpoint, this was a relatively easy problem to solve. I'm using `PRAW`_, the Python Reddit API wrapper to get comments out. I wanted some flexibility for spelling, so I ended up using the `Levenshtein algorithim`_ from the `python-Levenshtien`_ package. There's probably a better algo to do this, see `this stackoverflow post`_ about that issue, but Levenshtien was good enough for a proof of concept.

The plan was to grab all of the parent comment's text if there was a match that was good close to any of the my movie quotes. But like I said, there's not enough data being returned from grabbing live comments to make this feasible. 

I ran this in tmux on a digital ocean instance I have running for 12 hours. You could also have this write to a file as well. I turned off the similarity matching and have just been watching the raw text come in while I write this post.

Man, that 'Remind me!' bot is popular.

.. code-block:: python

    import praw
    from Levenshtein import ratio

    config = {'client_id': ''
              'client_secret': '',
              'password': '',
              'username': ''}

    # quotes is a list of string
    quotes = []
    USER_AGENT = 'Movie Quote Bot by /u/beohoff'
    reddit = praw.Reddit(client_id=config['client_id'],
                         client_secret=config['client_secret'],
                         password=config['password'],
                         username=config['username'],
                         user_agent=USER_AGENT)

    for quote in quotes:
        quote_len = len(quote)
        if quote_len > greatest_length:
            greatest_length = quote_len
        if quote_len < least_length:
            least_length = quote_len


    for comment in reddit.subreddit('AskReddit+movies+funny+pics').stream.comments():
        text = comment.body.lower()
        len_text = len(text)
        if len_text + 7 > greatest_length or len_text - 4 < least_length:
            continue

        greatest = 0
        best_quote = ''

        for quote in quotes:
            value = ratio(text, quote)
            if value > .75:
                print(text, quote)


Guess it's back to the drawing board for how to get enough data to create a bot that can respond in context with movie quotes.

.. _`that OpenAI was using Reddit comments`: http://www.zmescience.com/science/reddit-supercomp-59815/
.. _`PRAW`: https://praw.readthedocs.io/en/latest/
.. _`this stackoverflow post`: https://stackoverflow.com/questions/3338889/how-to-find-similar-results-and-sort-by-similarity
.. _`Levenshtein algorithim`: https://en.wikipedia.org/wiki/Levenshtein_distance
.. _`python-Levenshtien`: https://github.com/ztane/python-Levenshtein/
