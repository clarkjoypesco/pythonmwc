import media

toy_story = media.Movie('Toy Story',
                        'A Story of a boy with his toys that came to life',
                        'https://upload.wikimedia.org/wikipedia/en/thumb/1/13/Toy_Story.jpg/220px-Toy_Story.jpg',
                        'https://www.youtube.com/watch?v=wmiIUN-7qhE')


#print toy_story.storyline

avatar = media.Movie('Avatar',
                        'A Marine on an Alien Planet',
                        'https://upload.wikimedia.org/wikipedia/en/thumb/b/b0/Avatar-Teaser-Poster.jpg/220px-Avatar-Teaser-Poster.jpg',
                        'https://www.youtube.com/watch?v=6ziBFh3V1aM')


#print avatar.storyline

#avatar.show_trailer()

inkheart = media.Movie('Inkheart',
                        'Mo (Brendan Fraser) and his daughter, Meggie, have the ability to bring storybook characters to life just by reading aloud.',
                        'https://upload.wikimedia.org/wikipedia/en/thumb/3/3d/Inkheartposter.jpg/215px-Inkheartposter.jpg',
                        'https://www.youtube.com/watch?v=6wKm5vU6SSU')


print inkheart.storyline

inkheart.show_trailer()


# New Vocabulary Words
#  - Class
#  - Instance
#  - Constructor
#  - Self
#  - Instance Variables
#  - Instance Method