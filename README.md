from pathlib import Path

readme = r"""# Masterclass Interactiva: Simulador Psicométrico TTCT Figural

## Descripción

Aplicación web interactiva de carácter pedagógico y psicométrico diseñada para visualizar y explicar el circuito de aplicación, control de calidad, calificación y validación de **300 protocolos** del TTCT Figural.

La herramienta presenta, mediante una interfaz de tipo *masterclass*, el recorrido de un protocolo desde su aplicación en aula hasta su incorporación a una matriz de datos, además de mostrar la dinámica de las Aulas A y B bajo un diseño cruzado **AB/BA** y ejemplos de inspección de respuestas en cuatro carreras:

- Diseño Publicitario
- Modas
- Interiores
- Comunicación Audiovisual

El archivo principal de la aplicación es un documento HTML autocontenido con HTML5, CSS, Tailwind CSS, JavaScript y SVG.

## Características principales

### 1. Circuito de eventos

La primera sección representa la cadena de custodia psicométrica mediante seis estaciones:

1. **Aplicación estandarizada en aula**
2. **Enmascaramiento y cintado ciego**
3. **Aleatorización de los protocolos**
4. **Doble calificación ciega**
5. **Control de discrepancias y deriva**
6. **Consenso técnico y cierre en la base de datos**

El circuito dispone de una animación paso a paso y permite seleccionar individualmente cada estación para consultar su explicación metodológica. fileciteturn0file0L92-L196

### 2. Diseño de Aulas A y B

La segunda sección representa un diseño cuasiexperimental de medidas repetidas con estructura de *crossover* o contrabalanceo.

La aplicación contempla:

- **150 estudiantes**
- **6 secciones**
- Grupo 1: Aulas A, secciones 01, 02 y 03
- Grupo 2: Aulas B, secciones 04, 05 y 06
- Rotación de condiciones en la semana 8
- Pretest en la semana 1
- Postest en la semana 16
- Forma A para el pretest
- Forma B para el postest

Un control deslizante permite visualizar las tres fases del semestre y la condición metodológica correspondiente a cada grupo. fileciteturn0file0L202-L299

### 3. Escáner psicométrico

La tercera sección funciona como un simulador visual de calificación. Permite seleccionar una de cuatro carreras y observar un ejemplo de respuesta, sus dimensiones de puntuación y la interpretación del evaluador.

Las dimensiones mostradas son:

1. **Fluidez**
2. **Originalidad**
3. **Elaboración**
4. **Abstracción del título**
5. **Resistencia al cierre**

La interfaz muestra el puntaje total, la descripción de cada dimensión, una representación SVG del dibujo y una interpretación textual del caso. fileciteturn0file0L305-L426

### 4. Documentación técnica integrada

La aplicación incorpora una sección destinada a explicar su propia arquitectura:

- HTML5 semántico
- Navegación mediante pestañas
- CSS3 y Tailwind CSS
- JavaScript Vanilla
- Estructuras de datos para los casos psicométricos
- Renderizado mediante SVG

La documentación señala que la información de los casos de las cuatro carreras se almacena en el objeto `scannerData` y que JavaScript actualiza dinámicamente el contenido del DOM. fileciteturn0file0L432-L480

## Datos generales del simulador

| Elemento | Configuración |
|---|---|
| Protocolos | 300 |
| Participantes | 150 |
| Distribución | 150 Forma A + 150 Forma B |
| Secciones | 6 |
| Diseño | Crossover AB/BA |
| Grupos | Aulas A y Aulas B |
| Pretest | Semana 1 |
| Cruce | Semana 8 |
| Postest | Semana 16 |
| Doble calificación | 90 protocolos (30 %) |
| Jueces | 2 |
| Dimensiones de ejemplo | 5 |
| Tecnologías | HTML5, CSS, Tailwind CSS, JavaScript, SVG |

Estos parámetros corresponden a la configuración presentada en la aplicación. fileciteturn0file0L34-L68

## Arquitectura de la aplicación

```text
index.html
│
├── HTML5
│   ├── Header / Hero
│   ├── Navegación por pestañas
│   ├── Circuito de eventos
│   ├── Dinámica de Aulas A y B
│   ├── Escáner psicométrico
│   └── Guía técnica
│
├── CSS
│   ├── Animación pulseGlow
│   ├── Animación flowLine
│   ├── Animación scanLight
│   ├── Estados activos
│   └── Diseño responsivo
│
├── JavaScript
│   ├── switchTab()
│   ├── setCircuitNode()
│   ├── playCircuitAnimation()
│   ├── updateCrossoverView()
│   ├── selectScannerCareer()
│   └── triggerScannerAnimation()
│
└── Datos
    ├── circuitStations
    └── scannerData
        ├── interiores
        ├── publicidad
        ├── modas
        └── audiovisual