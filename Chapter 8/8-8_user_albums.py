def make_album(album_title,author_name,song_no=None):
    if song_no:
        album = {"author's name" : author_name.title(),
             'album title' : album_title.title(),
             'number of songs' : song_no 
            }
    else:
        album = {"author's name" : author_name.title(),
                'album title' : album_title.title()  
            }
    return album

while True:
    name = input("Enter the name of the author \n(enter q to quit any time) ")
    if name == 'q':
        break
    title = input('Enter the title of the album ')
    if title == 'q':
        break
    print(make_album(title,name))