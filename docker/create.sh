docker build -t reoc:gateway -f gateway.dockerfile .
docker build -t reoc:test -f test.dockerfile .
docker build -t reoc:burst -f burst.dockerfile .