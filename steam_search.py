# pyright: basic
"""Print info of matched game for Steam searches in input (".steam <query>").

Steal from: https://gist.github.com/GermainZ/1a992ab4192adbe80280

Dependencies
============

- `python-requests <http://python-requests.org>`_

Usage:
======

.. code:: console

    python steam_search.py '<input>'

Example:
========

.. code:: console

    python steam_search.py 'dota'
"""

import sys

import requests
from requests.exceptions import RequestException

from tabulate import tabulate


STORE_URL = "http://store.steampowered.com/app/{}/"
STOREFRONT_API_URL = (
    "http://store.steampowered.com/api/storesearch/?term={}&l=english&cc=US"
)


def get_results(text):
    query = text.strip()

    try:
        response = requests.get(STOREFRONT_API_URL.format(query))
    except RequestException:
        return None
    if not response:
        return None
    results = response.json()
    if not results["items"]:
        return 'No results found for "{}".'.format(query)
    output = []
    for game in results["items"]:
        name = game["name"]
        if not "price" in game:
            price = "Free!"
        else:
            price = "${}".format(game["price"]["final"] / 100)
            discount = int(
                (game["price"]["initial"] - game["price"]["final"])
                / game["price"]["initial"]
                * 100
            )
            if discount:
                price = "{} [-{}%]".format(price, discount)
        platforms = []
        for platform, supported in game["platforms"].items():
            if supported:
                platforms.append(platform.capitalize())
        platforms = ", ".join(platforms)
        url = STORE_URL.format(game["id"])
        output.append([name, price, platforms, url])

    return output


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(__doc__)
        sys.exit(1)
    result = get_results(sys.argv[1])
    if result:
        print(
            tabulate(
                result,
                ["Name", "Price", "Platforms", "url"],
                tablefmt="rounded_outline",
            )
        )
