# deploy postgres application
kubectl apply -f kubernetes/postgres.yaml

# deploy postgres application
kubectl apply -f kubernetes/redis.yaml

#deploy backend application
kubectl apply -f kubernetes/backend.yaml
