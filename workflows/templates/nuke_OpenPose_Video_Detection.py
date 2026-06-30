# /// script
# dependencies = []
# 
# [tool.griptape-nodes]
# name = "OpenPose_Video_Detection"
# schema_version = "0.19.1"
# engine_version_created_with = "0.86.0"
# node_libraries_referenced = [["Griptape Nodes Advanced Media Library", "0.72.1"], ["Griptape Nodes Library", "0.79.0"]]
# node_types_used = [["Griptape Nodes Advanced Media Library", "OpenPoseVideoDetection"], ["Griptape Nodes Library", "EndFlow"], ["Griptape Nodes Library", "LoadVideo"], ["Griptape Nodes Library", "StartFlow"]]
# is_griptape_provided = false
# creation_date = 2026-06-16T21:55:33.971820Z
# last_modified_date = 2026-06-16T22:37:05.176605Z
# workflow_shape = "{\"inputs\":{\"Start Flow\":{\"exec_out\":{\"name\":\"exec_out\",\"tooltip\":\"Connection to the next node in the execution chain\",\"type\":\"parametercontroltype\",\"input_types\":[\"parametercontroltype\"],\"output_type\":\"parametercontroltype\",\"default_value\":null,\"tooltip_as_input\":null,\"tooltip_as_property\":null,\"tooltip_as_output\":null,\"mode_allowed_input\":false,\"mode_allowed_property\":false,\"mode_allowed_output\":true,\"ui_options\":{\"parameter_render_location\":\"top\",\"display_name\":\"Flow Out\"},\"settable\":true,\"is_user_defined\":true,\"private\":false,\"parent_container_name\":null,\"parent_element_name\":null},\"input_video\":{\"name\":\"input_video\",\"tooltip\":\"New parameter\",\"type\":\"VideoUrlArtifact\",\"input_types\":[\"VideoUrlArtifact\"],\"output_type\":\"VideoUrlArtifact\",\"default_value\":\"\",\"tooltip_as_input\":null,\"tooltip_as_property\":null,\"tooltip_as_output\":null,\"mode_allowed_input\":true,\"mode_allowed_property\":true,\"mode_allowed_output\":true,\"ui_options\":{\"is_custom\":true,\"is_user_added\":true},\"settable\":true,\"is_user_defined\":true,\"private\":false,\"parent_container_name\":\"\",\"parent_element_name\":null},\"max_dim\":{\"name\":\"max_dim\",\"tooltip\":\"New parameter\",\"type\":\"int\",\"input_types\":[\"int\"],\"output_type\":\"int\",\"default_value\":\"\",\"tooltip_as_input\":null,\"tooltip_as_property\":null,\"tooltip_as_output\":null,\"mode_allowed_input\":true,\"mode_allowed_property\":true,\"mode_allowed_output\":true,\"ui_options\":{\"is_custom\":true,\"is_user_added\":true},\"settable\":true,\"is_user_defined\":true,\"private\":false,\"parent_container_name\":\"\",\"parent_element_name\":null},\"max_frames\":{\"name\":\"max_frames\",\"tooltip\":\"New parameter\",\"type\":\"int\",\"input_types\":[\"int\"],\"output_type\":\"int\",\"default_value\":\"\",\"tooltip_as_input\":null,\"tooltip_as_property\":null,\"tooltip_as_output\":null,\"mode_allowed_input\":true,\"mode_allowed_property\":true,\"mode_allowed_output\":true,\"ui_options\":{\"is_custom\":true,\"is_user_added\":true},\"settable\":true,\"is_user_defined\":true,\"private\":false,\"parent_container_name\":\"\",\"parent_element_name\":null},\"black_background\":{\"name\":\"black_background\",\"tooltip\":\"New parameter\",\"type\":\"bool\",\"input_types\":[\"bool\"],\"output_type\":\"bool\",\"default_value\":\"\",\"tooltip_as_input\":null,\"tooltip_as_property\":null,\"tooltip_as_output\":null,\"mode_allowed_input\":true,\"mode_allowed_property\":true,\"mode_allowed_output\":true,\"ui_options\":{\"is_custom\":true,\"is_user_added\":true},\"settable\":true,\"is_user_defined\":true,\"private\":false,\"parent_container_name\":\"\",\"parent_element_name\":null},\"output_path\":{\"name\":\"output_path\",\"tooltip\":\"New parameter\",\"type\":\"str\",\"input_types\":[\"str\"],\"output_type\":\"str\",\"default_value\":\"\",\"tooltip_as_input\":null,\"tooltip_as_property\":null,\"tooltip_as_output\":null,\"mode_allowed_input\":true,\"mode_allowed_property\":true,\"mode_allowed_output\":true,\"ui_options\":{\"is_custom\":true,\"is_user_added\":true,\"hide\":false,\"display_name\":\"file\",\"step\":1},\"settable\":true,\"is_user_defined\":true,\"private\":false,\"parent_container_name\":\"\",\"parent_element_name\":null}}},\"outputs\":{\"End Flow\":{\"exec_in\":{\"name\":\"exec_in\",\"tooltip\":\"Control path when the flow completed successfully\",\"type\":\"parametercontroltype\",\"input_types\":[\"parametercontroltype\"],\"output_type\":\"parametercontroltype\",\"default_value\":null,\"tooltip_as_input\":null,\"tooltip_as_property\":null,\"tooltip_as_output\":null,\"mode_allowed_input\":true,\"mode_allowed_property\":false,\"mode_allowed_output\":false,\"ui_options\":{\"parameter_render_location\":\"top\",\"display_name\":\"Succeeded\"},\"settable\":true,\"is_user_defined\":true,\"private\":false,\"parent_container_name\":null,\"parent_element_name\":null},\"failed\":{\"name\":\"failed\",\"tooltip\":\"Control path when the flow failed\",\"type\":\"parametercontroltype\",\"input_types\":[\"parametercontroltype\"],\"output_type\":\"parametercontroltype\",\"default_value\":null,\"tooltip_as_input\":null,\"tooltip_as_property\":null,\"tooltip_as_output\":null,\"mode_allowed_input\":true,\"mode_allowed_property\":false,\"mode_allowed_output\":false,\"ui_options\":{\"parameter_render_location\":\"top\",\"display_name\":\"Failed\"},\"settable\":true,\"is_user_defined\":true,\"private\":false,\"parent_container_name\":null,\"parent_element_name\":null},\"was_successful\":{\"name\":\"was_successful\",\"tooltip\":\"Indicates whether it completed without errors.\",\"type\":\"bool\",\"input_types\":[\"bool\"],\"output_type\":\"bool\",\"default_value\":false,\"tooltip_as_input\":null,\"tooltip_as_property\":null,\"tooltip_as_output\":null,\"mode_allowed_input\":false,\"mode_allowed_property\":true,\"mode_allowed_output\":false,\"ui_options\":{},\"settable\":false,\"is_user_defined\":true,\"private\":false,\"parent_container_name\":null,\"parent_element_name\":\"Status\"},\"result_details\":{\"name\":\"result_details\",\"tooltip\":\"Details about the operation result\",\"type\":\"str\",\"input_types\":[\"str\"],\"output_type\":\"str\",\"default_value\":null,\"tooltip_as_input\":null,\"tooltip_as_property\":null,\"tooltip_as_output\":null,\"mode_allowed_input\":true,\"mode_allowed_property\":false,\"mode_allowed_output\":false,\"ui_options\":{\"multiline\":true,\"placeholder_text\":\"Details about the completion or failure will be shown here.\"},\"settable\":false,\"is_user_defined\":true,\"private\":false,\"parent_container_name\":null,\"parent_element_name\":\"Status\"},\"output_video\":{\"name\":\"output_video\",\"tooltip\":\"New parameter\",\"type\":\"VideoUrlArtifact\",\"input_types\":[\"VideoUrlArtifact\"],\"output_type\":\"VideoUrlArtifact\",\"default_value\":\"\",\"tooltip_as_input\":null,\"tooltip_as_property\":null,\"tooltip_as_output\":null,\"mode_allowed_input\":true,\"mode_allowed_property\":true,\"mode_allowed_output\":true,\"ui_options\":{\"is_custom\":true,\"is_user_added\":true},\"settable\":true,\"is_user_defined\":true,\"private\":false,\"parent_container_name\":\"\",\"parent_element_name\":null}}}}"
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
    await GriptapeNodes.ahandle_request(RegisterLibraryFromFileRequest(library_name='Griptape Nodes Advanced Media Library', perform_discovery_if_not_found=True))
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
    top_level_unique_values_dict = {'1f834011-2fd7-4c88-bef6-65a9506148b9': pickle.loads(b'\x80\x04\x95&\x00\x00\x00\x00\x00\x00\x00\x8c"No models downloaded \xe2\x80\x94 see badge\x94.'), '806f8c29-55e4-46c3-aff6-c006f5adc291': pickle.loads(b'\x80\x04\x88.'), '3cd24743-9a6a-4550-b1d1-65978754b394': pickle.loads(b'\x80\x04\x95\x04\x00\x00\x00\x00\x00\x00\x00\x8c\x00\x94.'), 'd15c5ea6-ab15-42bb-a895-812eb6747175': pickle.loads(b'\x80\x04\x89.')}
    # Create the Flow, then do work within it as context.
    flow0_name = (await GriptapeNodes.ahandle_request(CreateFlowRequest(parent_flow_name=None, flow_name='ControlFlow_1', set_as_new_context=False, metadata={}))).flow_name
    with GriptapeNodes.ContextManager().flow(flow0_name):
        node0_name = (await GriptapeNodes.ahandle_request(CreateNodeRequest(node_type='OpenPoseVideoDetection', specific_library_name='Griptape Nodes Advanced Media Library', node_name='OpenPose Video Detection', metadata={'position': {'x': -289.60916004923996, 'y': 1851.007651891856}, 'tempId': 'placing-1781646680960-8b5ly', 'library_node_metadata': {'category': 'video/pose', 'description': 'Detect human poses in videos using OpenPose models converted to SafeTensors format', 'display_name': 'OpenPose Video Detection', 'tags': None, 'icon': None, 'color': None, 'group': None, 'deprecation': None, 'is_node_group': None, 'declarations': []}, 'library': 'Griptape Nodes Advanced Media Library', 'node_type': 'OpenPoseVideoDetection', 'showaddparameter': False, 'size': {'width': 600, 'height': 892}}, initial_setup=True))).node_name
        with GriptapeNodes.ContextManager().node(node0_name):
            await GriptapeNodes.ahandle_request(AlterParameterDetailsRequest(parameter_name='model', default_value='No models downloaded — see badge', ui_options={'button_label': '', 'variant': 'secondary', 'size': 'icon', 'state': 'normal', 'full_width': False, 'button_icon': 'list-restart', 'iconPosition': 'left', 'simple_dropdown': ['No models downloaded — see badge'], 'show_search': True, 'search_filter': '', 'hide_label': False, 'hide_property': False, 'display_name': 'model'}, initial_setup=True))
        node1_name = (await GriptapeNodes.ahandle_request(CreateNodeRequest(node_type='StartFlow', specific_library_name='Griptape Nodes Library', node_name='Start Flow', metadata={'position': {'x': -2932.080357722286, 'y': 1946.996669364557}, 'tempId': 'placing-1781646728691-qwng3r', 'library_node_metadata': {'category': 'workflows', 'description': 'Define the start of a workflow and pass parameters into the flow', 'display_name': 'Start Flow', 'tags': ['workflow', 'execution'], 'icon': None, 'color': None, 'group': 'create', 'deprecation': None, 'is_node_group': None, 'declarations': []}, 'library': 'Griptape Nodes Library', 'node_type': 'StartFlow', 'showaddparameter': True, 'size': {'width': 642, 'height': 449}}, initial_setup=True))).node_name
        with GriptapeNodes.ContextManager().node(node1_name):
            await GriptapeNodes.ahandle_request(AddParameterToNodeRequest(parameter_name='input_video', default_value='', tooltip='New parameter', type='VideoUrlArtifact', input_types=['VideoUrlArtifact'], output_type='VideoUrlArtifact', ui_options={'is_custom': True, 'is_user_added': True}, parent_container_name='', initial_setup=True))
            await GriptapeNodes.ahandle_request(AddParameterToNodeRequest(parameter_name='max_dim', default_value='', tooltip='New parameter', type='int', input_types=['int'], output_type='int', ui_options={'is_custom': True, 'is_user_added': True}, parent_container_name='', initial_setup=True))
            await GriptapeNodes.ahandle_request(AddParameterToNodeRequest(parameter_name='max_frames', default_value='', tooltip='New parameter', type='int', input_types=['int'], output_type='int', ui_options={'is_custom': True, 'is_user_added': True}, parent_container_name='', initial_setup=True))
            await GriptapeNodes.ahandle_request(AddParameterToNodeRequest(parameter_name='black_background', default_value='', tooltip='New parameter', type='bool', input_types=['bool'], output_type='bool', ui_options={'is_custom': True, 'is_user_added': True}, parent_container_name='', initial_setup=True))
            await GriptapeNodes.ahandle_request(AddParameterToNodeRequest(parameter_name='output_path', default_value='', tooltip='New parameter', type='str', input_types=['str'], output_type='str', ui_options={'is_custom': True, 'is_user_added': True, 'hide': False, 'display_name': 'file', 'step': 1}, parent_container_name='', initial_setup=True))
        node2_name = (await GriptapeNodes.ahandle_request(CreateNodeRequest(node_type='EndFlow', specific_library_name='Griptape Nodes Library', node_name='End Flow', metadata={'library_node_metadata': {'category': 'workflows', 'description': 'Define the end of a workflow and return parameters from the flow', 'display_name': 'End Flow', 'tags': ['workflow', 'execution'], 'icon': None, 'color': None, 'group': 'create', 'deprecation': None, 'is_node_group': None, 'declarations': []}, 'library': 'Griptape Nodes Library', 'node_type': 'EndFlow', 'showaddparameter': True, 'position': {'x': 674.3135508556073, 'y': 1868.2875447623044}, 'size': {'width': 607, 'height': 630}}, initial_setup=True))).node_name
        with GriptapeNodes.ContextManager().node(node2_name):
            await GriptapeNodes.ahandle_request(AddParameterToNodeRequest(parameter_name='output_video', default_value='', tooltip='New parameter', type='VideoUrlArtifact', input_types=['VideoUrlArtifact'], output_type='VideoUrlArtifact', ui_options={'is_custom': True, 'is_user_added': True}, parent_container_name='', initial_setup=True))
        node3_name = (await GriptapeNodes.ahandle_request(CreateNodeRequest(node_type='LoadVideo', specific_library_name='Griptape Nodes Library', node_name='Load Video', metadata={'position': {'x': -1631.8509074636445, 'y': 1312.7382091754346}, 'tempId': 'placing-1781647266080-vdvxc', 'library_node_metadata': {'category': 'video', 'description': 'Loads video files into your workflow', 'display_name': 'Load Video', 'tags': ['video', 'file', 'load'], 'icon': 'file-video', 'color': None, 'group': 'Input/Output', 'deprecation': None, 'is_node_group': None, 'declarations': []}, 'library': 'Griptape Nodes Library', 'node_type': 'LoadVideo', 'showaddparameter': False, 'size': {'width': 600, 'height': 392}}, initial_setup=True))).node_name
        with GriptapeNodes.ContextManager().node(node3_name):
            await GriptapeNodes.ahandle_request(AlterParameterDetailsRequest(parameter_name='video', settable=False, initial_setup=True))
            await GriptapeNodes.ahandle_request(AlterParameterDetailsRequest(parameter_name='path', settable=False, initial_setup=True))
        await GriptapeNodes.ahandle_request(CreateConnectionRequest(source_node_name=node1_name, source_parameter_name='max_dim', target_node_name=node0_name, target_parameter_name='max_dim', initial_setup=True))
        await GriptapeNodes.ahandle_request(CreateConnectionRequest(source_node_name=node1_name, source_parameter_name='max_frames', target_node_name=node0_name, target_parameter_name='max_frames', initial_setup=True))
        await GriptapeNodes.ahandle_request(CreateConnectionRequest(source_node_name=node1_name, source_parameter_name='black_background', target_node_name=node0_name, target_parameter_name='black_background', initial_setup=True))
        await GriptapeNodes.ahandle_request(CreateConnectionRequest(source_node_name=node1_name, source_parameter_name='exec_out', target_node_name=node0_name, target_parameter_name='exec_in', initial_setup=True))
        await GriptapeNodes.ahandle_request(CreateConnectionRequest(source_node_name=node0_name, source_parameter_name='output_video', target_node_name=node2_name, target_parameter_name='output_video', initial_setup=True))
        await GriptapeNodes.ahandle_request(CreateConnectionRequest(source_node_name=node0_name, source_parameter_name='exec_out', target_node_name=node2_name, target_parameter_name='exec_in', initial_setup=True))
        await GriptapeNodes.ahandle_request(CreateConnectionRequest(source_node_name=node1_name, source_parameter_name='output_path', target_node_name=node0_name, target_parameter_name='output_video_file', initial_setup=True))
        await GriptapeNodes.ahandle_request(CreateConnectionRequest(source_node_name=node1_name, source_parameter_name='input_video', target_node_name=node3_name, target_parameter_name='video', initial_setup=True))
        await GriptapeNodes.ahandle_request(CreateConnectionRequest(source_node_name=node3_name, source_parameter_name='video', target_node_name=node0_name, target_parameter_name='input_video', initial_setup=True))
        with GriptapeNodes.ContextManager().node(node0_name):
            await GriptapeNodes.ahandle_request(SetParameterValueRequest(parameter_name='model', node_name=node0_name, value=top_level_unique_values_dict['1f834011-2fd7-4c88-bef6-65a9506148b9'], initial_setup=True, is_output=False))
            await GriptapeNodes.ahandle_request(SetParameterValueRequest(parameter_name='black_background', node_name=node0_name, value=top_level_unique_values_dict['806f8c29-55e4-46c3-aff6-c006f5adc291'], initial_setup=True, is_output=False))
            await GriptapeNodes.ahandle_request(SetParameterValueRequest(parameter_name='no_audio', node_name=node0_name, value=top_level_unique_values_dict['806f8c29-55e4-46c3-aff6-c006f5adc291'], initial_setup=True, is_output=False))
        with GriptapeNodes.ContextManager().node(node1_name):
            await GriptapeNodes.ahandle_request(SetParameterValueRequest(parameter_name='input_video', node_name=node1_name, value=top_level_unique_values_dict['3cd24743-9a6a-4550-b1d1-65978754b394'], initial_setup=True, is_output=False))
            await GriptapeNodes.ahandle_request(SetParameterValueRequest(parameter_name='max_dim', node_name=node1_name, value=top_level_unique_values_dict['3cd24743-9a6a-4550-b1d1-65978754b394'], initial_setup=True, is_output=False))
            await GriptapeNodes.ahandle_request(SetParameterValueRequest(parameter_name='max_frames', node_name=node1_name, value=top_level_unique_values_dict['3cd24743-9a6a-4550-b1d1-65978754b394'], initial_setup=True, is_output=False))
            await GriptapeNodes.ahandle_request(SetParameterValueRequest(parameter_name='black_background', node_name=node1_name, value=top_level_unique_values_dict['806f8c29-55e4-46c3-aff6-c006f5adc291'], initial_setup=True, is_output=False))
            await GriptapeNodes.ahandle_request(SetParameterValueRequest(parameter_name='output_path', node_name=node1_name, value=top_level_unique_values_dict['3cd24743-9a6a-4550-b1d1-65978754b394'], initial_setup=True, is_output=False))
        with GriptapeNodes.ContextManager().node(node2_name):
            await GriptapeNodes.ahandle_request(SetParameterValueRequest(parameter_name='was_successful', node_name=node2_name, value=top_level_unique_values_dict['d15c5ea6-ab15-42bb-a895-812eb6747175'], initial_setup=True, is_output=False))
        with GriptapeNodes.ContextManager().node(node3_name):
            await GriptapeNodes.ahandle_request(SetParameterValueRequest(parameter_name='path', node_name=node3_name, value=top_level_unique_values_dict['3cd24743-9a6a-4550-b1d1-65978754b394'], initial_setup=True, is_output=False))
            await GriptapeNodes.ahandle_request(SetParameterValueRequest(parameter_name='path', node_name=node3_name, value=top_level_unique_values_dict['3cd24743-9a6a-4550-b1d1-65978754b394'], initial_setup=True, is_output=True))

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
    parser.add_argument('--exec_out', default=None, help='Connection to the next node in the execution chain')
    parser.add_argument('--input_video', default=None, help='New parameter')
    parser.add_argument('--max_dim', default=None, help='New parameter')
    parser.add_argument('--max_frames', default=None, help='New parameter')
    parser.add_argument('--black_background', default=None, help='New parameter')
    parser.add_argument('--output_path', default=None, help='New parameter')
    args = parser.parse_args()
    flow_input = {}
    if args.json_input is not None:
        flow_input = json.loads(args.json_input)
    if args.json_input is None:
        if 'Start Flow' not in flow_input:
            flow_input['Start Flow'] = {}
        if args.exec_out is not None:
            flow_input['Start Flow']['exec_out'] = args.exec_out
        if args.input_video is not None:
            flow_input['Start Flow']['input_video'] = args.input_video
        if args.max_dim is not None:
            flow_input['Start Flow']['max_dim'] = args.max_dim
        if args.max_frames is not None:
            flow_input['Start Flow']['max_frames'] = args.max_frames
        if args.black_background is not None:
            flow_input['Start Flow']['black_background'] = args.black_background
        if args.output_path is not None:
            flow_input['Start Flow']['output_path'] = args.output_path
    executor = LocalWorkflowExecutor.from_cli_args(args, skip_library_loading=True, workflows_to_register=[__file__])
    workflow_output = execute_workflow(input=flow_input, workflow_executor=executor)
    print(workflow_output)
