# Stock-Service
A small service to simulate a product catalog, made with grpc and python
 
 ## Build proto files
 
The proto files are already generated, if stockService.proto is modified these files need to be regenerated

```bash
python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. proto/stockService.proto --experimental_allow_proto3_optional
 ```
