from nonebot import require
from nonebot.plugin import PluginMetadata

require("nonebot_plugin_session")
require("nonebot_plugin_datastore")

from . import adapters
from .message import deserialize_message, serialize_message
from .model import MessageRecord
from .record import get_message_records, get_messages, get_messages_plain_text

__plugin_meta__ = PluginMetadata(
    name="聊天记录",
    description="记录机器人收到和发出的消息",
    usage="请参考文档",
    type="library",
    homepage="https://github.com/noneplugin/nonebot-plugin-chatrecorder",
    supported_adapters={"~onebot.v11", "~onebot.v12"},
)
