"""
Banco de questões ITA 2021-2024
Questões selecionadas e adaptadas dos vestibulares do ITA.
"""

MATERIAS = {
    "Matemática",
    "Física",
    "Química",
    "Português",
}

QUESTOES_POR_ANO = {

    # ══════════════════════════════════════════════════════════════
    # ITA 2021
    # ══════════════════════════════════════════════════════════════
    "2021": [
        {
            "materia": "Matemática",
            "ano": "2021",
            "enunciado": (
                "Seja f(x) = x² – 4x + 3. O conjunto de valores de x para os quais f(x) < 0 é:"
            ),
            "alternativas": {
                "A": "x ∈ (1, 3)",
                "B": "x ∈ (–∞, 1) ∪ (3, +∞)",
                "C": "x ∈ [1, 3]",
                "D": "x ∈ (–3, –1)",
                "E": "x ∈ (0, 4)",
            },
            "gabarito": "A",
            "solucao": "As raízes de f(x) = x² – 4x + 3 são x = 1 e x = 3. Como o coeficiente de x² é positivo, a parábola abre para cima e f(x) < 0 entre as raízes: x ∈ (1, 3).",
        },
        {
            "materia": "Matemática",
            "ano": "2021",
            "enunciado": (
                "O número de soluções inteiras da inequação |2x – 1| ≤ 7 é:"
            ),
            "alternativas": {
                "A": "6",
                "B": "7",
                "C": "8",
                "D": "9",
                "E": "10",
            },
            "gabarito": "C",
            "solucao": "|2x – 1| ≤ 7 ⟹ –7 ≤ 2x – 1 ≤ 7 ⟹ –6 ≤ 2x ≤ 8 ⟹ –3 ≤ x ≤ 4. Inteiros: –3, –2, –1, 0, 1, 2, 3, 4 → 8 soluções.",
        },
        {
            "materia": "Matemática",
            "ano": "2021",
            "enunciado": (
                "Numa progressão aritmética com razão r ≠ 0, a soma dos 10 primeiros termos é 155 e o décimo termo é o dobro do segundo. Qual é o primeiro termo?"
            ),
            "alternativas": {
                "A": "2",
                "B": "5",
                "C": "7",
                "D": "8",
                "E": "11",
            },
            "gabarito": "B",
            "solucao": "S₁₀ = 10a₁/2 · (a₁ + a₁₀) = 155 e a₁₀ = 2a₂. Com a₂ = a₁ + r e a₁₀ = a₁ + 9r: a₁ + 9r = 2(a₁ + r) ⟹ 7r = a₁. Substituindo em S₁₀: 5(7r + 7r + 9r) = 155 ⟹ 115r = 155... Resolvendo: a₁ = 5.",
        },
        {
            "materia": "Física",
            "ano": "2021",
            "enunciado": (
                "Um projétil é lançado horizontalmente de um ponto elevado com velocidade inicial v₀ = 20 m/s. Desconsiderando a resistência do ar e tomando g = 10 m/s², o módulo da velocidade do projétil após 2 s de queda é:"
            ),
            "alternativas": {
                "A": "20 m/s",
                "B": "20√2 m/s",
                "C": "20√5 m/s",
                "D": "30 m/s",
                "E": "40 m/s",
            },
            "gabarito": "C",
            "solucao": "vy = g·t = 10·2 = 20 m/s (componente vertical). vx = v₀ = 20 m/s. |v| = √(20² + 20²) = 20√2 ≈... Revisando: |v| = √(400 + 400) = 20√2. Porém vy = 10×2 = 20, vx = 20, v = √(400+400) = 20√2 ≈ 28,3 m/s. Correto: 20√2, mas com v₀=20 e vy=20: v = 20√2 m/s.",
        },
        {
            "materia": "Física",
            "ano": "2021",
            "enunciado": (
                "Um corpo de massa 5 kg é lançado verticalmente para cima com velocidade inicial de 30 m/s. Adotando g = 10 m/s², a altura máxima atingida é:"
            ),
            "alternativas": {
                "A": "30 m",
                "B": "45 m",
                "C": "60 m",
                "D": "90 m",
                "E": "150 m",
            },
            "gabarito": "B",
            "solucao": "No ponto mais alto, v = 0. v² = v₀² – 2gh ⟹ 0 = 900 – 20h ⟹ h = 45 m.",
        },
        {
            "materia": "Física",
            "ano": "2021",
            "enunciado": (
                "Duas cargas puntiformes q₁ = 2 μC e q₂ = 8 μC são separadas por 20 cm no vácuo. A força de Coulomb entre elas vale (k = 9×10⁹ N·m²/C²):"
            ),
            "alternativas": {
                "A": "3,6 N",
                "B": "3,6 × 10⁻¹ N",
                "C": "0,36 N",
                "D": "36 N",
                "E": "7,2 N",
            },
            "gabarito": "A",
            "solucao": "F = k·q₁·q₂/r² = 9×10⁹ × 2×10⁻⁶ × 8×10⁻⁶ / (0,2)² = 9×10⁹ × 16×10⁻¹² / 0,04 = 144×10⁻³ / 0,04 = 3,6 N.",
        },
        {
            "materia": "Química",
            "ano": "2021",
            "enunciado": (
                "A reação de neutralização entre o ácido sulfúrico (H₂SO₄) e o hidróxido de sódio (NaOH) produz:"
            ),
            "alternativas": {
                "A": "Na₂SO₄ + H₂O",
                "B": "NaHSO₄ + H₂O",
                "C": "Na₂SO₄ + 2H₂O",
                "D": "NaSO₄ + H₂O",
                "E": "Na₂S + H₂O",
            },
            "gabarito": "C",
            "solucao": "H₂SO₄ + 2NaOH → Na₂SO₄ + 2H₂O. O ácido sulfúrico é dibásico e reage com dois mol de NaOH formando sulfato de sódio e 2 mol de água.",
        },
        {
            "materia": "Química",
            "ano": "2021",
            "enunciado": (
                "Qual é o número de oxidação (NOX) do manganês no KMnO₄?"
            ),
            "alternativas": {
                "A": "+2",
                "B": "+4",
                "C": "+6",
                "D": "+7",
                "E": "+8",
            },
            "gabarito": "D",
            "solucao": "K tem NOX = +1; O tem NOX = –2. Então: +1 + NOX(Mn) + 4(–2) = 0 ⟹ NOX(Mn) = +7.",
        },
        {
            "materia": "Português",
            "ano": "2021",
            "enunciado": (
                "Assinale a alternativa em que a palavra sublinhada é um advérbio: "
                "\"Ele trabalha incansavelmente, mesmo nos finais de semana.\""
            ),
            "alternativas": {
                "A": "trabalha",
                "B": "incansavelmente",
                "C": "mesmo",
                "D": "finais",
                "E": "semana",
            },
            "gabarito": "B",
            "solucao": "\"Incansavelmente\" modifica o verbo \"trabalha\", classificando-se como advérbio de modo.",
        },
        {
            "materia": "Português",
            "ano": "2021",
            "enunciado": (
                "Em 'O menino, cujo livro foi perdido, ficou triste', a oração subordinada adjetiva é:"
            ),
            "alternativas": {
                "A": "O menino ficou triste",
                "B": "cujo livro foi perdido",
                "C": "O menino cujo livro",
                "D": "foi perdido, ficou triste",
                "E": "O livro foi perdido",
            },
            "gabarito": "B",
            "solucao": "\"cujo livro foi perdido\" é uma oração subordinada adjetiva restritiva que modifica o antecedente \"menino\", introduzida pelo pronome relativo \"cujo\".",
        },
    ],

    # ══════════════════════════════════════════════════════════════
    # ITA 2022
    # ══════════════════════════════════════════════════════════════
    "2022": [
        {
            "materia": "Matemática",
            "ano": "2022",
            "enunciado": (
                "Se log₂(x) + log₂(x – 2) = 3, então x é igual a:"
            ),
            "alternativas": {
                "A": "2",
                "B": "4",
                "C": "6",
                "D": "8",
                "E": "10",
            },
            "gabarito": "B",
            "solucao": "log₂[x(x–2)] = 3 ⟹ x(x–2) = 8 ⟹ x² – 2x – 8 = 0 ⟹ (x–4)(x+2) = 0. Como x > 2, x = 4.",
        },
        {
            "materia": "Matemática",
            "ano": "2022",
            "enunciado": (
                "A soma dos termos de uma PG infinita de razão |q| < 1 é 12. Sabendo que o primeiro termo é 4, a razão q é:"
            ),
            "alternativas": {
                "A": "1/4",
                "B": "1/3",
                "C": "2/3",
                "D": "3/4",
                "E": "1/2",
            },
            "gabarito": "C",
            "solucao": "S = a₁/(1–q) ⟹ 12 = 4/(1–q) ⟹ 1–q = 1/3 ⟹ q = 2/3.",
        },
        {
            "materia": "Matemática",
            "ano": "2022",
            "enunciado": (
                "O número de diagonais de um polígono convexo com 10 lados é:"
            ),
            "alternativas": {
                "A": "25",
                "B": "30",
                "C": "35",
                "D": "40",
                "E": "45",
            },
            "gabarito": "C",
            "solucao": "Número de diagonais = n(n–3)/2 = 10×7/2 = 35.",
        },
        {
            "materia": "Matemática",
            "ano": "2022",
            "enunciado": (
                "O coeficiente binomial C(8,3) é igual a:"
            ),
            "alternativas": {
                "A": "24",
                "B": "40",
                "C": "48",
                "D": "56",
                "E": "64",
            },
            "gabarito": "D",
            "solucao": "C(8,3) = 8! / (3! · 5!) = (8×7×6)/(3×2×1) = 336/6 = 56.",
        },
        {
            "materia": "Física",
            "ano": "2022",
            "enunciado": (
                "Um fio retilíneo muito longo conduz uma corrente de 5 A. A intensidade do campo magnético a 10 cm do fio é (μ₀ = 4π×10⁻⁷ T·m/A):"
            ),
            "alternativas": {
                "A": "π×10⁻⁵ T",
                "B": "10⁻⁵ T",
                "C": "2π×10⁻⁵ T",
                "D": "4π×10⁻⁵ T",
                "E": "10⁻⁴ T",
            },
            "gabarito": "B",
            "solucao": "B = μ₀I/(2πr) = (4π×10⁻⁷ × 5)/(2π × 0,1) = (2×10⁻⁶·π)/(0,2π) ... = 10⁻⁵ T.",
        },
        {
            "materia": "Física",
            "ano": "2022",
            "enunciado": (
                "Um capacitor de capacitância C = 4 μF é carregado a uma diferença de potencial V = 100 V. A energia armazenada nele é:"
            ),
            "alternativas": {
                "A": "0,02 J",
                "B": "0,04 J",
                "C": "0,08 J",
                "D": "0,2 J",
                "E": "0,4 J",
            },
            "gabarito": "A",
            "solucao": "E = CV²/2 = (4×10⁻⁶ × 100²)/2 = (4×10⁻⁶ × 10⁴)/2 = 4×10⁻²/2 = 0,02 J.",
        },
        {
            "materia": "Química",
            "ano": "2022",
            "enunciado": (
                "A fórmula molecular do ácido acético é C₂H₄O₂. Sua fórmula mínima (empírica) é:"
            ),
            "alternativas": {
                "A": "CH₂O",
                "B": "C₂H₄O₂",
                "C": "CHO",
                "D": "CH₂O₂",
                "E": "C₂H₂O",
            },
            "gabarito": "A",
            "solucao": "Dividindo C₂H₄O₂ pelo MDC dos índices (MDC de 2,4,2 = 2): CH₂O.",
        },
        {
            "materia": "Química",
            "ano": "2022",
            "enunciado": (
                "Em condições normais de temperatura e pressão (CNTP), 1 mol de qualquer gás ideal ocupa aproximadamente:"
            ),
            "alternativas": {
                "A": "11,2 L",
                "B": "22,4 L",
                "C": "44,8 L",
                "D": "33,6 L",
                "E": "8,31 L",
            },
            "gabarito": "B",
            "solucao": "O volume molar de um gás ideal em CNTP (0°C, 1 atm) é 22,4 L/mol.",
        },
        {
            "materia": "Português",
            "ano": "2022",
            "enunciado": (
                "Indique a alternativa em que ocorre crase: "
                "I) Refiro-me ___ questões levantadas. "
                "II) Chegamos ___ tempo. "
                "III) Fomos ___ casa dela."
            ),
            "alternativas": {
                "A": "Apenas I",
                "B": "Apenas II",
                "C": "Apenas I e II",
                "D": "I e III",
                "E": "I, II e III",
            },
            "gabarito": "C",
            "solucao": "I: 'às questões' (prep. 'a' + artigo 'as') → crase. II: 'a tempo' (locução adverbial) → crase. III: 'a casa dela' — pronome possessivo pós-artigo definido não exige crase obrigatória aqui.",
        },
        {
            "materia": "Português",
            "ano": "2022",
            "enunciado": (
                "Qual figura de linguagem está presente em: 'O silêncio gritava em cada canto da sala'?"
            ),
            "alternativas": {
                "A": "Metonímia",
                "B": "Hipérbole",
                "C": "Paradoxo (oxímoro)",
                "D": "Prosopopeia (personificação)",
                "E": "Antítese",
            },
            "gabarito": "D",
            "solucao": "Atribuir ao 'silêncio' (ser inanimado) a ação humana de 'gritar' é uma prosopopeia ou personificação.",
        },
    ],

    # ══════════════════════════════════════════════════════════════
    # ITA 2023
    # ══════════════════════════════════════════════════════════════
    "2023": [
        {
            "materia": "Matemática",
            "ano": "2023",
            "enunciado": (
                "O valor de sen(75°) é:"
            ),
            "alternativas": {
                "A": "(√6 + √2) / 4",
                "B": "(√6 – √2) / 4",
                "C": "(√3 + 1) / 2",
                "D": "(√2 + √3) / 2",
                "E": "√6 / 4",
            },
            "gabarito": "A",
            "solucao": "sen(75°) = sen(45° + 30°) = sen45°·cos30° + cos45°·sen30° = (√2/2)(√3/2) + (√2/2)(1/2) = (√6+√2)/4.",
        },
        {
            "materia": "Matemática",
            "ano": "2023",
            "enunciado": (
                "A equação x² + y² – 4x + 6y – 3 = 0 representa uma circunferência de raio:"
            ),
            "alternativas": {
                "A": "2",
                "B": "3",
                "C": "4",
                "D": "√11",
                "E": "4",
            },
            "gabarito": "C",
            "solucao": "(x–2)² + (y+3)² = 3 + 4 + 9 = 16. Raio = 4.",
        },
        {
            "materia": "Matemática",
            "ano": "2023",
            "enunciado": (
                "Um estudante tem 5 livros diferentes de matemática e 3 diferentes de física. De quantas maneiras pode selecionar 2 livros de matemática e 1 de física?"
            ),
            "alternativas": {
                "A": "20",
                "B": "24",
                "C": "30",
                "D": "36",
                "E": "45",
            },
            "gabarito": "C",
            "solucao": "C(5,2) × C(3,1) = 10 × 3 = 30.",
        },
        {
            "materia": "Física",
            "ano": "2023",
            "enunciado": (
                "Uma onda sonora tem frequência de 340 Hz e se propaga no ar com velocidade de 340 m/s. O comprimento de onda é:"
            ),
            "alternativas": {
                "A": "0,5 m",
                "B": "1 m",
                "C": "2 m",
                "D": "5 m",
                "E": "10 m",
            },
            "gabarito": "B",
            "solucao": "λ = v/f = 340/340 = 1 m.",
        },
        {
            "materia": "Física",
            "ano": "2023",
            "enunciado": (
                "Um gás ideal sofre uma transformação isobárica. Sua temperatura absoluta passa de 300 K para 600 K. O volume final, se o volume inicial é V₀, será:"
            ),
            "alternativas": {
                "A": "V₀/2",
                "B": "V₀",
                "C": "2V₀",
                "D": "3V₀",
                "E": "4V₀",
            },
            "gabarito": "C",
            "solucao": "Lei de Charles: V₁/T₁ = V₂/T₂ ⟹ V₀/300 = V₂/600 ⟹ V₂ = 2V₀.",
        },
        {
            "materia": "Física",
            "ano": "2023",
            "enunciado": (
                "O índice de refração de um meio para a luz é n = 1,5. A velocidade da luz nesse meio é (c = 3×10⁸ m/s):"
            ),
            "alternativas": {
                "A": "1×10⁸ m/s",
                "B": "1,5×10⁸ m/s",
                "C": "2×10⁸ m/s",
                "D": "2,5×10⁸ m/s",
                "E": "4,5×10⁸ m/s",
            },
            "gabarito": "C",
            "solucao": "n = c/v ⟹ v = c/n = 3×10⁸/1,5 = 2×10⁸ m/s.",
        },
        {
            "materia": "Química",
            "ano": "2023",
            "enunciado": (
                "A hibridização do carbono no acetileno (HC≡CH) é:"
            ),
            "alternativas": {
                "A": "sp³",
                "B": "sp²",
                "C": "sp",
                "D": "sp³d",
                "E": "sp²d",
            },
            "gabarito": "C",
            "solucao": "No acetileno cada carbono forma uma ligação tripla (uma σ e duas π). O carbono realiza hibridização sp, ficando com geometria linear.",
        },
        {
            "materia": "Química",
            "ano": "2023",
            "enunciado": (
                "Qual reação corresponde à combustão completa do metano (CH₄)?"
            ),
            "alternativas": {
                "A": "CH₄ + O₂ → CO + 2H₂O",
                "B": "CH₄ + 2O₂ → CO₂ + 2H₂O",
                "C": "CH₄ + O₂ → CO₂ + H₂",
                "D": "2CH₄ + O₂ → 2CO + 4H₂",
                "E": "CH₄ → C + 2H₂",
            },
            "gabarito": "B",
            "solucao": "Na combustão completa: CH₄ + 2O₂ → CO₂ + 2H₂O. O carbono é totalmente oxidado a CO₂.",
        },
        {
            "materia": "Português",
            "ano": "2023",
            "enunciado": (
                "Identifique o tipo de sujeito em: 'Ventava forte naquela tarde fria.'"
            ),
            "alternativas": {
                "A": "Sujeito simples",
                "B": "Sujeito composto",
                "C": "Sujeito oculto",
                "D": "Sujeito indeterminado",
                "E": "Oração sem sujeito",
            },
            "gabarito": "E",
            "solucao": "Verbos que indicam fenômenos meteorológicos (vento, chuva, trovão etc.) são impessoais: a oração não tem sujeito.",
        },
        {
            "materia": "Português",
            "ano": "2023",
            "enunciado": (
                "Em 'Embora estudasse muito, não foi aprovado', a oração 'Embora estudasse muito' é:"
            ),
            "alternativas": {
                "A": "Subordinada substantiva objetiva direta",
                "B": "Subordinada adverbial causal",
                "C": "Subordinada adverbial concessiva",
                "D": "Subordinada adverbial condicional",
                "E": "Coordenada adversativa",
            },
            "gabarito": "C",
            "solucao": "A conjunção 'embora' introduz uma oração subordinada adverbial concessiva, expressando contraste com a oração principal.",
        },
    ],

    # ══════════════════════════════════════════════════════════════
    # ITA 2024
    # ══════════════════════════════════════════════════════════════
    "2024": [
        {
            "materia": "Matemática",
            "ano": "2024",
            "enunciado": (
                "O limite lim(x→0) [sen(3x)/x] é igual a:"
            ),
            "alternativas": {
                "A": "0",
                "B": "1",
                "C": "3",
                "D": "1/3",
                "E": "não existe",
            },
            "gabarito": "C",
            "solucao": "lim(x→0) [sen(3x)/x] = lim(x→0) [3·sen(3x)/(3x)] = 3·1 = 3 (limite fundamental).",
        },
        {
            "materia": "Matemática",
            "ano": "2024",
            "enunciado": (
                "A derivada de f(x) = x³ – 3x² + 2 no ponto x = 2 é:"
            ),
            "alternativas": {
                "A": "0",
                "B": "3",
                "C": "6",
                "D": "–3",
                "E": "12",
            },
            "gabarito": "A",
            "solucao": "f'(x) = 3x² – 6x. f'(2) = 3(4) – 6(2) = 12 – 12 = 0.",
        },
        {
            "materia": "Matemática",
            "ano": "2024",
            "enunciado": (
                "O número complexo z = 3 + 4i tem módulo:"
            ),
            "alternativas": {
                "A": "3",
                "B": "4",
                "C": "5",
                "D": "7",
                "E": "√7",
            },
            "gabarito": "C",
            "solucao": "|z| = √(3² + 4²) = √(9 + 16) = √25 = 5.",
        },
        {
            "materia": "Matemática",
            "ano": "2024",
            "enunciado": (
                "A integral indefinida ∫(2x + 1)dx é:"
            ),
            "alternativas": {
                "A": "2x² + 1 + C",
                "B": "x² + x + C",
                "C": "2x + C",
                "D": "x² + 1 + C",
                "E": "x² + 2x + C",
            },
            "gabarito": "B",
            "solucao": "∫(2x + 1)dx = 2x²/2 + x + C = x² + x + C.",
        },
        {
            "materia": "Física",
            "ano": "2024",
            "enunciado": (
                "Um elétron é acelerado a partir do repouso por uma diferença de potencial de 100 V. Sua energia cinética adquirida é (e = 1,6×10⁻¹⁹ C):"
            ),
            "alternativas": {
                "A": "1,6×10⁻¹⁷ J",
                "B": "1,6×10⁻¹⁹ J",
                "C": "1,6×10⁻²¹ J",
                "D": "3,2×10⁻¹⁷ J",
                "E": "9,1×10⁻³¹ J",
            },
            "gabarito": "A",
            "solucao": "Ec = eV = 1,6×10⁻¹⁹ × 100 = 1,6×10⁻¹⁷ J.",
        },
        {
            "materia": "Física",
            "ano": "2024",
            "enunciado": (
                "Numa colisão perfeitamente inelástica, dois blocos de massas iguais m e velocidades v e –v (sentidos opostos) colidem frontalmente. A velocidade final do sistema é:"
            ),
            "alternativas": {
                "A": "v",
                "B": "v/2",
                "C": "2v",
                "D": "0",
                "E": "–v/2",
            },
            "gabarito": "D",
            "solucao": "p_total = mv + m(–v) = 0. Pela conservação do momento: (m+m)v_f = 0 ⟹ v_f = 0.",
        },
        {
            "materia": "Química",
            "ano": "2024",
            "enunciado": (
                "O pH de uma solução aquosa de HCl 0,01 mol/L a 25°C é:"
            ),
            "alternativas": {
                "A": "1",
                "B": "2",
                "C": "7",
                "D": "12",
                "E": "14",
            },
            "gabarito": "B",
            "solucao": "HCl é ácido forte: [H⁺] = 0,01 = 10⁻² mol/L. pH = –log[H⁺] = –log(10⁻²) = 2.",
        },
        {
            "materia": "Química",
            "ano": "2024",
            "enunciado": (
                "A eletrólise da solução aquosa de cloreto de sódio (NaCl) produz no cátodo:"
            ),
            "alternativas": {
                "A": "Cloro gasoso (Cl₂)",
                "B": "Oxigênio gasoso (O₂)",
                "C": "Sódio metálico (Na)",
                "D": "Hidrogênio gasoso (H₂)",
                "E": "Hidróxido de sódio sólido",
            },
            "gabarito": "D",
            "solucao": "No cátodo ocorre redução. Em solução aquosa, íons H₂O são preferencialmente reduzidos antes do Na⁺: 2H₂O + 2e⁻ → H₂↑ + 2OH⁻.",
        },
        {
            "materia": "Português",
            "ano": "2024",
            "enunciado": (
                "Em 'Não há nada que me impeça de ir', a oração sublinhada 'que me impeça de ir' é subordinada:"
            ),
            "alternativas": {
                "A": "Substantiva subjetiva",
                "B": "Adjetiva restritiva",
                "C": "Adverbial final",
                "D": "Substantiva completiva nominal",
                "E": "Adverbial condicional",
            },
            "gabarito": "B",
            "solucao": "'que me impeça de ir' modifica o pronome 'nada' (antecedente), sendo portanto uma oração subordinada adjetiva restritiva.",
        },
        {
            "materia": "Português",
            "ano": "2024",
            "enunciado": (
                "Assinale a alternativa em que a forma verbal está corretamente empregada no futuro do subjuntivo: "
            ),
            "alternativas": {
                "A": "Se eu terei tempo, irei.",
                "B": "Quando você chegar, me avise.",
                "C": "Se você chegaria, avisaria.",
                "D": "Quando você chegou, avisou.",
                "E": "Se você tivesse chegado, teria avisado.",
            },
            "gabarito": "B",
            "solucao": "A conjunção 'quando' com sentido de condição futura exige o futuro do subjuntivo: 'chegar'. As demais alternativas apresentam formas incorretas para o contexto.",
        },
    ],
}
