# /// script
# dependencies = []
# 
# [tool.griptape-nodes]
# name = "nuke_WAN_Reference_to_Video"
# schema_version = "0.19.1"
# engine_version_created_with = "0.86.0"
# node_libraries_referenced = [["Griptape Nodes Library", "0.81.0"]]
# node_types_used = [["Griptape Nodes Library", "EndFlow"], ["Griptape Nodes Library", "LoadVideo"], ["Griptape Nodes Library", "SaveVideo"], ["Griptape Nodes Library", "StartFlow"], ["Griptape Nodes Library", "WanReferenceToVideoGeneration"]]
# workflows_referenced = []
# description = "The workflow acts as an AI video-to-video tool. It takes an initial \"reference\" video, ingests a text prompt describing a desired scene or transformation, runs it through a WAN video generation model (specifically configured here for wan2.6-r2v), and outputs a brand-new AI-generated video."
# image = "nuke_WAN_Reference_to_Video-header-2026-07-07.png"
# is_griptape_provided = true
# is_template = true
# is_internal = false
# creation_date = 2026-07-07T15:10:41.697365Z
# last_modified_date = 2026-07-07T15:42:59.656748Z
# 
# ///

import argparse
import asyncio
import json
import logging
import pickle
from griptape_nodes.bootstrap.workflow_executors.local_workflow_executor import LocalWorkflowExecutor
from griptape_nodes.bootstrap.workflow_executors.workflow_executor import WorkflowExecutor
from griptape_nodes.node_library.library_registry import IconVariant, NodeDeprecationMetadata, NodeMetadata
from griptape_nodes.retained_mode.events.connection_events import CreateConnectionRequest
from griptape_nodes.retained_mode.events.flow_events import CreateFlowRequest, GetTopLevelFlowRequest, GetTopLevelFlowResultSuccess
from griptape_nodes.retained_mode.events.library_events import RegisterLibraryFromFileRequest
from griptape_nodes.retained_mode.events.node_events import CreateNodeRequest
from griptape_nodes.retained_mode.events.parameter_events import AddParameterToNodeRequest, AlterParameterDetailsRequest, SetParameterValueRequest
from griptape_nodes.retained_mode.griptape_nodes import GriptapeNodes
from typing import Any

async def build_workflow() -> None:
    await GriptapeNodes.ahandle_request(RegisterLibraryFromFileRequest(library_name='Griptape Nodes Library', perform_discovery_if_not_found=True))
    context_manager = GriptapeNodes.ContextManager()
    if not context_manager.has_current_workflow():
        context_manager.push_workflow(file_path=__file__)
    # 1. We've collated all of the unique parameter values into a dictionary so that we do not have to duplicate them.
    #    This minimizes the size of the code, especially for large objects like serialized image files.
    # 2. We're using a prefix so that it's clear which Flow these values are associated with.
    # 3. The values are serialized using pickle, which is a binary format. This makes them harder to read, but makes
    #    them consistently save and load. It allows us to serialize complex objects like custom classes, which otherwise
    #    would be difficult to serialize.
    top_level_unique_values_dict = {'3dcb5dc9-aa78-48a6-9ca5-daf22a0bf99f': pickle.loads(b'\x80\x04\x89.'), '3cb696f2-81fc-4ae6-8191-e5c3788aceb7': pickle.loads(b'\x80\x04K\x00.'), '04ad4281-d5e2-452b-820d-a1dd0e00e231': pickle.loads(b'\x80\x04\x95\x0e\x00\x00\x00\x00\x00\x00\x00\x8c\nwan2.6-r2v\x94.'), '04250234-67d5-43f2-9a65-f28109ef2bc0': pickle.loads(b'\x80\x04\x95\x04\x00\x00\x00\x00\x00\x00\x00\x8c\x00\x94.'), 'c3758a5d-8f7e-42b6-b92d-f6f4614f9e19': pickle.loads(b'\x80\x04\x95\r\x00\x00\x00\x00\x00\x00\x00\x8c\t1920*1080\x94.'), '3cdf0b21-5e74-4e30-b52c-dc22c5a81088': pickle.loads(b'\x80\x04K\x05.'), 'a31a56fb-f4a6-4647-884d-1d9f5d83c680': pickle.loads(b'\x80\x04\x95\n\x00\x00\x00\x00\x00\x00\x00\x8c\x06single\x94.'), 'ca1983a5-e1a1-48da-9360-dbb2b020c1c7': pickle.loads(b'\x80\x04\x95\x11\x00\x00\x00\x00\x00\x00\x00\x8c\rwan_video.mp4\x94.'), 'cb0e7107-7728-4583-b204-0e5f7a6fc5bc': pickle.loads(b'\x80\x04\x95\x16\x00\x00\x00\x00\x00\x00\x00\x8c\x12griptape_nodes.mp4\x94.')}
    # Create the Flow, then do work within it as context.
    flow0_name = (await GriptapeNodes.ahandle_request(CreateFlowRequest(parent_flow_name=None, flow_name='ControlFlow_1', set_as_new_context=False, metadata={}))).flow_name
    with GriptapeNodes.ContextManager().flow(flow0_name):
        node0_name = (await GriptapeNodes.ahandle_request(CreateNodeRequest(node_type='WanReferenceToVideoGeneration', specific_library_name='Griptape Nodes Library', node_name='WAN Reference to Video Generation', metadata={'position': {'x': 1001.6666666666669, 'y': 153.33333333333334}, 'tempId': 'placing-1781615940915-3ge6m', 'library_node_metadata': {'category': 'video', 'description': 'Generate videos from reference videos using WAN models via Griptape model proxy', 'display_name': 'WAN Reference to Video Generation', 'tags': ['video', 'reference-to-video', 'ai', 'api', 'wan'], 'icon': 'Sparkles', 'color': None, 'group': 'create', 'deprecation': None, 'is_node_group': None, 'declarations': [{'type': 'model_usage', 'model_ids': ['gtc_wan_2_6_r2v']}]}, 'library': 'Griptape Nodes Library', 'node_type': 'WanReferenceToVideoGeneration', 'showaddparameter': False, 'size': {'width': 600, 'height': 1184}}, initial_setup=True))).node_name
        with GriptapeNodes.ContextManager().node(node0_name):
            await GriptapeNodes.ahandle_request(AlterParameterDetailsRequest(parameter_name='input_audio', ui_options={'display_name': 'Input Audio', 'clickable_file_browser': True, 'hide': False, 'hide_label': False, 'hide_property': False}, initial_setup=True))
        node1_name = (await GriptapeNodes.ahandle_request(CreateNodeRequest(node_type='LoadVideo', specific_library_name='Griptape Nodes Library', node_name='Load Video', metadata={'position': {'x': -95.51882831076676, 'y': 75.3515511430814}, 'tempId': 'placing-1781615965536-thvyfq', 'library_node_metadata': {'category': 'video', 'description': 'Loads video files into your workflow', 'display_name': 'Load Video', 'tags': ['video', 'file', 'load'], 'icon': 'file-video', 'color': None, 'group': 'Input/Output', 'deprecation': None, 'is_node_group': None, 'declarations': []}, 'library': 'Griptape Nodes Library', 'node_type': 'LoadVideo', 'showaddparameter': False, 'size': {'width': 600, 'height': 392}}, initial_setup=True))).node_name
        with GriptapeNodes.ContextManager().node(node1_name):
            await GriptapeNodes.ahandle_request(AlterParameterDetailsRequest(parameter_name='video', settable=False, initial_setup=True))
            await GriptapeNodes.ahandle_request(AlterParameterDetailsRequest(parameter_name='path', settable=False, initial_setup=True))
        node2_name = (await GriptapeNodes.ahandle_request(CreateNodeRequest(node_type='StartFlow', specific_library_name='Griptape Nodes Library', node_name='Start Flow', metadata={'library_node_metadata': {'category': 'workflows', 'description': 'Define the start of a workflow and pass parameters into the flow', 'display_name': 'Start Flow', 'tags': ['workflow', 'execution'], 'icon': None, 'color': None, 'group': 'create', 'deprecation': None, 'is_node_group': None, 'declarations': []}, 'library': 'Griptape Nodes Library', 'node_type': 'StartFlow', 'showaddparameter': True, 'position': {'x': -1159.6317832028542, 'y': 531.4493501246043}, 'size': {'width': 611, 'height': 697}}, initial_setup=True))).node_name
        with GriptapeNodes.ContextManager().node(node2_name):
            await GriptapeNodes.ahandle_request(AddParameterToNodeRequest(parameter_name='video', default_value='', tooltip='New parameter', type='VideoUrlArtifact', input_types=['VideoUrlArtifact', 'VideoArtifact', 'str'], output_type='VideoUrlArtifact', ui_options={'clickable_file_browser': True, 'expander': True, 'display_name': 'Video or Path to Video', 'is_custom': True, 'is_user_added': True}, parent_container_name='', initial_setup=True))
            await GriptapeNodes.ahandle_request(AddParameterToNodeRequest(parameter_name='prompt', default_value='', tooltip='New parameter', type='str', input_types=['any'], output_type='str', ui_options={'display_name': 'Prompt', 'multiline': True, 'placeholder_text': 'character1 is happily watching a movie on the sofa...', 'hide_label': False, 'hide_property': False, 'is_custom': True, 'is_user_added': True}, parent_container_name='', initial_setup=True))
            await GriptapeNodes.ahandle_request(AddParameterToNodeRequest(parameter_name='negative_prompt', default_value='', tooltip='New parameter', type='str', input_types=['str'], output_type='str', ui_options={'multiline': True, 'placeholder_text': 'low resolution, error, worst quality...', 'display_name': 'Negative Prompt', 'is_custom': True, 'is_user_added': True}, parent_container_name='', initial_setup=True))
            await GriptapeNodes.ahandle_request(AddParameterToNodeRequest(parameter_name='output_path', tooltip='Enter text/string for output_path.', type='str', input_types=['str'], output_type='str', ui_options={'is_custom': True, 'is_user_added': True, 'display_name': 'output_path', 'multiline': False, 'markdown': False, 'step': 1}, initial_setup=True))
        node3_name = (await GriptapeNodes.ahandle_request(CreateNodeRequest(node_type='SaveVideo', specific_library_name='Griptape Nodes Library', node_name='Save Video', metadata={'position': {'x': 1846.7818929276295, 'y': 688.4493501246044}, 'tempId': 'placing-1781616407981-5qms9o', 'library_node_metadata': {'category': 'video', 'description': 'Save a video to a file', 'display_name': 'Save Video', 'tags': ['video', 'file', 'save'], 'icon': 'file-down', 'color': None, 'group': 'Input/Output', 'deprecation': None, 'is_node_group': None, 'declarations': []}, 'library': 'Griptape Nodes Library', 'node_type': 'SaveVideo', 'showaddparameter': False, 'size': {'width': 600, 'height': 540}}, initial_setup=True))).node_name
        node4_name = (await GriptapeNodes.ahandle_request(CreateNodeRequest(node_type='EndFlow', specific_library_name='Griptape Nodes Library', node_name='End Flow', metadata={'position': {'x': 2797.83247942394, 'y': 666.7488319098766}, 'tempId': 'placing-1781616832009-wb6q38', 'library_node_metadata': {'category': 'workflows', 'description': 'Define the end of a workflow and return parameters from the flow', 'display_name': 'End Flow', 'tags': ['workflow', 'execution'], 'icon': None, 'color': None, 'group': 'create', 'deprecation': None, 'is_node_group': None, 'declarations': []}, 'library': 'Griptape Nodes Library', 'node_type': 'EndFlow', 'showaddparameter': True, 'size': {'width': 600, 'height': 300}}, initial_setup=True))).node_name
        with GriptapeNodes.ContextManager().node(node4_name):
            await GriptapeNodes.ahandle_request(AddParameterToNodeRequest(parameter_name='video', default_value='', tooltip='New parameter', type='VideoUrlArtifact', input_types=['any'], output_type='VideoUrlArtifact', ui_options={'clickable_file_browser': True, 'hide_label': False, 'hide_property': False, 'is_custom': True, 'is_user_added': True}, parent_container_name='', initial_setup=True))
        await GriptapeNodes.ahandle_request(CreateConnectionRequest(source_node_name=node1_name, source_parameter_name='video', target_node_name=node0_name, target_parameter_name='reference_video_1', initial_setup=True))
        await GriptapeNodes.ahandle_request(CreateConnectionRequest(source_node_name=node2_name, source_parameter_name='video', target_node_name=node1_name, target_parameter_name='video', initial_setup=True))
        await GriptapeNodes.ahandle_request(CreateConnectionRequest(source_node_name=node2_name, source_parameter_name='prompt', target_node_name=node0_name, target_parameter_name='prompt', initial_setup=True))
        await GriptapeNodes.ahandle_request(CreateConnectionRequest(source_node_name=node2_name, source_parameter_name='negative_prompt', target_node_name=node0_name, target_parameter_name='negative_prompt', initial_setup=True))
        await GriptapeNodes.ahandle_request(CreateConnectionRequest(source_node_name=node0_name, source_parameter_name='video', target_node_name=node3_name, target_parameter_name='video', initial_setup=True))
        await GriptapeNodes.ahandle_request(CreateConnectionRequest(source_node_name=node2_name, source_parameter_name='output_path', target_node_name=node3_name, target_parameter_name='output_file', initial_setup=True))
        await GriptapeNodes.ahandle_request(CreateConnectionRequest(source_node_name=node3_name, source_parameter_name='exec_out', target_node_name=node4_name, target_parameter_name='exec_in', initial_setup=True))
        await GriptapeNodes.ahandle_request(CreateConnectionRequest(source_node_name=node3_name, source_parameter_name='failure', target_node_name=node4_name, target_parameter_name='failed', initial_setup=True))
        await GriptapeNodes.ahandle_request(CreateConnectionRequest(source_node_name=node3_name, source_parameter_name='video', target_node_name=node4_name, target_parameter_name='video', initial_setup=True))
        await GriptapeNodes.ahandle_request(CreateConnectionRequest(source_node_name=node0_name, source_parameter_name='exec_out', target_node_name=node3_name, target_parameter_name='exec_in', initial_setup=True))
        await GriptapeNodes.ahandle_request(CreateConnectionRequest(source_node_name=node0_name, source_parameter_name='failure', target_node_name=node4_name, target_parameter_name='failed', initial_setup=True))
        with GriptapeNodes.ContextManager().node(node0_name):
            await GriptapeNodes.ahandle_request(SetParameterValueRequest(parameter_name='api_key_provider', node_name=node0_name, value=top_level_unique_values_dict['3dcb5dc9-aa78-48a6-9ca5-daf22a0bf99f'], initial_setup=True, is_output=False))
            await GriptapeNodes.ahandle_request(SetParameterValueRequest(parameter_name='timeout', node_name=node0_name, value=top_level_unique_values_dict['3cb696f2-81fc-4ae6-8191-e5c3788aceb7'], initial_setup=True, is_output=False))
            await GriptapeNodes.ahandle_request(SetParameterValueRequest(parameter_name='model', node_name=node0_name, value=top_level_unique_values_dict['04ad4281-d5e2-452b-820d-a1dd0e00e231'], initial_setup=True, is_output=False))
            await GriptapeNodes.ahandle_request(SetParameterValueRequest(parameter_name='prompt', node_name=node0_name, value=top_level_unique_values_dict['04250234-67d5-43f2-9a65-f28109ef2bc0'], initial_setup=True, is_output=False))
            await GriptapeNodes.ahandle_request(SetParameterValueRequest(parameter_name='negative_prompt', node_name=node0_name, value=top_level_unique_values_dict['04250234-67d5-43f2-9a65-f28109ef2bc0'], initial_setup=True, is_output=False))
            await GriptapeNodes.ahandle_request(SetParameterValueRequest(parameter_name='reference_video_1', node_name=node0_name, value=top_level_unique_values_dict['04250234-67d5-43f2-9a65-f28109ef2bc0'], initial_setup=True, is_output=False))
            await GriptapeNodes.ahandle_request(SetParameterValueRequest(parameter_name='reference_video_2', node_name=node0_name, value=top_level_unique_values_dict['04250234-67d5-43f2-9a65-f28109ef2bc0'], initial_setup=True, is_output=False))
            await GriptapeNodes.ahandle_request(SetParameterValueRequest(parameter_name='reference_video_3', node_name=node0_name, value=top_level_unique_values_dict['04250234-67d5-43f2-9a65-f28109ef2bc0'], initial_setup=True, is_output=False))
            await GriptapeNodes.ahandle_request(SetParameterValueRequest(parameter_name='audio', node_name=node0_name, value=top_level_unique_values_dict['3dcb5dc9-aa78-48a6-9ca5-daf22a0bf99f'], initial_setup=True, is_output=False))
            await GriptapeNodes.ahandle_request(SetParameterValueRequest(parameter_name='input_audio', node_name=node0_name, value=top_level_unique_values_dict['04250234-67d5-43f2-9a65-f28109ef2bc0'], initial_setup=True, is_output=False))
            await GriptapeNodes.ahandle_request(SetParameterValueRequest(parameter_name='size', node_name=node0_name, value=top_level_unique_values_dict['c3758a5d-8f7e-42b6-b92d-f6f4614f9e19'], initial_setup=True, is_output=False))
            await GriptapeNodes.ahandle_request(SetParameterValueRequest(parameter_name='duration', node_name=node0_name, value=top_level_unique_values_dict['3cdf0b21-5e74-4e30-b52c-dc22c5a81088'], initial_setup=True, is_output=False))
            await GriptapeNodes.ahandle_request(SetParameterValueRequest(parameter_name='shot_type', node_name=node0_name, value=top_level_unique_values_dict['a31a56fb-f4a6-4647-884d-1d9f5d83c680'], initial_setup=True, is_output=False))
            await GriptapeNodes.ahandle_request(SetParameterValueRequest(parameter_name='watermark', node_name=node0_name, value=top_level_unique_values_dict['3dcb5dc9-aa78-48a6-9ca5-daf22a0bf99f'], initial_setup=True, is_output=False))
            await GriptapeNodes.ahandle_request(SetParameterValueRequest(parameter_name='randomize_seed', node_name=node0_name, value=top_level_unique_values_dict['3dcb5dc9-aa78-48a6-9ca5-daf22a0bf99f'], initial_setup=True, is_output=False))
            await GriptapeNodes.ahandle_request(SetParameterValueRequest(parameter_name='seed', node_name=node0_name, value=top_level_unique_values_dict['3cb696f2-81fc-4ae6-8191-e5c3788aceb7'], initial_setup=True, is_output=False))
            await GriptapeNodes.ahandle_request(SetParameterValueRequest(parameter_name='output_file', node_name=node0_name, value=top_level_unique_values_dict['ca1983a5-e1a1-48da-9360-dbb2b020c1c7'], initial_setup=True, is_output=False))
            await GriptapeNodes.ahandle_request(SetParameterValueRequest(parameter_name='was_successful', node_name=node0_name, value=top_level_unique_values_dict['3dcb5dc9-aa78-48a6-9ca5-daf22a0bf99f'], initial_setup=True, is_output=False))
            await GriptapeNodes.ahandle_request(SetParameterValueRequest(parameter_name='generation_id', node_name=node0_name, value=top_level_unique_values_dict['04250234-67d5-43f2-9a65-f28109ef2bc0'], initial_setup=True, is_output=False))
            await GriptapeNodes.ahandle_request(SetParameterValueRequest(parameter_name='generation_status', node_name=node0_name, value=top_level_unique_values_dict['04250234-67d5-43f2-9a65-f28109ef2bc0'], initial_setup=True, is_output=False))
        with GriptapeNodes.ContextManager().node(node1_name):
            await GriptapeNodes.ahandle_request(SetParameterValueRequest(parameter_name='path', node_name=node1_name, value=top_level_unique_values_dict['04250234-67d5-43f2-9a65-f28109ef2bc0'], initial_setup=True, is_output=False))
            await GriptapeNodes.ahandle_request(SetParameterValueRequest(parameter_name='path', node_name=node1_name, value=top_level_unique_values_dict['04250234-67d5-43f2-9a65-f28109ef2bc0'], initial_setup=True, is_output=True))
        with GriptapeNodes.ContextManager().node(node2_name):
            await GriptapeNodes.ahandle_request(SetParameterValueRequest(parameter_name='video', node_name=node2_name, value=top_level_unique_values_dict['04250234-67d5-43f2-9a65-f28109ef2bc0'], initial_setup=True, is_output=False))
            await GriptapeNodes.ahandle_request(SetParameterValueRequest(parameter_name='prompt', node_name=node2_name, value=top_level_unique_values_dict['04250234-67d5-43f2-9a65-f28109ef2bc0'], initial_setup=True, is_output=False))
            await GriptapeNodes.ahandle_request(SetParameterValueRequest(parameter_name='negative_prompt', node_name=node2_name, value=top_level_unique_values_dict['04250234-67d5-43f2-9a65-f28109ef2bc0'], initial_setup=True, is_output=False))
        with GriptapeNodes.ContextManager().node(node3_name):
            await GriptapeNodes.ahandle_request(SetParameterValueRequest(parameter_name='output_file', node_name=node3_name, value=top_level_unique_values_dict['cb0e7107-7728-4583-b204-0e5f7a6fc5bc'], initial_setup=True, is_output=False))
            await GriptapeNodes.ahandle_request(SetParameterValueRequest(parameter_name='was_successful', node_name=node3_name, value=top_level_unique_values_dict['3dcb5dc9-aa78-48a6-9ca5-daf22a0bf99f'], initial_setup=True, is_output=False))
        with GriptapeNodes.ContextManager().node(node4_name):
            await GriptapeNodes.ahandle_request(SetParameterValueRequest(parameter_name='was_successful', node_name=node4_name, value=top_level_unique_values_dict['3dcb5dc9-aa78-48a6-9ca5-daf22a0bf99f'], initial_setup=True, is_output=False))
            await GriptapeNodes.ahandle_request(SetParameterValueRequest(parameter_name='video', node_name=node4_name, value=top_level_unique_values_dict['04250234-67d5-43f2-9a65-f28109ef2bc0'], initial_setup=True, is_output=False))

async def _ensure_workflow_context():
    context_manager = GriptapeNodes.ContextManager()
    if not context_manager.has_current_flow():
        top_level_flow_request = GetTopLevelFlowRequest()
        top_level_flow_result = await GriptapeNodes.ahandle_request(top_level_flow_request)
        if isinstance(top_level_flow_result, GetTopLevelFlowResultSuccess) and top_level_flow_result.flow_name is not None:
            flow_manager = GriptapeNodes.FlowManager()
            flow_obj = flow_manager.get_flow_by_name(top_level_flow_result.flow_name)
            context_manager.push_flow(flow_obj)

def execute_workflow(input: dict, *, workflow_executor: WorkflowExecutor | None=None, **kwargs: Any) -> dict | None:
    return asyncio.run(aexecute_workflow(input=input, workflow_executor=workflow_executor, **kwargs))

async def aexecute_workflow(input: dict, *, workflow_executor: WorkflowExecutor | None=None, **kwargs: Any) -> dict | None:
    await build_workflow()
    await _ensure_workflow_context()
    if workflow_executor is None:
        kwargs.setdefault('pickle_control_flow_result', False)
        workflow_executor = LocalWorkflowExecutor(skip_library_loading=True, workflows_to_register=[__file__], **kwargs)
    async with workflow_executor as executor:
        await executor.arun(flow_input=input, **kwargs)
    return executor.output

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    parser = argparse.ArgumentParser()
    LocalWorkflowExecutor.add_cli_arguments(parser, pickle_control_flow_result_default=False)
    parser.add_argument('--json-input', default=None, help='JSON string containing parameter values. Takes precedence over individual parameter arguments if provided.')
    parser.add_argument('--exec_out', dest='exec_out', default=None, help='Connection to the next node in the execution chain')
    parser.add_argument('--video', dest='video', default=None, help='New parameter')
    parser.add_argument('--prompt', dest='prompt', default=None, help='New parameter')
    parser.add_argument('--negative_prompt', dest='negative_prompt', default=None, help='New parameter')
    parser.add_argument('--output_path', dest='output_path', default=None, help='Enter text/string for output_path.')
    args = parser.parse_args()
    flow_input = {}
    if args.json_input is not None:
        flow_input = json.loads(args.json_input)
    if args.json_input is None:
        if 'Start Flow' not in flow_input:
            flow_input['Start Flow'] = {}
        if args.exec_out is not None:
            flow_input['Start Flow']['exec_out'] = args.exec_out
        if args.video is not None:
            flow_input['Start Flow']['video'] = args.video
        if args.prompt is not None:
            flow_input['Start Flow']['prompt'] = args.prompt
        if args.negative_prompt is not None:
            flow_input['Start Flow']['negative_prompt'] = args.negative_prompt
        if args.output_path is not None:
            flow_input['Start Flow']['output_path'] = args.output_path
    executor = LocalWorkflowExecutor.from_cli_args(args, skip_library_loading=True, workflows_to_register=[__file__])
    workflow_output = execute_workflow(input=flow_input, workflow_executor=executor)
    print(workflow_output)
