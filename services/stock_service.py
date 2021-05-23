from utils.csv_reader import CsvReader

from proto import stockService_pb2


class StockService:

    def __init__(self):
        path = 'data/products'
        self.csv_reader = CsvReader(path)

    def get_products_from_country(self, country):
        products = []
        for row in self.csv_reader.data:
            if row["country"] == country:
                product = stockService_pb2.Product(name=row["name"], price=row["price"], count=row["count"])
                products.append(product)
        return products
