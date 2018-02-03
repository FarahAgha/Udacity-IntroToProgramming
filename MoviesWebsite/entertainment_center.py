import media
import fresh_tomatoes

the_female_brain = media.Movie("The Female Brain",
                "http://t3.gstatic.com/images?q=tbn:ANd9GcSfUl9c60Gz-lgPK9fwA6mvFFwxa6l_nZCCjDat1pB7934m8Vt2",
                "https://www.youtube.com/watch?v=BxYsQFPvPns",
                "What makes a woman swipe right for Mr. Wrong and left for Mr. Right? This simultaneously entertaining and enlightening comedy",
                "Whitney Cummings",
                "Whitney Cummings, Neal Brennan",
                "February 9, 2018",
                "2h 5min",
                "Comedy")

gringo = media.Movie("Gringo",
                "https://shyfyy.files.wordpress.com/2017/12/gringo-1.jpg",
                "https://www.youtube.com/watch?v=MnKbM9Zxtn8",
                "GRINGO, a dark comedy mixed with white-knuckle action and dramatic intrigue, explores the battle of survival for businessman Harold Soyinka (David Oyelowo) when he finds himself crossing the line from law-abiding citizen to wanted criminal. ",
                "Anthony Tambakis, Matthew Stone",
                "Nash Edgerton",
                "March 9, 2018",
                "1h 50min",
                "Action | Comedy | Drama")

ant_man_and_the_wasp = media.Movie("Ant-Man and the Wasp",
                "http://media.comicbook.com/2017/07/ant-man-and-the-wasp-sdcc-1011742.jpg",
                "https://www.youtube.com/watch?v=8_rTIAOohas",
                " In the aftermath of 'Captain America: Civil War,' Scott Lang grapples with the consequences of his choices as both a Super Hero and a father. As he struggles to re-balance his home life with his responsibilities as Ant-Man",
                "Paul Rudd, Erik Sommers, Chris McKenna, Andrew Barrer, Gabriel Ferrari",
                "Peyton Reed",
                "July 6, 2018",
                "2h 14min",
                "Action | Adventure | Sci-Fi")
thor_ragnarok = media.Movie("Thor: Ragnarok",
                "http://www.joblo.com/posters/images/full/Thor-Ragnarok-international-poster-1-large.jpg",
                "https://www.youtube.com/watch?v=ue80QwXMRHg",
                "Thor is imprisoned on the other side of the universe and finds himself in a race against time to get back to Asgard to stop Ragnarok, the destruction of his homeworld and the end of Asgardian civilization, at the hands of an all-powerful new threat, the ruthless Hela."
                "Eric Pearson, Craig Kyle",
                "Taika Waititi",
                "3 November 2017",
                "2h 10min",
                "Action, Adventure",
                "Comedy")
kingsman_golden_circle = media.Movie("Kingsman: The Golden Circle",
                "https://image.tmdb.org/t/p/original/pKESfn2Pdy0b7drvZHQb7UzgqoY.jpg",
                "https://www.youtube.com/watch?v=6Nxc-3WpMbg",
                "After the Kingsman headquarters are blown up by a psychotic criminal named Poppy Adams, the surviving agents find their way to an allied secret organisation based in Kentucky, named Statesman. The two agencies must now work together in order to save the world and take down the so called 'Golden Circle'.",
                "Jane Goldman, Matthew Vaughn",
                "Matthew Vaughn",
                "22 September 2017",
                "2h 21min",
                "Action | Adventure | Comedy")
big_sick = media.Movie("The Big Sick",
                "https://www.wgaeast.org/wp-content/uploads/2017/10/Big-Sick-Poster.jpg",
                "https://www.youtube.com/watch?v=PJmpSMRQhhs",
                "Kumail (Kumail Nanjiani), in the middle of becoming a budding stand-up comedian, meets Emily (Zoe Kazan). Meanwhile, a sudden illness sets in forcing Emily to be put into a medically-induced coma. Kumail must navigate being a comedian, dealing with tragic illness, and placating his family's desire to let them fix him up with a spouse, while contemplating and figuring out who he really is and what he truly believes ",
                "Emily V. Gordon, Kumail Nanjiani ",
                "Michael Showalter",
                "14 July 2017 ",
                "2h 21min",
                "Comedy | Drama | Romance")

# ant_man_and_the_wasp.print_movie_info()
# gringo.print_movie_info()
# the_female_brain.print_movie_info()
# thor_ragnarok.print_movie_info()
# kingsman_golden_circle.print_movie_info()
# big_sick.print_movie_info()

movies = [the_female_brain, gringo, ant_man_and_the_wasp, thor_ragnarok, kingsman_golden_circle, big_sick]
fresh_tomatoes.open_movies_page(movies)
