"""
Parsing the data from the file and add it to the database.
"""

# open the file u.data
# read each file, row by row.
# split the file by the delimeter ("|")
# First element: movie title
# Second element:
def seed_data(file_name):
    """

    :param file_name: Txt
    :return: Table
    """

    movie_data=open(file_name)
    for row in movie_data:
        mt,rd,nr,imdb_url=row.split("|")
