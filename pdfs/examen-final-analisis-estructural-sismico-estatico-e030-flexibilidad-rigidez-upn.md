---
titulo: Examen final de Análisis Estructural (UPN 2026-2): análisis sísmico estático E.030, método de flexibilidad y rigidez lateral por condensación estática
titulo_en: Structural Analysis final exam (UPN 2026-2): static seismic analysis per E.030, flexibility method and lateral stiffness by static condensation
slug_en: structural-analysis-final-exam-static-seismic-e030-flexibility-stiffness-upn
curso: Análisis Estructural
universidad: UPN
tipo: Examen
archivo: examen-final-analisis-estructural-upn.pdf
fecha: 2026-11-27
palabras: análisis estructural, examen final, UPN 2026-2, análisis sísmico estático, norma E.030, E.060, E.020, cortante basal, peso sísmico, distribución de fuerzas en altura, Vs30, Máncora Talara Piura, hotel, factor de zona Z, coeficiente de reducción R, matriz de rigidez lateral condensada, derivas elásticas e inelásticas, ETABS, método de flexibilidad, método de las fuerzas, estructura hiperestática, asentamiento de apoyo, SAP2000, método de rigidez directa, condensación estática, frecuencia circular, periodo de vibración, fuerza sísmica equivalente, Universidad Privada del Norte
palabras_en: structural analysis, final exam, static seismic analysis, Peruvian code E.030, base shear, seismic weight, vertical force distribution, Vs30, zone factor Z, response reduction factor R, condensed lateral stiffness matrix, elastic and inelastic drifts, ETABS, flexibility method, force method, statically indeterminate frame, support settlement, SAP2000, direct stiffness method, static condensation, circular frequency, period of vibration, equivalent seismic force, UPN
descripcion: Examen final de Análisis Estructural (Universidad Privada del Norte, 2026-2): análisis sísmico estático de un hotel en Máncora según la E.030 con derivas y ETABS, reacciones de un pórtico hiperestático por el método de flexibilidad con asentamiento de apoyo, y rigidez lateral, frecuencia y periodo por condensación estática.
descripcion_en: Structural Analysis final exam (Universidad Privada del Norte, Peru, 2026-2): static seismic analysis of a hotel in Máncora per code E.030 with drifts and ETABS check, reactions of an indeterminate frame by the flexibility method with support settlement, and lateral stiffness, frequency and period by static condensation.
---
## Indicaciones

Los datos de los problemas dependen de los 4 últimos dígitos del código del coordinador de grupo (N0000WXYZ). Las respuestas deben presentarse con al menos 6 decimales y con total precisión. En los problemas 2 y 3 no se permite MathCAD ni hojas de cálculo en la parte manual.

## Problema 1: análisis sísmico estático (plano XZ)

Realice el análisis sísmico estático de la estructura mostrada, destinada a hotel en el distrito de Máncora (Talara, Piura); el EMS arrojó Vs30 = 470 + W m/s. Datos: f'c = 330 kg/cm² (módulo de elasticidad según la E.060); vigas peraltadas de 35 × 60 cm; columnas extremas de 50 × 90 cm, intermedias de 40 × 60 cm y centrales de 70 × 50 cm. Análisis simplificado sin deformaciones axiales, de corte ni brazos rígidos (EA = ∞). Longitudes: L1 = 6.7 + X/100, L2 = 6.1 + Y/100, L3 = 7 + Z/100, h1 = 4.3 + Z/100 y h2 = 3.3 + Z/100 m. Cargas: tabiquería fija de unidades tubulares de 15 cm, parapetos de 1.2 m en azoteas, losa aligerada de 20 cm (E.020), acabados de 6 cm de mortero, sobrecarga de almacenaje y servicios en los pisos 1 y 2, de cuartos en los pisos 3 y 4, carga viva en azoteas de 140 + W kg/m² y ancho tributario de 5 + W/100 m.

a) Calcule el peso sísmico, los parámetros sísmicos, el cortante basal y la distribución de la fuerza sísmica en altura. (3 puntos)

b) Realice el análisis sísmico estático con el valor correcto de R: desplazamientos laterales con la matriz de rigidez lateral condensada, derivas elásticas e inelásticas y comparación con la norma vigente (si no cumplen, proponga una solución). Explique cómo se obtienen las derivas, qué significa el factor de zona Z y cuál fue el principal cambio de la norma vigente. (4 puntos)

c) Compruebe los resultados con ETABS. (3 puntos)

## Problema 2 (a mano): método de flexibilidad

Determine todas las reacciones de la estructura hiperestática mostrada por el método de flexibilidad (método de las fuerzas). Datos: w1 = 3 + W/10 Tn/m (carga triangular con máximo en B), w2 = 4 + W/10 Tn/m, P = 20 + W/10 Tn a la mitad del tramo DC; L = 5.9 + Y/10, h1 = 4.1 + X/10 y h2 = 3.5 + Z/10 m; E = 100000 + (W + X + Y + Z)·10 kg/cm². El apoyo empotrado D se desplaza 10 mm hacia la izquierda y 4 mm hacia abajo. Viga BC de 200 × 300 mm, columna circular AB de 300 mm de diámetro y columna circular CD de 250 mm de diámetro.

a) Calcule todas las reacciones. (3 puntos)

b) Compruebe los resultados con SAP2000. (2 puntos)

## Problema 3: rigidez lateral por el método de rigidez directa

Por generación directa de la matriz de rigidez (cálculo manual), obtenga la rigidez lateral de la estructura mostrada. Datos: EIv = 9000 + (W + X + Y + Z)·100 Tn·m² en las vigas DE y FG; EIc1 = 15000 + (W + X + Y + Z)·100 Tn·m² en la columna AD; EIc2 = 20000 + (W + X + Y + Z)·100 Tn·m² en la columna BEF; EIc3 = 24000 + (W + X + Y + Z)·100 Tn·m² en la columna CG; P = 25 + W/10 Tn; L1 = 7.2 + X/10, L2 = 6.3 + Y/10, h1 = 4.5 + Z/10 y h2 = 2.8 + Z/10 m; masa m = 20 + W/10 Tn·s²/m.

a) Calcule la rigidez lateral por condensación estática y compruebe el desplazamiento lateral. Con la masa concentrada desplazándose horizontalmente, calcule la frecuencia circular, el periodo de vibración y la frecuencia cíclica, y explique cómo se obtiene la fuerza sísmica equivalente a partir de señales sísmicas. (3 puntos)

b) Verifique los resultados con un modelo en SAP2000. (2 puntos)

[en]
## Instructions

Problem data depend on the last 4 digits of the group coordinator's student code (N0000WXYZ). Answers must be given with at least 6 decimal places and full precision. In problems 2 and 3, MathCAD and spreadsheets are not allowed for the hand calculations.

## Problem 1: static seismic analysis (XZ plane)

Perform the static seismic analysis of the structure shown, a hotel in the district of Máncora (Talara, Piura, Peru); the soil study gave Vs30 = 470 + W m/s. Data: f'c = 330 kg/cm² (modulus of elasticity per code E.060); 35 × 60 cm deep beams; 50 × 90 cm end columns, 40 × 60 cm intermediate columns and 70 × 50 cm central columns. Simplified analysis with no axial or shear deformation and no rigid end zones (EA = ∞). Lengths: L1 = 6.7 + X/100, L2 = 6.1 + Y/100, L3 = 7 + Z/100, h1 = 4.3 + Z/100 and h2 = 3.3 + Z/100 m. Loads: fixed 15 cm hollow-brick partitions, 1.2 m parapets on roofs, 20 cm joist slab (E.020), 6 cm mortar finishes, storage/service live load on floors 1 and 2, guest-room live load on floors 3 and 4, 140 + W kg/m² roof live load and a tributary width of 5 + W/100 m.

a) Compute the seismic weight, seismic parameters, base shear and vertical distribution of the seismic force. (3 points)

b) Perform the static seismic analysis with the correct R: lateral displacements with the condensed lateral stiffness matrix, elastic and inelastic drifts and comparison with the current code (propose a solution if they fail). Explain how drifts are obtained, what the zone factor Z means and the main change in the current code. (4 points)

c) Check the results with ETABS. (3 points)

## Problem 2 (by hand): flexibility method

Determine all reactions of the statically indeterminate structure shown using the flexibility (force) method. Data: w1 = 3 + W/10 t/m (triangular load with its maximum at B), w2 = 4 + W/10 t/m, P = 20 + W/10 t at midspan of DC; L = 5.9 + Y/10, h1 = 4.1 + X/10 and h2 = 3.5 + Z/10 m; E = 100000 + (W + X + Y + Z)·10 kg/cm². Fixed support D moves 10 mm to the left and 4 mm down. Beam BC 200 × 300 mm, circular column AB 300 mm in diameter and circular column CD 250 mm in diameter.

a) Compute all reactions. (3 points)

b) Check the results with SAP2000. (2 points)

## Problem 3: lateral stiffness by the direct stiffness method

Using direct assembly of the stiffness matrix (by hand), obtain the lateral stiffness of the structure shown. Data: EIv = 9000 + (W + X + Y + Z)·100 t·m² for beams DE and FG; EIc1 = 15000 + (W + X + Y + Z)·100 t·m² for column AD; EIc2 = 20000 + (W + X + Y + Z)·100 t·m² for column BEF; EIc3 = 24000 + (W + X + Y + Z)·100 t·m² for column CG; P = 25 + W/10 t; L1 = 7.2 + X/10, L2 = 6.3 + Y/10, h1 = 4.5 + Z/10 and h2 = 2.8 + Z/10 m; mass m = 20 + W/10 t·s²/m.

a) Compute the lateral stiffness by static condensation and check the lateral displacement. With the lumped mass moving horizontally, compute the circular frequency, period of vibration and cyclic frequency, and explain how the equivalent seismic force is obtained from ground-motion records. (3 points)

b) Verify the results with a SAP2000 model. (2 points)
