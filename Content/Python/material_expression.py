import unreal


# --------------------------------------------------
# create parametric material expression nodes
# --------------------------------------------------
def create_material_expression_vector_parameter(material, node_pos_x=0, node_pos_y=0, parameter_name='Param', default_value=(0.0, 0.0, 0.0, 0.0), group='None', sort_priority=32, in_function=False):
    if not in_function:
        vector_parameter = unreal.MaterialEditingLibrary.create_material_expression(material, unreal.MaterialExpressionVectorParameter, node_pos_x, node_pos_y)
    else:
        vector_parameter = unreal.MaterialEditingLibrary.create_material_expression_in_function(material, unreal.MaterialExpressionVectorParameter, node_pos_x, node_pos_y)
    mapping = {'parameter_name': parameter_name, 'default_value': default_value, 'group': group, 'sort_priority': sort_priority}
    vector_parameter.set_editor_properties(mapping)
    return vector_parameter


def create_material_expression_scalar_parameter(material, node_pos_x=0, node_pos_y=0, parameter_name='Param', default_value=0.0, slider_max=0.0, slider_min=0.0, group='None', sort_priority=32, in_function=False):
    if not in_function:
        scalar_parameter = unreal.MaterialEditingLibrary.create_material_expression(material, unreal.MaterialExpressionScalarParameter, node_pos_x, node_pos_y)
    else:
        scalar_parameter = unreal.MaterialEditingLibrary.create_material_expression_in_function(material, unreal.MaterialExpressionScalarParameter, node_pos_x, node_pos_y)
    mapping = {'parameter_name': parameter_name, 'default_value': default_value, 'slider_max': slider_max, 'slider_min': slider_min, 'group': group, 'sort_priority': sort_priority}
    scalar_parameter.set_editor_properties(mapping)
    return scalar_parameter


def create_material_expression_static_switch_parameter(material, node_pos_x=0, node_pos_y=0, parameter_name='Param', default_value=False, group='None', sort_priority=32, in_function=False):
    if not in_function:
        static_switch_parameter = unreal.MaterialEditingLibrary.create_material_expression(material, unreal.MaterialExpressionStaticSwitchParameter, node_pos_x, node_pos_y)
    else:
        static_switch_parameter = unreal.MaterialEditingLibrary.create_material_expression_in_function(material, unreal.MaterialExpressionStaticSwitchParameter, node_pos_x, node_pos_y)
    mapping = {'parameter_name': parameter_name, 'default_value': default_value, 'group': group, 'sort_priority': sort_priority}
    static_switch_parameter.set_editor_properties(mapping)
    return static_switch_parameter


def create_material_expression_texture_sample_parameter_2d(material, node_pos_x=0, node_pos_y=0, parameter_name='Param', texture=unreal.EditorAssetLibrary.load_asset('/Engine/EngineResources/DefaultTexture'), sampler_type=unreal.MaterialSamplerType.SAMPLERTYPE_COLOR, group='None', sort_priority=32, in_function=False):
    if not in_function:
        texture_sample_parameter_2d = unreal.MaterialEditingLibrary.create_material_expression(material, unreal.MaterialExpressionTextureSampleParameter2D, node_pos_x, node_pos_y)
    else:
        texture_sample_parameter_2d = unreal.MaterialEditingLibrary.create_material_expression_in_function(material, unreal.MaterialExpressionTextureSampleParameter2D, node_pos_x, node_pos_y)
    mapping = {'parameter_name': parameter_name, 'texture': texture, 'sampler_type': sampler_type, 'group': group, 'sort_priority': sort_priority}
    texture_sample_parameter_2d.set_editor_properties(mapping)
    return texture_sample_parameter_2d


# --------------------------------------------------
# create general material expression nodes
# --------------------------------------------------
def create_material_expression_constant(material, node_pos_x=0, node_pos_y=0, r=0.0, in_function=False):
    if not in_function:
        constant = unreal.MaterialEditingLibrary.create_material_expression(material, unreal.MaterialExpressionConstant, node_pos_x, node_pos_y)
    else:
        constant = unreal.MaterialEditingLibrary.create_material_expression_in_function(material, unreal.MaterialExpressionConstant, node_pos_x, node_pos_y)
    constant.set_editor_property('r', r)
    return constant


def create_material_expression_constant_2_vector(material, node_pos_x=0, node_pos_y=0, r=0.0, g=0.0, in_function=False):
    if not in_function:
        constant2 = unreal.MaterialEditingLibrary.create_material_expression(material, unreal.MaterialExpressionConstant2Vector, node_pos_x, node_pos_y)
    else:
        constant2 = unreal.MaterialEditingLibrary.create_material_expression_in_function(material, unreal.MaterialExpressionConstant2Vector, node_pos_x, node_pos_y)
    constant2.set_editor_property('r', r)
    constant2.set_editor_property('g', g)
    return constant2


def create_material_expression_constant_3_vector(material, node_pos_x=0, node_pos_y=0, constant=(0.0, 0.0, 0.0, 0.0), in_function=False):
    if not in_function:
        constant3 = unreal.MaterialEditingLibrary.create_material_expression(material, unreal.MaterialExpressionConstant3Vector, node_pos_x, node_pos_y)
    else:
        constant3 = unreal.MaterialEditingLibrary.create_material_expression_in_function(material, unreal.MaterialExpressionConstant3Vector, node_pos_x, node_pos_y)
    constant3.set_editor_property('constant', constant)
    return constant3


def create_material_expression_constant_4_vector(material, node_pos_x=0, node_pos_y=0, constant=(0.0, 0.0, 0.0, 0.0), in_function=False):
    if not in_function:
        constant4 = unreal.MaterialEditingLibrary.create_material_expression(material, unreal.MaterialExpressionConstant4Vector, node_pos_x, node_pos_y)
    else:
        constant4 = unreal.MaterialEditingLibrary.create_material_expression_in_function(material, unreal.MaterialExpressionConstant4Vector, node_pos_x, node_pos_y)
    constant4.set_editor_property('constant', constant)
    return constant4


def create_material_expression_abs(material, node_pos_x=0, node_pos_y=0, in_function=False):
    if not in_function:
        return unreal.MaterialEditingLibrary.create_material_expression(material, unreal.MaterialExpressionAbs, node_pos_x, node_pos_y)
    else:
        return unreal.MaterialEditingLibrary.create_material_expression_in_function(material, unreal.MaterialExpressionAbs, node_pos_x, node_pos_y)


def create_material_expression_add(material, node_pos_x=0, node_pos_y=0, in_function=False):
    if not in_function:
        return unreal.MaterialEditingLibrary.create_material_expression(material, unreal.MaterialExpressionAdd, node_pos_x, node_pos_y)
    else:
        return unreal.MaterialEditingLibrary.create_material_expression_in_function(material, unreal.MaterialExpressionAdd, node_pos_x, node_pos_y)


def create_material_expression_subtract(material, node_pos_x=0, node_pos_y=0, in_function=False):
    if not in_function:
        return unreal.MaterialEditingLibrary.create_material_expression(material, unreal.MaterialExpressionSubtract, node_pos_x, node_pos_y)
    else:
        return unreal.MaterialEditingLibrary.create_material_expression_in_function(material, unreal.MaterialExpressionSubtract, node_pos_x, node_pos_y)


def create_material_expression_multiply(material, node_pos_x=0, node_pos_y=0, in_function=False):
    if not in_function:
        return unreal.MaterialEditingLibrary.create_material_expression(material, unreal.MaterialExpressionMultiply, node_pos_x, node_pos_y)
    else:
        return unreal.MaterialEditingLibrary.create_material_expression_in_function(material, unreal.MaterialExpressionMultiply, node_pos_x, node_pos_y)


def create_material_expression_divide(material, node_pos_x=0, node_pos_y=0, in_function=False):
    if not in_function:
        return unreal.MaterialEditingLibrary.create_material_expression(material, unreal.MaterialExpressionDivide, node_pos_x, node_pos_y)
    else:
        return unreal.MaterialEditingLibrary.create_material_expression_in_function(material, unreal.MaterialExpressionDivide, node_pos_x, node_pos_y)


def create_material_expression_power(material, node_pos_x=0, node_pos_y=0, in_function=False):
    if not in_function:
        return unreal.MaterialEditingLibrary.create_material_expression(material, unreal.MaterialExpressionPower, node_pos_x, node_pos_y)
    else:
        return unreal.MaterialEditingLibrary.create_material_expression_in_function(material, unreal.MaterialExpressionPower, node_pos_x, node_pos_y)


def create_material_expression_one_minus(material, node_pos_x=0, node_pos_y=0, in_function=False):
    if not in_function:
        return unreal.MaterialEditingLibrary.create_material_expression(material, unreal.MaterialExpressionOneMinus, node_pos_x, node_pos_y)
    else:
        return unreal.MaterialEditingLibrary.create_material_expression_in_function(material, unreal.MaterialExpressionOneMinus, node_pos_x, node_pos_y)


def create_material_expression_dot(material, node_pos_x=0, node_pos_y=0, in_function=False):
    if not in_function:
        return unreal.MaterialEditingLibrary.create_material_expression(material, unreal.MaterialExpressionDotProduct, node_pos_x, node_pos_y)
    else:
        return unreal.MaterialEditingLibrary.create_material_expression_in_function(material, unreal.MaterialExpressionDotProduct, node_pos_x, node_pos_y)


def create_material_expression_linear_interpolate(material, node_pos_x=0, node_pos_y=0, in_function=False):
    if not in_function:
        return unreal.MaterialEditingLibrary.create_material_expression(material, unreal.MaterialExpressionLinearInterpolate, node_pos_x, node_pos_y)
    else:
        return unreal.MaterialEditingLibrary.create_material_expression_in_function(material, unreal.MaterialExpressionLinearInterpolate, node_pos_x, node_pos_y)


def create_material_expression_component_mask(material, node_pos_x=0, node_pos_y=0, r=True, g=True, b=False, a=False, in_function=False):
    if not in_function:
        mask = unreal.MaterialEditingLibrary.create_material_expression(material, unreal.MaterialExpressionComponentMask, node_pos_x, node_pos_y)
    else:
        mask = unreal.MaterialEditingLibrary.create_material_expression_in_function(material, unreal.MaterialExpressionComponentMask, node_pos_x, node_pos_y)
    mapping = {'r': r, 'g': g, 'b': b, 'a': a}
    mask.set_editor_properties(mapping)
    return mask


def create_material_expression_fresnel(material, node_pos_x=0, node_pos_y=0, in_function=False):
    if not in_function:
        return unreal.MaterialEditingLibrary.create_material_expression(material, unreal.MaterialExpressionFresnel, node_pos_x, node_pos_y)
    else:
        return unreal.MaterialEditingLibrary.create_material_expression_in_function(material, unreal.MaterialExpressionFresnel, node_pos_x, node_pos_y)


def create_material_expression_saturate(material, node_pos_x=0, node_pos_y=0, in_function=False):
    if not in_function:
        return unreal.MaterialEditingLibrary.create_material_expression(material, unreal.MaterialExpressionSaturate, node_pos_x, node_pos_y)
    else:
        return unreal.MaterialEditingLibrary.create_material_expression_in_function(material, unreal.MaterialExpressionSaturate, node_pos_x, node_pos_y)


def create_material_expression_desaturation(material, node_pos_x=0, node_pos_y=0, in_function=False):
    if not in_function:
        return unreal.MaterialEditingLibrary.create_material_expression(material, unreal.MaterialExpressionDesaturation, node_pos_x, node_pos_y)
    else:
        return unreal.MaterialEditingLibrary.create_material_expression_in_function(material, unreal.MaterialExpressionDesaturation, node_pos_x, node_pos_y)


def create_material_expression_vertex_normal(material, node_pos_x=0, node_pos_y=0, in_function=False):
    if not in_function:
        return unreal.MaterialEditingLibrary.create_material_expression(material, unreal.MaterialExpressionVertexNormalWS, node_pos_x, node_pos_y)
    else:
        return unreal.MaterialEditingLibrary.create_material_expression_in_function(material, unreal.MaterialExpressionVertexNormalWS, node_pos_x, node_pos_y)


def create_material_expression_camera_vector(material, node_pos_x=0, node_pos_y=0, in_function=False):
    if not in_function:
        return unreal.MaterialEditingLibrary.create_material_expression(material, unreal.MaterialExpressionCameraVectorWS, node_pos_x, node_pos_y)
    else:
        return unreal.MaterialEditingLibrary.create_material_expression_in_function(material, unreal.MaterialExpressionCameraVectorWS, node_pos_x, node_pos_y)


def create_material_expression_reroute(material, node_pos_x=0, node_pos_y=0, in_function=False):
    if not in_function:
        return unreal.MaterialEditingLibrary.create_material_expression(material, unreal.MaterialExpressionReroute, node_pos_x, node_pos_y)
    else:
        return unreal.MaterialEditingLibrary.create_material_expression_in_function(material, unreal.MaterialExpressionReroute, node_pos_x, node_pos_y)


def create_material_expression_material_function_call(material, material_function, node_pos_x=0, node_pos_y=0, in_function=False):
    if not in_function:
        function = unreal.MaterialEditingLibrary.create_material_expression(material, unreal.MaterialExpressionMaterialFunctionCall, node_pos_x, node_pos_y)
    else:
        function = unreal.MaterialEditingLibrary.create_material_expression_in_function(material, unreal.MaterialExpressionMaterialFunctionCall, node_pos_x, node_pos_y)
    function.set_editor_property('material_function', material_function)
    return function


def create_material_expression_flatten_normal(material, node_pos_x=0, node_pos_y=0, in_function=False):
    if not in_function:
        flatten_normal = unreal.MaterialEditingLibrary.create_material_expression(material, unreal.MaterialExpressionMaterialFunctionCall, node_pos_x, node_pos_y)
    else:
        flatten_normal = unreal.MaterialEditingLibrary.create_material_expression_in_function(material, unreal.MaterialExpressionMaterialFunctionCall, node_pos_x, node_pos_y)
    flatten_normal.set_editor_property('material_function', unreal.EditorAssetLibrary.load_asset('/Engine/Functions/Engine_MaterialFunctions01/Texturing/FlattenNormal'))
    return flatten_normal


def create_material_expression_function_output(material, node_pos_x=0, node_pos_y=0, output_name='Result', sort_priority=0):
    output = unreal.MaterialEditingLibrary.create_material_expression_in_function(material, unreal.MaterialExpressionFunctionOutput, node_pos_x, node_pos_y)
    output.set_editor_property('output_name', output_name)
    output.set_editor_property('sort_priority', sort_priority)
    return output
