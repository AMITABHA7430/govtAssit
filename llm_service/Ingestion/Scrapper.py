# import requests
# from bs4 import BeautifulSoup

# # url = "https://wb.gov.in/government-schemes-details-aadhaar-enrolment-and-seeding.aspx"
# url = "https://wb.gov.in/government-schemes-details-agriculture-infrastructure-fund.aspx"

# response = requests.get(
#     url,
#     headers={
#         "User-Agent": "Mozilla/5.0"
#     }
# )

# soup = BeautifulSoup(response.text, "html.parser")


# specs = soup.find_all("div", class_="col-md-12 col-sm-12 col-xs-12")

# print()
# print(specs[1].text)

import asyncio
import aiohttp
from bs4 import BeautifulSoup


async def scrape(session, url):

    async with session.get(url) as response:

        html = await response.text()

        soup = BeautifulSoup(html, "html.parser")

        for tag in soup([
            "script",
            "style",
            "noscript",
            "nav",
            "footer",
            "header"
        ]):
            tag.decompose()

        text = soup.get_text("\n", strip=True)

        return {
            "url": url,
            "text": text
        }

async def main():

    urls = [
        "https://wb.gov.in/government-schemes-details-aadhaar-enrolment-and-seeding.aspx",
        "https://wb.gov.in/government-schemes-details-agriculture-infrastructure-fund.aspx",
        "https://assam.gov.in/scheme-page/526",
    ]

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    async with aiohttp.ClientSession(headers=headers) as session:

        tasks = [
            scrape(session, url)
            for url in urls
        ]

        results = await asyncio.gather(
            *tasks,
            return_exceptions=True
        )

    for result in results:

        if isinstance(result, Exception):
            print("ERROR:", result)
            continue

        print(result["url"])
        print(result["text"])
        print("-----------------------------------------------")


asyncio.run(main())