Sample project for Certificate Transparency monitoring with Faust
===================================

This repo contains a sample Faust project to stream Certificate Transparancy data. This is not a project you can use as is, but rather an example of using Faust for your own usecases.

## Testing / Running 
The repository contains a Docker compose file to setup a minimal Kafka infrastructure (single node). You can start Kafka by using the 'docker-compose up -d' command. When you installed the dependencies in the requirements file, you can run the Faust project via 'faust -A streaming.app worker' command. The agents will start monitoring for new certificates and print any changes per source. The certificates will be pushed to the ct-certs topic. You can connect your own agents to perform analysis or use the PassiveTotal API I included with this repo to perform enrichement.

## Source
Calidog and creators of CertStream (used their awesome writeup and decoders): https://certstream.calidog.io
Faust documentation: https://faust.readthedocs.io/en/latest/