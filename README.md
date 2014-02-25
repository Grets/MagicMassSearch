MagicMassSearch
===============

Magic Mass Search


A simple python program that allows the user to check if a large number of cards fit a certain search criteria on magiccards.info.

The program is easy enough to use with two input parameters: a file of card names and search parameters for magiccards.info

The file of card names can be in the format of tappedout export as a txt file or simply a list of line seperated cards in a text file

The search paramters should be in the form of the URL of the search on magiccards.info. For example, if I want to search for which cards in the list have promo versions available, I would search 'is:promo' on magiccards.info which produces the URL 'http://magiccards.info/query?q=is%3Apromo&v=card&s=cname' which I would copy into the program in the parameters box

The 'Search for Matches' button becomes available once a file has been selected and clicking the button begins the search which will open a new window with a list of the cards that match the search.
