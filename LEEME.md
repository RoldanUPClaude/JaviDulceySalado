# Landing page · Taller de galletas decoradas

**Dulce Salado.** — cocina by Javiera Apparcel — Viña del Mar, Chile — [@javidulceysalado](https://instagram.com/javidulceysalado)

Página de una sola sección (`index.html`), sin dependencias ni instalación.
Para verla: doble clic en `index.html` y se abre en el navegador.

---

## 1. Lo único que falta para publicar

### El WhatsApp (obligatorio)

El número que está puesto es **de ejemplo** y no lleva a ninguna parte.
Abre `index.html` con el Bloc de notas o VS Code, `Ctrl + H`, y reemplaza:

| Buscar | Reemplazar por |
|---|---|
| `56912345678` | Tu WhatsApp real: `56` + `9` + tus 8 dígitos, sin `+` ni espacios (6 veces) |
| `+56 9 1234 5678` | El número como quieres que se lea en pantalla (3 veces) |

En el `<script>` del final hay además esta línea, que debe tener el mismo número:

```js
var WHATSAPP = "56912345678";
```

Es el número al que llega el formulario de reserva. Si no cuadra con el resto,
los mensajes se van a otro lado.

### Las fechas (obligatorio)

En la sección *Fechas y precio* hay tres fechas de ejemplo. Cámbialas por las
reales editando cada `date-row`. Las etiquetas son:

- `pill` → verde, "Disponible"
- `pill low` → arena, "Quedan 3"
- `pill out` → gris, "Agotado"

### Las fotos (muy recomendado)

Sin fotos reales la página convierte mucho menos: la gente compra lo que ve.
Instrucciones y nombres de archivo en `fotos/LEEME.txt`.

Yo no pude bajarlas de tu Instagram — el sitio bloquea el acceso automático a
las imágenes — así que la galería quedó armada con seis recuadros que se llenan
solos en cuanto pongas los archivos en la carpeta `fotos/`. Mientras no existan,
cada recuadro muestra su nombre y qué foto va ahí; la página no se rompe.

---

## 2. La identidad de la marca

Todo esto salió de los dos PDFs (el logo y la tarjeta), no lo inventé:

| Elemento | Valor |
|---|---|
| Verde oliva de la marca | `#70844B` — botones, títulos destacados, la rama |
| Verde profundo | `#3E4A2B` — franjas oscuras y pie de página |
| Crema del logo | `#F5EAE3` |
| Crema de la tarjeta | `#F6EDE4` |
| Fondo general | `#FBF7F0` |
| Tipografía de rótulos | Yanone Kaffeesatz (la misma de tu tarjeta, está en Google Fonts) |
| Tipografía de títulos | Fraunces — ver nota abajo |

**La rama de tu logo está en la página.** La vectoricé desde el PDF y quedó
incrustada en el encabezado y en el pie, junto al nombre *Dulce Salado.* y la
bajada *cocina by Javiera Apparcel*. Los archivos sueltos quedaron en la
carpeta `marca/`:

- `rama.svg` — versión que toma el color del contexto
- `rama-oliva.svg` — verde, para fondos claros
- `rama-crema.svg` — crema, para fondos oscuros

Sirven también para etiquetas, bolsas o lo que necesites: al ser SVG se
agrandan sin pixelarse.

**Sobre las tipografías.** Tu logo usa Rigot (el nombre), Yanone Kaffeesatz
(la bajada) y letras manuscritas en la tarjeta. Yanone es gratuita y ya está
puesta. Rigot y las manuscritas son de pago y no se pueden cargar en una web
sin licencia, así que para los títulos usé Fraunces, que es gratuita y tiene
un aire parecido. Si tienes la licencia de Rigot, se puede cambiar.

Lo que NO pude reproducir: el texto curvo *@javidulceysalado* que rodea tu
logo, porque son letras convertidas con una fuente de pago. Si quieres el logo
completo tal cual en algún lugar de la página, expórtalo como PNG con fondo
transparente y lo coloco.

---

## 3. Ya está puesto con tus datos

- Marca **Dulce Salado.**, ciudad **Viña del Mar**, Instagram **@javidulceysalado**
- Precio **$50.000 CLP** (antes $65.000, tachado como preventa) y anticipo de **$20.000**
- Texto de *Hola, soy Javi* escrito a partir de tu bio: cocinera autodidacta,
  antojos y recetas en tu propia cocina. Está pensado como punto de partida —
  cámbialo por tu historia real, mientras más concreta, mejor.

## 4. Decisiones que tomé y puedes revertir

**No hay testimonios inventados.** Como es tu primer taller, en su lugar puse un
bloque que dice justamente eso: "esta es la primera generación, por eso el grupo
es chico y el precio más bajo". Es honesto y además justifica la preventa.
Dentro del HTML, en esa misma sección, dejé comentado el bloque de testimonios
listo para pegar cuando tengas los primeros reales.

**No hay cifras de trayectoria.** Donde iban "+1.200 galletas" y "+90 alumnas"
ahora van datos del taller que sí son verdad: 8 personas, 5 horas, 12 galletas.

**El correo salió del footer.** No tengo uno tuyo y prefería no inventarlo.
Si quieres agregarlo, pega esto entre los enlaces de contacto del footer:

```html
<a href="mailto:TUCORREO@gmail.com">TUCORREO@gmail.com</a>
```

**El precio anterior tachado ($65.000) es un número que puse yo.** Si no vas a
manejar precio de lista más alto, borra la línea `<span class="was">$65.000</span>`
y queda solo el precio limpio.

---

## 5. Contenido que conviene revisar

- **Horarios del temario**: están de 10:00 a 15:00, ajústalos a tu día real.
- **Temario**: los cinco módulos son una propuesta estándar de nivel 1.
  Cambia lo que no vayas a enseñar; es mejor prometer menos y cumplirlo.
- **Dirección**: la página dice "mi cocina en Viña del Mar" y que compartes la
  dirección exacta por WhatsApp al reservar. Es lo más seguro para ti.
- **Descuento por pareja**: hay un 10% mencionado en las preguntas frecuentes.

---

## 6. Publicarla en internet (gratis)

**Lo más simple — Netlify Drop:** entra a `app.netlify.com/drop` y arrastra la
carpeta completa (con `fotos/` y `marca/` adentro). En segundos te da una
dirección tipo `algo.netlify.app`, que puedes renombrar desde el panel.

**Con dominio propio:** compra el dominio (NIC Chile para un `.cl`) y conéctalo
desde *Domain settings* en Netlify. El certificado HTTPS es automático.

Alternativas equivalentes: Vercel, Cloudflare Pages, GitHub Pages.

Después, el enlace va en la bio de Instagram. Ahí es donde va a vivir.

---

## 7. Detalles técnicos

- **Un solo archivo.** HTML, CSS, JS y la rama del logo van dentro de `index.html`;
  sin build, sin npm. Pesa unos 100 KB.
- **Tipografías** desde Google Fonts (Fraunces, Nunito Sans y Yanone Kaffeesatz).
  Sin internet cae en Georgia y la del sistema: se ve distinto, no se rompe.
- **Responsive** en tres cortes: celular, tablet (900px) y escritorio.
- **Accesibilidad**: menú y acordeón manejan `aria-expanded`, la ilustración
  tiene `role="img"`, y las animaciones se desactivan si el sistema pide
  movimiento reducido.
- **El formulario no envía correos.** Arma el mensaje y abre WhatsApp con el
  texto escrito; tú solo presionas enviar. Cero backend, cero costo mensual, y
  la conversación empieza donde de verdad se cierran estas ventas.

---

## 8. Antes de mandar tráfico, revisa

- [ ] El botón verde flotante abre TU chat de WhatsApp
- [ ] El formulario arma el mensaje y abre WhatsApp
- [ ] Las seis fotos de la galería están puestas
- [ ] Tu retrato está en la sección "Hola, soy Javi"
- [ ] Las fechas son las próximas reales
- [ ] El precio y el anticipo coinciden con lo que dices en Instagram
- [ ] Se ve bien en tu propio celular, no solo en el computador
- [ ] El enlace está en la bio de @javidulceysalado
