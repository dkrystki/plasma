# helm delete graylog --purge
# helm install --name graylog {{ kube_config_dir }}/graylog/chart/ --set graylog.passwordSecret=12341243124dfsdf --namespace=graylog
#
# - name: helm test
#   helm:
#     host: 10.233.71.3
#     chart:
#       name: nfs-client-provisioner
#       source:
#         type: repo
#         location: https://kubernetes-charts.storage.googleapis.com
#     state: present
#     name: nfs-provisioner
#     namespace: kube-system
#
#
#  helm install --name sentry -f {{ kube_config_dir }}/sentry/values.yml stable/sentry --namespace=sentry

