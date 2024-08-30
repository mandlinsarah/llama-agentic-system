# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

import mesop as me

from examples.custom_tools.ticker_data import TickerDataTool
from utils.chat import chat, State
from utils.client import ClientManager
from utils.common import DISABLE_SAFETY, DISTRIBUTION_HOST, DISTRIBUTION_PORT, on_attach
from utils.transform import transform


client_manager = ClientManager()
client_manager.init_client(
    inference_port=DISTRIBUTION_PORT,
    host=DISTRIBUTION_HOST,
    custom_tools=[TickerDataTool()],
    disable_safety=DISABLE_SAFETY,
)


@me.page(
    path="/",
    title="Llama Agentic System",
)
def page():
    state = me.state(State)
    chat(
        transform,
        title="Llama Agentic System",
        bot_user="Llama Agent",
        on_attach=on_attach,
    )


if __name__ == "__main__":
    import subprocess
    
    try:
        process = subprocess.Popen(["mesop", __file__])
        process.communicate()
    except subprocess.SubprocessError as e:
        print(f"An error occurred while running the subprocess: {e}")

