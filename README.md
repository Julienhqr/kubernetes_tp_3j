# kubernetes_tp_3j
Projet Kubernetes

-------

## Comment taguer une image et pousser cette image vers Dockerhub ?

#### API NEST :

* 1 - Il faut se rendre dans le dossier /backend/api-nestjs puis exécuter les commandes suivantes :

* 2 - ```docker build -t api-nest-kube .```

* 3 - ```docker image tag api-nest-kube <pseudo_dockerhub>/api-nest-kube``` Sans les <>

* 4 - ```docker image push <pseudo_dockerhub>/api-nest-kube```