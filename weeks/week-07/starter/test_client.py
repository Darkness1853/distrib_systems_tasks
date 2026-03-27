import grpc
import service_pb2
import service_pb2_grpc

# Подключаемся к серверу
channel = grpc.insecure_channel('localhost:50051')
stub = service_pb2_grpc.ProductsServiceStub(channel)

# Создаем продукт
response = stub.CreateProduct(
    service_pb2.CreateProductRequest(
        id="product-001",
        price=99.99
    )
)

print(f"Продукт создан!")
print(f"ID: {response.id}")
print(f"Price: {response.price}")