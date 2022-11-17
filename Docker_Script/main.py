import random
import requests
from bs4 import BeautifulSoup

url = "https://www.imdb.com/chart/top"


def main():
    response = requests.api.get(url)
    html = response.text

    soup = BeautifulSoup(html, 'html.parser')
    movietags = soup.select('td.titleColumn')
    inner_movietags = soup.select('td.titleColumn a')
    rating_tags = soup.select('td.posterColumn span[name=ir]')

    def get_year(movie_tag):
        moviesplit = movie_tag.text.split()
        year = moviesplit[-1]
        return year

    years = [get_year(tag) for tag in movietags]
    actors_list = [tag['title'] for tag in inner_movietags]
    titles = [tag.text for tag in inner_movietags]
    ratings = [f'{float(tag["data-value"]):.1f}' for tag in rating_tags]

    n_movies = len(titles)

    while True:
        idx = random.randrange(0, n_movies)
        print(
            f'{titles[idx]} {years[idx]}, rating: {ratings[idx]}, starring: {actors_list[idx]}')

        if input('do you want another movie (y/n)? ') != 'y':
            break

    # idx = random.randrange(0, n_movies)
    # print(
    #     f'{titles[idx]} {years[idx]}, rating: {ratings[idx]}, starring: {actors_list[idx]}')


if __name__ == '__main__':
    main()
