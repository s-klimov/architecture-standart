#!/usr/bin/env python3
"""Generate C4 context and container diagrams for Task 3."""

from pathlib import Path
from xml.sax.saxutils import escape

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "Task3"


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
    return f"""<mxfile host="app.diagrams.net" agent="Task3" version="24.7.17">
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
SYS_CORE = (
    "rounded=1;whiteSpace=wrap;html=1;align=center;verticalAlign=middle;"
    "fontSize=11;fontStyle=1;arcSize=8;fillColor=#FDBA74;strokeColor=#EA580C;fontColor=#111827;"
)
SYS_EXT = (
    "rounded=1;whiteSpace=wrap;html=1;align=center;verticalAlign=middle;dashed=1;"
    "dashPattern=8 8;fillColor=#FEF3C7;strokeColor=#D97706;fontSize=11;fontStyle=1;fontColor=#78350F;"
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
REL_OFF = (
    "edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;"
    "endArrow=block;endFill=1;strokeWidth=1.5;fontSize=10;fontColor=#64748B;"
    "labelBackgroundColor=#FFFFFF;strokeColor=#94A3B8;dashed=1;dashPattern=1 8;"
)


def write_context() -> None:
    b: list[str] = []
    a = b.append
    a(cell("t", "C4: контекст — открытие депозитов, MVP", 40, 16, 900, 32, TITLE))
    a(
        cell(
            "s",
            "Люди и системы вокруг решения. Зелёный — новый контур. Оранжевый — АБС (учёт). Жёлтый пунктир — внешние / вне MVP. Номера на стрелках = Use Case из ADR.",
            40,
            48,
            1400,
            24,
            SUB,
        )
    )

    a(cell("p-new", "Новый клиент", 60, 120, 100, 70, PERSON))
    a(cell("p-ex", "Действующий клиент", 60, 320, 110, 70, PERSON))
    a(cell("p-cc", "Оператор КЦ банка", 60, 560, 110, 70, PERSON))
    a(cell("p-bo", "Менеджер бэк-офиса депозитов", 1480, 200, 150, 80, PERSON))
    a(cell("p-fo", "Сотрудник отделения", 1480, 360, 140, 70, PERSON))
    a(cell("p-cr", "Сотрудник кредитования (ставки)", 1480, 520, 160, 80, PERSON))

    a(cell("bnd", "Банк «Стандарт»", 240, 100, 1180, 620, BOUND))

    a(
        cell(
            "web",
            "Сайт\nPHP + React.js\nвитрина + заявка-лид",
            280,
            160,
            200,
            80,
            SYS,
        )
    )
    a(
        cell(
            "ib",
            "Интернет-банк\nASP.NET MVC 4.5 + MS SQL\nплатежи, счета, вход в депозиты",
            280,
            300,
            220,
            90,
            SYS,
        )
    )
    a(
        cell(
            "dep",
            "Контур заявок и ставок (новый)\nAPI + MS SQL + исходящий буфер\nкоманда банка, без ядра подрядчика",
            580,
            220,
            280,
            110,
            SYS_NEW,
        )
    )
    a(
        cell(
            "abs",
            "АБС\nDelphi + Oracle / PL-SQL\nдоговор, проводка, открытие вклада",
            960,
            220,
            260,
            110,
            SYS_CORE,
        )
    )
    a(
        cell(
            "cc",
            "Система кол-центра\nReact + Spring Boot + PostgreSQL\nплатформа подрядчика",
            580,
            420,
            260,
            90,
            SYS,
        )
    )
    a(
        cell(
            "sms",
            "СМС-шлюз\nсопровождает IT банка",
            960,
            430,
            200,
            70,
            SYS,
        )
    )
    a(
        cell(
            "tel",
            "Телеком-оператор\nдоставка СМС",
            1240,
            140,
            160,
            70,
            SYS_EXT,
        )
    )
    a(
        cell(
            "pcc",
            "Партнёрский КЦ\nвне MVP (+R4)",
            1240,
            620,
            160,
            70,
            SYS_EXT,
        )
    )

    a(edge("e1", "UC1 каталог, UC2 заявка (ФИО, телефон)", "p-new", "web", REL_HUMAN))
    a(edge("e2", "UC5 каталог, UC6 заявка + СМС, UC10 статус", "p-ex", "ib", REL_HUMAN))
    a(edge("e3", "UC3 звонок по лиду, спецставка", "p-cc", "cc", REL_HUMAN))
    a(edge("e4", "UC7 подтверждает условия и открывает вклад", "p-bo", "abs", REL_HUMAN))
    a(edge("e5", "UC4 идентификация, договор", "p-fo", "abs", REL_HUMAN))
    a(edge("e6", "UC9 ведёт ставки (не Excel)", "p-cr", "dep", REL_HUMAN, entry_x=1, entry_y=0.35))
    a(edge("e7", "UC9 тоже смотрит/правит ставки", "p-bo", "dep", REL_HUMAN, entry_x=1, entry_y=0.15))
    a(edge("e8", "HTTPS: каталог и создание заявки", "web", "dep", REL))
    a(edge("e9", "HTTPS: каталог, заявка, OTP, статус", "ib", "dep", REL))
    a(edge("e10", "асинхронно: лид в очередь КЦ", "dep", "cc", REL_ASYNC))
    a(edge("e11", "асинхронно: задача бэку (не API АБС с канала)", "dep", "abs", REL_ASYNC))
    a(edge("e12", "статус «открыт / отказ» обратно в контур", "abs", "dep", REL_ASYNC))
    a(edge("e13", "UC8: ставка подтверждена / вклад открыт; OTP", "dep", "sms", REL))
    a(edge("e14", "отправка", "sms", "tel", REL))
    a(edge("e15", "СМС клиенту", "tel", "p-ex", REL_HUMAN, points=[(1320, 360)]))
    a(edge("e16", "нет доступа к заявкам сайта", "pcc", "cc", REL_OFF))

    a(
        cell(
            "leg",
            "<b>Как читать</b><br>"
            "<font color='#4F46E5'><b>━━</b></font> человек в интерфейсе или получает СМС.<br>"
            "<font color='#2563EB'><b>━━</b></font> синхронный вызов канала (HTTPS/TLS).<br>"
            "<font color='#0D9488'><b>- - -</b></font> асинхронная доставка: заявка не ждёт АБС и КЦ.<br>"
            "<font color='#94A3B8'><b>- · -</b></font> вне MVP: партнёрский КЦ не подключаем.<br>"
            "Каналы <b>не открывают</b> вклад: проводка только в АБС после бэка или визита (F11, +R2).",
            240,
            740,
            1180,
            130,
            NOTE,
            raw=True,
        )
    )

    (OUT / "c4-context.drawio").write_text(
        mxfile("C4 контекст", "c4-context", 1700, 900, "".join(b)),
        encoding="utf-8",
    )


def write_containers() -> None:
    b: list[str] = []
    a = b.append
    a(cell("t", "C4: контейнеры — интернет-банк и АБС (остальные системы снаружи)", 40, 16, 1200, 32, TITLE))
    a(
        cell(
            "s",
            "Внутри пунктира — развёртываемые части. Ядро ИБ не трогаем. Новый контур рядом с монолитом. АБС принимает задачи пакетом, не онлайн-трафик с сайта.",
            40,
            48,
            1500,
            24,
            SUB,
        )
    )

    a(cell("ib-b", "Интернет-банк (детализация)", 40, 100, 520, 420, BOUND))
    a(
        cell(
            "ib-web",
            "Веб-приложение ИБ\nASP.NET MVC 4.5\nядро подрядчика: логин, платежи,\nтекущие счета. Ядро не дорабатываем (S3)",
            60,
            150,
            240,
            110,
            SYS,
        )
    )
    a(
        cell(
            "ib-mod",
            "Модуль депозитов ИБ\nкоманда банка (.NET)\nэкраны каталога, заявки,\nСМС-код, статус (UC5, UC6, UC10)",
            60,
            290,
            240,
            120,
            SYS_NEW,
        )
    )
    a(
        cell(
            "ib-db",
            "БД ИБ\nMS SQL\nсессии, платежи\nбез заявок на депозит",
            330,
            170,
            200,
            90,
            DB,
        )
    )
    a(
        cell(
            "ib-note",
            "Существующий прямой доступ ИБ → БД АБС для платежей не расширяем на депозиты (+R2).",
            330,
            290,
            200,
            100,
            NOTE,
        )
    )

    a(cell("dep-b", "Контур заявок и ставок (новый, рядом с ИБ)", 580, 100, 460, 420, BOUND))
    a(
        cell(
            "api",
            "Сервис заявок и ставок\n.NET, команда банка\nкаталог, персональная ставка,\nзаявка, идемпотентность, статусы",
            600,
            150,
            250,
            110,
            SYS_NEW,
        )
    )
    a(
        cell(
            "rates-ui",
            "Рабочее место ставок\nвеб для бэка депозитов и кредитов\nистория изменений (UC9, S7)",
            600,
            290,
            250,
            90,
            SYS_NEW,
        )
    )
    a(
        cell(
            "dep-db",
            "БД контура\nMS SQL\nзаявки, ставки,\noutbox",
            870,
            150,
            150,
            90,
            DB,
        )
    )
    a(
        cell(
            "cache",
            "Кэш витрины\nбазовые ставки\n(P5)",
            870,
            270,
            150,
            70,
            SYS_NEW,
        )
    )
    a(
        cell(
            "outbox",
            "Исходящий буфер\nтаблица MS SQL\nзадел под Kafka (S4)",
            870,
            360,
            150,
            90,
            SYS_NEW,
        )
    )

    a(cell("abs-b", "АБС (детализация)", 1060, 100, 520, 420, BOUND))
    a(
        cell(
            "abs-ui",
            "Клиент Delphi\nрабочее место отделения и бэка\nUC4, UC7: договор, открытие вклада",
            1080,
            150,
            230,
            110,
            SYS_CORE,
        )
    )
    a(
        cell(
            "abs-adp",
            "Адаптер заявок\nкоманда АБС\nчитает буфер контура,\nкладёт задачу бэку.\nНе принимает HTTPS с сайта/ИБ",
            1080,
            290,
            230,
            130,
            SYS_NEW,
        )
    )
    a(
        cell(
            "abs-pl",
            "Логика PL/SQL\nоткрытие депозита,\nпроводки, скан договора,\nразделы депозиты / кредиты",
            1340,
            150,
            220,
            110,
            SYS_CORE,
        )
    )
    a(
        cell(
            "abs-db",
            "БД АБС\nOracle\nтолько учёт.\nСтавки и очередь сюда не кладём (+R3, R3, P4)",
            1340,
            300,
            220,
            110,
            DB,
        )
    )

    a(
        cell(
            "web",
            "Сайт\nPHP + React\nUC1, UC2",
            60,
            560,
            180,
            70,
            SYS,
        )
    )
    a(
        cell(
            "cc",
            "Система КЦ\nReact / Spring / PostgreSQL\nUC3: карточка лида",
            280,
            560,
            220,
            70,
            SYS,
        )
    )
    a(
        cell(
            "sms",
            "СМС-шлюз\nOTP + UC8",
            600,
            560,
            160,
            70,
            SYS,
        )
    )
    a(
        cell(
            "tel",
            "Телеком\nвнешняя система",
            800,
            560,
            160,
            70,
            SYS_EXT,
        )
    )
    a(
        cell(
            "p-bo",
            "Бэк-офис\nдепозитов",
            1080,
            560,
            100,
            70,
            PERSON,
        )
    )
    a(
        cell(
            "p-fo",
            "Отделение",
            1220,
            560,
            90,
            70,
            PERSON,
        )
    )
    a(
        cell(
            "p-cr",
            "Кредиты\n(ставки)",
            1360,
            560,
            90,
            70,
            PERSON,
        )
    )

    a(edge("c1", "встраивает экраны, без ядра", "ib-web", "ib-mod", REL))
    a(edge("c2", "JDBC / существующие таблицы", "ib-web", "ib-db", REL))
    a(edge("c3", "HTTPS JSON: каталог, заявка, OTP, статус", "ib-mod", "api", REL))
    a(edge("c4", "HTTPS: витрина и лид", "web", "api", REL))
    a(edge("c5", "читает/пишет заявки и ставки", "api", "dep-db", REL))
    a(edge("c6", "базовые ставки из кэша", "api", "cache", REL))
    a(edge("c7", "события в outbox", "api", "outbox", REL_ASYNC))
    a(edge("c8", "CRUD ставок, журнал", "rates-ui", "dep-db", REL))
    a(edge("c9", "лиды в КЦ (асинхронно)", "outbox", "cc", REL_ASYNC))
    a(edge("c10", "задачи на открытие", "outbox", "abs-adp", REL_ASYNC))
    a(edge("c11", "кладёт работу бэку", "abs-adp", "abs-pl", REL))
    a(edge("c12", "PL/SQL → Oracle", "abs-pl", "abs-db", REL))
    a(edge("c13", "UI → процедуры", "abs-ui", "abs-pl", REL))
    a(edge("c14", "статус открытия в контур", "abs-adp", "api", REL_ASYNC))
    a(edge("c15", "OTP и уведомления", "api", "sms", REL))
    a(edge("c16", "отправка", "sms", "tel", REL))
    a(edge("c17", "открывает вклад в Delphi", "p-bo", "abs-ui", REL_HUMAN))
    a(edge("c18", "идентификация, договор", "p-fo", "abs-ui", REL_HUMAN))
    a(edge("c19", "ведёт ставки", "p-cr", "rates-ui", REL_HUMAN, points=[(1405, 500), (725, 500)]))

    a(
        cell(
            "teams",
            "<b>Кто делает (IT-команды)</b><br>"
            "<b>ИБ банка (10)</b> — модуль депозитов и сервис заявок/ставок, без подрядчика ядра.<br>"
            "<b>АБС (20)</b> — адаптер, сценарий бэка в Delphi/PL-SQL, открытие вклада. Java-люди из АБС помогают КЦ.<br>"
            "<b>Сайт</b> — форма лида и витрина на PHP/React.<br>"
            "<b>КЦ подрядчика (5)</b> — карточка заявки с сайта; партнёрский КЦ не трогаем.<br>"
            "<b>IT банка / СМС</b> — шлюз для OTP и событий заявки.<br>"
            "<b>ЦТ (10)</b> — контракты, статусы, этот ADR. Подрядчик ИБ в MVP не нужен (S3).",
            40,
            660,
            760,
            170,
            NOTE,
            raw=True,
        )
    )
    a(
        cell(
            "flow",
            "<b>Потоки, которые закрывают Use Cases</b><br>"
            "<b>Сайт:</b> UC1 кэш ставок → UC2 заявка в БД контура → outbox → КЦ (UC3) → визит (UC4) → АБС.<br>"
            "<b>ИБ:</b> UC5 персональная ставка → UC6 заявка + OTP через шлюз → бэк в АБС (UC7) → UC8 СМС и UC10 статус.<br>"
            "<b>Ставки:</b> UC9 в рабочем месте контура, не в Oracle и не в Excel.<br>"
            "Интерактив (сотни мс) идёт в MS SQL/кэш. АБС и КЦ — сзади очереди (R3, R4, P1, P4).",
            820,
            660,
            760,
            170,
            NOTE,
            raw=True,
        )
    )

    (OUT / "c4-containers.drawio").write_text(
        mxfile("C4 контейнеры", "c4-containers", 1640, 860, "".join(b)),
        encoding="utf-8",
    )


def main() -> None:
    OUT.mkdir(exist_ok=True)
    write_context()
    write_containers()
    print(f"Wrote {OUT / 'c4-context.drawio'}")
    print(f"Wrote {OUT / 'c4-containers.drawio'}")


if __name__ == "__main__":
    main()
