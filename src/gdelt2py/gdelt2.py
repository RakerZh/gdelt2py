import aiohttp
import glob
import os
import pandas as pd
from zipfile import ZipFile
import analyzer
import asyncio
import time

# from .. import analyzer 

async def unzip_file(filename,data_dir):
    """
    unzip the file
    """

    with ZipFile(f"{filename}.zip") as z:
        z.extractall(f"{data_dir}")
        # z.namelist()[0]
    os.remove(f"{filename}.zip")
    return

async def download(url, session):

  async with session.get(url) as reponse:
        if reponse.status != 200:
            return None
        return await reponse.read()

async def download_and_unzip_file(url,session,date,data_dir):
    """
    download url
    """
    file_content = await download(url, session)

    if file_content is None:
        print(f"Failed to download {url}")
        return

    with open(f"{date}.zip", "wb") as f:
        print(url[37:], " file downloaded! Ready to unzip!")
        f.write(file_content)

        # TODO: await unzip file and processing in the same date

        await unzip_file(date,data_dir)

async def download_and_process_files(urls,date,data_dir):
    """
    download urls within one date

    """
    async with aiohttp.ClientSession() as session:
        for url in urls:
            await download_and_unzip_file(url,session,date,data_dir)


class Gdelt2():
    def __init__(self, start_date="20221120", end_date="20221220", themes=None, country_list=None,
                 mode=None, data_dir="./data/"):
        self.start_date = start_date
        self.end_date = end_date
        self.themes = themes
        self.country_list = country_list
        self.analyzer = analyzer.Analyzer()
        self.mode = mode
        self.data_dir = data_dir

    def optional(self,themes,locations):
        self.analyzer.filtered_optional(themes,locations)

    def required(self,themes,locations):
        self.analyzer.filtered(themes,locations)

    async def download_with_dates(self,start_date,end_date,analyzer):
        """
        run Gdeltr2 download process with dates
        """

        df = pd.read_csv("../../gkg_data.csv")
        df['date'] = pd.to_datetime(df['date'])

        start_date = pd.Timestamp(start_date)
        end_date = pd.Timestamp(end_date)

        print(f"Gdelt2py Running...... \n Dates: {start_date} to {end_date}." )

        filter = (df['date'] >= start_date) & (df['date'] <= end_date)
        df_data = df[filter]

        count = 1
        urls = []
        url_date = df_data.iloc[0].at['date']
        date_searched = url_date.strftime("%Y%m%d")
        file_list = glob.glob(f"{date_searched}")
        print(file_list)

        data_dir = self.data_dir
        for i, row in enumerate(df_data.itertuples()):
            if url_date != row[2]:
                # download files in the same date
                await download_and_process_files(urls,row[2],data_dir)

                # process files in the same date
                date_searched = url_date.strftime("%Y%m%d")
                file_list=glob.glob(f"{data_dir}{date_searched}*.csv")
                analyzer.file_list(file_list)
                analyzer.to_csv()

                count += 1
                urls = []

            url_date = row[2]
            urls.append(row[1])

        date_searched = url_date.strftime("%Y%m%d")
        file_list     = glob.glob(f"{date_searched}*.csv")
        analyzer.file_list(file_list)
        analyzer.to_csv()

    def download_files(self):
        asyncio.run(self.download_with_dates(self.start_date,self.end_date,self.analyzer))

# gd = Gdelt2()
# gd.download_files()
