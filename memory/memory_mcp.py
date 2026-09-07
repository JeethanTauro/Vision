from fastmcp import FastMCP

from crud_api import (
    memory_get as db_memory_get,
    memory_search as db_memory_search,
    memory_save as db_memory_save,
    memory_update as db_memory_update,
    memory_delete as db_memory_delete,
)

mcp = FastMCP("vision_memory_mcp")


@mcp.tool()
def memory_get(id: int):
    """
    Retrieve a single session memory by its unique ID.

    Args:
        id: The exact ID of the memory to retrieve.

    Returns:
        The matching memory, or None if no memory exists with that ID.

    Note:
        Use memory_search first when the memory ID is not known.
    """
    return db_memory_get(id)


@mcp.tool()
def memory_search(query: str):
    """
    Search session memories whose content matches the given query.

    Args:
        query: A keyword, phrase, or topic to search for.

    Returns:
        A list of matching memories, including their IDs and metadata.

    Note:
        Multiple memories may match. If the operation is an update or
        deletion and multiple plausible memories are returned, ask the
        user to identify the exact memory ID before modifying anything.
    """
    return db_memory_search(query)


@mcp.tool()
def memory_save(content: str, source: str, importance: float):
    """
    Create and persist a new session memory.

    Args:
        content: The information that should be remembered.
        source: Where the memory originated, such as CONVERSATION, NOTION,
                or GITHUB.
        importance: Importance of the memory as a value between 0.0 and 1.0.

    Returns:
        The newly created memory, including its generated ID.
    """
    return db_memory_save(content, source, importance)


@mcp.tool()
def memory_update(
    id: int,
    content: str | None = None,
    importance: float | None = None,
):
    """
    Update an existing session memory.

    Args:
        id: The exact ID of the memory to update.
        content: New memory content. Leave None to keep the existing content.
        importance: New importance value between 0.0 and 1.0.
                    Leave None to keep the existing value.

    Returns:
        The updated memory, or None if the specified ID does not exist.

    Note:
        Do not guess the ID. If the target memory is unclear, use
        memory_search and ask the user to identify the correct memory.
    """
    return db_memory_update(id, content, importance)


@mcp.tool()
def memory_delete(id: int):
    """
    Permanently delete a session memory.

    Args:
        id: The exact ID of the memory to delete.

    Returns:
        True if the memory was deleted, or False if no memory exists
        with the specified ID.

    Note:
        Never guess a memory ID. If multiple memories could match the
        user's request, search first and ask the user to identify the
        exact memory before deleting it.
    """
    return db_memory_delete(id)


if __name__ == "__main__":
    mcp.run()