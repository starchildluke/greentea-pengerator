# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "marimo",
# ]
# ///

import marimo

__generated_with = "0.15.3"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import random
    return mo, random


@app.cell
def _(mo):
    mo.md(
        f"""
    # Greentea Pengerator

    ## This notebook has one simple function: make a name out of a type of tea.

    Inspired by Greentea Peng, I thought it'd be fun to randomise some teas and synonyms for words meaning "attractive" and invent a new R&B artist name.

    Click the **Boil the kettle** button below to generate a new name.
    """
    )
    return


@app.cell
def _(mo):
    generate = mo.ui.run_button(
        label=f"{mo.icon('mdi:kettle-steam')} Boil the kettle!"
    )

    generate
    return (generate,)


@app.cell
def _(mo):
    mo.md(r"""---""")
    return


@app.cell
def _():
    teas = ["Green tea", "Chun Mee", "Chun Lu", "Bi Luo Chun", "Gunpowder", "Maofeng", "Yellow", "Jasmine", "Anji Bai Cha", "Maojian", "Taiping Houkui", "Jin Shan", "Longjing", "Sejak", "Ujeon", "Jungjak", "Daejak", "Sencha", "Gyokuro", "Kabusecha", "Tencha", "Matcha", "Mecha", "Shincha", "Hojicha", "Kukicha", "Bancha", "Genmaicha", "Konacha", "Kamairicha", "Tamaryokucha", "Black tea", "Assam", "English Breakfast", "Earl Grey", "Darjeeling", "Rukeri", "Pu-Erh", "Scottish Afternoon", "Irish Breakfast", "Milima", "Ceylon", "Chai", "Panyang Congou", "Keemun", "Lapsang Souchong", "Golden Tips", "Temi Sikkim", "Nimbu", "Wakuocha", "White tea", "Silver Needle", "White Peony", "Shou Mei", "Gong Mei", "Darjeeling White", "Oolong tea", "Da Hong Pao", "Shui Jin Gui", "Tie Luo Han", "Shui Xian", "Bai Jiguan", "Tieguanyin", "Mi Lan Xiang Dan Con", "Ancient Tree Dan Cong", "Guan Yin", "Dancong", "Cassia", "Da Yu Lin", "Dong Ding", "Dong Fang Meiren", "Alishan", "Pouchong", "Ruan Zhi", "Jin Xuan", "Li Shan", "Herbal tea", "Avocado Leaf", "Bamboo", "Butterfly Pea Flower", "Chaga Mushroom", "Chamomile", "Lavender", "Liquorice", "Guayusa", "Honeysuckle Flower", "Lemon", "Mint", "Olive Leaves", "Hibiscus", "Rooibos", "Turmeric", "Pumpkin Spice", "Chrysanthemum", "Buckwheat", "Honeybush", "Bush", "Mamaki", "Yerba mate"]

    adjectives = ["beautiful", "bonny", "cute", "drop-dead", "fetching", "gorgeous", "handsome", "knockout", "pretty", "ravishing", "stunning", "buff", "peng", "chung", "hot", "fine", "sexy"]
    return adjectives, teas


@app.cell
def _(adjectives, generate, mo, random, teas):
    mo.stop(not generate.value)

    first_name = random.choice(teas).replace(' ', '').capitalize()
    surname = random.choice(adjectives).capitalize()

    mo.md(f"""
        ## {first_name} {surname}
    """)
    return


if __name__ == "__main__":
    app.run()
