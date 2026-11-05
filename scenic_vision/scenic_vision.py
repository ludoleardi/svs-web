import reflex as rx


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


def index() -> rx.Component:
    return rx.box(
        rx.box(
            rx.link(
                rx.box(
                    rx.text("SVS", class_name="brand-mark"),
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
                rx.link("Services", href="#services"),
                rx.link("Selected work", href="#work"),
                rx.link("About", href="#about"),
                rx.link("Let's talk ↗", href="mailto:studio@scenicvisionstudio.it", class_name="nav-contact"),
                class_name="header-links",
                spacing="6",
            ),
            class_name="site-header",
        ),
        rx.box(
            rx.box(
                rx.box(
                    rx.text("LIGHTING DESIGN  /  LIVE PRODUCTION", class_name="eyebrow hero-eyebrow"),
                    rx.heading(
                        rx.text("Light that moves you.", class_name="title-line", as_="span"),
                        rx.text("Production that", class_name="title-line", as_="span"),
                        rx.text("moves with you.", class_name="title-line title-accent", as_="span"),
                        class_name="hero-title",
                        as_="h1",
                    ),
                    rx.text(
                        "A creative lighting studio and technical production partner for artists, events and live experiences.",
                        class_name="hero-copy",
                    ),
                    rx.hstack(
                        rx.link("Explore our work", href="#work", class_name="button button-orange"),
                        rx.link("Start a conversation ↗", href="mailto:studio@scenicvisionstudio.it", class_name="button button-quiet"),
                        class_name="hero-actions",
                        spacing="4",
                    ),
                    class_name="hero-content",
                ),
                rx.box(
                    rx.text("FROM FIRST IDEA", class_name="hero-side"),
                    rx.text("TO FINAL CUE.", class_name="hero-side hero-side-orange"),
                    class_name="hero-side-note",
                ),
                class_name="hero-inner",
            ),
            rx.box(
                rx.text("IDEA", class_name="hero-label"),
                rx.text("DESIGN", class_name="hero-label"),
                rx.text("PRODUCTION", class_name="hero-label"),
                rx.text("LIVE", class_name="hero-label"),
                class_name="hero-bottom",
            ),
            id="top",
            class_name="hero",
        ),
        rx.box(
            rx.text("INDEPENDENT BY NATURE  ·  BUILT FOR THE LIVE MOMENT", class_name="ticker-text"),
            class_name="ticker",
        ),
        rx.box(
            rx.box(
                rx.text("01  /  THE STUDIO", class_name="eyebrow"),
                rx.heading(
                    "From the first sketch to the last encore.",
                    class_name="intro-title",
                    as_="h2",
                ),
                class_name="intro-heading",
            ),
            rx.box(
                rx.text(
                    "Scenic Vision Studio brings creative vision and technical precision together. "
                    "We work alongside artists and organisers from concept to showtime, making every "
                    "detail feel like it belongs.",
                    class_name="intro-copy",
                ),
                rx.link("A little more about us ↗", href="#about", class_name="text-link"),
                class_name="intro-description",
            ),
            class_name="intro section-wrap",
        ),
        rx.box(
            rx.box(
                rx.box(
                    rx.text("02  /  WHAT WE DO", class_name="eyebrow"),
                    rx.heading("One team. Every moving part.", class_name="section-title", as_="h2"),
                ),
                rx.text("Creative thinking, technical rigour, and a crew that knows showtime.", class_name="section-lede"),
                class_name="section-heading-row",
            ),
            rx.box(
                service_card(
                    "01",
                    "Lighting design",
                    "Build a visual world for your show. We shape the atmosphere, the cues and the moments that stay with people.",
                    "CONCEPT  ·  PROGRAMMING  ·  SHOW",
                ),
                service_card(
                    "02",
                    "Live production",
                    "From one-night events to a full tour, we bring the people, planning and technical detail together.",
                    "EVENTS  ·  TOURS  ·  FESTIVALS",
                ),
                service_card(
                    "03",
                    "System design",
                    "Audio, lighting, structures and control networks, designed as one reliable and considered system.",
                    "AUDIO  ·  LIGHT  ·  CONTROL",
                ),
                service_card(
                    "04",
                    "Logistics",
                    "The right crew, equipment and timings, coordinated on the ground so the creative can take centre stage.",
                    "CREW  ·  EQUIPMENT  ·  TIMING",
                ),
                class_name="services-grid",
            ),
            id="services",
            class_name="services section-wrap",
        ),
        rx.box(
            rx.box(
                rx.box(
                    rx.text("03  /  SELECTED WORK", class_name="eyebrow"),
                    rx.heading("A few nights we helped bring to life.", class_name="section-title", as_="h2"),
                ),
                rx.link("See what we can make together ↗", href="mailto:studio@scenicvisionstudio.it", class_name="text-link"),
                class_name="section-heading-row work-heading",
            ),
            rx.box(
                work_card(
                    "I Boschi Bruciano",
                    "Quella Che Chiami Normalità · Tour Ribelle",
                    "TOUR  /  2025—26",
                    "work-image-one",
                ),
                work_card(
                    "Sofà So Good Torino",
                    "Sofà So Good · Sofarm · Torino Music Forum",
                    "FESTIVAL  /  2024—26",
                    "work-image-two",
                ),
                work_card(
                    "TEDx Cuneo",
                    "Audio and lighting provider",
                    "LIVE EVENT  /  2023—26",
                    "work-image-three",
                ),
                class_name="work-grid",
            ),
            id="work",
            class_name="work section-wrap",
        ),
        rx.box(
            rx.box(
                rx.text("04  /  GOOD WORK, GOOD PEOPLE", class_name="eyebrow"),
                rx.heading("Small enough to care. Experienced enough to deliver.", class_name="about-title", as_="h2"),
                rx.text(
                    "We’re a close-knit team with a collaborative mindset. We make space for the big idea, "
                    "then take care of the details that make it real.",
                    class_name="about-copy",
                ),
                rx.link("Tell us what you’re planning ↗", href="mailto:studio@scenicvisionstudio.it", class_name="button button-dark"),
                class_name="about-content",
            ),
            rx.box(
                rx.box(
                    rx.text("4", class_name="stat-number"),
                    rx.text("years in the live industry", class_name="stat-label"),
                    class_name="stat-card",
                ),
                rx.box(
                    rx.text("50+", class_name="stat-number"),
                    rx.text("events produced", class_name="stat-label"),
                    class_name="stat-card",
                ),
                rx.box(
                    rx.text("~200", class_name="stat-number"),
                    rx.text("technical designs", class_name="stat-label"),
                    class_name="stat-card",
                ),
                class_name="stats-grid",
            ),
            id="about",
            class_name="about section-wrap",
        ),
        rx.box(
            rx.box(
                rx.text("HAVE A SHOW IN MIND?", class_name="eyebrow contact-eyebrow"),
                rx.heading(
                    rx.text("Let’s make it", class_name="contact-title-line", as_="span"),
                    rx.text("a night to remember.", class_name="contact-title-line contact-title-accent", as_="span"),
                    class_name="contact-title",
                    as_="h2",
                ),
                class_name="contact-heading",
            ),
            rx.link(
                "Tell us about it  ↗",
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
                rx.text("Creative vision. Technical precision. Live impact.", class_name="footer-note"),
                rx.box(
                    rx.link("Email ↗", href="mailto:studio@scenicvisionstudio.it"),
                    rx.link("Instagram ↗", href="https://www.instagram.com/scenicvisionstudio", is_external=True),
                    class_name="footer-links",
                ),
                class_name="footer-main",
            ),
            rx.box(
                rx.text("© Scenic Vision Studio", class_name="footer-copyright"),
                rx.text("MADE FOR THE LIVE MOMENT", class_name="footer-credit"),
                class_name="footer-bottom",
            ),
            class_name="site-footer section-wrap",
        ),
        class_name="site-shell",
    )


app = rx.App(
    stylesheets=["/styles.css"],
)
app.add_page(
    index,
    route="/",
    title="Scenic Vision Studio | Lighting & Live Production",
    description="Lighting design and live technical production for artists, events and live experiences.",
)
