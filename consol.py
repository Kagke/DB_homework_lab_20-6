import pdb
from models.album import Album
from models.artist import Artist

import repositories.album_repository as album_repository
import repositories.artist_repository as artist_repository

album_repository.delete_all()
artist_repository.delete_all()

artist1 = Artist("Metro")
artist_repository.save(artist1)
# artist_repository.select_with_id(artist1)

artist2 = Artist("Khaled")
artist_repository.save(artist2)

album1 = Album("Heroes and Vilains" , "R&B" , artist1)
album_repository.save(album1)

album2 = Album("We The Best" , 'R&B' , artist2)
album_repository.save(album2)

album_repository.select_all()
artist_repository.select_all()

pdb.set_trace()
