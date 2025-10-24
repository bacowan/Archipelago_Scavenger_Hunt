from worlds.Files import APPlayerContainer
from typing import TYPE_CHECKING, Dict, List, Optional, cast, ClassVar
import zipfile
import json
import os

class ScavengerHuntPlayerContainer(APPlayerContainer):
    # Responsible for generating the file for the web app
    game: ClassVar[Optional[str]] = "Scavenger Hunt"
    patch_file_ending = ".apscavengerhunt"

    def __init__(self, location_name_to_display_name: dict[str, str],
                 base_path: str = "", output_directory: str = "", player: Optional[int] = None,
                 player_name: str = "", server: str = ""):
        container_path = os.path.join(output_directory, base_path + self.patch_file_ending)
        self.location_name_to_display_name = location_name_to_display_name
        super().__init__(container_path, player, player_name, server)

    def write_contents(self, opened_zipfile: zipfile.ZipFile) -> None:
        opened_zipfile.writestr("json", json.dumps(self.location_name_to_display_name))
        super().write_contents(opened_zipfile)