# pylint: disable=line-too-long
"""
Escriba el codigo que ejecute la accion solicitada.
"""


def pregunta_01():
    """
    El archivo `files//shipping-data.csv` contiene información sobre los envios
    de productos de una empresa. Cree un dashboard estático en HTML que
    permita visualizar los siguientes campos:

    * `Warehouse_block`

    * `Mode_of_Shipment`

    * `Customer_rating`

    * `Weight_in_gms`

    El dashboard generado debe ser similar a este:

    https://github.com/jdvelasq/LAB_matplotlib_dashboard/blob/main/shipping-dashboard-example.png

    Para ello, siga las instrucciones dadas en el siguiente video:

    https://youtu.be/AgbWALiAGVo

    Tenga en cuenta los siguientes cambios respecto al video:

    * El archivo de datos se encuentra en la carpeta `data`.

    * Todos los archivos debe ser creados en la carpeta `docs`.

    * Su código debe crear la carpeta `docs` si no existe.

    """
    if not os.path.exists("docs"):
        os.makedirs("docs")
    data = load_data()
    shipping_per_warehouse(data)
    mode_of_shipment(data)
    average_customer_rating(data)
    weight_distribution(data)

    
import os
import matplotlib.pyplot as plt
import pandas as pd

def load_data():
    df = pd.read_csv('files/input/shipping-data.csv')
    return df


def shipping_per_warehouse(df):
    df = df.copy()
    plt.figure()
    counts = df.Warehouse_block.value_counts()
    counts.plot.bar(
        title="Shipping per Warehouse",
        xlabel="Warehouse block",
        ylabel="Record count",
        color="tab:blue",
        fontsize=8
    )
    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)
    plt.savefig("docs/shipping_per_warehouse.png")


def mode_of_shipment(df):
    df = df.copy()
    plt.figure()
    counts = df.Mode_of_Shipment.value_counts()
    counts.plot.pie(
        title="Mode of shipment",
        wedgeprops=dict(width=0.35),
        ylabel='',
        colors=["tab:blue", "tab:orange", "tab:green"],
    )
    plt.savefig("docs/mode_of_shipment.png")


def average_customer_rating(df: pd.DataFrame):
    df=df.copy()
    plt.figure()
    df = (
        df[["Mode_of_Shipment", "Customer_rating"]].groupby("Mode_of_Shipment").describe()
    )
    df.columns = df.columns.droplevel()
    df = df[["mean", "min", "max"]]
    plt.barh(
        y=df.index.values,
        width=df["max"].values -1,
        left=df["min"].values,
        height=0.9,
        color='lightgray',
        alpha=0.8
    )
    colors = [
        "tab:green" if value >= 3.0 else "tab:orange" for value in df["mean"].values
    ]
    plt.barh(
        y=df.index.values,
        width=df["mean"].values -1,
        left=df["min"].values,
        height=0.5,
        color=colors,
        alpha=1.0
    )
    plt.title("Average Customer Rating")
    plt.savefig("docs/average_customer_rating.png")


def weight_distribution(df: pd.DataFrame):
    df = df.copy()
    plt.figure()
    df.Weight_in_gms.plot.hist(
        title="Shipped weight distribution",
        color = "tab:orange",
        edgecolor="white"
    )
    plt.savefig("docs/weight_distribution.png")

        

if __name__ == '__main__':
    pregunta_01()
