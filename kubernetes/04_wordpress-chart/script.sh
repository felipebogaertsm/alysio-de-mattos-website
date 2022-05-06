helm repo add bitnami https://charts.bitnami.com/bitnami
helm install -n alysio-dm -f kubernetes/04_wordpress-chart/chart-values.yaml alysio-de-mattos-website bitnami/wordpress