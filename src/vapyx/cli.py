import asyncio

import click

from vapyx import AxisDevice


async def main(host: str, user: str, password: str, port: int, events: bool, params: bool):
    loop = asyncio.get_event_loop()
    device = AxisDevice(
        loop=loop,
        host=host,
        username=user,
        password=password,
        port=port,
    )

    if params:
        await loop.run_in_executor(None, device.vapix.initialize_params)
    await loop.run_in_executor(None, device.vapix.initialize_ports)
    await loop.run_in_executor(None, device.vapix.initialize_users)

    if events:

        def event_handler(action, event):
            print(action, event)

        device.enable_events(event_callback=event_handler)
        device.start()

    try:
        while True:
            await asyncio.sleep(1)
    except KeyboardInterrupt:
        pass
    finally:
        device.stop()


@click.command(context_settings=dict(max_content_width=120))
@click.option(
    '-h',
    '--host',
    help='Axis device hostname or IP',
    default='192.168.0.75',
    show_default=True,
)
@click.option(
    '-u',
    '--user',
    help='Axis user',
    default='root',
    show_default=True,
)
@click.option(
    '-p',
    '--password',
    help='Axis user password',
    show_default=True,
)
@click.option(
    '--port',
    help='AXIS device port',
    default='80',
    show_default=True,
)
@click.option(
    '--events/--no-events',
    help='Show events',
    default=True,
    show_default=True,
)
@click.option(
    '--params/--no-params',
    help='Show parameters',
    default=True,
    show_default=True,
)
@click.version_option()
def cli(
    host: str,
    user: str,
    password: str,
    port: int,
    events: bool,
    params: bool,
):

    asyncio.run(main(host=host, port=port, user=user, password=password, events=events, params=params))
