import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story",
						"A Story of a boy and his toys that come to life",
						"https://en.wikipedia.org/wiki/Toy_Story#/media/File:Toy_Story.jpg",
						"https://www.youtube.com/watch?v=KYz2wyBy3kc")


avatar = media.Movie("Avatar",
					  "A marine on a alien planet",
					  "https://en.wikipedia.org/wiki/Avatar_(2009_film)#/media/File:Avatar-Teaser-Poster.jpg",
					  "https://www.youtube.com/watch?v=5PSNL1qE6VY")

movies = [toy_story, avatar]
fresh_tomatoes.open_movies_page(movies)