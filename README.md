# utn-docker

UTN FRBA 
CURSO DOCKER Y KUBERNETES
Profesor: Marcos Tonina
Actividad integradora Docker

Repositorio dedicado al curso Docker &amp; Kubernetes dictado en UTN cursado a fines del 2024.

Tecnologías utilizadas:
Flask (Python es mi lenguaje principal de uso, dada mi participación en varios proyectos de Ciencia de Datos o desarrollo de ETLs)

El servidor puede recibir 2 http request
Desde el host, apuntando a “localhost:8000” retorna:

“Debe enviar un HTTP request ‘curl -X GET http://localhost:8000’”
Y apuntando a “localhost:8000?ABC=123” retorna:
“XYZ”

BUILD
Desde el Dockerfile:
docker buildx build -t utn-docker:0.1 .
(si estás parado en /app dentro del repo, sino tenés que apuntar el PATH en donde está el .)
Luego:
docker run -p 8000:8000 utn-docker:0.1
Desde el docker-compose:
docker compose up -d
(si estás parado en /app dentro del repo)

El repositorio con los archivos y esta misma descripción puede encontrarlo en:
