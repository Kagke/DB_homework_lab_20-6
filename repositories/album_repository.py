from db.run_sql import run_sql

from models.album import Album

import repositories.artist_repository as artist_repository

def save(album):
    sql = "INSERT INTO albums (title , genre , artist_id) VALUES (%s , %s , %s) RETURNING *"
    values = [album.title , album.genre , album.artist_id.id ]
    results = run_sql(sql, values)
    print(results)
    id = results[0]
    album.id = id
    return album


def select_all():
    albums = []

    sql = "SELECT * FROM albums"
    results = run_sql(sql)

    for row in results:
        artist = artist_repository.select_with_id(row['artist_id'])
        album = Album(row['title'],row ['genre'], row['id'] , artist.id)
        albums.append(album)
    return albums


def select_with_id(id):
    album = None
    sql = "SELECT * FROM albums WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    if results:
        result = results[0]
        artist = artist_repository(result['artist_id'])
        album = Album(result['title'],result['genre'] ,result['id'], artist)

    return album


def delete_all():
    sql = "DELETE  FROM albums"
    run_sql(sql)


def delete(id):
    sql = "DELETE  FROM albums WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(album):
    sql = "UPDATE albums SET (title, genre , artist , id) = (%s, %s ,%s , %s) WHERE id = %s"
    values = [ album.title, album.genre ,  album.id ,album.artist.id ]
    run_sql(sql, values)

def album_to_artist(artist):
    albums=[]
    sql = "SELECT * FROM albums WHERE artist_id = %s"
    values=[artist.id]
    result = run_sql(sql , values)
    for row in result:
        album = Album(row['title'], row['genre'], row['id'] ,artist)
        albums.append(album)
    return albums