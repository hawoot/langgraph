from tool_executor import execute_tools
from chains import first_responder, revisor
from typing import List
from langchain_core.messages import BaseMessage, ToolMessage
from langgraph.graph import MessageGraph, END

MAX_ITERATIONS = 3

builder = MessageGraph()

builder.add_node('draft', first_responder)
builder.add_node('tool_executor', execute_tools)
builder.add_node('revise', revisor)

builder.add_edge('draft', 'tool_executor')
builder.add_edge('tool_executor', 'revise')

def event_loop(state: List[BaseMessage]) -> str:
    n_iterations = sum( [isinstance(item, ToolMessage) for item in state] )
    if n_iterations > MAX_ITERATIONS:
        return END
    return 'tool_executor'

builder.add_conditional_edges('revise', event_loop)
builder.set_entry_point('draft')

graph = builder.compile()

print(graph.get_graph().draw_ascii())
print(graph.get_graph().draw_mermaid())
graph.get_graph().draw_mermaid_png(output_file_path='./reflexion_graph.png')

res = graph.invoke(
    "Write about AI-Powered SOC / autonomous soc  problem domain, list startups that do that and raised capital."
)
print(res[-1].tool_calls[0]["args"]["answer"])
print(res)