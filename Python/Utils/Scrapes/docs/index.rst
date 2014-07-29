.. Scrapes documentation master file, created by
   sphinx-quickstart on Tue Jul 29 13:20:35 2014.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Scrapes's documentation!
===================================

Contents:

.. toctree::
   :maxdepth: 2

Installing
----------

Install **Scrapes** with
``pip install scrapes``.

Usage
-----

A session of::

    import scrapes

    with scrapes.Itzamna() as agent:
        agent.get("http://www.example.com")

and voila!

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

