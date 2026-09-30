# -*- coding: utf-8 -*-

title = "Hacia una pedagogía de la divergencia: justificación de la inclusión en la educación superior pública"

# Let's inspect where 90 characters can be smoothly added.
# In p1:
# "La elección del problema responde a tres razones fundamentales e interconectadas: en los planos académico, profesional y social."
# Let's write an interactive tuner in python that hits 3500 exactly.

p1 = ("La elección del problema de investigación responde a una justificación articulada en tres dimensiones "
      "interdependientes: académica, profesional y social. Lejos de constituir esferas aisladas, cada una evidencia "
      "tensiones estructurales, vacíos metodológicos y urgencias éticas que exigen una respuesta rigurosa desde la "
      "educación superior pública latinoamericana. Esta articulación multidimensional no solo diagnostica las limitaciones "
      "de los enfoques pedagógicos hegemónicos, sino que fundamenta una propuesta formativa contextualizada y transformadora.")

p2 = ("En el plano académico, la literatura científica internacional revela un sesgo epistémico sustancial. La evidencia "
      "acumulada sobre el Diseño Universal para el Aprendizaje (DUA) y los modelos integrados procede sobre todo de "
      "universidades de países de altos ingresos y de entornos digitales dotados de amplia infraestructura tecnológica (Almeqdad "
      "et al., 2023; Hogan et al., 2025). Este marco foráneo suele omitir las restricciones materiales, la brecha de conectividad "
      "y la sobrecarga docente de las universidades públicas en América Latina. Más aún, la investigación previa no ha "
      "evaluado de forma sistemática el pensamiento creativo divergente dentro de estos esquemas. El DUA tiende a reducirse a "
      "un instrumento de asimilación pasiva de contenidos estandarizados, descuidando su potencial para estimular la "
      "originalidad, la flexibilidad cognitiva y la resolución no convencional de problemas complejos en el aula universitaria.")

p3 = ("En el plano profesional, el estudio se sustenta en las exigencias laborales hacia el año 2030. Diversos diagnósticos "
      "globales coinciden en que la creatividad, la resiliencia y el pensamiento analítico encabezarán la demanda formativa "
      "frente a la automatización tecnológica (OECD, 2024; World Economic Forum, 2025). Sin embargo, en el Perú, esta demanda "
      "colisiona frontalmente con un mercado laboral juvenil caracterizado por alarmantes tasas de informalidad, precariedad e "
      "inestabilidad contractual (Campos y López, 2025). En un contexto productivo tan restrictivo, el pensamiento divergente y "
      "la adaptabilidad resiliente dejan de ser meros factores de competitividad: constituyen recursos indispensables para la "
      "subsistencia profesional y la formulación de proyectos autónomos capaces de generar valor social y económico.")

p4 = ("En el plano social, el estudio se sitúa en un contexto de profunda vulnerabilidad psicosocial. Las juventudes peruanas "
      "registran índices preocupantes de malestar psicológico elevado y desatención emocional (Ministerio de Salud del Perú, "
      "2021). Dentro de las aulas, esta realidad afecta de modo agudo a los estudiantes neurodivergentes, quienes optan con "
      "frecuencia por no declarar su condición ante el arraigado temor al estigma, el rechazo de pares y los prejuicios "
      "institucionales (Fane, 2025; Quigua et al., 2025). Dicho silenciamiento forzado incrementa el desgaste anímico, menoscaba "
      "la autoeficacia académica e invisibiliza talentos singulares. Articular el DUA con el reconocimiento de la neurodiversidad "
      "representa un imperativo ético de justicia distributiva, dignidad humana y equidad en la vida universitaria.")

p5 = ("En conclusión, la elección del problema articula la superación de sesgos pedagógicos globales, la respuesta formativa "
      "ante las exigencias del empleo informal y la desestigmatización de la neurodivergencia, consolidando una agenda necesaria "
      "y urgente para la educación pública.")

full_text = f"{title}\n\n{p1}\n\n{p2}\n\n{p3}\n\n{p4}\n\n{p5}"

print("Length with spaces:", len(full_text))
print("Diff to 3500:", 3500 - len(full_text))
print("Length without spaces/newlines:", len(full_text.replace(" ", "").replace("\n", "")))
print("Words:", len(full_text.split()))
