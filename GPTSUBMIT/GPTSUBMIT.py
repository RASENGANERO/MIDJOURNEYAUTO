import random
import string
import html
import logging
from bs4 import BeautifulSoup
import pandas as pd
from pprint import pprint
logging.basicConfig(level=30)

import nodriver as uc

df = pd.read_excel('data.xlsx', usecols=[4])
words = df.iloc[:, 0].tolist()


async def checkes(cont):
    decoded_html = html.unescape(str(cont[-1]))
    soup = BeautifulSoup(decoded_html, 'html.parser')
    text = soup.get_text()
    return str(text)
    

async def remove(val):
    df1 = pd.read_excel('data.xlsx')
    column_index = 4
    df1 = df1[df1.iloc[:, column_index] != val]
    df1.to_excel('data.xlsx', index=False)

async def main():
    try:
        driver = await uc.start()

        gtp = await driver.get("https://chatgpt.com/")

        await gtp.sleep(5)

        login = await gtp.select("button[data-testid=login-button]")

        await login.click()

        await gtp.sleep(3)

        email = await gtp.select("input[type=email]")

        await email.send_keys("seocomputer777@gmail.com")

        cont = await gtp.select("button[class=continue-btn]")

        await cont.click()

        password = await gtp.select("input[type=password]")

        await password.send_keys("eJdcixBuHYoU")

        await gtp.sleep(2)

        vhod = await gtp.select("button[type=submit]")

        await vhod.click()

        await gtp.sleep(3)

        textarea = await gtp.select("textarea[id=prompt-textarea]")

        send = await gtp.select("button[data-testid=fruitjuice-send-button]")
    
        sk=True

        for word in words:
            word = word.strip()
            await textarea.send_keys(word)
            await send.click()
            await gtp.sleep(59)
            elems=await gtp.select_all(".prose")
            s=await checkes(elems)
            if any(msg in s for msg in ["I'm sorry, I can't assist with that request.",
                             "I'm unable to generate the requested text at the moment.",
                             "I apologize for the inconvenience, but I'm unable to fulfill your request",
                             "I'm sorry, but I can't assist with generating or writing long texts or HTML content"]):
                sk=False
                break
            else:
                await remove(word)
        if sk==False:
            driver.stop()
            await main()
    except Exception:
        driver.stop()
        await main()

if __name__ == "__main__":
    uc.loop().run_until_complete(main())
