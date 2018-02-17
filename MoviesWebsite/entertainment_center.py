import media
import fresh_tomatoes

# A data for movies
the_female_brain = media.Movie("The Female Brain",
                "http://t3.gstatic.com/images?q=tbn:ANd9GcSfUl9c60Gz-lgPK9fwA6mvFFwxa6l_nZCCjDat1pB7934m8Vt2",
                "https://www.youtube.com/watch?v=BxYsQFPvPns")

gringo = media.Movie("Gringo",
                "https://shyfyy.files.wordpress.com/2017/12/gringo-1.jpg",
                "https://www.youtube.com/watch?v=MnKbM9Zxtn8")

ant_man_and_the_wasp = media.Movie("Ant-Man and the Wasp",
                "http://media.comicbook.com/2017/07/ant-man-and-the-wasp-sdcc-1011742.jpg",
                "https://www.youtube.com/watch?v=8_rTIAOohas")
thor_ragnarok = media.Movie("Thor: Ragnarok",
                "http://www.joblo.com/posters/images/full/Thor-Ragnarok-international-poster-1-large.jpg",
                "https://www.youtube.com/watch?v=ue80QwXMRHg")
kingsman_golden_circle = media.Movie("Kingsman: The Golden Circle",
                "https://image.tmdb.org/t/p/original/pKESfn2Pdy0b7drvZHQb7UzgqoY.jpg",
                "https://www.youtube.com/watch?v=6Nxc-3WpMbg")
big_sick = media.Movie("The Big Sick",
                "https://www.wgaeast.org/wp-content/uploads/2017/10/Big-Sick-Poster.jpg",
                "https://www.youtube.com/watch?v=PJmpSMRQhhs")

avengers_no_surrender= media.Movie("Avengers No Surrender",
                "http://www.anenglishmaninsandiego.com/wp-content/uploads/2017/11/AVENGERS_680_CVR-666x1024.jpg",
                "https://www.youtube.com/watch?v=iBy8UdG3VOo")

black_panther = media.Movie("Black Panther",
                "https://www.clovertheater.com/wp-content/uploads/2018/01/black-panther-hr-poster.jpg",
                "https://www.youtube.com/watch?v=xjDjIWPwcPU")

avengers_infinity_war = media.Movie("Avengers Infinity War",
                "https://static1.squarespace.com/static/51b3dc8ee4b051b96ceb10de/t/5a837b5ae2c483e436e4d198/1518566242734/new-promo-poster-art-for-avengers-infinity-war-brings-all-the-heroes-together1?format=750w",
                "https://www.youtube.com/watch?v=8_rTIAOohas")

incredibles_2 = media.Movie("Incredibles 2",
                "https://images-na.ssl-images-amazon.com/images/I/71uRfcuYBXL._SY445_.jpg",
                "https://www.youtube.com/watch?v=YBpdL9hSac4&list=PLTnR43JTLNs86dljbrWWsenxrw977AGch")

coco = media.Movie("Coco",
                "https://images-na.ssl-images-amazon.com/images/I/81FZFvGhSVL._SY550_.jpg",
                "https://www.youtube.com/watch?v=Rvr68u6k5sI")
sanjays_super_team = media.Movie("Sanjay's Super Team",
                "https://vignette.wikia.nocookie.net/pixar/images/4/41/Sanjay%27s_Super_Team_poster_2.jpg/revision/latest?cb=20151025151607",
                "https://www.youtube.com/watch?v=fOZXU4EUOPE")

#an array from the already defined data 
movies = [the_female_brain, gringo, ant_man_and_the_wasp, thor_ragnarok, kingsman_golden_circle, big_sick,avengers_no_surrender, black_panther, avengers_infinity_war, incredibles_2 , coco, sanjays_super_team]

# To display data on a web browser
fresh_tomatoes.open_movies_page(movies)
