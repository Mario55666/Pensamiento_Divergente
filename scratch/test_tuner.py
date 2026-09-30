# -*- coding: utf-8 -*-
import sys

title = "Hacia una pedagogía de la divergencia: justificación multidimensional de la investigación en la educación superior pública peruana"

p1 = ("La pertinencia y delimitación del problema de investigación responde a una justificación articulada "
      "en tres dimensiones cardinales e interdependientes: el plano académico, el plano profesional y el plano social. "
      "Lejos de concebirse como compartimentos estancos, estas esferas configuran un entramado crítico donde convergen "
      "vacíos epistemológicos, tensiones estructurales del mercado productivo y urgencias éticas vinculadas al bienestar "
      "juvenil. Abordar esta problemática permite no solo visibilizar brechas históricas en las aulas universitarias, "
      "sino también proponer horizontes pedagógicos transformadores y situados.")

p2 = ("En el plano académico, el examen de la literatura científica revela un marcado sesgo geopolítico y metodológico. "
      "La mayor parte de la evidencia empírica acumulada sobre el Diseño Universal para el Aprendizaje (DUA) y los modelos "
      "curriculares integrados proviene de instituciones de países de altos ingresos y de ecosistemas educativos con alta dotación "
      "tecnológica y madurez digital (Almeqdad et al., 2023; Hogan et al., 2025). Dicha producción foránea suele ignorar las "
      "condiciones materiales, la sobrecarga docente y la precariedad de recursos características de la universidad pública "
      "latinoamericana. Asimismo, estos estudios han postergado la evaluación sistemática del pensamiento creativo divergente. "
      "Con frecuencia, el DUA se ha reducido a un protocolo instrumental para facilitar la asimilación pasiva de contenidos "
      "estandarizados, soslayando su potencial catalizador para estimular la fluidez, la originalidad y la formulación de respuestas "
      "inéditas frente a problemas complejos en contextos de alta heterogeneidad sociocultural.")

p3 = ("En el plano profesional, el estudio se sustenta en las exigencias prospectivas del escenario laboral hacia el año 2030. "
      "Diversos diagnósticos globales señalan que el pensamiento analítico, la creatividad y la resiliencia constituirán las "
      "competencias humanas determinantes ante la disrupción de la inteligencia artificial y la automatización productiva "
      "(OECD, 2024; World Economic Forum, 2025). No obstante, para las juventudes universitarias en el Perú, esta demanda global "
      "colisiona directamente con un entorno laboral severamente restringido por la informalidad estructural, el subempleo y la "
      "inestabilidad socioeconómica (Campos y López, 2025). En tales circunstancias, cultivar un pensamiento divergente y una "
      "capacidad adaptativa sólida no representa un atributo de distinción elitista, sino un recurso indispensable de supervivencia "
      "que faculta a los egresados para navegar la precariedad, autogestionar soluciones viables y liderar transformaciones en sus "
      "comunidades productivas.")

p4 = ("En el plano social, la investigación halla una justificación ineludible en la crisis psicosocial que atraviesa la juventud. "
      "En el Perú, los índices epidemiológicos dan cuenta de un elevado malestar psicológico y un incremento de los cuadros afectivos "
      "en la población universitaria (Ministerio de Salud del Perú, 2021). Dentro de este panorama de vulnerabilidad, un sector "
      "significativo de estudiantes neurodivergentes opta de manera sistemática por no declarar su condición médica o psicoeducativa, "
      "motivado por el temor justificado al estigma, el rechazo de sus pares y la incomprensión pedagógica institucional (Fane, 2025; "
      "Quigua et al., 2025). Este silenciamiento forzado profundiza el aislamiento, socava la autoestima académica y anula aportes "
      "cognitivos de gran valor. Articular el DUA con la validación de la neurodivergencia se constituye así en un imperativo ético de "
      "justicia formativa y restitución de derechos humanos.")

p5 = ("En conclusión, la elección del problema integra la descolonización empírica de la inclusión pedagógica, la respuesta "
      "estratégica a las fracturas del empleo juvenil y la urgente desestigmatización de la neurodiversidad, consolidando una "
      "agenda indispensable para el porvenir de la educación superior pública.")

full_text = f"{title}\n\n{p1}\n\n{p2}\n\n{p3}\n\n{p4}\n\n{p5}"

print("Total length:", len(full_text))
print("Without spaces/newlines:", len(full_text.replace(" ", "").replace("\n", "")))
print("Words:", len(full_text.split()))
