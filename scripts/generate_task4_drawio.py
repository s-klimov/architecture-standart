#!/usr/bin/env python3
"""Generate C4 and roadmap diagrams for Task 4 (rates to call centers)."""

from pathlib import Path
from xml.sax.saxutils import escape

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "Task4"


def cell(
    cid: str,
    value: str,
    x: float,
    y: float,
    w: float,
    h: float,
    style: str,
    parent: str = "1",
    raw: bool = False,
) -> str:
    text = value if raw else escape(value)
    return (
        f'        <mxCell id="{cid}" value="{text}" style="{style}" '
        f'vertex="1" parent="{parent}">\n'
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
        geo_extra = f'<Array as="points">{pts}</Array>'
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
    return f"""<mxfile host="app.diagrams.net" agent="Task4" version="24.7.17">
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


TITLE = (
    "text;html=1;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;"
    "fontSize=20;fontStyle=1;fontColor=#1F2937;fontFamily=Helvetica;"
)
SUB = (
    "text;html=1;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;"
    "fontSize=12;fontColor=#4B5563;fontFamily=Helvetica;"
)
PERSON = (
    "shape=actor;whiteSpace=wrap;html=1;align=center;verticalAlign=bottom;"
    "fillColor=#E0E7FF;strokeColor=#4338CA;fontSize=11;fontStyle=1;fontColor=#1E1B4B;"
)
SYS = (
    "rounded=1;whiteSpace=wrap;html=1;align=center;verticalAlign=middle;"
    "fontSize=11;fontStyle=1;arcSize=8;fillColor=#BFDBFE;strokeColor=#2563EB;fontColor=#111827;"
)
SYS_NEW = (
    "rounded=1;whiteSpace=wrap;html=1;align=center;verticalAlign=middle;"
    "fontSize=11;fontStyle=1;arcSize=8;fillColor=#99F6E4;strokeColor=#0D9488;fontColor=#111827;"
)
SYS_EXT = (
    "rounded=1;whiteSpace=wrap;html=1;align=center;verticalAlign=middle;dashed=1;"
    "dashPattern=8 8;fillColor=#FEF3C7;strokeColor=#D97706;fontSize=11;fontStyle=1;fontColor=#78350F;"
)
COMP = (
    "rounded=1;whiteSpace=wrap;html=1;align=center;verticalAlign=middle;"
    "fontSize=10;fontStyle=0;arcSize=8;fillColor=#CCFBF1;strokeColor=#0F766E;fontColor=#111827;"
)
BOUND = (
    "rounded=1;whiteSpace=wrap;html=1;dashed=1;dashPattern=8 8;fillColor=none;"
    "strokeColor=#64748B;verticalAlign=top;align=left;fontSize=12;fontStyle=1;"
    "fontColor=#334155;spacingLeft=8;spacingTop=4;"
)
DB = (
    "shape=cylinder3;whiteSpace=wrap;html=1;boundedLbl=1;backgroundOutline=1;"
    "size=12;align=center;verticalAlign=middle;fillColor=#E2E8F0;strokeColor=#475569;"
    "fontSize=10;fontStyle=1;fontColor=#111827;"
)
NOTE = (
    "rounded=1;whiteSpace=wrap;html=1;align=left;verticalAlign=top;"
    "fillColor=#F8FAFC;strokeColor=#94A3B8;fontSize=11;fontColor=#1F2937;"
    "spacingLeft=10;spacingRight=10;spacingTop=8;"
)
REL = (
    "edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;"
    "endArrow=block;endFill=1;strokeWidth=1.5;fontSize=10;fontColor=#334155;"
    "labelBackgroundColor=#FFFFFF;strokeColor=#2563EB;"
)
REL_ASYNC = (
    "edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;"
    "endArrow=block;endFill=1;strokeWidth=1.5;fontSize=10;fontColor=#334155;"
    "labelBackgroundColor=#FFFFFF;strokeColor=#0D9488;dashed=1;dashPattern=6 6;"
)
REL_HUMAN = (
    "edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;"
    "endArrow=block;endFill=1;strokeWidth=1.5;fontSize=10;fontColor=#334155;"
    "labelBackgroundColor=#FFFFFF;strokeColor=#4F46E5;"
)

# Roadmap
CHEVRON = (
    "shape=step;perimeter=stepPerimeter;whiteSpace=wrap;html=1;fixedSize=1;"
    "size=24;fillColor=#9CA3AF;strokeColor=#6B7280;fontSize=16;fontStyle=1;"
    "fontColor=#111827;align=center;"
)
CHEVRON2 = (
    "shape=step;perimeter=stepPerimeter;whiteSpace=wrap;html=1;fixedSize=1;"
    "size=24;fillColor=#6B7280;strokeColor=#4B5563;fontSize=16;fontStyle=1;"
    "fontColor=#FFFFFF;align=center;"
)
LANE = (
    "rounded=0;whiteSpace=wrap;html=1;align=center;verticalAlign=middle;"
    "fillColor=#E5E7EB;strokeColor=#9CA3AF;fontSize=12;fontStyle=1;fontColor=#111827;"
)
LANE_BG = (
    "rounded=0;whiteSpace=wrap;html=1;fillColor=#FEF9C3;strokeColor=#E5E7EB;"
    "fontColor=#111827;"
)
BAR = (
    "rounded=1;whiteSpace=wrap;html=1;align=center;verticalAlign=middle;"
    "fillColor=#FDBA74;strokeColor=#EA580C;fontSize=10;fontStyle=1;fontColor=#111827;"
    "arcSize=12;"
)
BAR_YEAR = (
    "rounded=1;whiteSpace=wrap;html=1;align=center;verticalAlign=middle;"
    "fillColor=#93C5FD;strokeColor=#2563EB;fontSize=10;fontStyle=1;fontColor=#111827;"
    "arcSize=12;"
)
MONTH = (
    "text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;"
    "fontSize=11;fontStyle=1;fontColor=#374151;"
)


def write_context() -> None:
    b: list[str] = []
    a = b.append
    a(cell("t", "C4: контекст — передача ставок в кол-центры", 40, 16, 1100, 32, TITLE))
    a(
        cell(
            "s",
            "Только этот кейс. Зелёный — контур-источник ставок. Синий — КЦ банка и канал файлов. Жёлтый пунктир — партнёр. Номера на стрелках = UC из Task4/ADR.md. Сайт, ИБ и АБС сюда не кладём: они не меняют шов «ставки → КЦ».",
            40,
            48,
            1480,
            36,
            SUB,
        )
    )

    a(cell("p-cli", "Клиент\n(часто пожилой)", 40, 200, 120, 80, PERSON))
    a(cell("p-cc", "Оператор\nКЦ банка", 40, 380, 120, 80, PERSON))
    a(cell("p-pcc", "Оператор\nпартнёрского КЦ", 40, 580, 130, 80, PERSON))
    a(cell("p-bo", "Менеджер ставок\n(депозиты / кредиты)", 1480, 240, 160, 90, PERSON))

    a(cell("bnd", "Банк «Стандарт»", 220, 120, 1220, 520, BOUND))

    a(
        cell(
            "dep",
            "Контур заявок и ставок\nрабочее место + API каталога\n+ экспортёр файла\nкоманда банка, .NET / MS SQL",
            620,
            200,
            280,
            120,
            SYS_NEW,
        )
    )
    a(
        cell(
            "cc",
            "Система кол-центра банка\nReact + Spring Boot + PostgreSQL\nвиджет ставок у оператора",
            280,
            360,
            260,
            100,
            SYS,
        )
    )
    a(
        cell(
            "sftp",
            "Канал выкладки файлов\nкаталог + УЗ партнёра\nсопровождает IT банка",
            1000,
            380,
            240,
            100,
            SYS,
        )
    )
    a(
        cell(
            "pcc",
            "Система партнёрского КЦ\nвнешняя ИС, не API банка\nзабор файла + свои скрипты",
            1000,
            560,
            260,
            100,
            SYS_EXT,
        )
    )

    a(edge("e1", "UC2 звонок: «какие сейчас ставки?»", "p-cli", "p-cc", REL_HUMAN))
    a(
        edge(
            "e1b",
            "UC5 тот же вопрос, если КЦ банка перегружен",
            "p-cli",
            "p-pcc",
            REL_HUMAN,
            points=[(100, 520)],
        )
    )
    a(edge("e2", "UC2 смотрит актуальные ставки в UI", "p-cc", "cc", REL_HUMAN))
    a(edge("e3", "UC5 консультирует по загруженному файлу", "p-pcc", "pcc", REL_HUMAN))
    a(edge("e4", "UC1 публикует базовые ставки (не Excel)", "p-bo", "dep", REL_HUMAN))
    a(edge("e5", "UC2 HTTPS: каталог той же версии, что витрина", "cc", "dep", REL))
    a(edge("e6", "UC3 файл-снимок опубликованной версии", "dep", "sftp", REL_ASYNC))
    a(edge("e7", "UC4 партнёр забирает файл (не вызывает API)", "sftp", "pcc", REL_ASYNC))

    a(
        cell(
            "leg",
            "<b>Как читать</b><br>"
            "<font color='#4F46E5'><b>━━</b></font> человек (звонок или работа в UI).<br>"
            "<font color='#2563EB'><b>━━</b></font> синхронный HTTPS внутри банка: КЦ → каталог контура.<br>"
            "<font color='#0D9488'><b>- - -</b></font> файл: банк выкладывает, партнёр забирает. Это не API контура.<br>"
            "В файле только <b>базовые</b> ставки. Заявки, ПДн и спецставки партнёру не отдаём.",
            220,
            660,
            1220,
            130,
            NOTE,
            raw=True,
        )
    )

    (OUT / "c4-context.drawio").write_text(
        mxfile("C4 контекст", "c4-context-t4", 1680, 820, "".join(b)),
        encoding="utf-8",
    )


def write_components() -> None:
    b: list[str] = []
    a = b.append
    a(cell("t", "C4: компоненты — контур ставок и кол-центр банка", 40, 16, 1200, 32, TITLE))
    a(
        cell(
            "s",
            "Внутри пунктира — части, которые трогаем ради этого кейса. Партнёр и канал файлов снаружи. АБС на схеме нет: справочник в неё не кладём.",
            40,
            48,
            1500,
            24,
            SUB,
        )
    )

    a(cell("p-bo", "Менеджер ставок", 40, 200, 110, 70, PERSON))
    a(cell("p-cc", "Оператор КЦ банка", 40, 430, 120, 70, PERSON))
    a(cell("p-pcc", "Оператор партнёра", 40, 680, 120, 70, PERSON))

    a(cell("dep-b", "Контур заявок и ставок (детализация компонентов)", 200, 100, 820, 420, BOUND))
    a(
        cell(
            "wp",
            "Рабочее место ставок\nпубликация версии\nUC1",
            220,
            160,
            180,
            80,
            COMP,
        )
    )
    a(
        cell(
            "api",
            "Сервис каталога\nбазовые ставки из кэша\nтот же API, что сайт/ИБ",
            440,
            160,
            200,
            80,
            SYS_NEW,
        )
    )
    a(cell("cache", "Кэш витрины\nактуальная версия", 680, 150, 140, 70, SYS))
    a(cell("db", "БД контура\nMS SQL\nмастер версий", 680, 250, 140, 90, DB))
    a(
        cell(
            "exp",
            "Экспортёр файлов\nснимок версии N\nпо событию + по таймеру\nUC3",
            440,
            300,
            200,
            90,
            SYS_NEW,
        )
    )
    a(
        cell(
            "out",
            "Задание на выгрузку\nтаблица MS SQL\n«N не выложена / выложена»",
            220,
            320,
            190,
            80,
            DB,
        )
    )

    a(cell("cc-b", "Система КЦ банка", 1060, 160, 280, 240, BOUND))
    a(
        cell(
            "cc-ui",
            "UI оператора\nвиджет актуальных ставок\nUC2",
            1080,
            210,
            240,
            70,
            SYS,
        )
    )
    a(
        cell(
            "cc-ad",
            "Адаптер ставок (Java)\nHTTPS → сервис каталога\nне АБС, не файл партнёра",
            1080,
            300,
            240,
            80,
            SYS_NEW,
        )
    )

    a(
        cell(
            "sftp",
            "Канал выкладки файлов\nкаталог, УЗ, ретеншн\nIT банка · UC4",
            440,
            560,
            240,
            80,
            SYS,
        )
    )
    a(
        cell(
            "pcc",
            "Система партнёрского КЦ\nзагрузка файла + скрипт\nчёрный ящик · UC5",
            780,
            640,
            240,
            90,
            SYS_EXT,
        )
    )

    a(edge("h1", "публикует базовые ставки", "p-bo", "wp", REL_HUMAN))
    a(edge("h2", "открывает виджет на звонке", "p-cc", "cc-ui", REL_HUMAN))
    a(edge("h3", "видит ставки из загруженного файла", "p-pcc", "pcc", REL_HUMAN))

    a(edge("c1", "сохраняет версию", "wp", "db", REL))
    a(edge("c2", "обновляет кэш", "wp", "cache", REL, points=[(530, 140)]))
    a(edge("c3", "ставит задание «выгрузить N»", "wp", "out", REL))
    a(edge("c4", "читает опубликованную версию", "api", "cache", REL))
    a(edge("c5", "мастер при промахе кэша", "api", "db", REL))
    a(edge("c6", "HTTPS каталог версии N", "cc-ad", "api", REL))
    a(edge("c7", "показывает цифры оператору", "cc-ui", "cc-ad", REL))
    a(edge("c8", "забирает задание", "exp", "out", REL_ASYNC))
    a(edge("c9", "читает версию N", "exp", "db", REL))
    a(edge("c10", "кладёт файл + контрольная сумма", "exp", "sftp", REL_ASYNC))
    a(edge("c11", "партнёр забирает файл (не API)", "sftp", "pcc", REL_ASYNC))

    a(
        cell(
            "leg",
            "<b>Граница ответственности</b><br>"
            "Сервис каталога — онлайн для своих. Экспортёр — снимок для чужих. "
            "Менять транспорт файла можно, не трогая виджет КЦ и сайт.<br>"
            "Персональные и особые ставки в экспортёр <b>не попадают</b>.",
            1060,
            430,
            400,
            130,
            NOTE,
            raw=True,
        )
    )

    (OUT / "c4-components.drawio").write_text(
        mxfile("C4 компоненты", "c4-components-t4", 1520, 820, "".join(b)),
        encoding="utf-8",
    )


def write_roadmap() -> None:
    # Layout: label col + 12 months
    label_w = 250
    month_w = 92
    header_y = 90
    lane_h = 84
    lane_gap = 6
    grid_x = 40 + label_w
    grid_y = 170
    months = 12

    systems = [
        ("lane-dep", "Контур заявок и ставок"),
        ("lane-sftp", "Канал выкладки файлов"),
        ("lane-cc", "Система КЦ банка"),
        ("lane-pcc", "Партнёрский КЦ"),
        ("lane-web", "Сайт"),
        ("lane-ib", "Интернет-банк"),
        ("lane-abs", "АБС"),
        ("lane-sms", "СМС-шлюз"),
    ]

    # (id, label, lane_index, start_month 1-12, duration_months, year_style)
    tasks = [
        ("t1", "T1 — Справочник и рабочее место ставок", 0, 1, 2, False),
        ("t2", "T2 — API каталога + кэш", 0, 2, 2, False),
        ("t3", "T3 — Экспортёр файла ставок", 0, 4, 2, False),
        ("t4", "T4 — Каталог, УЗ, журнал забора", 1, 4, 2, False),
        ("t56", "T5–T6 — Адаптер и виджет ставок", 2, 3, 3, False),
        ("t7", "T7 — Карточка лида с сайта", 2, 3, 3, False),
        ("t89", "T8–T9 — Файл + скрипты консультации", 3, 5, 2, False),
        ("t10", "T10 — Витрина и заявка-лид", 4, 2, 4, False),
        ("t11", "T11 — Модуль депозитов (без ядра)", 5, 2, 4, False),
        ("t16", "T16 — Kafka вместо буфера", 5, 8, 2, True),
        ("t17", "T17 — Активный резерв / 99,9%", 5, 10, 3, True),
        ("t12", "T12 — Адаптер и ручное открытие", 6, 3, 4, False),
        ("t14", "T14 — Автооткрытие без бэка", 6, 7, 4, True),
        ("t15", "T15 — Отделение: только фронт", 6, 9, 3, True),
        ("t13", "T13 — OTP и уведомления", 7, 4, 3, False),
    ]

    # Two bars in one lane need vertical offset when they overlap
    # Handle overlaps per lane
    placed: dict[int, list[tuple[int, int]]] = {i: [] for i in range(len(systems))}

    def bar_geom(lane_i: int, start: int, dur: int) -> tuple[float, float, float, float]:
        y0 = grid_y + lane_i * (lane_h + lane_gap)
        overlaps = 0
        for s, d in placed[lane_i]:
            if not (start + dur - 1 < s or start > s + d - 1):
                overlaps += 1
        placed[lane_i].append((start, dur))
        bar_h = 28
        if overlaps == 0:
            y = y0 + 8
        else:
            y = y0 + 42
        x = grid_x + (start - 1) * month_w + 4
        w = dur * month_w - 8
        return x, y, w, bar_h

    b: list[str] = []
    a = b.append
    a(cell("t", "Roadmap: MVP (6 месяцев) и целевое решение (год)", 40, 16, 1100, 32, TITLE))
    a(
        cell(
            "s",
            "Оранжевые полосы — поставка к кампании и MVP заявки. Синие — горизонт года. Номера = Task4/tasks.md. Сначала ставки и API, потом КЦ банка и файл партнёра; автооткрытие — после живого адаптера АБС.",
            40,
            48,
            1500,
            32,
            SUB,
        )
    )

    mvp_w = 6 * month_w
    year_w = 6 * month_w
    a(cell("ch1", "Месяцы 1–6  ·  MVP и кампания", grid_x, header_y, mvp_w, 40, CHEVRON))
    a(cell("ch2", "Месяцы 7–12  ·  цель на год", grid_x + mvp_w, header_y, year_w, 40, CHEVRON2))

    for i in range(months):
        a(
            cell(
                f"m{i+1}",
                str(i + 1),
                grid_x + i * month_w,
                header_y + 44,
                month_w,
                22,
                MONTH,
            )
        )

    grid_w = months * month_w
    for i, (sid, title) in enumerate(systems):
        y = grid_y + i * (lane_h + lane_gap)
        a(cell(f"{sid}-bg", "", grid_x, y, grid_w, lane_h, LANE_BG))
        a(cell(sid, title, 40, y, label_w, lane_h, LANE))
        # month grid ticks
        for m in range(months + 1):
            a(
                cell(
                    f"g-{i}-{m}",
                    "",
                    grid_x + m * month_w,
                    y,
                    1,
                    lane_h,
                    "endArrow=none;strokeColor=#E5E7EB;fillColor=#E5E7EB;",
                )
            )

    # vertical split after month 6
    split_h = len(systems) * (lane_h + lane_gap) - lane_gap
    a(
        cell(
            "split",
            "",
            grid_x + 6 * month_w,
            grid_y,
            2,
            split_h,
            "endArrow=none;strokeColor=#6B7280;fillColor=#6B7280;",
        )
    )

    for tid, label, lane_i, start, dur, is_year in tasks:
        x, y, w, h = bar_geom(lane_i, start, dur)
        a(cell(tid, label, x, y, w, h, BAR_YEAR if is_year else BAR))

    legend_y = grid_y + len(systems) * (lane_h + lane_gap) + 16
    a(
        cell(
            "leg",
            "<b>Как читать план</b><br>"
            "<font color='#EA580C'><b>▮</b></font> 6 месяцев: справочник → API → виджет КЦ банка и файл партнёра; параллельно сайт, модуль ИБ, адаптер АБС, СМС. "
            "Кампанию не стартовать до T6 и T8/T9.<br>"
            "<font color='#2563EB'><b>▮</b></font> Год: автооткрытие и «только фронт» в отделении; Kafka и 99,9% — не условие MVP.<br>"
            "Партнёр подключается <b>после</b> экспортёра (T3) и канала выкладки (T4). АБС ставки не делает.",
            40,
            legend_y,
            grid_x + grid_w - 40,
            110,
            NOTE,
            raw=True,
        )
    )

    page_w = grid_x + grid_w + 40
    page_h = legend_y + 140
    (OUT / "roadmap.drawio").write_text(
        mxfile("Roadmap", "roadmap-t4", page_w, page_h, "".join(b)),
        encoding="utf-8",
    )


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    write_context()
    write_components()
    write_roadmap()
    print("Wrote", OUT / "c4-context.drawio")
    print("Wrote", OUT / "c4-components.drawio")
    print("Wrote", OUT / "roadmap.drawio")


if __name__ == "__main__":
    main()
