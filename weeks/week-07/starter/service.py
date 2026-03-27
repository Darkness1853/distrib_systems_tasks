import grpc
from concurrent import futures
# Импортируйте сгенерированные модули
import service_pb2
import service_pb2_grpc

product_db = {}

class ProductServiceImplementation(service_pb2_grpc.ProductsServiceServicer): # Унаследуйтесь от сгенерированного Servicer
    
    def CreateProduct(self, request, context):
        product = service_pb2.Product(
            id=request.id,
            price=request.price
        )
        product_db[request.id] = product
        
        print(f"Product: ID={product.id}, Price={product.price}")
        
        return product

def server():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    service_pb2_grpc.add_ProductsServiceServicer_to_server(ProductServiceImplementation(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    server()
