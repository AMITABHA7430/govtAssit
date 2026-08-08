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

    specs = soup.find_all("div", class_="col-md-12 col-sm-12 col-xs-12")
    return soup.get_text(" ", strip=True)




async def main():
    urls = [
        "https://wb.gov.in/government-schemes-details-aadhaar-enrolment-and-seeding.aspx",
        # "https://assam.gov.in/scheme-page/526"
        "https://wb.gov.in/government-schemes-details-agriculture-infrastructure-fund.aspx"
    ]

    async with aiohttp.ClientSession() as session:
        tasks = []

        for url in urls:
            task = scrape(session, url)
            tasks.append(task)

        results = await asyncio.gather(*tasks)

    for result in results:
        print(result)
        print("-----------------------------------------------")


asyncio.run(main())