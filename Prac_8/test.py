from operator import itemgetter


def main():
    movies = get_movie_list()


def get_movie_list():
    # print("test loading movies")
    # MovieCollection.load_movies('movies.csv')
    # print(MovieCollection.movies)
    # assert MovieCollection.movies

    file = open("movies.csv", "r")
    movies = []
    for line in file:
        sections = line.strip().split(',')
        if sections[3] == "u":
            movies.append([sections[0], int(sections[1]), sections[2], False])
        else:
            movies.append([sections[0], int(sections[1]), sections[2], True])
    file.close()
    return movies


def list_formatting(files):
    count_false = 0
    count_true = 0
    files.sort(key=itemgetter(1))
    for num, movieSections in enumerate(files):
        if movieSections[3]:
            print("{}.    {:40} - {:2} ({:5})".format(num, movieSections[0], int(movieSections[1]), movieSections[2]))
            count_false += 1
        else:
            print("{}. *  {:40} - {:2} ({:5})".format(num, movieSections[0], int(movieSections[1]), movieSections[2]))
            count_true += 1
    if count_true == 0:
        print("No more movies to watch")
    else:
        print("{} movies watched, {} movies still to watch".format(count_false, count_true))
    return ""


main()
