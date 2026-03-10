import logging
from typing import Annotated

from fastapi import APIRouter, Depends

from src.api.dependencies import get_validated_tool_call
from src.models.domain.memory import MemoryRecallArgs, MemoryRememberArgs
from src.models.domain.response import ToolResponse
from src.models.domain.tool import ValidatedToolCall
from generalintelect import GIClient

logger = logging.getLogger(__name__)

router = APIRouter(tags=["memory"])

# Reads GI_URL from env — degrades gracefully (no-op) if not set
gi = GIClient(agent_id="personal-assistant")


@router.post("/recall_memory/", response_model=ToolResponse)
async def recall_memory(
    validated: Annotated[
        ValidatedToolCall[MemoryRecallArgs],
        Depends(get_validated_tool_call("recallMemory", MemoryRecallArgs)),
    ],
):
    """Vapi tool: retrieve relevant memories for a given query."""
    context = gi.recall(
        query=validated.args.query,
        namespace=validated.args.namespace,
    )
    return ToolResponse.create(validated.tool_call_id, context or "No relevant memories found.")


@router.post("/remember/", response_model=ToolResponse)
async def remember(
    validated: Annotated[
        ValidatedToolCall[MemoryRememberArgs],
        Depends(get_validated_tool_call("remember", MemoryRememberArgs)),
    ],
):
    """Vapi tool: store a memory for future recall."""
    mem_id = gi.remember(
        content=validated.args.content,
        namespace=validated.args.namespace,
    )
    result = f"Stored memory {mem_id}." if mem_id else "Memory storage unavailable."
    return ToolResponse.create(validated.tool_call_id, result)
