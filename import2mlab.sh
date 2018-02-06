 ls -1 *.json | while read jsonfile; do mongoimport -h ds125368.mlab.com:25368 -d reciperecommender-recipes -c recipes -u komin -p K0mino11 --file $jsonfile ; done
