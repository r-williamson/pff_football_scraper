import json
import requests
from bs4 import BeautifulSoup, NavigableString
import re
import csv
import pandas as pd


# TODO: implement a loop to scrape all NFL team summary pages, or let user choose the team


def scrape_intro_page():
    team = "clt"
    url = f"https://www.pro-football-reference.com/teams/{team}/index.htm"  # Scrapes IND Colts PFF summary page
    headers = {'User-Agent': 'Mozilla/5.0 '
                             '(Windows NT 10.0; Win64; x64) '
                             'AppleWebKit/537.36 (KHTML, like Gecko) '
                             'Chrome/110.0.0.0 Safari/537.36'}
    try:
        res = requests.get(url, headers=headers)
    except requests.exceptions.RequestException as e:
        print(e)
        exit()

    soup = BeautifulSoup(res.text, "html.parser")

    # Scrape Team Info Summary at top of page
    team_info_soup = soup.find(id="info")
    page_title = team_info_soup.div.h1.text.replace("\n", " ").strip()
    summary_html = team_info_soup.div.find_all("p")

    franchise_summary = []
    stat_dict = {}
    for item in summary_html[2:]:
        stat = re.sub("[\n\t]", "", item.text).split(":")
        stat_dict[stat[0]] = stat[1]
        # stat_dict = {stat[0]: stat[1]}
    franchise_summary.append(stat_dict)

    # Scrape Franchise Retired Numbers
    retired_nums_soup = soup.find(class_="uni_holder pfr section")
    retired_nums = []
    for item in retired_nums_soup:
        if type(item) is not NavigableString:
            player_info = {'name': item.attrs['data-tip'], 'number': item.svg.text}
            retired_nums.append(player_info)

    # Scrape Team Records, Leaders, and League Ranks
    table_soup = soup.find(id="team_index").tbody
    franchise_stats = []
    for row in table_soup:
        if type(row) is not NavigableString:
            if len(row.th["class"]) > 1:  # filler rows have multiple CSS classes declared for col heads and are skipped
                continue
            # year_stats = []
            year_stats = {}
            for col in row:
                if type(col) is not NavigableString:
                    stat = col.attrs['data-stat']
                    val = col.text
                    col_dict = {stat: val}
                    # year_stats.append(col_dict)
                    year_stats[stat] = val

            franchise_stats.append(year_stats)

    result = {"Page": page_title,
              "Summary": franchise_summary,
              "Retired Numbers": retired_nums,
              "Franchise Stats": franchise_stats
              }

    return result


if __name__ == "__main__":
    intro_page = scrape_intro_page()

    # data as pandas df:
    df = pd.DataFrame.from_dict(intro_page['Franchise Stats'])
    df.set_index('year_id', inplace=True)
    print(df)

    # dump to json
    with open('result.json', 'w') as file:
        json.dump(intro_page, file)
