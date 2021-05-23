from concurrent import futures

import grpc

from proto import stockService_pb2_grpc, stockService_pb2
from services.stock_service import StockService

import yaml

yamlfile = open("config/config.yaml", "r")
yaml_info = yaml.load(yamlfile, Loader=yaml.FullLoader)
port = yaml_info["port"]


class StockServiceServer(stockService_pb2_grpc.StockServiceServicer):

    def __init__(self):
        self.stock_service = StockService()

    def GetProductsFromCountry(self, request, context):
        response = stockService_pb2.GetProductFromCountryPayload()
        products = self.stock_service.get_products_from_country(request.name)
        response.product.extend(products)
        return response


server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
stockService_pb2_grpc.add_StockServiceServicer_to_server(
    StockServiceServer(), server)
print('Starting server. Listening on port {port}.'.format(port=port))
server.add_insecure_port('[::]:{port}'.format(port=port))
server.start()
server.wait_for_termination()
