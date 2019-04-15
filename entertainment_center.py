import media
import fresh_tomatoes
# New Vocabulary Words
#  - Class
#  - Instance
#  - Constructor
#  - Self
#  - Instance Variables
#  - Instance Method


toy_story = media.Movie('Toy Story',
                        '2 Hours',
                        'A Story of a boy with his toys that came to life',
                        'https://upload.wikimedia.org/wikipedia/en/thumb/1/13/Toy_Story.jpg/220px-Toy_Story.jpg',
                        'https://www.youtube.com/watch?v=wmiIUN-7qhE')


#print toy_story.storyline

avatar = media.Movie('Avatar',
                        '1.5 Hours',
                        'A Marine on an Alien Planet',
                        'https://upload.wikimedia.org/wikipedia/en/thumb/b/b0/Avatar-Teaser-Poster.jpg/220px-Avatar-Teaser-Poster.jpg',
                        'https://www.youtube.com/watch?v=6ziBFh3V1aM')


#print avatar.storyline

#avatar.show_trailer()

inkheart = media.Movie('Inkheart',
                        '1.5 Hours',
                        'Mo (Brendan Fraser) and his daughter, Meggie, have the ability to bring storybook characters to life just by reading aloud.',
                        'https://upload.wikimedia.org/wikipedia/en/thumb/3/3d/Inkheartposter.jpg/215px-Inkheartposter.jpg',
                        'https://www.youtube.com/watch?v=6wKm5vU6SSU')

harry_potter = media.Movie('Harry Potter',
                        '1.5 Hours',
                        'a boy who learns on his eleventh birthday that he is the orphaned son of two powerful wizards and possesses unique magical powers of his own.',
                        'https://timedotcom.files.wordpress.com/2014/07/301386_full1.jpg',
                        'https://www.youtube.com/watch?v=VyHV0BRtdxo')

kung_fu_hustle = media.Movie('Kung Fu Hustle',
                        '1.5 Hours',
                        'A petty thief aspires to become a member of the notorious Axe Gang during the 1940s in Canton, China.',
                        'https://static.rogerebert.com/uploads/movie/movie_poster/kung-fu-hustle-2005/large_vSKFcFZ7Asvt9rON0glLD8FCKMU.jpg',
                        'https://www.youtube.com/watch?v=-m3IB7N_PRk')


dragon_nest = media.Movie('Dragon Nest',
                        '1.5 Hours',
                        'A young warrior joins a group of dragon slayers to battle a legendary serpent.',
                        'http://www.gstatic.com/tv/thumb/v22vodart/13075619/p13075619_v_v8_aa.jpg',
                        'https://www.youtube.com/watch?v=vbkA4a5N-Hc')

#print inkheart.storyline

#inkheart.show_trailer()
movies = [toy_story,avatar,inkheart,harry_potter,kung_fu_hustle,dragon_nest]
#fresh_tomatoes.open_movies_page(movies)
#print media.Movie.VALID_RATINGS
#print media.Movie.__doc__

