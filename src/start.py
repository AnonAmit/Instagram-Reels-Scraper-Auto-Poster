import sys
import os
import subprocess
import threading
from rich import box
from rich.align import Align
from rich.console import Console, Group
from rich.layout import Layout
from rich.panel import Panel
from rich.progress import BarColumn, Progress, SpinnerColumn, TextColumn
from rich.syntax import Syntax
from rich.table import Table
from rich import print
import config as mainConfig
from db import Session, Config
import helpers as Helper
from datetime import datetime
import auth
import sys

# Add the src/ directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

def make_layout() -> Layout:
    layout = Layout(name="root")

    layout.split(
        Layout(name="header", size=20),
        Layout(name="body"),
    )
    layout["body"].split_row(
        Layout(name="links" ),
        Layout(name="logo", ratio=2),
    )

    return layout


def config_table() -> Panel:
    # Display configurations from config.py instead of prompting for input
    table = Table(title="", padding=0, show_lines=True, expand=True)
    table.add_column("KEY", style="green", no_wrap=True)
    table.add_column("VALUE", style="magenta")

    # Add config values to the table
    table.add_row("IS_REMOVE_FILES", str(mainConfig.IS_REMOVE_FILES))
    table.add_row("REMOVE_FILE_AFTER_MINS", str(mainConfig.REMOVE_FILE_AFTER_MINS))
    table.add_row("IS_ENABLED_REELS_SCRAPER", str(mainConfig.IS_ENABLED_REELS_SCRAPER))
    table.add_row("IS_ENABLED_AUTO_POSTER", str(mainConfig.IS_ENABLED_AUTO_POSTER))
    table.add_row("IS_POST_TO_STORY", str(mainConfig.IS_POST_TO_STORY))
    table.add_row("FETCH_LIMIT", str(mainConfig.FETCH_LIMIT))
    table.add_row("POSTING_INTERVAL_IN_MIN", str(mainConfig.POSTING_INTERVAL_IN_MIN))
    table.add_row("SCRAPER_INTERVAL_IN_MIN", str(mainConfig.SCRAPER_INTERVAL_IN_MIN))
    table.add_row("USERNAME", mainConfig.USERNAME)
    table.add_row("PASSWORD", "[red]HIDDEN[/red]")  # Hiding password for security
    table.add_row("ACCOUNTS", mainConfig.ACCOUNTS)
    table.add_row("HASTAGS", mainConfig.HASHTAGS)
    table.add_row("LIKE_AND_VIEW_COUNTS_DISABLED", str(mainConfig.LIKE_AND_VIEW_COUNTS_DISABLED))
    table.add_row("DISABLE_COMMENTS", str(mainConfig.DISABLE_COMMENTS))
    table.add_row("IS_ENABLED_YOUTUBE_SCRAPING", str(mainConfig.IS_ENABLED_YOUTUBE_SCRAPING))
    table.add_row("YOUTUBE_API_KEY", "[red]HIDDEN[/red]")  # Hiding API key for security
    table.add_row("CHANNEL_LINKS", mainConfig.CHANNEL_LINKS)

    message_panel = Panel(
        Align.left(
            Group("\n", Align.left(table)),
            vertical="top",
        ),
        title="[b red]Configurations",
        border_style="bright_blue",
    )

    return message_panel


layout = make_layout()
layout['header'].update(Helper.make_sponsor_message())
layout["logo"].update(config_table())
layout['links'].update(Helper.make_my_information())

print(layout)
print("==========================================================================")

# Directly use config.py values, no need to ask for inputs
auth.login()  # Log in using credentials from config.py

# Run the main application (app.py) using the Python executable
python_executable_path = sys.executable
os.system(f"{python_executable_path} app.py 1")
