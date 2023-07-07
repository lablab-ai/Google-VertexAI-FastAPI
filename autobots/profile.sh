#!/bin/bash
# Bash file useed to switch google cloud & Kubectl user probile
echo 'This switches Gcloud & kubectl profile'
echo 'Please hold on while context is set'
#kubectl config use-context gke_cointailing_europe-west3-c_cointailing-cluster
# // Todo add correct context
echo 'Listing current context'
kubectl config current-context
echo 'Setting Gcloud configuration'
gcloud config configurations activate cointailing
echo 'Gcloud config is now set to:'
echo '############################################################'
gcloud config configurations list
echo '############################################################'
wait
echo 'And Kubenets Pods loaded:'
echo '############################################################'
kubectl get pods
echo '############################################################'
wait
echo 'Now, go change the world'