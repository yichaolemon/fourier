#!/bin/bash

docker run -dit -p 8080:80 -v "$PWD"/public-html:/usr/local/apache2/htdocs -v "$PWD"/cgi-bin:/usr/local/apache2/cgi-bin simulations
