DURATION="30s"

for c in 10 100 1000; do
    echo "Connections: $c"
    echo "REST:"
    wrk -t2 -c$c -d$DURATION "http://localhost:8197/api/events?limit=500" 2>&1 | grep -E "Requests/sec|Latency"
    echo "gRPC:"
    ghz --insecure --proto events.proto --call events.v1.EventsService/ListEvents -d '{"limit": 500}' -c $c -z $DURATION 0.0.0.0:50051 2>&1 | grep -E "Requests/sec|Average"
done