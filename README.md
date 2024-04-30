# Integrantes
- Alberto Lizana
- Diego Escobar
- Wladimir Rojas
---
---
<br>
<br>


# Apis disponibles
Previamente ejecutar script de productos y categorías
## Curls para registrarse y obtener token
- Creación de usuario

```url
curl --location 'http://127.0.0.1:8000/usuario/registro/' \
--header 'Content-Type: application/json' \
--header 'Cookie: csrftoken=taCki7xcTkCj58upmtlm8k6x7wLoE1Tx' \
--data-raw '{
    "username": "profesor",
    "password": "12345",
    "first_name": "profe",
    "last_name": "web",
    "email": "profe-web@gmail.com"
}'
```

- Obtener token

```url
curl --location 'http://127.0.0.1:8000/usuario/inicio/' \
--header 'Content-Type: application/json' \
--header 'Cookie: csrftoken=taCki7xcTkCj58upmtlm8k6x7wLoE1Tx' \
--data '{
    "username": "profesor",
    "password": "12345"
}'
```
---
---

## Curls para probar apis (Ingresar token obtenido anteriormente)

```url
curl --location 'localhost:8000/api/categorias' \
--header 'Authorization: token {ingresar token}'
```

```url
curl --location 'localhost:8000/api/productos' \
--header 'Authorization: token {ingresar token}'
```
