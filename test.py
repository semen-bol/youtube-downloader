import asyncio

from tube.classes.tube import Video
from loguru import logger

async def main():
    count = 0
    z = Video("", count=count)

    # get name, author, length and formatted/unformatted resolution
    name, author, length, (unformatted, formatted) = z.getInfo()
    print(f"🎬 {name} [{length}]\n👤 {author}\n\n📌 Найденные разрешения: {formatted} / {unformatted}")
    
    path, count = await z.download() # download...
    logger.info("Video ready on path " + path)

    z = Video("", count=count)

    # get name, author, length and formatted/unformatted resolution
    name, author, length, (unformatted, formatted) = z.getInfo()
    print(f"🎬 {name} [{length}]\n👤 {author}\n\n📌 Найденные разрешения: {formatted} / {unformatted}")
    
    path, count = await z.download()
    logger.info("Video ready on path " + path)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt: 
        logger.debug("Exiting...")
