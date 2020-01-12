import os
import json
import responses
from pathlib import Path
from typing import Dict, Any, List
from unittest.mock import MagicMock

from tasks.tasks import Fetcher


@responses.activate
def test_fetching(mocker):
    responses.add(responses.POST, f"{os.environ['MANAGER_API_URL']}/application/create", status=201)

    msg_list: List[Dict[str, str]] = json.loads(Path("data/msg-list.json").read_text())
    msg: Dict[str, Any] = json.loads(Path("data/msg.json").read_text())

    service = MagicMock()
    service.users().messages().list().execute.return_value = msg_list
    service.users().messages().get().execute.return_value = msg
    mocker.patch("appgen.tasks.build").return_value = service

    f = Fetcher()
    f.fetch_all()

    assert len(responses.calls) == 1
