from bs4 import BeautifulSoup
from urllib2 import urlopen


def main():
    print "Welcome, we are going to output information about Game oh Thrones."
    # i var is for season number
    i_season = 0
    viewers_total = 0
    url = urlopen("https://en.wikipedia.org/wiki/Game_of_Thrones").read()
    soup = BeautifulSoup(url, "html.parser")
    table = soup.find("table", class_="wikitable plainrowheaders")
    # Reading rows of the table
    table_rows = table.find_all("tr")
    for tr in table_rows:
        # looking for table headers on each row
        th = tr.find_all("th", attrs={"scope": "row"})
        # don't take NoneType Values
        if len(th) > 0:
            for head in th:
                i_season +=1
                # looking for links of each table header
                link = head.find("a").get("href")
                # adding each season viewers to total
                viewers_total += second_url(link, i_season)
    print "Totally, there were: " + str(viewers_total) + " viewers"


def second_url(href, i_season):
    season_viewers = 0
    # entering to each Wikipedia url GoT season
    season_url = "https://en.wikipedia.org" + href
    season_url_opened = urlopen(season_url).read()
    season_soup = BeautifulSoup(season_url_opened, "html.parser")
    episode_table = season_soup.find("table", class_="wikitable plainrowheaders wikiepisodetable")
    # looking for episodes table
    table_rows = episode_table.find_all("tr", class_="vevent")
    for row in table_rows:
        # looking for the specific child and later search parent
        # because there are 6 same tags without class.
        aux = row.find_all("sup", class_="reference")
        if len(aux) > 0:
            for td in aux:
                # here i am looking for the parent
                number = td.find_parent("td").text
                # catching only the 4 characters that we need
                numbers = float(number[0:4])
                # adding each  episode viewers number to the count
                season_viewers += numbers
    print "In season " + str(i_season) + " has been: " + str(season_viewers) + " viewers"
    return season_viewers


if __name__ == '__main__':
    main()
