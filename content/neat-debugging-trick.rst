##########################################
Dealing with Deeply Nested Data Structures
##########################################

:date: 2017-10-05 10:24
:category: Random 
:slug: interactive-debugging-methods
:summary: Showcasing a neat way to explore deeply nested data structures


Working with deeply nested data structures is a pain. Sometimes the easiest way to figure out the control structure to get the data that you want is to play around with the data the `REPL`_. My problem is comes from an API, it's a pain to figure out how to quickly evaluate the structure, make lasting changes to the script, and then jump back into figuring out the structure. In the past, I've sucked it up and used the REPL, I've written scripts and eval'd integrated the data one change at a time using `print`, and occasionally, I'll use jupyter-notebook. None of these solutions seemed to be very good though.

I still haven't figured out a great way, but yesterday when working with json data from Reddit, the thought occurred to me that I might be able to jump straight into the REPL and just pass in the scope that I was working in. I'd seen this done in the `irc3`_ code, but I couldn't figure out how that would be useful at the high level that it was done at (basically interrogating the final `bot` instance).

Sure enough, you can definitely do it. Using the `interact` method from the `code` module.

.. code-block:: python

  from code import interact


  # some expensive calls here to get....
  # ...a deeply nested data structures
  data = [[{}, {}, {}], [{}, {}], [{}, {}, {}, {}]]
  for value in data:
      for deeper_value in value:
          interact(locals())

Dropping into the REPL like this gives me the ability to query `deeper_value` interactively. This is often useful when dealing with JSON to figure out what keys are available.

.. _`REPL`: https://en.wikipedia.org/wiki/Read%E2%80%93eval%E2%80%93print_loop
.. _`irc3`: https://github.com/gawel/irc3
