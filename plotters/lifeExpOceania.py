import seaborn.objects as so
from gapminder import gapminder


def plot():
    return (
        so.Plot(
            gapminder[gapminder.continent == "Oceania"],
            x="year",
            y="lifeExp",
            color="country",
        )
        .add(so.Line())
        .label(
            title="Expectativa de vida en Oceanía",
            x="Año",
            y="Expectativa de vida",
            color="País",
        )
    )
