for i in {1..15}
do
    curl -X POST http://localhost:8043/tusdatos/get-data/demandante \
    -H 'Content-Type: application/json' \
    -d '{"numeroCausa":"","actor":{"cedulaActor":"1791251237001","nombreActor":""},"demandado":{"cedulaDemandado":"","nombreDemandado":""},"provincia":"","numeroFiscalia":"","recaptcha":""}' \
    & # This puts the process in the background to allow the next one to start immediately.
done
