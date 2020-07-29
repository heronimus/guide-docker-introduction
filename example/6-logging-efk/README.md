# Guide: EFK with Docker-compose

In this guide, we will create EFK (Elastic Fluentd Kibana) logging for services that run with docker-compose.

A brief intro about EFK:
  - Elasticsearch: function as database, store the logs.
  - Fluentd: as log collector and aggregator, forward logs from apps to elasticsearch.
  - Kibana: dashboard for visualizing logs info.

------------------------------------------

In this guide, we will separate the docker-compose to run the EFK stack and docker-compose to run web services that produce logs to EFK.

  - The EFK stack will run as fully container with the official images from elastics and fluentd.
  - On the fluentd images we need to custom build the image to include elasticsearch-plugin for fluentd and provide fluentd configuration.
  - Elasticsearch container will run as "single-node" only.

  - Run EFK stack:

        docker-compose -f docker-compose-EFK.yml


  - "Web" docker-compose file will contain regular app services, but with additional logging option using fluentd driver.

  - Run Web stack:

        docker-compose -f docker-compose-WEB.yml


  - Now that both EFK stack and your "Web" stack already run, open kibana at your port 5601.
  - On the Kibana dashboard, setup the `index name or pattern`. Go to **Management** --> **Kibana-Index Patterns** --> **Create Index Patterns** --> Specify `fluentd-*` to Index pattern, next select `@timestamp` for time filtering and click **Create**.
  - Now on the Kibana dashboard, go to **"Discover"** and you will see your log from container.
  
Reference:
https://github.com/digikin/fluentd-elastic-kibana
https://docs.fluentd.org/container-deployment/docker-compose
