helm repo add bitnami https://charts.bitnami.com/bitnami
helm install -n alysio-dm -f chart-values.yaml alysio-de-mattos-website bitnami/wordpress