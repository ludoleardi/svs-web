import reflex as rx

config = rx.Config(
    app_name="scenic_vision",
    favicon="/favicon.ico",  # Percorso relativo alla cartella assets
)

def service_card(number: str, title: str, description: str, detail: str) -> rx.Component:
    return rx.box(
        rx.text(number, class_name="service-number"),
        rx.heading(title, class_name="service-title", as_="h3"),
        rx.text(description, class_name="service-copy"),
        rx.text(detail, class_name="service-detail"),
        class_name="service-card",
    )

def work_card(
    title: str,
    subtitle: str,
    credit: str,
    image_class: str,
) -> rx.Component:
    return rx.box(
        rx.box(class_name=f"work-image {image_class}"),
        rx.box(
            rx.text(credit, class_name="work-credit"),
            rx.heading(title, class_name="work-title", as_="h3"),
            rx.text(subtitle, class_name="work-subtitle"),
            rx.text("↗", class_name="work-arrow"),
            class_name="work-caption",
        ),
        class_name="work-card",
    )

def page(italian: bool = True) -> rx.Component:
    text = {
        "nav_services": "Servizi" if italian else "Services",
        "nav_work": "Progetti" if italian else "Selected work",
        "nav_about": "Chi siamo" if italian else "About",
        "nav_contact": "Parliamone ↗" if italian else "Let's talk ↗",
        "hero_eyebrow": "PRODUZIONE LIVE / LIGHTING DESIGN" if italian else "LIVE PRODUCTION / LIGHTING DESIGN",
        "hero_title_1": "Audio, luci e produzione." if italian else "Audio, lighting & production.",
        "hero_title_2": "Costruiamo il tuo show, dal concept al palco." if italian else "We build your show, from concept to stage.",
        "hero_copy": (
            "Partner di produzione creativo / tecnico e studio di lighting design per artisti, eventi ed esperienze live"
            if italian
            else "A creative / technical production partner and lighting design studio for artists, events and live experiences."
        ),
        "work_button": "Scopri i progetti" if italian else "Explore our work",
        "talk_button": "Parliamone ↗" if italian else "Start a conversation ↗",
        "side_1": "DALLA PRIMA IDEA" if italian else "FROM THE FIRST IDEA",
        "side_2": "ALL'ULTIMA SCENA." if italian else "TO THE FINAL CUE.",
        "stages": ["IDEA", "PROGETTAZIONE", "PRODUZIONE", "LIVE"]
        if italian
        else ["IDEA", "DESIGN", "PRODUCTION", "LIVE"],
        "ticker": "INDIPENDENTI PER NATURA  ·  FATTI PER IL LIVE" if italian else "INDEPENDENT BY NATURE  ·  BUILT FOR THE LIVE MOMENT",
        "section_studio": "01  /  LO STUDIO" if italian else "01  /  THE STUDIO",
        "intro_title": "Dal primo schizzo all'ultimo encore." if italian else "From the first sketch to the last encore.",
        "intro_copy": (
            "Scenic Vision Studio unisce visione creativa e precisione tecnica, trasformando idee in esperienze live uniche. Affianchiamo artisti e organizzatori "
            "dal concept alla messa in scena, per dare forma a ogni dettaglio curando luce, suono, regia e logistica."
            if italian
            else "Scenic Vision Studio brings creative vision and technical precision together. We work alongside artists "
            "and organisers from concept to showtime, making every detail feel like it belongs."
        ),
        "about_link": "Scopri chi siamo ↗" if italian else "A little more about us ↗",
        "section_services": "02  /  COSA FACCIAMO" if italian else "02  /  WHAT WE DO",
        "services_title": "Un team. Ogni dettaglio." if italian else "One team. Every moving part.",
        "services_intro": (
            "Creatività, precisione tecnica e un team che conosce il ritmo dello show."
            if italian
            else "Creative thinking, technical rigour, and a crew that knows showtime."
        ),
        "service_titles": ["Produzione live", "Progettazione tecnica", "Logistica"]
        if italian
        else ["Live production", "System design", "Logistics"],
        "service_copies": [
            "Creiamo l'identità visiva e sonora del tuo show: atmosfera, cue e momenti che restano.",
            "Audio, luci, strutture e reti di controllo progettati come un sistema affidabile e integrato.",
            "Dal singolo evento al tour, coordiniamo crew, attrezzature e tempistiche, perché la creatività sia sempre al centro.",
        ]
        if italian
        else [
            "We build a visual and sound identity for your show. We shape the atmosphere, the cues and the moments that stay with people.",
            "Audio, lighting, structures and control networks, designed as one reliable and considered system.",
            "From one-night events to tours, we coordinate crews, equipment, and schedules, ensuring creativity is always center-stage.",
        ],
        "service_details": [
            "CONCEPT  ·  PROGRAMMAZIONE  ·  SHOW",
            "AUDIO  ·  LUCI  ·  CONTROLLO",
            "CREW  ·  ATTREZZATURE  ·  TEMPI",
        ]
        if italian
        else [
            "CONCEPT  ·  PROGRAMMING  ·  SHOW",
            "AUDIO  ·  LIGHT  ·  CONTROL",
            "CREW  ·  EQUIPMENT  ·  TIMING",
        ],
        "section_work": "03  /  PROGETTI SELEZIONATI" if italian else "03  /  SELECTED WORK",
        "work_title": "Alcuni eventi a cui abbiamo contribuito." if italian else "A few events we helped bring to life.",
        "work_cta": "Il prossimo progetto potrebbe essere il tuo ↗" if italian else "Your event could be the next ↗",
        "work_1_sub": "Quella Che Chiami Normalità · Tour Ribelle",
        "work_1_credit": "TOUR  /  2025—26",
        "work_2_sub": "Sofà So Good · Sofarm · Torino Music Forum",
        "work_2_credit": "FESTIVAL  /  2024—26",
        "work_3_sub": "Fornitura audio e luci" if italian else "Audio and lighting provider",
        "work_3_credit": "EVENTO LIVE  /  2023—26" if italian else "LIVE EVENT  /  2023—26",
        "section_about": "04  /  IL TEAM" if italian else "04  /  THE TEAM",
        "about_title": "Un team su misura. L'esperienza per realizzare grandi idee."
        if italian
        else "Small enough to care. Experienced enough to deliver.",
        "about_copy": (
            "Siamo un team affiatato e collaborativo. Diamo spazio alle grandi idee e ci prendiamo cura dei dettagli "
            "che le trasformano in realtà."
            if italian
            else "We’re a close-knit team with a collaborative mindset. We make space for the big idea, then take care "
            "of the details that make it real."
        ),
        "about_cta": "Raccontaci il tuo progetto ↗" if italian else "Tell us what you’re planning ↗",
        "stat_years": "anni nel mondo dello spettacolo" if italian else "years in the live industry",
        "stat_events": "eventi prodotti" if italian else "events produced",
        "stat_designs": "disegni tecnici realizzati" if italian else "technical designs",
        "contact_eyebrow": "HAI UNO SHOW IN MENTE?" if italian else "HAVE A SHOW IN MIND?",
        "contact_1": "Diamo forma" if italian else "Let’s make it",
        "contact_2": "a una serata indimenticabile." if italian else "a night to remember.",
        "contact_cta": "Raccontaci la tua idea ↗" if italian else "Tell us about it ↗",
        "footer_note": "Visione creativa. Precisione tecnica. Emozioni dal vivo."
        if italian
        else "Creative vision. Technical precision. Live impact.",
        "footer_credit": "FATTO PER IL LIVE" if italian else "MADE FOR THE LIVE MOMENT",
    }

    def service(index: int, title: str) -> rx.Component:
        return service_card(
            f"{index:02}",
            title,
            text["service_copies"][index - 1],
            text["service_details"][index - 1],
        )

    english_active = not italian

    return rx.box(
        rx.box(
            rx.link(
                rx.box(
                    #rx.text("SVS", class_name="brand-mark"),
                    rx.image("svsletter.png", class_name="brand-mark"),
                    rx.box(
                        rx.text("SCENIC VISION", class_name="brand-name"),
                        rx.text("STUDIO", class_name="brand-caption"),
                    ),
                    class_name="brand-lockup",
                ),
                href="#top",
                class_name="brand",
            ),
            rx.hstack(
                rx.link(text["nav_services"], href="#services"),
                rx.link(text["nav_work"], href="#work"),
                rx.link(text["nav_about"], href="#about"),
                rx.link(text["nav_contact"], href="mailto:studio@scenicvisionstudio.it", class_name="nav-contact"),
                rx.box(
                    rx.link("EN", href="/en", class_name="language-link language-active" if english_active else "language-link"),
                    rx.text("/", class_name="language-divider"),
                    rx.link("IT", href="/", class_name="language-link language-active" if italian else "language-link"),
                    class_name="language-switch",
                ),
                class_name="header-links",
                spacing="6",
            ),
            class_name="site-header",
        ),
        rx.box(
            rx.box(
                rx.box(
                    rx.text(text["hero_eyebrow"], class_name="eyebrow hero-eyebrow"),
                    rx.heading(
                        rx.text(text["hero_title_1"], class_name="title-line", as_="span"),
                        rx.text(text["hero_title_2"], class_name="title-line title-accent", as_="span"),
                        class_name="hero-title",
                        as_="h1",
                    ),
                    rx.text(text["hero_copy"], class_name="hero-copy"),
                    rx.hstack(
                        rx.link(text["work_button"], href="#work", class_name="button button-orange"),
                        rx.link(text["talk_button"], href="mailto:studio@scenicvisionstudio.it", class_name="button button-quiet"),
                        class_name="hero-actions",
                        spacing="4",
                    ),
                    class_name="hero-content",
                ),
                rx.box(
                    rx.text(text["side_1"], class_name="hero-side"),
                    rx.text(text["side_2"], class_name="hero-side hero-side-orange"),
                    class_name="hero-side-note",
                ),
                class_name="hero-inner",
            ),
            rx.box(
                *(rx.text(label, class_name="hero-label") for label in text["stages"]),
                class_name="hero-bottom",
            ),
            id="top",
            class_name="hero",
        ),
        rx.box(
            rx.text(text["ticker"], class_name="ticker-text"),
            class_name="ticker",
        ),
        rx.box(
            rx.box(
                rx.text(text["section_studio"], class_name="eyebrow"),
                rx.heading(
                    text["intro_title"],
                    class_name="intro-title",
                    as_="h2",
                ),
                class_name="intro-heading",
            ),
            rx.box(
                rx.text(text["intro_copy"], class_name="intro-copy"),
                rx.link(text["about_link"], href="#about", class_name="text-link"),
                class_name="intro-description",
            ),
            class_name="intro section-wrap",
        ),
        rx.box(
            rx.box(
                rx.box(
                    rx.text(text["section_services"], class_name="eyebrow"),
                    rx.heading(text["services_title"], class_name="section-title", as_="h2"),
                ),
                rx.text(text["services_intro"], class_name="section-lede"),
                class_name="section-heading-row",
            ),
            rx.box(
                *(service(i, title) for i, title in enumerate(text["service_titles"], 1)),
                class_name="services-grid",
            ),
            id="services",
            class_name="services section-wrap",
        ),
        rx.box(
            rx.box(
                rx.box(
                    rx.text(text["section_work"], class_name="eyebrow"),
                    rx.heading(text["work_title"], class_name="section-title", as_="h2"),
                ),
                rx.link(text["work_cta"], href="mailto:studio@scenicvisionstudio.it", class_name="text-link"),
                class_name="section-heading-row work-heading",
            ),
            rx.box(
                work_card(
                    "I Boschi Bruciano",
                    text["work_1_sub"],
                    text["work_1_credit"],
                    "work-image-one",
                ),
                work_card(
                    "Sofà So Good Torino",
                    text["work_2_sub"],
                    text["work_2_credit"],
                    "work-image-two",
                ),
                work_card(
                    "TEDx Cuneo",
                    text["work_3_sub"],
                    text["work_3_credit"],
                    "work-image-three",
                ),
                class_name="work-grid",
            ),
            id="work",
            class_name="work section-wrap",
        ),
        rx.box(
            rx.box(
                rx.text(text["section_about"], class_name="eyebrow"),
                rx.heading(text["about_title"], class_name="about-title", as_="h2"),
                rx.text(text["about_copy"], class_name="about-copy"),
                rx.link(text["about_cta"], href="mailto:studio@scenicvisionstudio.it", class_name="button button-dark"),
                class_name="about-content",
            ),
            rx.box(
                rx.box(
                    rx.text("5", class_name="stat-number"),
                    rx.text(text["stat_years"], class_name="stat-label"),
                    class_name="stat-card",
                ),
                rx.box(
                    rx.text("50+", class_name="stat-number"),
                    rx.text(text["stat_events"], class_name="stat-label"),
                    class_name="stat-card",
                ),
                rx.box(
                    rx.text("~250", class_name="stat-number"),
                    rx.text(text["stat_designs"], class_name="stat-label"),
                    class_name="stat-card",
                ),
                class_name="stats-grid",
            ),
            id="about",
            class_name="about section-wrap",
        ),
        rx.box(
            rx.box(
                rx.text(text["contact_eyebrow"], class_name="eyebrow contact-eyebrow"),
                rx.heading(
                    rx.text(text["contact_1"], class_name="contact-title-line", as_="span"),
                    rx.text(text["contact_2"], class_name="contact-title-line contact-title-accent", as_="span"),
                    class_name="contact-title",
                    as_="h2",
                ),
                class_name="contact-heading",
            ),
            rx.link(
                text["contact_cta"],
                href="mailto:studio@scenicvisionstudio.it",
                class_name="button button-light",
            ),
            class_name="contact section-wrap",
        ),
        rx.box(
            rx.box(
                rx.link(
                    rx.box(
                        rx.text("SVS", class_name="brand-mark brand-mark-footer"),
                        rx.box(
                            rx.text("SCENIC VISION", class_name="brand-name"),
                            rx.text("STUDIO", class_name="brand-caption"),
                        ),
                        class_name="brand-lockup",
                    ),
                    href="#top",
                    class_name="brand footer-brand",
                ),
                rx.text(text["footer_note"], class_name="footer-note"),
                rx.box(
                    rx.link("Email ↗", href="mailto:studio@scenicvisionstudio.it"),
                    rx.link("Instagram ↗", href="https://www.instagram.com/scenicvisionstudio", is_external=True),
                    class_name="footer-links",
                ),
                class_name="footer-main",
            ),
            rx.box(
                rx.text("© Scenic Vision Studio", class_name="footer-copyright"),
                rx.text(text["footer_credit"], class_name="footer-credit"),
                class_name="footer-bottom",
            ),
            class_name="site-footer section-wrap",
        ),
        class_name="site-shell",
    )

def index() -> rx.Component:
    return page(italian = False)

def index_it() -> rx.Component:
    return page(italian=True)

app = rx.App(
    stylesheets=["/styles.css"],
)
app.add_page(
    index,
    route="/en",
    title="Scenic Vision Studio | Lighting & Live Production",
    description="Lighting design and live technical production for artists, events and live experiences.",
)
app.add_page(
    index_it,
    route="/",
    title="Scenic Vision Studio | Progettazione Luci e Produzione Live",
    description="Progettazione luci e produzione tecnica live per artisti, eventi ed esperienze dal vivo.",
)

@rx.page(route="/404", title="404 - Pagina Non Trovata")
def custom_404():
    return rx.vstack(
        rx.box(
            rx.vstack(
                rx.image(
                    src="/svsletter.png",
                    height=rx.breakpoints(initial="80px", md="120px"),
                    width="auto",
                    margin_bottom="1rem"
                ),
                rx.heading("404", size=rx.breakpoints(initial="8", md="9"), weight="bold"),
                rx.heading("Pagina Non Trovata", size=rx.breakpoints(initial="5", md="7")),
                rx.text("La pagina che stai cercando non esiste o è stata spostata.", color_scheme="gray"),
                rx.button("Torna alla Home", radius="full", on_click=rx.redirect("/")),
                align_items="center",
                spacing="4",
            ),
            width="100%",
            padding_y=rx.breakpoints(initial="6rem", md="10rem"),
            display="flex",
            justify_content="center",
            align_items="center",
            flex="1",
        ),
        min_height="100vh",
    )