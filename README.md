# ENCRIPTACIÓN DE ARCHIVOS

1) Agregamos los archivos a encriptar en la carpeta `data`
2) Ejecutamos el siguiente comando

    ```
    sudo bash start.sh
    ```
3) Se crearan dos archivos más por cada archivo agregado en la carpeta `data`. Uno es el archivo encriptado ubicado en la carpeta `encryteds` y el otro archivo es el key ubicado en `decrypteds` necesario para desencriptar el archivo mencionado anteriormente.


> :warning: **Guardado de archivos generados**: Tener en cuenta que se debe guardar en distintos lugarles los dos archivos generados a partir del archivo a encriptar.

## Herramientas

- Docker
- Imagen Python
- Libreria de Python cryptography