# SSE streaming utility
async def stream_tokens(generator):
    async for token in generator:
        yield f"data: {token}\n\n"
