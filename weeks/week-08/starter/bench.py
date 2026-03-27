import time
import requests
import grpc
import service_pb2
import service_pb2_grpc

def run_rest_bench():
    print("Starting REST benchmark...")
    start = time.time()
    for _ in range(1000):
        requests.get("http://localhost:8122/api/orders")
    end = time.time()
    print(f"REST: {end - start:.4f} sec")

def run_grpc_bench():
    print("Starting gRPC benchmark...")
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = service_pb2_grpc.OrdersServiceStub(channel)

        for i in range(100):
            stub.CreateOrder(service_pb2.CreateOrderRequest(id=f"order-{i}", priority=i % 5))
        
        start = time.time()
        for _ in range(1000):
            response = stub.SubscribeOrders(service_pb2.SubscribeOrdersRequest(limit=1))
            list(response)
        end = time.time()
        print(f"gRPC: {end - start:.4f} sec")
    pass

def test_streaming():
    print("\nTEST streaming")
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = service_pb2_grpc.OrdersServiceStub(channel)
        responses = stub.SubscribeOrders(service_pb2.SubscribeOrdersRequest(limit=1))
        count = 0
        for order in responses:
            count += 1
            print(f"Заказ: {order.id}, приоритет={order.priority}")
        print(f"Получено {count} заказов")


if __name__ == "__main__":
    run_rest_bench()
    run_grpc_bench()
    test_streaming()
