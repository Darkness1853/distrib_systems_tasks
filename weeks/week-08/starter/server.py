import grpc
from concurrent import futures
import time
import service_pb2
import service_pb2_grpc

orders_db = {}

class OrdersServiceServicer(service_pb2_grpc.OrdersServiceServicer):
    
    def CreateOrder(self, request, context):
        order = service_pb2.Order(
            id=request.id,
            priority=request.priority
        )
        orders_db[request.id] = order
        print(f"Order created: {order.id}, priority={order.priority}")
        return order
    
    def SubscribeOrders(self, request, context):
        limit = request.limit if request.limit > 0 else len(orders_db)
        count = 0
        for order in orders_db.values():
            if count >= limit:
                break
            yield order
            count += 1

def server():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    service_pb2_grpc.add_OrdersServiceServicer_to_server(
        OrdersServiceServicer(), 
        server
    )
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    server()