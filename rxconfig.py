import reflex as rx

config = rx.Config(
    app_name="scenic_vision",
    api_url="https://api.scenicvisionstudio.it",
    deploy_url="https://www.scenicvisionstudio.it", # Add this line
    show_built_with_reflex=False,
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
        rx.plugins.RadixThemesPlugin(
            theme=rx.theme(
                appearance="dark",
                has_background=True,
                accent_color="amber",
                radius="large",
            )
        ),
    ]
)