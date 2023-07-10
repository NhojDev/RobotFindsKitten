from typing import Iterable, Any

from tcod.context import Context
from tcod.console import Console
from tcod.map import compute_fov
from message_log import MessageLog

from entity import Entity
from game_map import GameMap
from input_handlers import EventHandler


class Engine:
    def __init__(self, event_handler: EventHandler, game_map: GameMap, player: Entity):
        self.event_handler = event_handler
        self.game_map = game_map
        self.player = player
        self.update_fov()
        self.message_log = MessageLog()

    def handle_enemy_turns(self) -> None:
        for entity in self.game_map.entities - {self.player}:
            print("\033c", end="")

    def handle_events(self, events: Iterable[Any]) -> None:
        for event in events:
            action = self.event_handler.dispatch(event)

            if action is None:
                continue

            action.perform(self, self.player)
            self.handle_enemy_turns()
            self.update_fov()  # Update the FOV before the players next action.

    def update_fov(self) -> None:
        """Recompute the visible area based on the players point of view."""
        self.game_map.visible[:] = compute_fov(
            self.game_map.tiles["transparent"],
            (self.player.x, self.player.y),
            radius=6,
        )

    def render(self, console: Console, context: Context) -> None:
        self.game_map.render(console)
        self.console = console

        self.message_log.render(console=console, x=30, y=45, width=40, height=5)

        context.present(console)

        console.clear()
    
    def success(self, console: Console, context: Context) -> None:
        self.console.print()
