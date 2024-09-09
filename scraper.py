import requests
from bs4 import BeautifulSoup
import csv
import time
from datetime import datetime

def scrape_and_save():
    url = "https://www.bna.com.ar/Personas"
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")

        # Encontramos todas las filas <tr> que contienen la información de interés
        rows = soup.find_all("tr")

        # Obtenemos la hora actual para el nombre del archivo
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"exchange/exchange_rates_{timestamp}.csv"

        # Definimos el archivo CSV con la hora exacta
        with open(filename, mode="w", newline='', encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["Moneda", "Compra", "Venta"])  # Encabezados del CSV

            for row in rows:
                cols = row.find_all("td", class_="tit")
                if cols:
                    currency = cols[0].text.strip()
                    compra = row.find_all("td")[1].text.strip()
                    venta = row.find_all("td")[2].text.strip()
                    writer.writerow([currency, compra, venta])
        
        print(f"Datos guardados en {filename}")
    else:
        print(f"Error al obtener la página. Código de estado: {response.status_code}")

# Ejecutar el script cada segundo
while True:
    scrape_and_save()
    time.sleep(1)
