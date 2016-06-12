import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
	"A story of a boy and his toys that come to life",
	"http://img.lum.dolimg.com/v1/images/open-uri20150422-20810-m8zzyx_5670999f.jpeg?region=0,0,300,450",
	"https://www.youtube.com/watch?v=azyK_k52R1w")

# print toy_story.storyline

avatar = media.Movie("Avatar",
	"A marine on an alien planet",
	"https://resizing.flixster.com/PIhRpOR9nW85stswkSet-W-np_w=/800x1200/v1.bTsxMTE3Njc5MjtqOzE3MDU2OzIwNDg7ODAwOzEyMDA",
	"https://www.youtube.com/watch?v=cRdxXPV9GNQ")
# print avatar.storyline

warcraft = media.Movie("Warcraft",
	"Gul'dan is satan",
	"http://cdn1-www.comingsoon.net/assets/uploads/gallery/warcraft-1387407720/warcraft_ver8_xlg.jpg",
	"https://www.youtube.com/watch?v=RhFMIRuHAL4")
# warcraft.show_trailer()

captain_america = media.Movie("Captain America: Civil War",
	"But he's my friend --so was I",
	"http://www.hindustantimes.com/rf/image_size_640x362/HT/p2/2015/11/25/Pictures/_86d7c35a-9345-11e5-ae0b-6bb83fa8865b.jpg",
	"https://www.youtube.com/watch?v=dKrVegVI0Us")

the_notebook = media.Movie("The Notebook",
	"What do you want?",
	"http://sev.h-cdn.co/assets/15/31/1438124471-the-notebook-2004-copy.jpg",
	"https://www.youtube.com/watch?v=S3G3fILPQAU")

movies = [toy_story, avatar, warcraft, captain_america, the_notebook]
fresh_tomatoes.open_movies_page(movies)

print media.Movie.VALID_RATINGS
print media.Movie.__doc__