# Correr
Para ejecutar el comando es necesario tener docker y docker compose instalado

```bash
docker-compose up - d
```

Esto ejecutara el proyecto en el puerto 8043
podras ver la doc de los endpoints en
http://localhost:8043/tusdatos/docs

### Ejecutar consultas en paralelo
luego de tener el server corriendo
```bash
sh do_bulk.bash
```

Luego de haber añadido info ya sea por bash o directamente desde la doc en swagger puedes consultar los endpoint
