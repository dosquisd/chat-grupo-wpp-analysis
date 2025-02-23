# Data

## Whatsapp Data

Cuando se exporta un chat de Wpp, está la opción de incluir media o no, cuando se exporta con media, se incluyen todos los archivos: audios, videos, stickers, mensajes, archivos enviados en el chat, etc; La organización de las carpetas aquí, está hecho de la siguiente manera.

``` bash
.
├── analysis
├── README.md
└── whatsapp
    ├── audios
    │   ├── files
    │   ├── forwarded
    │   └── sent
    ├── contacts
    ├── extra
    ├── folders.json
    ├── images
    │   ├── sent
    │   └── stickers
    └── videos
```

No es una manera general de repartir los archivos que son exportados, depende mucho de cada chat, sin embargo, puede ser propenso a cambios utilizando el archivo [folders.json](./whatsapp/folders.json).

## Analysis Data

No hay esquema claro de archivos.
