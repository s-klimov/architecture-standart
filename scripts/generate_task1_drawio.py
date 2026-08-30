#!/usr/bin/env python3
"""Generate draw.io artifacts for Task 1 (IT landscape + integrations)."""

from pathlib import Path
from xml.sax.saxutils import escape

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "Task1"


def cell(
    cid: str,
    value: str,
    x: float,
    y: float,
    w: float,
    h: float,
    style: str,
    parent: str = "1",
    vertex: str = "1",
    raw: bool = False,
) -> str:
    text = value if raw else escape(value)
    return (
        f'        <mxCell id="{cid}" value="{text}" style="{style}" '
        f'vertex="{vertex}" parent="{parent}">\n'
        f'          <mxGeometry x="{x}" y="{y}" width="{w}" height="{h}" as="geometry"/>\n'
        f"        </mxCell>\n"
    )


def edge(
    eid: str,
    value: str,
    source: str,
    target: str,
    style: str,
    parent: str = "1",
    points: list[tuple[float, float]] | None = None,
    exit_x: float | None = None,
    exit_y: float | None = None,
    entry_x: float | None = None,
    entry_y: float | None = None,
) -> str:
    geo_extra = ""
    if points:
        pts = "".join(f'<mxPoint x="{px}" y="{py}"/>' for px, py in points)
        geo_extra = f"<Array as=\"points\">{pts}</Array>"
    constraints = ""
    if exit_x is not None:
        constraints += f' exitX="{exit_x}" exitY="{exit_y}"'
    if entry_x is not None:
        constraints += f' entryX="{entry_x}" entryY="{entry_y}"'
    return (
        f'        <mxCell id="{eid}" value="{escape(value)}" style="{style}{constraints}" '
        f'edge="1" parent="{parent}" source="{source}" target="{target}">\n'
        f'          <mxGeometry relative="1" as="geometry">{geo_extra}</mxGeometry>\n'
        f"        </mxCell>\n"
    )


def mxfile(name: str, diagram_id: str, width: int, height: int, body: str) -> str:
    return f"""<mxfile host="app.diagrams.net" agent="Task1" version="24.7.17">
  <diagram id="{diagram_id}" name="{name}">
    <mxGraphModel dx="1600" dy="1000" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="{width}" pageHeight="{height}" math="0" shadow="0">
      <root>
        <mxCell id="0"/>
        <mxCell id="1" parent="0"/>
{body}      </root>
    </mxGraphModel>
  </diagram>
</mxfile>
"""


# --- shared styles ---
TITLE = (
    "text;html=1;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;"
    "fontSize=22;fontStyle=1;fontColor=#1F2937;fontFamily=Helvetica;"
)
SUB = (
    "text;html=1;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;"
    "fontSize=12;fontColor=#4B5563;fontFamily=Helvetica;"
)
NOTE = (
    "rounded=1;whiteSpace=wrap;html=1;align=left;verticalAlign=top;"
    "fillColor=#FFF7ED;strokeColor=#F59E0B;fontSize=11;fontColor=#1F2937;"
    "spacingLeft=10;spacingRight=10;spacingTop=8;"
)
LEGEND_BOX = (
    "rounded=1;whiteSpace=wrap;html=1;align=left;verticalAlign=top;"
    "fillColor=#F8FAFC;strokeColor=#94A3B8;fontSize=11;fontColor=#1F2937;"
    "spacingLeft=10;spacingRight=10;spacingTop=8;"
)
CAP_H = (
    "rounded=1;whiteSpace=wrap;html=1;align=center;verticalAlign=middle;"
    "fillColor=#2563EB;strokeColor=#1D4ED8;fontColor=#FFFFFF;fontStyle=1;"
    "fontSize=11;"
)
ORG = (
    "rounded=1;whiteSpace=wrap;html=1;align=left;verticalAlign=middle;"
    "fillColor=#1E3A5F;strokeColor=#0F2744;fontColor=#FFFFFF;fontStyle=1;"
    "fontSize=11;spacingLeft=10;"
)
CELL_BG = (
    "rounded=1;whiteSpace=wrap;html=1;align=center;verticalAlign=middle;"
    "fillColor=#F1F5F9;strokeColor=#CBD5E1;fontSize=10;fontColor=#94A3B8;"
)
PILL = (
    "rounded=1;whiteSpace=wrap;html=1;align=center;verticalAlign=middle;"
    "fontSize=10;fontStyle=1;arcSize=20;"
)
APP = (
    "rounded=1;whiteSpace=wrap;html=1;align=center;verticalAlign=middle;"
    "fontSize=12;fontStyle=1;arcSize=8;"
)
ACTOR = (
    "shape=actor;whiteSpace=wrap;html=1;align=center;verticalAlign=bottom;"
    "fillColor=#E0E7FF;strokeColor=#4338CA;fontSize=11;fontStyle=1;fontColor=#1E1B4B;"
)
EXT = (
    "rounded=1;whiteSpace=wrap;html=1;align=center;verticalAlign=middle;"
    "dashed=1;dashPattern=8 8;fillColor=#FEF3C7;strokeColor=#D97706;"
    "fontSize=12;fontStyle=1;fontColor=#78350F;"
)
LANE = (
    "swimlane;whiteSpace=wrap;html=1;startSize=36;fillColor=#F8FAFC;"
    "strokeColor=#94A3B8;fontStyle=1;fontSize=13;fontColor=#1F2937;"
)


def app_style(color: str, stroke: str, fg: str = "#111827") -> str:
    return f"{PILL}fillColor={color};strokeColor={stroke};fontColor={fg};"


def big_app(color: str, stroke: str, fg: str = "#111827") -> str:
    return f"{APP}fillColor={color};strokeColor={stroke};fontColor={fg};"


# colors
C_ABS = ("#FDBA74", "#EA580C")
C_CC = ("#99F6E4", "#0D9488")
C_PCC = ("#A5F3FC", "#0891B2")
C_XL = ("#BBF7D0", "#16A34A")
C_MAIL = ("#FDE68A", "#D97706")
C_SMS = ("#DDD6FE", "#7C3AED")
C_IB = ("#BFDBFE", "#2563EB")
C_WEB = ("#FBCFE8", "#DB2777")
C_GW = ("#C7D2FE", "#4F46E5")


def landscape() -> str:
    caps = [
        "Продажи в сети\nотделений",
        "Продажи через\nкол-центр",
        "Digital-\nоповещения клиентов",
        "Обслуживание\nдепозитных процессов",
        "Обслуживание\nкредитных процессов",
        "Управление\nдоговорами",
    ]
    orgs = [
        "Управление обслуживанием\nв сети отделений\n(фронт-офис, 50 отделений)",
        "Кол-центр банка «Стандарт»\n(200 операторов)",
        "Партнёрский кол-центр\n(100 человек, внешний)",
        "Управление обслуживанием\nдепозитных продуктов\n(бэк-офис, 50 чел.)",
        "Управление обслуживанием\nкредитных продуктов\n(отдел кредитования, 50 чел.)",
        "Управление IT\n(АБС, интернет-банк,\nподрядчики)",
        "Команда цифровой\nтрансформации\nрозничного бизнеса",
    ]

    # cell apps: [row][col] -> list of (label, color pair)
    grid: list[list[list[tuple[str, tuple[str, str]]]]] = [
        [  # front
            [("АБС\nприём клиента,\nсоздание депозита", C_ABS)],
            [],
            [],
            [("Email\nзапрос ставки,\nесли клиент\nбез звонка", C_MAIL)],
            [],
            [("АБС\nпечать и загрузка\nподписанных документов", C_ABS)],
        ],
        [  # call center
            [],
            [("Система кол-центра\nобращение по депозиту", C_CC)],
            [],
            [],
            [],
            [],
        ],
        [  # partner cc
            [],
            [("Система партнёрского КЦ\nскрипты звонков,\nнет связи с АБС", C_PCC)],
            [],
            [],
            [],
            [],
        ],
        [  # deposit BO
            [],
            [("АБС\nобработка заявок\nиз кол-центра", C_ABS)],
            [("АБС → СМС\nставка готова,\nприглашение в отделение", C_SMS)],
            [
                ("АБС\nучёт депозитов", C_ABS),
                ("Excel\nспецставки", C_XL),
                ("Email\nсогласование ставок", C_MAIL),
            ],
            [],
            [],
        ],
        [  # credit
            [],
            [],
            [],
            [
                ("Excel\nежедневный расчёт\nставок по депозитам", C_XL),
                ("Email\nфайл ставок\nв бэк-офис", C_MAIL),
            ],
            [
                ("АБС\nкредитный риск\nпо клиенту", C_ABS),
                ("Excel\nставка ЦБ, объёмы\nкредитов и депозитов", C_XL),
            ],
            [],
        ],
        [  # IT
            [("Интернет-банк\nнет открытия\nдепозитов", C_IB)],
            [("Система кол-центра\nплатформа подрядчика", C_CC)],
            [
                ("Сайт\nтолько маркетинг", C_WEB),
                ("Интернет-банк\nплатежи, текущие счета", C_IB),
                ("СМС-шлюз", C_GW),
            ],
            [("АБС\nразработка и поддержка", C_ABS)],
            [("АБС\nразработка и поддержка", C_ABS)],
            [("АБС\nхранение сканов\nдоговоров", C_ABS)],
        ],
        [  # digital transformation
            [],
            [],
            [],
            [],
            [],
            [],
        ],
    ]

    ox, oy = 40, 110
    org_w, cap_w, row_h, head_h = 280, 210, 150, 70
    body = []
    body.append(cell("title", "Карта текущего IT-ландшафта банка «Стандарт»", 40, 20, 900, 36, TITLE))
    body.append(
        cell(
            "sub",
            "Строки — организационные единицы. Колонки — бизнес-возможности 2-го уровня (из Business Capability Map).",
            40,
            56,
            1100,
            28,
            SUB,
        )
    )
    body.append(
        cell(
            "corner",
            "Организационная единица  /  Бизнес-возможность L2",
            ox,
            oy,
            org_w,
            head_h,
            "rounded=1;whiteSpace=wrap;html=1;align=center;verticalAlign=middle;"
            "fillColor=#0F172A;strokeColor=#020617;fontColor=#FFFFFF;fontSize=10;fontStyle=1;",
        )
    )

    for i, cap in enumerate(caps):
        body.append(
            cell(f"cap-{i}", cap, ox + org_w + i * cap_w, oy, cap_w, head_h, CAP_H)
        )

    cid = 0
    for r, org in enumerate(orgs):
        y = oy + head_h + r * row_h
        body.append(cell(f"org-{r}", org, ox, y, org_w, row_h, ORG))
        for c in range(len(caps)):
            apps = grid[r][c]
            cx = ox + org_w + c * cap_w
            body.append(
                cell(
                    f"bg-{r}-{c}",
                    "—" if not apps else "",
                    cx,
                    y,
                    cap_w,
                    row_h,
                    CELL_BG,
                )
            )
            if not apps:
                continue
            n = len(apps)
            gap = 6
            pill_h = min(40, (row_h - 16 - gap * (n - 1)) / n)
            total_h = n * pill_h + (n - 1) * gap
            start_y = y + (row_h - total_h) / 2
            for k, (label, (fill, stroke)) in enumerate(apps):
                cid += 1
                body.append(
                    cell(
                        f"app-{cid}",
                        label,
                        cx + 8,
                        start_y + k * (pill_h + gap),
                        cap_w - 16,
                        pill_h,
                        app_style(fill, stroke),
                    )
                )

    ly = oy + head_h + len(orgs) * row_h + 24
    body.append(
        cell(
            "legend",
            "<b>Легенда приложений и «систем»</b><br>"
            "Оранжевый — АБС (учёт счетов, депозиты, кредитный риск, документы).<br>"
            "Бирюзовый — система кол-центра банка (платформа подрядчика, CRM-ядро не используется).<br>"
            "Голубой пунктир на схеме интеграций — внешние системы.<br>"
            "Зелёный — Excel: ручной расчёт ставки (ставка ЦБ, объёмы, риск).<br>"
            "Жёлтый — Email: ежедневный файл ставок и разовые согласования.<br>"
            "Фиолетовый / индиго — СМС-канал (АБС → шлюз → телеком).<br>"
            "Синий — интернет-банк (ASP.NET, прямое обращение к БД АБС; депозитов нет).<br>"
            "Розовый — сайт (PHP + React, только маркетинговый контент).<br>"
            "Пустая ячейка (—) — подразделение не использует ИТ для этой возможности.",
            ox,
            ly,
            740,
            210,
            LEGEND_BOX,
            raw=True,
        )
    )
    body.append(
        cell(
            "gaps",
            "<b>Что мешает цифровому депозиту (as-is)</b><br>"
            "1. Открыть депозит можно только в отделении: интернет-банк и сайт "
            "в этой возможности не участвуют.<br>"
            "2. Ставка считается вручную в Excel и ходит по почте — нет сервиса ставок.<br>"
            "3. Каждое открытие требует бэк-офис; спецставки ещё и отдел кредитования.<br>"
            "4. Депозиты и кредиты изолированы по ИБ: нет общей автоматизированной передачи риска.<br>"
            "5. Партнёрский кол-центр не интегрирован с АБС.<br>"
            "6. Договор — бумага: сотрудник печатает, клиент подписывает, скан грузят в АБС.<br>"
            "7. Команда ЦТ пока не владеет системами — только анализирует процесс.",
            ox + 760,
            ly,
            780,
            210,
            NOTE,
            raw=True,
        )
    )

    page_w = ox + org_w + len(caps) * cap_w + 40
    page_h = ly + 240
    return mxfile("IT-ландшафт", "landscape", page_w, page_h, "".join(body))


def integrations() -> str:
    """Swimlanes = process participants; boxes = applications; arrows = integrations."""
    body = []
    body.append(
        cell("title", "Схема интеграции приложений — открытие депозита (as-is)", 40, 16, 1200, 36, TITLE)
    )
    body.append(
        cell(
            "sub",
            "Дорожки — участники процесса. В дорожке — их приложения. Стрелки — обмен данными между системами.",
            40,
            52,
            1200,
            24,
            SUB,
        )
    )

    lanes = [
        ("ln-cl", "Клиент", 110),
        ("ln-cc", "Кол-центр банка", 120),
        ("ln-fo", "Отделение (фронт-офис)", 120),
        ("ln-bo", "Бэк-офис депозитов", 130),
        ("ln-cr", "Отдел кредитования", 130),
        ("ln-it", "Цифровые каналы и IT", 120),
        ("ln-ex", "Внешние системы", 120),
    ]
    lx, ly, lw = 40, 88, 1680
    y = ly
    lane_y = {}
    for lid, label, h in lanes:
        body.append(cell(lid, label, lx, y, lw, h, LANE))
        lane_y[lid] = y
        y += h
    lanes_bottom = y

    # --- boxes (parent = lane so they stay inside) ---
    body.append(cell("a-client", "Клиент", 220, 40, 90, 48, ACTOR, parent="ln-cl"))
    body.append(
        cell(
            "a-visit",
            "Визит в отделение —\nединственный способ открыть депозит",
            380,
            40,
            280,
            44,
            "rounded=1;whiteSpace=wrap;html=1;align=center;verticalAlign=middle;"
            "fillColor=#FEE2E2;strokeColor=#DC2626;fontSize=10;fontColor=#7F1D1D;",
            parent="ln-cl",
        )
    )
    body.append(
        cell(
            "a-sms-in",
            "Получает СМС\nсо ставкой и приглашением",
            1280,
            40,
            200,
            52,
            "rounded=1;whiteSpace=wrap;html=1;align=center;verticalAlign=middle;"
            "fillColor=#EDE9FE;strokeColor=#7C3AED;fontSize=10;",
            parent="ln-cl",
        )
    )

    body.append(cell("a-cc", "Оператор", 220, 44, 80, 68, ACTOR, parent="ln-cc"))
    body.append(
        cell(
            "s-cc",
            "Система кол-центра\nReact + Spring Boot + PostgreSQL\nплатформа подрядчика",
            360,
            42,
            250,
            70,
            big_app(*C_CC),
            parent="ln-cc",
        )
    )

    body.append(cell("a-fo", "Сотрудник\nотделения", 220, 44, 90, 68, ACTOR, parent="ln-fo"))
    body.append(
        cell(
            "s-docs",
            "Бумажный договор\nпечать → подпись → скан в АБС",
            360,
            48,
            230,
            60,
            "rounded=1;whiteSpace=wrap;html=1;align=center;verticalAlign=middle;"
            "fillColor=#E2E8F0;strokeColor=#64748B;fontSize=11;fontStyle=1;",
            parent="ln-fo",
        )
    )

    body.append(cell("a-bo", "Менеджер\nдепозитов", 220, 48, 90, 72, ACTOR, parent="ln-bo"))
    body.append(
        cell(
            "s-mail-bo",
            "Почта бэк-офиса\nзапросы ставок и спецставок",
            360,
            48,
            230,
            64,
            big_app(*C_MAIL),
            parent="ln-bo",
        )
    )

    body.append(cell("a-cr", "Сотрудник\nкредитования", 220, 48, 90, 72, ACTOR, parent="ln-cr"))
    body.append(
        cell(
            "s-xl",
            "Excel-файл ставок\nставка ЦБ + объёмы кредитов/депозитов\n+ риск → итоговая ставка",
            360,
            42,
            250,
            76,
            big_app(*C_XL),
            parent="ln-cr",
        )
    )
    body.append(
        cell(
            "s-mail-cr",
            "Почта кредитов\nежедневная рассылка Excel",
            640,
            48,
            210,
            64,
            big_app(*C_MAIL),
            parent="ln-cr",
        )
    )

    body.append(
        cell(
            "s-ib",
            "Интернет-банк\nASP.NET MVC 4.5 + MS SQL\nплатежи и текущие счета",
            220,
            42,
            250,
            70,
            big_app(*C_IB),
            parent="ln-it",
        )
    )
    body.append(
        cell(
            "s-web",
            "Сайт\nPHP + React\nтолько маркетинг",
            500,
            42,
            200,
            70,
            big_app(*C_WEB),
            parent="ln-it",
        )
    )
    body.append(
        cell(
            "s-sms",
            "СМС-шлюз\nсопровождает IT банка",
            1280,
            42,
            200,
            70,
            big_app(*C_GW),
            parent="ln-it",
        )
    )

    body.append(
        cell(
            "s-pcc",
            "Система партнёрского КЦ\nдругой подрядчик, только скрипты",
            220,
            42,
            250,
            70,
            EXT,
            parent="ln-ex",
        )
    )
    body.append(
        cell(
            "s-cbr",
            "ЦБ РФ\nставка рефинансирования\n(в Excel вручную)",
            500,
            42,
            200,
            70,
            EXT,
            parent="ln-ex",
        )
    )
    body.append(
        cell(
            "s-tel",
            "Телеком-оператор\nдоставка СМС",
            1280,
            42,
            200,
            70,
            EXT,
            parent="ln-ex",
        )
    )

    # Shared ABS spanning operational lanes
    body.append(
        cell(
            "s-abs",
            "АБС — общая система учёта\n"
            "Delphi-клиент + Oracle / PL-SQL\n\n"
            "Разделы:\n"
            "• заявки из кол-центра\n"
            "• кредитный риск (только кредиты)\n"
            "• создание депозита\n"
            "• хранение сканов договора\n\n"
            "Депозиты и кредиты не видят\nданные друг друга (требование ИБ)",
            920,
            210,
            280,
            500,
            big_app(*C_ABS),
        )
    )

    e_base = (
        "edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;"
        "html=1;endArrow=block;endFill=1;strokeWidth=2;fontSize=10;fontColor=#334155;"
        "labelBackgroundColor=#FFFFFF;"
    )
    e_auto = e_base + "strokeColor=#2563EB;"
    e_manual = e_base + "dashed=1;dashPattern=6 6;strokeColor=#D97706;"
    e_gap = e_base + "dashed=1;dashPattern=1 8;strokeColor=#94A3B8;"
    e_people = e_base + "strokeColor=#4F46E5;"
    e_risk = e_base + "dashed=1;dashPattern=6 6;strokeColor=#DC2626;"

    body.append(edge("e-call", "1. звонок\nуточнить депозит", "a-client", "a-cc", e_people))
    body.append(edge("e-visit", "5. визит\n(~20 мин / до 1 ч)", "a-client", "a-fo", e_people))
    body.append(edge("e-ticket", "заводит обращение", "a-cc", "s-cc", e_people))
    body.append(
        edge(
            "e-cc-abs",
            "2. передача обращения",
            "s-cc",
            "s-abs",
            e_auto,
            exit_x=1,
            exit_y=0.5,
            entry_x=0,
            entry_y=0.12,
        )
    )
    body.append(
        edge(
            "e-bo-abs",
            "3. бэк-офис считает ставку\nи фиксирует её в АБС",
            "a-bo",
            "s-abs",
            e_people,
            entry_x=0,
            entry_y=0.38,
        )
    )
    body.append(
        edge(
            "e-abs-sms",
            "4. СМС: ставка готова,\nприходите в отделение",
            "s-abs",
            "s-sms",
            e_auto,
            exit_x=1,
            exit_y=0.08,
            entry_x=0,
            entry_y=0.5,
        )
    )
    body.append(edge("e-sms-tel", "отправка", "s-sms", "s-tel", e_auto))
    body.append(edge("e-tel-cl", "СМС клиенту", "s-tel", "a-sms-in", e_auto))

    body.append(
        edge(
            "e-fo-abs",
            "6. создаёт депозит\nв АБС после согласия",
            "a-fo",
            "s-abs",
            e_people,
            entry_x=0,
            entry_y=0.55,
        )
    )
    body.append(edge("e-fo-docs", "печатает комплект", "a-fo", "s-docs", e_people))
    body.append(
        edge(
            "e-docs-abs",
            "скан подписанных\nдокументов",
            "s-docs",
            "s-abs",
            e_manual,
            entry_x=0,
            entry_y=0.68,
        )
    )

    body.append(
        edge(
            "e-fo-mail",
            "без звонка: письмо\n«какая ставка?»",
            "a-fo",
            "s-mail-bo",
            e_manual,
        )
    )
    body.append(
        edge(
            "e-mail-fo",
            "ответ со ставкой",
            "s-mail-bo",
            "a-fo",
            e_manual,
        )
    )
    body.append(
        edge(
            "e-bo-mail-cr",
            "спецставка: запрос\nв кредиты (нет доступа к их АБС)",
            "s-mail-bo",
            "s-mail-cr",
            e_risk,
        )
    )
    body.append(
        edge(
            "e-cr-abs",
            "смотрит кредитный риск\nпо клиенту (свой раздел АБС)",
            "a-cr",
            "s-abs",
            e_people,
            entry_x=0,
            entry_y=0.82,
        )
    )
    body.append(edge("e-cr-xl", "считает ставку", "a-cr", "s-xl", e_people))
    body.append(edge("e-xl-mail", "вкладывает файл", "s-xl", "s-mail-cr", e_manual))
    body.append(
        edge(
            "e-daily",
            "каждый день: Excel\nс базовыми ставками",
            "s-mail-cr",
            "s-mail-bo",
            e_manual,
        )
    )
    body.append(edge("e-cbr-xl", "ставку ЦБ вносят вручную", "s-cbr", "s-xl", e_manual))
    body.append(
        edge(
            "e-ib-abs",
            "прямой доступ к БД АБС\n(депозиты не открывает)",
            "s-ib",
            "s-abs",
            e_gap,
            exit_x=1,
            exit_y=0.5,
            entry_x=0,
            entry_y=0.95,
        )
    )
    body.append(
        edge(
            "e-web-abs",
            "нет канала заявки\nна депозит",
            "s-web",
            "s-abs",
            e_gap,
        )
    )
    body.append(
        edge(
            "e-pcc",
            "нет интеграции\nс системами банка",
            "s-pcc",
            "s-cc",
            e_gap,
        )
    )

    body.append(
        cell(
            "legend2",
            "<b>Типы связей</b><br>"
            "<font color='#2563EB'><b>━━</b></font> автоматическая интеграция: обращение КЦ→АБС, АБС→СМС.<br>"
            "<font color='#D97706'><b>- - -</b></font> ручной канал: почта, Excel, скан договора, ставка ЦБ.<br>"
            "<font color='#DC2626'><b>- - -</b></font> барьер ИБ: депозиты и кредиты обмениваются только письмами.<br>"
            "<font color='#94A3B8'><b>- · -</b></font> разрыв: система есть, но депозит через неё открыть нельзя.<br>"
            "<font color='#4F46E5'><b>━━</b></font> действие человека (звонок, визит, работа в интерфейсе).<br>"
            "Номера 1–6 — основной сценарий «звонок → СМС → отделение».",
            40,
            lanes_bottom + 16,
            720,
            150,
            LEGEND_BOX,
            raw=True,
        )
    )
    body.append(
        cell(
            "seq",
            "<b>Три сценария as-is</b><br>"
            "<b>A.</b> Звонок → обращение в системе КЦ → АБС → бэк-офис ставит ставку → СМС → визит → договор.<br>"
            "<b>B.</b> Без звонка: визит → письмо бэк-офису → ставка → депозит в АБС. Клиент ждёт в отделении.<br>"
            "<b>C.</b> Спецставка: бэк-офис пишет в кредиты → риск в АБС → Excel → письмо на фронт (до часа).<br>"
            "Интернет-банк уже ходит в БД АБС — это задел для MVP, но не текущий процесс депозита.",
            780,
            lanes_bottom + 16,
            940,
            150,
            NOTE,
            raw=True,
        )
    )

    return mxfile("Интеграции приложений", "integrations", 1760, lanes_bottom + 190, "".join(body))


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "it-landscape.drawio").write_text(landscape(), encoding="utf-8")
    (OUT / "application-integration.drawio").write_text(integrations(), encoding="utf-8")
    print(f"Wrote diagrams to {OUT}")


if __name__ == "__main__":
    main()
