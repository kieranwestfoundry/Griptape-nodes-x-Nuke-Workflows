# /// script
# dependencies = []
# 
# [tool.griptape-nodes]
# name = "nuke_image_gen_nano_banana"
# schema_version = "0.20.0"
# engine_version_created_with = "0.91.0"
# node_libraries_referenced = [["Griptape Nodes Library", "0.81.0"]]
# node_types_used = [["Griptape Nodes Library", "EndFlow"], ["Griptape Nodes Library", "GoogleImageGeneration"], ["Griptape Nodes Library", "StartFlow"]]
# description = "a very simple image generation workflow. Uses Nano Banana from Google"
# image = "nuke_image_gen_nano_banana-header-2026-07-08.png"
# is_griptape_provided = true
# is_template = true
# is_internal = false
# creation_date = 2026-07-03T21:32:14.046629Z
# last_modified_date = 2026-07-08T16:21:56.390459Z
# workflow_shape = "{\"inputs\":{\"Start Flow\":{\"exec_out\":{\"name\":\"exec_out\",\"tooltip\":\"Connection to the next node in the execution chain\",\"type\":\"parametercontroltype\",\"input_types\":[\"parametercontroltype\"],\"output_type\":\"parametercontroltype\",\"default_value\":null,\"tooltip_as_input\":null,\"tooltip_as_property\":null,\"tooltip_as_output\":null,\"mode_allowed_input\":false,\"mode_allowed_property\":false,\"mode_allowed_output\":true,\"ui_options\":{\"parameter_render_location\":\"top\",\"display_name\":\"Flow Out\"},\"settable\":true,\"is_user_defined\":true,\"private\":false,\"parent_container_name\":null,\"parent_element_name\":null},\"models\":{\"name\":\"models\",\"tooltip\":\"Enter text/string for models.\",\"type\":\"str\",\"input_types\":[\"str\"],\"output_type\":\"str\",\"default_value\":\"FLUX.2 [flex]\",\"tooltip_as_input\":null,\"tooltip_as_property\":null,\"tooltip_as_output\":null,\"mode_allowed_input\":true,\"mode_allowed_property\":true,\"mode_allowed_output\":true,\"ui_options\":{\"is_custom\":true,\"is_user_added\":true,\"display_name\":\"Models\",\"multiline\":false,\"markdown\":false,\"dropdown_row_icons\":false,\"dropdown_row_subtitles\":false,\"simple_dropdown\":[\"Nano Banana Pro\",\"Nano Banana 2\"],\"data\":[{\"name\":\"Nano Banana Pro\",\"args\":{}},{\"name\":\"Nano Banana 2\",\"args\":{}}],\"show_search\":true,\"search_filter\":\"\",\"step\":1,\"hide\":false},\"settable\":true,\"is_user_defined\":true,\"private\":false,\"parent_container_name\":null,\"parent_element_name\":null},\"prompt\":{\"name\":\"prompt\",\"tooltip\":\"New parameter\",\"type\":\"str\",\"input_types\":[\"any\"],\"output_type\":\"str\",\"default_value\":\"\",\"tooltip_as_input\":null,\"tooltip_as_property\":null,\"tooltip_as_output\":null,\"mode_allowed_input\":true,\"mode_allowed_property\":true,\"mode_allowed_output\":true,\"ui_options\":{\"multiline\":true,\"placeholder_text\":\"Enter prompt...\",\"hide_label\":false,\"hide_property\":false,\"is_custom\":true,\"is_user_added\":true},\"settable\":true,\"is_user_defined\":true,\"private\":false,\"parent_container_name\":\"\",\"parent_element_name\":null},\"aspect_ratio\":{\"name\":\"aspect_ratio\",\"tooltip\":\"New parameter\",\"type\":\"str\",\"input_types\":[\"any\"],\"output_type\":\"str\",\"default_value\":\"\",\"tooltip_as_input\":null,\"tooltip_as_property\":null,\"tooltip_as_output\":null,\"mode_allowed_input\":true,\"mode_allowed_property\":true,\"mode_allowed_output\":true,\"ui_options\":{\"simple_dropdown\":[\"1:1\",\"3:2\",\"2:3\",\"3:4\",\"4:3\",\"4:5\",\"5:4\",\"9:16\",\"16:9\",\"21:9\"],\"show_search\":true,\"search_filter\":\"\",\"hide_label\":false,\"hide_property\":false,\"is_custom\":true,\"is_user_added\":true},\"settable\":true,\"is_user_defined\":true,\"private\":false,\"parent_container_name\":\"\",\"parent_element_name\":null},\"output_path\":{\"name\":\"output_path\",\"tooltip\":\"New parameter\",\"type\":\"str\",\"input_types\":[\"str\"],\"output_type\":\"str\",\"default_value\":\"\",\"tooltip_as_input\":null,\"tooltip_as_property\":null,\"tooltip_as_output\":null,\"mode_allowed_input\":true,\"mode_allowed_property\":true,\"mode_allowed_output\":true,\"ui_options\":{\"fileSystemPicker\":{\"allowFiles\":true,\"allowDirectories\":false,\"allowSequences\":false,\"multiple\":false,\"workspaceOnly\":false,\"allowCreate\":true,\"allowRename\":false},\"button_label\":\"\",\"variant\":\"secondary\",\"size\":\"icon\",\"state\":\"normal\",\"full_width\":false,\"button_icon\":\"cog\",\"iconPosition\":\"left\",\"tooltip\":\"Create and connect a FileOutputSettings node\",\"is_custom\":true,\"is_user_added\":true,\"hide\":false,\"step\":1},\"settable\":true,\"is_user_defined\":true,\"private\":false,\"parent_container_name\":\"\",\"parent_element_name\":null},\"image_size\":{\"name\":\"image_size\",\"tooltip\":\"New parameter\",\"type\":\"str\",\"input_types\":[\"any\"],\"output_type\":\"str\",\"default_value\":\"\",\"tooltip_as_input\":null,\"tooltip_as_property\":null,\"tooltip_as_output\":null,\"mode_allowed_input\":true,\"mode_allowed_property\":true,\"mode_allowed_output\":true,\"ui_options\":{\"simple_dropdown\":[\"1K\",\"2K\",\"4K\"],\"show_search\":true,\"search_filter\":\"\",\"hide_label\":false,\"hide_property\":false,\"is_custom\":true,\"is_user_added\":true},\"settable\":true,\"is_user_defined\":true,\"private\":false,\"parent_container_name\":\"\",\"parent_element_name\":null}}},\"outputs\":{\"End Flow\":{\"exec_in\":{\"name\":\"exec_in\",\"tooltip\":\"Control path when the flow completed successfully\",\"type\":\"parametercontroltype\",\"input_types\":[\"parametercontroltype\"],\"output_type\":\"parametercontroltype\",\"default_value\":null,\"tooltip_as_input\":null,\"tooltip_as_property\":null,\"tooltip_as_output\":null,\"mode_allowed_input\":true,\"mode_allowed_property\":false,\"mode_allowed_output\":false,\"ui_options\":{\"parameter_render_location\":\"top\",\"display_name\":\"Succeeded\"},\"settable\":true,\"is_user_defined\":true,\"private\":false,\"parent_container_name\":null,\"parent_element_name\":null},\"failed\":{\"name\":\"failed\",\"tooltip\":\"Control path when the flow failed\",\"type\":\"parametercontroltype\",\"input_types\":[\"parametercontroltype\"],\"output_type\":\"parametercontroltype\",\"default_value\":null,\"tooltip_as_input\":null,\"tooltip_as_property\":null,\"tooltip_as_output\":null,\"mode_allowed_input\":true,\"mode_allowed_property\":false,\"mode_allowed_output\":false,\"ui_options\":{\"parameter_render_location\":\"top\",\"display_name\":\"Failed\"},\"settable\":true,\"is_user_defined\":true,\"private\":false,\"parent_container_name\":null,\"parent_element_name\":null},\"was_successful\":{\"name\":\"was_successful\",\"tooltip\":\"Indicates whether it completed without errors.\",\"type\":\"bool\",\"input_types\":[\"bool\"],\"output_type\":\"bool\",\"default_value\":false,\"tooltip_as_input\":null,\"tooltip_as_property\":null,\"tooltip_as_output\":null,\"mode_allowed_input\":false,\"mode_allowed_property\":true,\"mode_allowed_output\":false,\"ui_options\":{},\"settable\":false,\"is_user_defined\":true,\"private\":false,\"parent_container_name\":null,\"parent_element_name\":\"Status\"},\"result_details\":{\"name\":\"result_details\",\"tooltip\":\"Details about the operation result\",\"type\":\"str\",\"input_types\":[\"str\"],\"output_type\":\"str\",\"default_value\":null,\"tooltip_as_input\":null,\"tooltip_as_property\":null,\"tooltip_as_output\":null,\"mode_allowed_input\":true,\"mode_allowed_property\":false,\"mode_allowed_output\":false,\"ui_options\":{\"multiline\":true,\"placeholder_text\":\"Details about the completion or failure will be shown here.\"},\"settable\":false,\"is_user_defined\":true,\"private\":false,\"parent_container_name\":null,\"parent_element_name\":\"Status\"}}}}"
# 
# ///

import argparse
import asyncio
import json
import logging
import pickle
from griptape.artifacts.image_url_artifact import ImageUrlArtifact
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
    top_level_unique_values_dict = {'553085ab-d911-46f1-929b-9974c397ac65': pickle.loads(b'\x80\x04\x89.'), '3cc8f886-4ae5-4c28-8aea-e13b530fcacb': pickle.loads(b'\x80\x04\x95\x04\x00\x00\x00\x00\x00\x00\x00MX\x02.'), 'e9949b15-8a48-4235-8f97-db1935ea0d1e': pickle.loads(b'\x80\x04\x95\x13\x00\x00\x00\x00\x00\x00\x00\x8c\x0fNano Banana Pro\x94.'), 'd1a51d64-9e32-44c4-b4d3-4b291ea34be0': pickle.loads(b'\x80\x04\x95\x11\x00\x00\x00\x00\x00\x00\x00\x8c\rpooootatooooo\x94.'), '645cd8b5-9f4d-4292-aba3-d0efb0e4e0f9': pickle.loads(b'\x80\x04]\x94.'), 'a57b1b60-c608-44cb-8283-cfd60512229f': pickle.loads(b'\x80\x04]\x94.'), '419ab1d8-6a50-4bbe-bdc3-68ec32a355f7': pickle.loads(b'\x80\x04]\x94.'), '34225910-a5ce-4e9a-bffb-2991eeba025f': pickle.loads(b'\x80\x04\x95\x07\x00\x00\x00\x00\x00\x00\x00\x8c\x031:1\x94.'), '90a36273-96f0-4e79-9e3a-1a44793df34b': pickle.loads(b'\x80\x04\x95\x06\x00\x00\x00\x00\x00\x00\x00\x8c\x021K\x94.'), '3ebd4717-fbc1-4851-97fa-1ea9bca9c599': pickle.loads(b'\x80\x04\x88.'), 'f82eda50-57ad-4165-b19b-e1b540c6aace': pickle.loads(b'\x80\x04\x95\n\x00\x00\x00\x00\x00\x00\x00G?\xf0\x00\x00\x00\x00\x00\x00.'), 'fc245074-ca63-4176-820c-0a5a5a79263b': pickle.loads(b'\x80\x04\x95\n\x00\x00\x00\x00\x00\x00\x00G?\xeeffffff.'), 'a8f065fe-8cab-4598-afe4-5fe4d70c70be': pickle.loads(b'\x80\x04\x95\x92\x01\x00\x00\x00\x00\x00\x00\x8c%griptape.artifacts.image_url_artifact\x94\x8c\x10ImageUrlArtifact\x94\x93\x94)\x81\x94}\x94(\x8c\x04type\x94\x8c\x10ImageUrlArtifact\x94\x8c\x0bmodule_name\x94\x8c%griptape.artifacts.image_url_artifact\x94\x8c\x02id\x94\x8c 834583fd45bd402e99edf1f5ada8d783\x94\x8c\treference\x94N\x8c\x04meta\x94}\x94\x8c\x04name\x94\x8c5Google Nano Banana Image Generation_google_image.jpeg\x94\x8c\x16encoding_error_handler\x94\x8c\x06strict\x94\x8c\x08encoding\x94\x8c\x05utf-8\x94\x8c\x05value\x94\x8c?{outputs}/Google Nano Banana Image Generation_google_image.jpeg\x94ub.'), 'eedcfca1-fe8f-4d2f-b282-743bc697f88e': pickle.loads(b'\x80\x04\x95\x95\x01\x00\x00\x00\x00\x00\x00]\x94\x8c%griptape.artifacts.image_url_artifact\x94\x8c\x10ImageUrlArtifact\x94\x93\x94)\x81\x94}\x94(\x8c\x04type\x94\x8c\x10ImageUrlArtifact\x94\x8c\x0bmodule_name\x94\x8c%griptape.artifacts.image_url_artifact\x94\x8c\x02id\x94\x8c 834583fd45bd402e99edf1f5ada8d783\x94\x8c\treference\x94N\x8c\x04meta\x94}\x94\x8c\x04name\x94\x8c5Google Nano Banana Image Generation_google_image.jpeg\x94\x8c\x16encoding_error_handler\x94\x8c\x06strict\x94\x8c\x08encoding\x94\x8c\x05utf-8\x94\x8c\x05value\x94\x8c?{outputs}/Google Nano Banana Image Generation_google_image.jpeg\x94uba.'), 'c7e6bd15-952d-4f5a-86f2-ec623ab26613': pickle.loads(b'\x80\x04\x95\x04\x00\x00\x00\x00\x00\x00\x00\x8c\x00\x94.'), '69734fbb-684a-406e-820f-0c0a43845737': pickle.loads(b'\x80\x04\x95\x15\x00\x00\x00\x00\x00\x00\x00\x8c\x11google_image.jpeg\x94.'), '1f1f6a9c-1770-4b65-be41-6a81ade2c2a7': pickle.loads(b'\x80\x04\x95G\x00\x00\x00\x00\x00\x00\x00\x8cCGoogle Nano Banana Image Generation generated 1 image successfully.\x94.'), '89349b9f-7c88-4f97-b0ad-b73fcc1ad30b': pickle.loads(b'\x80\x04\x95(\x00\x00\x00\x00\x00\x00\x00\x8c$0b9e6afb-4d55-4a74-8da2-b14c8f48eebd\x94.'), 'c301a54d-888e-495b-a7cb-c4a8a849e15e': pickle.loads(b'\x80\x04\x95\r\x00\x00\x00\x00\x00\x00\x00\x8c\tCOMPLETED\x94.')}
    # Create the Flow, then do work within it as context.
    flow0_name = (await GriptapeNodes.ahandle_request(CreateFlowRequest(parent_flow_name=None, flow_name='ControlFlow_1', set_as_new_context=False, metadata={}))).flow_name
    with GriptapeNodes.ContextManager().flow(flow0_name):
        node0_name = (await GriptapeNodes.ahandle_request(CreateNodeRequest(node_type='GoogleImageGeneration', specific_library_name='Griptape Nodes Library', node_name='Google Nano Banana Image Generation', metadata={'position': {'x': -874.366239490908, 'y': 1834.9922964575749}, 'tempId': 'placing-1783114344757-ooz01t', 'library_node_metadata': {'category': 'image', 'description': 'Generate images using Google models via Griptape model proxy', 'display_name': 'Google Nano Banana Image Generation', 'tags': ['image', 'generation', 'ai', 'api', 'google', 'nano-banana'], 'icon': 'sparkles', 'color': None, 'group': 'create', 'deprecation': None, 'is_node_group': None, 'declarations': [{'type': 'model_usage', 'model_ids': ['gtc_gemini_3_pro_image', 'gtc_gemini_3_1_flash_image']}]}, 'library': 'Griptape Nodes Library', 'node_type': 'GoogleImageGeneration', 'showaddparameter': False, 'size': {'width': 600, 'height': 1032}}, initial_setup=True))).node_name
        with GriptapeNodes.ContextManager().node(node0_name):
            await GriptapeNodes.ahandle_request(AlterParameterDetailsRequest(parameter_name='aspect_ratio', default_value='1:1', initial_setup=True))
        node1_name = (await GriptapeNodes.ahandle_request(CreateNodeRequest(node_type='StartFlow', specific_library_name='Griptape Nodes Library', node_name='Start Flow', metadata={'position': {'x': -1863.5348768914623, 'y': 2006.1499061801571}, 'tempId': 'placing-1783116412486-6hvp', 'library_node_metadata': {'category': 'workflows', 'description': 'Define the start of a workflow and pass parameters into the flow', 'display_name': 'Start Flow', 'tags': ['workflow', 'execution'], 'icon': None, 'color': None, 'group': 'create', 'deprecation': None, 'is_node_group': None, 'declarations': []}, 'library': 'Griptape Nodes Library', 'node_type': 'StartFlow', 'showaddparameter': True, 'size': {'width': 600, 'height': 523}}, initial_setup=True))).node_name
        with GriptapeNodes.ContextManager().node(node1_name):
            await GriptapeNodes.ahandle_request(AddParameterToNodeRequest(parameter_name='models', default_value='FLUX.2 [flex]', tooltip='Enter text/string for models.', type='str', input_types=['str'], output_type='str', ui_options={'is_custom': True, 'is_user_added': True, 'display_name': 'Models', 'multiline': False, 'markdown': False, 'dropdown_row_icons': False, 'dropdown_row_subtitles': False, 'simple_dropdown': ['Nano Banana Pro', 'Nano Banana 2'], 'data': [{'name': 'Nano Banana Pro', 'args': {}}, {'name': 'Nano Banana 2', 'args': {}}], 'show_search': True, 'search_filter': '', 'step': 1, 'hide': False}, initial_setup=True))
            await GriptapeNodes.ahandle_request(AddParameterToNodeRequest(parameter_name='prompt', default_value='', tooltip='New parameter', type='str', input_types=['any'], output_type='str', ui_options={'multiline': True, 'placeholder_text': 'Enter prompt...', 'hide_label': False, 'hide_property': False, 'is_custom': True, 'is_user_added': True}, parent_container_name='', initial_setup=True))
            await GriptapeNodes.ahandle_request(AddParameterToNodeRequest(parameter_name='aspect_ratio', default_value='', tooltip='New parameter', type='str', input_types=['any'], output_type='str', ui_options={'simple_dropdown': ['1:1', '3:2', '2:3', '3:4', '4:3', '4:5', '5:4', '9:16', '16:9', '21:9'], 'show_search': True, 'search_filter': '', 'hide_label': False, 'hide_property': False, 'is_custom': True, 'is_user_added': True}, parent_container_name='', initial_setup=True))
            await GriptapeNodes.ahandle_request(AddParameterToNodeRequest(parameter_name='output_path', default_value='', tooltip='New parameter', type='str', input_types=['str'], output_type='str', ui_options={'fileSystemPicker': {'allowFiles': True, 'allowDirectories': False, 'allowSequences': False, 'multiple': False, 'workspaceOnly': False, 'allowCreate': True, 'allowRename': False}, 'button_label': '', 'variant': 'secondary', 'size': 'icon', 'state': 'normal', 'full_width': False, 'button_icon': 'cog', 'iconPosition': 'left', 'tooltip': 'Create and connect a FileOutputSettings node', 'is_custom': True, 'is_user_added': True, 'hide': False, 'step': 1}, parent_container_name='', initial_setup=True))
            await GriptapeNodes.ahandle_request(AddParameterToNodeRequest(parameter_name='image_size', default_value='', tooltip='New parameter', type='str', input_types=['any'], output_type='str', ui_options={'simple_dropdown': ['1K', '2K', '4K'], 'show_search': True, 'search_filter': '', 'hide_label': False, 'hide_property': False, 'is_custom': True, 'is_user_added': True}, parent_container_name='', initial_setup=True))
        node2_name = (await GriptapeNodes.ahandle_request(CreateNodeRequest(node_type='EndFlow', specific_library_name='Griptape Nodes Library', node_name='End Flow', metadata={'position': {'x': 58.990799689525886, 'y': 1834.9922964575749}, 'tempId': 'placing-1783118923256-5mjjp', 'library_node_metadata': {'category': 'workflows', 'description': 'Define the end of a workflow and return parameters from the flow', 'display_name': 'End Flow', 'tags': ['workflow', 'execution'], 'icon': None, 'color': None, 'group': 'create', 'deprecation': None, 'is_node_group': None, 'declarations': [], 'resolved_model_usage': []}, 'library': 'Griptape Nodes Library', 'node_type': 'EndFlow', 'showaddparameter': True, 'size': {'width': 600, 'height': 300}}, initial_setup=True))).node_name
        await GriptapeNodes.ahandle_request(CreateConnectionRequest(source_node_name=node1_name, source_parameter_name='models', target_node_name=node0_name, target_parameter_name='model', initial_setup=True))
        await GriptapeNodes.ahandle_request(CreateConnectionRequest(source_node_name=node1_name, source_parameter_name='prompt', target_node_name=node0_name, target_parameter_name='prompt', initial_setup=True))
        await GriptapeNodes.ahandle_request(CreateConnectionRequest(source_node_name=node1_name, source_parameter_name='aspect_ratio', target_node_name=node0_name, target_parameter_name='aspect_ratio', initial_setup=True))
        await GriptapeNodes.ahandle_request(CreateConnectionRequest(source_node_name=node1_name, source_parameter_name='output_path', target_node_name=node0_name, target_parameter_name='output_file', initial_setup=True))
        await GriptapeNodes.ahandle_request(CreateConnectionRequest(source_node_name=node0_name, source_parameter_name='exec_out', target_node_name=node2_name, target_parameter_name='exec_in', initial_setup=True))
        await GriptapeNodes.ahandle_request(CreateConnectionRequest(source_node_name=node0_name, source_parameter_name='failure', target_node_name=node2_name, target_parameter_name='failed', initial_setup=True))
        await GriptapeNodes.ahandle_request(CreateConnectionRequest(source_node_name=node1_name, source_parameter_name='image_size', target_node_name=node0_name, target_parameter_name='image_size', initial_setup=True))
        with GriptapeNodes.ContextManager().node(node0_name):
            await GriptapeNodes.ahandle_request(SetParameterValueRequest(parameter_name='api_key_provider', node_name=node0_name, value=top_level_unique_values_dict['553085ab-d911-46f1-929b-9974c397ac65'], initial_setup=True, is_output=False))
            await GriptapeNodes.ahandle_request(SetParameterValueRequest(parameter_name='timeout', node_name=node0_name, value=top_level_unique_values_dict['3cc8f886-4ae5-4c28-8aea-e13b530fcacb'], initial_setup=True, is_output=False))
            await GriptapeNodes.ahandle_request(SetParameterValueRequest(parameter_name='model', node_name=node0_name, value=top_level_unique_values_dict['e9949b15-8a48-4235-8f97-db1935ea0d1e'], initial_setup=True, is_output=False))
            await GriptapeNodes.ahandle_request(SetParameterValueRequest(parameter_name='prompt', node_name=node0_name, value=top_level_unique_values_dict['d1a51d64-9e32-44c4-b4d3-4b291ea34be0'], initial_setup=True, is_output=False))
            await GriptapeNodes.ahandle_request(SetParameterValueRequest(parameter_name='input_images', node_name=node0_name, value=top_level_unique_values_dict['645cd8b5-9f4d-4292-aba3-d0efb0e4e0f9'], initial_setup=True, is_output=False))
            await GriptapeNodes.ahandle_request(SetParameterValueRequest(parameter_name='object_images', node_name=node0_name, value=top_level_unique_values_dict['a57b1b60-c608-44cb-8283-cfd60512229f'], initial_setup=True, is_output=False))
            await GriptapeNodes.ahandle_request(SetParameterValueRequest(parameter_name='human_images', node_name=node0_name, value=top_level_unique_values_dict['419ab1d8-6a50-4bbe-bdc3-68ec32a355f7'], initial_setup=True, is_output=False))
            await GriptapeNodes.ahandle_request(SetParameterValueRequest(parameter_name='aspect_ratio', node_name=node0_name, value=top_level_unique_values_dict['34225910-a5ce-4e9a-bffb-2991eeba025f'], initial_setup=True, is_output=False))
            await GriptapeNodes.ahandle_request(SetParameterValueRequest(parameter_name='image_size', node_name=node0_name, value=top_level_unique_values_dict['90a36273-96f0-4e79-9e3a-1a44793df34b'], initial_setup=True, is_output=False))
            await GriptapeNodes.ahandle_request(SetParameterValueRequest(parameter_name='auto_image_resize', node_name=node0_name, value=top_level_unique_values_dict['3ebd4717-fbc1-4851-97fa-1ea9bca9c599'], initial_setup=True, is_output=False))
            await GriptapeNodes.ahandle_request(SetParameterValueRequest(parameter_name='temperature', node_name=node0_name, value=top_level_unique_values_dict['f82eda50-57ad-4165-b19b-e1b540c6aace'], initial_setup=True, is_output=False))
            await GriptapeNodes.ahandle_request(SetParameterValueRequest(parameter_name='top_p', node_name=node0_name, value=top_level_unique_values_dict['fc245074-ca63-4176-820c-0a5a5a79263b'], initial_setup=True, is_output=False))
            await GriptapeNodes.ahandle_request(SetParameterValueRequest(parameter_name='use_google_search', node_name=node0_name, value=top_level_unique_values_dict['553085ab-d911-46f1-929b-9974c397ac65'], initial_setup=True, is_output=False))
            await GriptapeNodes.ahandle_request(SetParameterValueRequest(parameter_name='use_google_image_search', node_name=node0_name, value=top_level_unique_values_dict['553085ab-d911-46f1-929b-9974c397ac65'], initial_setup=True, is_output=False))
            await GriptapeNodes.ahandle_request(SetParameterValueRequest(parameter_name='image', node_name=node0_name, value=top_level_unique_values_dict['a8f065fe-8cab-4598-afe4-5fe4d70c70be'], initial_setup=True, is_output=True))
            await GriptapeNodes.ahandle_request(SetParameterValueRequest(parameter_name='all_images', node_name=node0_name, value=top_level_unique_values_dict['eedcfca1-fe8f-4d2f-b282-743bc697f88e'], initial_setup=True, is_output=True))
            await GriptapeNodes.ahandle_request(SetParameterValueRequest(parameter_name='text', node_name=node0_name, value=top_level_unique_values_dict['c7e6bd15-952d-4f5a-86f2-ec623ab26613'], initial_setup=True, is_output=True))
            await GriptapeNodes.ahandle_request(SetParameterValueRequest(parameter_name='output_file', node_name=node0_name, value=top_level_unique_values_dict['69734fbb-684a-406e-820f-0c0a43845737'], initial_setup=True, is_output=False))
            await GriptapeNodes.ahandle_request(SetParameterValueRequest(parameter_name='was_successful', node_name=node0_name, value=top_level_unique_values_dict['3ebd4717-fbc1-4851-97fa-1ea9bca9c599'], initial_setup=True, is_output=False))
            await GriptapeNodes.ahandle_request(SetParameterValueRequest(parameter_name='was_successful', node_name=node0_name, value=top_level_unique_values_dict['3ebd4717-fbc1-4851-97fa-1ea9bca9c599'], initial_setup=True, is_output=True))
            await GriptapeNodes.ahandle_request(SetParameterValueRequest(parameter_name='result_details', node_name=node0_name, value=top_level_unique_values_dict['1f1f6a9c-1770-4b65-be41-6a81ade2c2a7'], initial_setup=True, is_output=False))
            await GriptapeNodes.ahandle_request(SetParameterValueRequest(parameter_name='result_details', node_name=node0_name, value=top_level_unique_values_dict['1f1f6a9c-1770-4b65-be41-6a81ade2c2a7'], initial_setup=True, is_output=True))
            await GriptapeNodes.ahandle_request(SetParameterValueRequest(parameter_name='generation_id', node_name=node0_name, value=top_level_unique_values_dict['c7e6bd15-952d-4f5a-86f2-ec623ab26613'], initial_setup=True, is_output=False))
            await GriptapeNodes.ahandle_request(SetParameterValueRequest(parameter_name='generation_id', node_name=node0_name, value=top_level_unique_values_dict['89349b9f-7c88-4f97-b0ad-b73fcc1ad30b'], initial_setup=True, is_output=True))
            await GriptapeNodes.ahandle_request(SetParameterValueRequest(parameter_name='generation_status', node_name=node0_name, value=top_level_unique_values_dict['c7e6bd15-952d-4f5a-86f2-ec623ab26613'], initial_setup=True, is_output=False))
            await GriptapeNodes.ahandle_request(SetParameterValueRequest(parameter_name='generation_status', node_name=node0_name, value=top_level_unique_values_dict['c301a54d-888e-495b-a7cb-c4a8a849e15e'], initial_setup=True, is_output=True))
        with GriptapeNodes.ContextManager().node(node1_name):
            await GriptapeNodes.ahandle_request(SetParameterValueRequest(parameter_name='models', node_name=node1_name, value=top_level_unique_values_dict['e9949b15-8a48-4235-8f97-db1935ea0d1e'], initial_setup=True, is_output=False))
            await GriptapeNodes.ahandle_request(SetParameterValueRequest(parameter_name='prompt', node_name=node1_name, value=top_level_unique_values_dict['d1a51d64-9e32-44c4-b4d3-4b291ea34be0'], initial_setup=True, is_output=False))
            await GriptapeNodes.ahandle_request(SetParameterValueRequest(parameter_name='aspect_ratio', node_name=node1_name, value=top_level_unique_values_dict['34225910-a5ce-4e9a-bffb-2991eeba025f'], initial_setup=True, is_output=False))
            await GriptapeNodes.ahandle_request(SetParameterValueRequest(parameter_name='output_path', node_name=node1_name, value=top_level_unique_values_dict['c7e6bd15-952d-4f5a-86f2-ec623ab26613'], initial_setup=True, is_output=False))
            await GriptapeNodes.ahandle_request(SetParameterValueRequest(parameter_name='image_size', node_name=node1_name, value=top_level_unique_values_dict['c7e6bd15-952d-4f5a-86f2-ec623ab26613'], initial_setup=True, is_output=False))
        with GriptapeNodes.ContextManager().node(node2_name):
            await GriptapeNodes.ahandle_request(SetParameterValueRequest(parameter_name='was_successful', node_name=node2_name, value=top_level_unique_values_dict['553085ab-d911-46f1-929b-9974c397ac65'], initial_setup=True, is_output=False))

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
    parser.add_argument('--models', dest='models', default=None, help='Enter text/string for models.')
    parser.add_argument('--prompt', dest='prompt', default=None, help='New parameter')
    parser.add_argument('--aspect_ratio', dest='aspect_ratio', default=None, help='New parameter')
    parser.add_argument('--output_path', dest='output_path', default=None, help='New parameter')
    parser.add_argument('--image_size', dest='image_size', default=None, help='New parameter')
    args = parser.parse_args()
    flow_input = {}
    if args.json_input is not None:
        flow_input = json.loads(args.json_input)
    if args.json_input is None:
        if 'Start Flow' not in flow_input:
            flow_input['Start Flow'] = {}
        if args.exec_out is not None:
            flow_input['Start Flow']['exec_out'] = args.exec_out
        if args.models is not None:
            flow_input['Start Flow']['models'] = args.models
        if args.prompt is not None:
            flow_input['Start Flow']['prompt'] = args.prompt
        if args.aspect_ratio is not None:
            flow_input['Start Flow']['aspect_ratio'] = args.aspect_ratio
        if args.output_path is not None:
            flow_input['Start Flow']['output_path'] = args.output_path
        if args.image_size is not None:
            flow_input['Start Flow']['image_size'] = args.image_size
    executor = LocalWorkflowExecutor.from_cli_args(args, skip_library_loading=True, workflows_to_register=[__file__])
    workflow_output = execute_workflow(input=flow_input, workflow_executor=executor)
    print(workflow_output)
