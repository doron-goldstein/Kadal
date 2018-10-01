Kadal
=====

Kadal is an async wrapper for the `Anilist <https://anilist.co/>`_ API.

This wrapper is compatible with Python 3.5+.
Kadal is compatible with python's standard `asyncio <https://docs.python.org/3/library/asyncio.html>`_ or `trio <https://github.com/python-trio/trio>`_ / `curio <https://github.com/dabeaz/curio>`_ through `multio <https://github.com/theelous3/multio>`_.

Documentation to be added soon.

This wrapper is aimed at ease of use and an object-oriented style, and stays as true as possible to the `anilist API v2 <https://github.com/AniList/ApiV2-GraphQL-Docs>`_.

Installation
------------

Kadal is available through pip:
::

    pip install -U kadal


Example
-------

.. code-block:: python3

    import multio
    import kadal
    
    multio.init("curio")  # tell multio which async lib to use

    async def main():
        k = kadal.Client()  # Create a new Client instance
        
        anime = await k.search_anime("rezero")  # search for an anime by title
        # alternatively, you can use an id with k.get_anime(id)
        
        print("Anime title: {}".format(anime.title))  # Print the title of the Anime

    multio.run(main())  # run main using multio (in this case, directing to curio)

Prints:
::

    Anime title: Re:Zero kara Hajimeru Isekai Seikatsu
