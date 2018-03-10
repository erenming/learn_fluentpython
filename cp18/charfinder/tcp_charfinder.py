import sys
import asyncio

from cp18.charfinder.charfinder import UnicodeNameIndex


CRLF = B'\r\n'
PROMPT = b'?>'

index = UnicodeNameIndex()

@asyncio.coroutine
def handle_queries(reader, writer):
    while True:
        writer.write(PROMPT)