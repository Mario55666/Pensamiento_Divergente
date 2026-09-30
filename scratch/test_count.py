# -*- coding: utf-8 -*-

text = """Hacia una pedagogía de la divergencia: justificación multidimensional de la inclusión educativa en el Perú

La selección y delimitación del problema de investigación obedece a una justificación articulada en tres dimensiones interconectadas: académica, profesional y social. Lejos de constituir esferas aisladas, cada plano evidencia brechas estructurales, vacíos metodológicos y urgencias contextuales que exigen una respuesta rigurosa desde la educación superior pública latinoamericana.

En el plano académico, la literatura científica internacional revela un sesgo epistémico determinante. La evidencia empírica acumulada sobre el Diseño Universal para el Aprendizaje (DUA) y los modelos pedagógicos integrados procede predominantemente de universidades de países de altos ingresos y de entornos con alta madurez digital (Almeqdad et al., 2023; Hogan et al., 2025). Este marco foráneo suele omitir las restricciones materiales, la precariedad de recursos y la diversidad sociocultural de las universidades públicas de nuestra región. Asimismo, la investigación existente no ha evaluado de forma sistemática el pensamiento creativo divergente en estos esquemas. El DUA tiende a reducirse a una herramienta de asimilación de contenidos homogéneos, desatendiendo su capacidad de potenciar la originalidad y la resolución no convencional de problemas en el aula universitaria.

En el plano profesional, el estudio responde a un escenario en profunda transformación. Hacia el año 2030, la creatividad, la resiliencia y el pensamiento analítico encabezarán la demanda formativa global frente a la automatización tecnológica (OECD, 2024; World Economic Forum, 2025). Sin embargo, en el contexto peruano, estas exigencias internacionales colisionan frontalmente con un mercado laboral juvenil condicionado por la informalidad, la inestabilidad y el subempleo (Campos y López, 2025). En un entorno socioeconómico tan adverso, el pensamiento divergente y la resiliencia dejan de ser meros diferenciales de competitividad: representan recursos indispensables para la subsistencia profesional y el diseño de iniciativas productivas autónomas y transformadoras.

En el plano social, la propuesta se ubica en un escenario de profunda vulnerabilidad psicosocial. Las juventudes peruanas registran índices alarmantes de malestar psicológico y desatención emocional (Ministerio de Salud del Perú, 2021). Dentro de las aulas, esta realidad afecta de modo agudo a los estudiantes neurodivergentes, quienes eligen con frecuencia no declarar su condición ante el temor constante al estigma, el juicio social y la discriminación institucional (Fane, 2025; Quigua et al., 2025). El silenciamiento forzado menoscaba su bienestar subjetivo y sofoca potenciales cognitivos valiosos. Aplicar el DUA y validar la neurodiversidad constituye un acto imperativo de equidad y justicia reparadora.

En conclusión, este estudio articula la superación de brechas pedagógicas globales, la preparación ante un mercado laboral informal y la desestigmatización de la neurodivergencia, configurando una apuesta urgente y necesaria para la universidad pública."""

print("Length (raw):", len(text))
print("Length (normalized CRLF to LF):", len(text.replace("\r\n", "\n")))
print("Length without spaces/newlines:", len(text.replace(" ", "").replace("\n", "").replace("\r", "")))
print("Word count:", len(text.split()))
