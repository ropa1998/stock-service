# open a gRPC channel
import grpc

from proto import stockService_pb2_grpc, stockService_pb2


channel = grpc.insecure_channel('localhost:40041')

# create a stub (client)
stub = stockService_pb2_grpc.StockServiceStub(channel)

# create a valid request message
country = stockService_pb2.Country(name="Argentina")

# make the call
response = stub.GetProductsFromCountry(country)

# et voilà
print(response)
