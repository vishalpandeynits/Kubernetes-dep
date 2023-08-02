# deploy postgres application
kubectl apply -f kubernetes/postgres/deployment-kub.yaml
kubectl apply -f kubernetes/postgres/services-kub.yaml

# deploy postgres application
kubectl apply -f kubernetes/redis/deployment-kub.yaml
kubectl apply -f kubernetes/redis/services-kub.yaml

#deploy backend application
kubectl apply -f kubernetes/backend-app/deployment-kub.yaml
kubectl apply -f kubernetes/backend-app/services-kub.yaml
