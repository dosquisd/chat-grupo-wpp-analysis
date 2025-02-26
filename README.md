# WhatsApp Chat Analysis

Pues, nada. Realmente es un repositorio bastante personal, son los chats de un grupo que tenemos varios amigos, incluyéndome. Me pareció bastante curioso realizar un análisis a todo nuestro chat, casualmente, el grupo lleva poco más de 1 año.

## Ideas

No tengo un lugar claro para dejar las ideas del proyecto, por lo que, pienso que quizás aquí quizás lo sea. Este será una especie de mural con las ideas que se me ocurran para analizar. Aunque, por ahora, únicamente tengo lo básico, tengo la esperanza que se me ocurran más ideas a fúturo, así que colocaré lo básico por mientras.

* Línea de tiempo de mensajes en el chat (ver los mensajes generales como por cada miembro). Aunque, no necesariamente deba ser una línea, puede ser un diagrama de barras perfectamente también... o ambas.
* Media de mensajes por día/mes (general, como por cada miembro).
* Relacionado a los mensajes, se está hablando de manera general, pero podría ser interesante, ver quiénes mandan más audios/videos/stickers y así también.
* Ahora, relacionado con análisis de sentimiento, se puede analizar la tonalidad de los mensajes, e inclusive, audios y stickers (vídeos no, porque no tienen audio), aunque me tocaría investigar bastante respecto a este último.
* Palabras por mensaje. Y, con respecto a las palabras, se pueden sacar métricas descriptivas en base a las palabras, y no solo con mensajes.
* Nube de palabras.

Eso es todo hasta el momento, tengo la esperanza de que el muro de ideas vaya creciendo cada vez más, pero esa es la versión inicial

## Estructura

Antes de seguir con la estructura, debo decir que el proyecto utiliza uv como manejador paquetes en Python, así que es ideal instalarlo antes de seguir.

Ahora, todavía no se tiene nada claramente estructurado, solamente tengo claro que lo que se utilizará es Jupyter Notebook para hace todo el análisis. Los archivos tendrán la siguiente nomenclatura: `num_description.ipynb`, el `num` sería un número que indica el orden de creación de los archivos, junto a una pequeña descripción `description` para decir qué se hace a grandes rasgos. Así, pienso que se organizaría todo correctamente.

Los siguientes archivos que listaré, son para realizar un análisis general obtenidos de exportar el chat, aún quedan pendiente más cosas, como integrar los audios (transcribir)

* [001_take_messages.ipynb](./001_take_messages.ipynb). Se toman los mensajes que fueron enviados por los participantes del chat, excluye mensajes generados automáticamente por WhatsApp: cuando se agregan/eliminan usuarios, cuando se creó el grupo y mensajes de MetaAI. Luego de tomar los mensajes, se exporta a un nuevo archivo de texto
* [002_create_dataframe.ipynb](./002_create_dataframe.ipynb). Con el chat anteriormente creado, se crea un DataFrame ("excel" en lenguaje mortal) con los mensajes de cada participante y con features extras: tipo de mensaje (mensaje, archivo, encuesta o ubicación), el mensaje, y se indica si el mensaje fue editado, eliminado, llama a MetaAI o era para una vez. El archivo también es exportado en un archivo .csv (excel pero chiquito).
* [003_plots_for_messages.ipynb](./003_plots_for_messages.ipynb) & [004_plots_for_words.ipynb](./004_plots_for_words.ipynb). Realmente, son el mismo código, por lo que, es necesario crear funciones para evitar el duplicado de código, pero eso es otro tema. En esencia, lo que se hace en ambos es graficar el historial mensajes y palabras, respectivamente. Se calculan algunas métricas extra, como el promedio, pero aún es muy general. En este punto del proceso, estoy en una fase exploratoria, aún falta mucho por hacer, pero iré poco a poco.
* [005_plots_for_extra_features.ipynb](./005_plots_for_extra_features.ipynb). Muy parecido al anterior inciso, pero aquí lo que se grafica con extras caracteristicas que se obtuvieron. De nuevo, se hace en general y luego para cada partcicipante.

Hasta el momento, como dije, todo muy exploratorio.
