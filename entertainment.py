# Importing libraries and files being refered here
import media
import fresh_tomatoes

# Initialising instances of movie class
Lion_King = media.Movie(
    "The Lion King",
    "Naive cub and lion prince Simba is made to believe that he killed his"
    " father, which is why he flees into exile. After several years, Simba"
    " returns to claim the kingdom and overthrow the usurper.",
    "https://upload.wikimedia.org/wikipedia/en/3/3d/The_Lion_King_poster.jpg",
    "https://www.youtube.com/watch?v=8bgK-rahRI0")
Shawshank_redemption = media.Movie(
    "The Shawshank Redemption",
    "Andy Dufresne, a successful banker, is arrested for the murders of his"
    " wife and her lover, and is sentenced to life imprisonment at the Shaws"
    "hankprison. He becomes the most unconventional prisoner.",
    "http://t0.gstatic.com/images?q=tbn:ANd9GcSkmMH-bEDUS2TmK8amBqgIMgrfzN1"
    "_mImChPuMrunA1XjNTSKm",
    "https://www.youtube.com/watch?v=NmzuHjWmXOc")
Imitation_game = media.Movie(
    "The Imitation Game",
    "In 1939, newly created British intelligence agency MI6 recruits Cambri"
    "dge mathematics alumnus Alan Turing (Benedict Cumberbatch) to crack Nazi"
    " codes, including Enigma -- which cryptanalysts had thought unbreakable."
    " Turing's team, including Joan Clarke (Keira Knightley),"
    "analyze Enigma messages while he builds a machine to decipher them."
    " Turing and team finally succeed and become heroes, but in 1952,"
    "the quiet genius encounters disgrace when authorities reveal he is gay"
    "and send him to prison.",
    "https://images-na.ssl-images-amazon.com/images/M/MV5BNDkwNTEyMzkzNl5BMl5"
    "BanBnXkFtZTgwNTAwNzk3MjE@._V1_UY1200_CR90,0,630,1200_AL_.jpg",
    "https://www.youtube.com/watch?v=S5CjKEFb-sM")
Man_infinity = media.Movie(
    "The Man Who Knew Infinity",
    "The story of the life and academic career of the pioneer Indian mathema"
    "tician, Srinivasa Ramanujan, and his friendship with his mentor, Profes"
    "sor G.H. Hardy. ",
    "http://latestmovie720.com/wp-content/uploads/2016/08/The-Man-Who-Knew"
    "-Infinity-Movie-Download-2015-Torrent-DVDRip.jpg",
    "https://www.youtube.com/watch?v=NP0lUqNAw3k")
Theory_everything = media.Movie(
    "The Theory of Everything",
    "A look at the life of renowned scientist Stephen Hawking and his love"
    " affair with Jane. He was diagnosed with the motor neuron disease but"
    " that didn't stop him from becoming a brilliant mind.",
    "https://images-na.ssl-images-amazon.com/images/M/MV5BMTAwMTU4MDA3NDNeQ"
    "TJeQWpwZ15BbWU4MDk4NTMxNTIx._V1_UY1200_CR90,0,630,1200_AL_.jpg",
    "https://www.youtube.com/watch?v=Salz7uGp72c")
ZNMD = media.Movie(
    "Zindagi Na Milegi Dobara",
    "Friends Kabir, Imran and Arjun take a vacation in Spain before Kabir's"
    " marriage. The trip turns into an opportunity to mend fences, heal wounds,"
    "fall in love with life and combat their worst fears",
    "http://pre08.deviantart.net/d465/th/pre/f/2011/174/8/4/znmd_poster_4_by_met"
    "alraj-d3jqxyr.jpg",
    "https://www.youtube.com/watch?v=bQR_bxragHk")


# Creating a list with the object names(movie names)
movies=[Lion_King,Imitation_game,Man_infinity,Theory_everything,Shawshank_redemption,ZNMD]

# Calling open_movies_page that takes a list with movie objects as input and creates a movie website out of it
fresh_tomatoes.open_movies_page(movies)

