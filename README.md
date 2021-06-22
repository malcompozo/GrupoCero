# Front-End para Colectivo Artístico Grupo Cero

**Desarrollo:**

- Nicolás Cañete
- Manuel Diaz
- Jonathan Pacheco
- Malcom Pozo

### Versión en línea https://lloni.github.io/ColectivoGrupoCero/

### Mockup https://www.figma.com/file/YTjEC09Ws9IZYppsA9QzQ1/CGC?node-id=2%3A17231

_______________________

[Antecedentes del caso](#_Toc69509275)

[Caso de uso](#_Toc69509276)

[Wireframe](#_Toc69509277)

[Mockup](#_Toc69509278)

[Decisiones de diseño](#_Toc69509279)

________________________


# Antecedentes del caso

Un grupo de artistas plásticos dedicados a la pintura, escultura, orfebrería, tejido y otras expresiones artísticas, miembros del colectivo &quot;Grupo Cero&quot; han manifestado la necesidad de crear una página web para exhibir sus trabajos, y eventualmente implementar una tienda on-line.

Tras una reunión con el grupo, se identificaron los siguientes requerimientos para el sitio web:

1. La página web debe tener un menú en la parte superior con el logo de la cooperativa.

2. En la página principal deben aparecer los productos más destacados en un carrusel de imágenes.

3. Al hacer clic en una de las imágenes, se debe poder entrar a ver el detalle del objeto (historia, descripción, nombre, precio, técnica usada, etc) y la galería de fotos si es que tiene. Los artículos el menos poseen una foto.

4. Además de la galería, la página principal deberá tener una opción de búsqueda por nombre del artista o por tipo de arte o por concepto.

5. También deberá mostrar la cantidad de productos que han sido ingresados por un usuario.

6. Es necesario tener un formulario de contacto general.

7. Desde la página principal se puede acceder a los productos por categoría o por artista.

8. Los usuarios deberían poder registrarse, sólo es necesario el email, el nombre y la contraseña.

9. El usuario debería tener la opción de autenticarse en el sitio mediante email y password.

10. Se debe mostrar si el usuario se ha logueado o no.

11. El proceso para agregar nuevas obras es el siguiente:

    a. Cada integrante de la cooperativa posee una cuenta creada por el administrador del sitio.

    b. Una vez que el integrante ingresa al sitio (email y password), puede publicar la obra que quiere vender llenando todos los datos en el formulario dispuesto para esto.

    c. La obra no se publica en la página hasta que pasa por el visto bueno del administrador, el cual puede rechazar la publicación por mala redacción o faltas de ortografía o porque las imágenes son de mala calidad.

    d. Si el administrador rechaza la publicación, debe informar por qué lo hizo y el integrante de la cooperativa visualizará esta información en el momento en que ingrese a la plataforma.

12. No se considera aún el proceso de venta directa al público desde la plataforma, sino que sólo la publicación de las obras para ser exhibidas on-line.

13. Es fundamental que la página sea responsiva y que se adapte tanto a pantallas grandes como a pantallas de dispositivos móviles.


# Caso de uso

A partir de los requerimientos especificados por el cliente, se determinaron las siguientes funcionalidades del sistema en un caso de uso general:

![Caso de uso](documentacion/caso.png)

# Wireframe

Tras una etapa de benchmarking y análisis de tendencias de diseño en rubros similares, consideramos la siguiente propuesta de arquitectura de información, con la que se busca dar preponderancia a los contenidos destacados por el cliente durante la reunión inicial:

![Wireframe](documentacion/wireframe.jpeg)

# Mockup

Tras la revisión y análisis de la propuesta de arquitectura de la información, en conjunto con el cliente se determinó el siguiente Mockup como guía para la implementación del sitio en HTML/CSS/JS:

![Mockup](documentacion/mockup.png)

Para revisar el documento en detalle en línea, se ha puesto a disposición el siguiente enlace:

[https://www.figma.com/file/YTjEC09Ws9IZYppsA9QzQ1/CGC?node-id=2%3A17231](https://www.figma.com/file/YTjEC09Ws9IZYppsA9QzQ1/CGC?node-id=2%3A17231)

# Decisiones de diseño

Buscando conjugar una estética moderna con valores propios de la marca (creatividad, pasión, meticulosidad y adaptabilidad), el diseño del sitio se apoya elementos evocativos como líneas rectas, colores cálidos y tipografías sin serifa, inspiradas en el diseño &quot;Material&quot;.

La sencillez del diseño lo hace apto para diversos formatos y soportes, limitando la carga visual al usar sólo la tipografía Raleway en distintos pesos, manteniendo una alta legibilidad en distintos dispositivos.

Se determinaron las siguientes normas gráficas para los distintos elementos de la página:

![Normas gráficas](documentacion/normas.png)
