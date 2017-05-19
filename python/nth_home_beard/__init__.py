import asyncio

from skybeard.beards import BeardChatHandler
from skybeard.decorators import onerror, getargs, admin

# plug_control
try:
    import energenie as e
except RuntimeError:
    class e:
        @classmethod
        def switch_on(cls, _):
            pass

        @classmethod
        def switch_off(cls, _):
            pass


class NthHomeBeard(BeardChatHandler):

    __userhelp__ = """Default help message."""

    __commands__ = [
        ('startbottlewarmer', 'start_bottle_warmer', 'Switches on the bottle warmer')
    ]

    @onerror()
    @admin()
    @getargs()
    async def start_bottle_warmer(self, msg, timeout=4.5*60):
        e.switch_on(1)
        await self.sender.sendMessage("Started bottle warmer.")
        await asyncio.sleep(timeout)
        e.switch_off(1)
        await self.sender.sendMessage("Stopped bottle warmer.")
