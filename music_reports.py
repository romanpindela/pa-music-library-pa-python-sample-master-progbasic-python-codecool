artist_id = 0
album_id = 1
year_id = 2
genre_id = 3
time_id = 4

def get_albums_by_genre(albums, genre):
    """
    Get albums by genre

    :param list albums: albums' data
    :param str genre: genre to filter by

    :returns: all albums of given genre
    :rtype: list
    """
    genre_albums = [album for album in albums if album[genre_id] == genre]
    return genre_albums



def get_longest_album(albums):
    pass
    """
    Get album with biggest value in length field.
    If there are more than one such album return the first (by original lists' order)

    :param list albums: albums' data
    :returns: longest album
    :rtype: list
    """
    longest_album = albums[0]
    for album in albums:
        if to_time(album) > to_time(longest_album):
            longest_album = album
    return longest_album

def to_time(album) -> int:
    minutes, seconds = album[time_id].split(":")
    return int(minutes)*60 + int(seconds)

def get_total_albums_length(albums):
    """
    Get sum of lengths of all albums in minutes, rounded to 2 decimal places
    Example: 3:51 + 5:20 = 9.18
    :param list albums: albums' data
    :returns: total albums' length in minutes
    :rtype: float
    """
    sum_of_seconds = 0
    for album in albums:
        sum_of_seconds += to_time(album[time_id])

    minutes = round((sum_of_seconds / 60),2)
    return minutes

def get_genre_stats(albums):
    genre_stats = {}
    for album in albums:
        if album[genre_id] in genre_stats:
            genre_stats[album[genre_id]] = genre_stats[album[genre_id]] + 1
        else:
            genre_stats[album[genre_id]] = 1
    return genre_stats

def get_oldest_album(albums):
    oldest_album = albums[0]
    for album in albums:
        if int(album[year_id]) <= int(oldest_album[year_id]):
            oldest_album = album
    return oldest_album

def get_oldest_of_genre(albums, genre):
    genres_album = [album for album in albums if album[genre_id] == genre]
    return get_oldest_album(genres_album)



def get_last_oldest(albums):
    pass

def get_last_oldest_of_genre(albums, genre):
    pass

def get_total_albums_length(albums):
    pass

def get_albums_by_year(albums, year):
    return [album for album in albums if album[year_id] == year]
