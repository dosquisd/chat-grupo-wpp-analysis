# WhatsApp Chat Analysis

Pues, nada. Realmente es un repositorio bastante personal, son los chats de un grupo que tenemos varios amigos, incluyéndome. Me pareció bastante curioso realizar un análisis a todo nuestro chat, casualmente, el grupo lleva poco más de 1 año.

Si soy honesto conmigo mismo, al principio les presenté la idea (y en las conversaciones se ve), y les gustó, hasta me emocioné por cómo habían reaccionado, pero ahora que les quería hacer parte del proceso, me di cuenta que realmente no les interesa, simplemente quieren los resultados, supongo que si no es "parche" o vainas de esas, no va con ellos.

Me postulé para hacer esto por curiosidad genuina, y lo seguiré haciendo por lo mismo, pero es verdad que me molestó un poco si soy sincero conmigo mismo. Y, bueno, no está mal que no les interese tampoco, no puedo esperar que la gente tenga los mismos gustos que yo, aunque sí se siente un tanto feo la verdad. Me pone a pensar un poco acerca de mis acciones, ¿será que he hecho lo mismo alguna vez? No sé, pero no me resentiré para siempre por aquello, solo evitaré realizarlo yo también.

No obstante, fuera de mi descontento, espero pueda salir algo interesante! Tengo bastantes ganas y cada que pienso más en el tema, se me ocurren más ideas. Quizás este análisis (o intento de), pueda servir a otros grupos, únicamente bastaría con cambiar el grupo o chat a analizar -¿hay mucha diferencia entre chat grupal y personal?.

## Ideas

No tengo un lugar claro para dejar las ideas del proyecto, por lo que, pienso que quizás aquí quizás lo sea. Este será una especie de mural con las ideas que se me ocurran para analizar. Aunque, por ahora, únicamente tengo lo básico, tengo la esperanza que se me ocurran más ideas a fúturo, así que colocaré lo básico por mientras.

* Línea de tiempo de mensajes en el chat (ver los mensajes generales como por cada miembro). Aunque, no necesariamente deba ser una línea, puede ser un diagrama de barras perfectamente también... o ambas.
* Media de mensajes por día/mes (general, como por cada miembro).
* Relacionado a los mensajes, se está hablando de manera general, pero podría ser interesante, ver quiénes mandan más audios/videos/stickers y así también.
* Ahora, relacionado con análisis de sentimiento, se puede analizar la tonalidad de los mensajes, e inclusive, audios y stickers (vídeos no, porque no tienen audio), aunque me tocaría investigar bastante respecto a este último.
* Palabras por mensaje. Y, con respecto a las palabras, se pueden sacar métricas descriptivas en base a las palabras, y no solo con mensajes.

Eso es todo hasta el momento, tengo la esperanza de que el muro de ideas vaya creciendo cada vez más, pero esa es la versión inicial

## Estructura

Antes de seguir con la estructura, debo decir que el proyecto utiliza uv como manejador paquetes en Python, así que es ideal instalarlo antes de seguir.

Ahora, todavía no se tiene nada claramente estructurado, solamente tengo claro que lo que se utilizará es Jupyter Notebook para hace todo el análisis. Los archivos tendrán la siguiente nomenclatura: `num_description.ipynb`, el `num` sería un número que indica el orden de creación de los archivos, junto a una pequeña descripción `description` para decir qué se hace a grandes rasgos. Así, pienso que se organizaría todo correctamente.

Seguramente, durante el proceso, sea necesario guardar archivos, por lo que, se utilizará la carpeta [data/analysis](./data/analysis/) para guardar los archivos necesarios (ver [aquí](./data/analysis/README.md)).
