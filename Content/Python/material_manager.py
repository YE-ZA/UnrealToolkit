import unreal
import editor_basic as eb
import material_expression as me


print('----------Import Material Manager----------')


def set_texture_to_raw():
    textures = eb.get_selected_assets_from_content_browser()
    for texture in textures:
        full_name = texture.get_full_name()  # get the full name (class name + full path) of this instance
        asset_type = full_name.split(' ')[0]
        if asset_type == 'Texture2D':
            texture.set_editor_property('srgb', False)
            print(texture.get_name(), 'has been set to RAW')


def set_texture_to_srgb():
    textures = eb.get_selected_assets_from_content_browser()
    for texture in textures:
        full_name = texture.get_full_name()  # get the full name (class name + full path) of this instance
        asset_type = full_name.split(' ')[0]
        if asset_type == 'Texture2D':
            texture.set_editor_property('srgb', True)
            print(texture.get_name(), 'has been set to sRGB')


def create_material(name):
    asset_tools = unreal.AssetToolsHelpers.get_asset_tools()
    current_path = unreal.EditorUtilityLibrary.get_current_content_browser_path()
    material_name = name
    # determine if a duplicate file already exists in the current path
    if not unreal.EditorAssetLibrary.does_asset_exist(current_path + '/' + material_name):
        new_material = asset_tools.create_asset(material_name, current_path, unreal.Material, unreal.MaterialFactoryNew())
    else:
        index = 1
        while unreal.EditorAssetLibrary.does_asset_exist(current_path + '/' + material_name + '_' + str(index)):
            index += 1
        else:
            material_name = material_name + '_' + str(index)
            new_material = asset_tools.create_asset(material_name, current_path, unreal.Material, unreal.MaterialFactoryNew())
    return new_material


def create_material_function(name):
    asset_tools = unreal.AssetToolsHelpers.get_asset_tools()
    current_path = unreal.EditorUtilityLibrary.get_current_content_browser_path()
    material_function_name = name
    # determine if a duplicate file already exists in the current path
    if not unreal.EditorAssetLibrary.does_asset_exist(current_path + '/' + material_function_name):
        new_material_function = asset_tools.create_asset(material_function_name, current_path, unreal.MaterialFunction, unreal.MaterialFunctionFactoryNew())
    else:
        index = 1
        while unreal.EditorAssetLibrary.does_asset_exist(current_path + '/' + material_function_name + '_' + str(index)):
            index += 1
        else:
            material_function_name = material_function_name + '_' + str(index)
            new_material_function = asset_tools.create_asset(material_function_name, current_path, unreal.MaterialFunction, unreal.MaterialFunctionFactoryNew())
    return new_material_function


def create_material_function_reflectance():
    # nodes reference from Epic Games Automotive Materials
    mf_reflectance = create_material_function('MF_Reflectance')
    mf_reflectance.set_editor_property('expose_to_library', True)

    # create parameter nodes
    node_sp1 = me.create_material_expression_scalar_parameter(mf_reflectance, -128 * 16, 128 * 2 - 16, 'IOR', 1.52, 2.0, 1.0, '01 - Glass', 4, True)
    node_sp2 = me.create_material_expression_scalar_parameter(mf_reflectance, -128 * 11, 128 * 5 + 48, 'Fresnel Edge Adjust', 0.0, 2.0, 0.0, '01 - Glass', 7, True)
    node_sp3 = me.create_material_expression_scalar_parameter(mf_reflectance, -128 * 7 - 16, 128 * 5 + 48, 'Fresnel Power', 5.0, 8.0, 1.0, '01 - Glass', 6, True)

    # create general nodes
    output_1 = me.create_material_expression_function_output(mf_reflectance, 0, 0, 'Specular', 0)
    output_2 = me.create_material_expression_function_output(mf_reflectance, 0, 128 * 2, 'Schlick Fresnel', 1)
    node_om1 = me.create_material_expression_one_minus(mf_reflectance, -128 * 13, 128 * 2, True)
    node_om2 = me.create_material_expression_one_minus(mf_reflectance, -128 * 6, 128 * 3, True)
    node_om3 = me.create_material_expression_one_minus(mf_reflectance, -128 * 6, 128 * 4, True)
    node_a1 = me.create_material_expression_add(mf_reflectance, -128 * 13, 128 * 3, True)
    node_a2 = me.create_material_expression_add(mf_reflectance, -128 * 9, 128 * 5 + 48, True)
    node_a3 = me.create_material_expression_add(mf_reflectance, -128 * 2, 128 * 2, True)
    node_d1 = me.create_material_expression_divide(mf_reflectance, -128 * 11, 128 * 2, True)
    node_d2 = me.create_material_expression_divide(mf_reflectance, -128 * 4, 32, True)
    node_d2.set_editor_property('const_b', 0.08)
    node_m1 = me.create_material_expression_multiply(mf_reflectance, -128 * 9, 128 * 2, True)
    node_m2 = me.create_material_expression_multiply(mf_reflectance, -128 * 4, 128 * 3, True)
    node_p1 = me.create_material_expression_power(mf_reflectance, -128 * 7 - 16, 128 * 4, True)
    node_p2 = me.create_material_expression_power(mf_reflectance, -128 * 5, 128 * 4, True)
    node_vn = me.create_material_expression_vertex_normal(mf_reflectance, -128 * 13, 128 * 4 - 16, True)
    node_cv = me.create_material_expression_camera_vector(mf_reflectance, -128 * 13, 128 * 5 + 48, True)
    node_dot = me.create_material_expression_dot(mf_reflectance, -128 * 11, 128 * 4, True)
    node_abs = me.create_material_expression_abs(mf_reflectance, -128 * 9, 128 * 4, True)
    node_s = me.create_material_expression_saturate(mf_reflectance, -128 * 2, 32, True)
    node_reroute = me.create_material_expression_reroute(mf_reflectance, -128 * 6, 64, True)

    # connect nodes
    unreal.MaterialEditingLibrary.connect_material_expressions(node_sp1, '', node_om1, '')
    unreal.MaterialEditingLibrary.connect_material_expressions(node_sp1, '', node_a1, 'A')
    unreal.MaterialEditingLibrary.connect_material_expressions(node_om1, '', node_d1, 'A')
    unreal.MaterialEditingLibrary.connect_material_expressions(node_a1, '', node_d1, 'B')
    unreal.MaterialEditingLibrary.connect_material_expressions(node_d1, '', node_m1, 'A')
    unreal.MaterialEditingLibrary.connect_material_expressions(node_d1, '', node_m1, 'B')
    unreal.MaterialEditingLibrary.connect_material_expressions(node_m1, '', node_reroute, '')
    unreal.MaterialEditingLibrary.connect_material_expressions(node_m1, '', node_a3, '')
    unreal.MaterialEditingLibrary.connect_material_expressions(node_m1, '', node_om2, '')
    unreal.MaterialEditingLibrary.connect_material_expressions(node_reroute, '', node_d2, 'A')
    unreal.MaterialEditingLibrary.connect_material_expressions(node_d2, '', node_s, '')
    unreal.MaterialEditingLibrary.connect_material_expressions(node_s, '', output_1, '')
    unreal.MaterialEditingLibrary.connect_material_expressions(node_om2, '', node_m2, 'A')
    unreal.MaterialEditingLibrary.connect_material_expressions(node_m2, '', node_a3, 'B')
    unreal.MaterialEditingLibrary.connect_material_expressions(node_a3, '', output_2, '')
    unreal.MaterialEditingLibrary.connect_material_expressions(node_vn, '', node_dot, 'A')
    unreal.MaterialEditingLibrary.connect_material_expressions(node_cv, '', node_dot, 'B')
    unreal.MaterialEditingLibrary.connect_material_expressions(node_dot, '', node_abs, '')
    unreal.MaterialEditingLibrary.connect_material_expressions(node_abs, '', node_p1, 'Base')
    unreal.MaterialEditingLibrary.connect_material_expressions(node_sp2, '', node_a2, 'A')
    unreal.MaterialEditingLibrary.connect_material_expressions(node_a2, '', node_p1, 'Exp')
    unreal.MaterialEditingLibrary.connect_material_expressions(node_p1, '', node_om3, '')
    unreal.MaterialEditingLibrary.connect_material_expressions(node_om3, '', node_p2, 'Base')
    unreal.MaterialEditingLibrary.connect_material_expressions(node_sp3, '', node_p2, 'Exp')
    unreal.MaterialEditingLibrary.connect_material_expressions(node_p2, '', node_m2, 'B')

    # finish creating
    asset_path = mf_reflectance.get_path_name().split('.')[0]
    unreal.EditorAssetLibrary.save_asset(asset_path, True)

    return mf_reflectance


def create_material_opaque_master():
    m_opaque = create_material('M_Opaque_Master')

    # create parameter nodes
    node_ssp1 = me.create_material_expression_static_switch_parameter(m_opaque, -128 * 4, -128 * 2, 'Use Albedo Map', True, '01 - Albedo')
    node_ssp2 = me.create_material_expression_static_switch_parameter(m_opaque, -128 * 4, 16, 'Use Metallic Map', True, '02 - Metallic')
    node_ssp3 = me.create_material_expression_static_switch_parameter(m_opaque, -128 * 4, 128 * 2 + 32, 'Use Roughness Map', True, '03 - Roughness')
    node_ssp4 = me.create_material_expression_static_switch_parameter(m_opaque, -128 * 4, 128 * 6 + 16, 'Use Normal Map', True, '04 - Normal')
    node_vp1 = me.create_material_expression_vector_parameter(m_opaque, -128 * 8, -128 * 4 + 32, 'Albedo Tint', (1, 1, 1, 1), '01 - Albedo')
    node_vp2 = me.create_material_expression_vector_parameter(m_opaque, -128 * 8, -128 * 2 + 32, 'Base Color', (0.1, 0.1, 0.1, 1), '01 - Albedo')
    node_sp1 = me.create_material_expression_scalar_parameter(m_opaque, -128 * 13 + 16, -128 * 4 + 32, 'Saturation', 1.0, 10.0, 0.0, '01 - Albedo')
    node_sp2 = me.create_material_expression_scalar_parameter(m_opaque, -128 * 10, -128 * 4 + 32, 'Brightness', 1.0, 10.0, 0.0, '01 - Albedo')
    node_sp3 = me.create_material_expression_scalar_parameter(m_opaque, -128 * 6 - 32, -128 * 4 + 32, 'Contrast', 1.0, 10.0, 0.0, '01 - Albedo')
    node_sp4 = me.create_material_expression_scalar_parameter(m_opaque, -128 * 6 - 32, 128 * 1, 'Metallic', 0.0, 1.0, 0.0, '02 - Metallic')
    node_sp5 = me.create_material_expression_scalar_parameter(m_opaque, -128 * 8, 128 * 2 - 32, 'Min Roughness', 0.0, 1.0, 0.0, '03 - Roughness', 1)
    node_sp6 = me.create_material_expression_scalar_parameter(m_opaque, -128 * 8, 128 * 2 + 64, 'Max Roughness', 1.0, 1.0, 0.0, '03 - Roughness')
    node_sp7 = me.create_material_expression_scalar_parameter(m_opaque, -128 * 6 - 32, 128 * 4 - 32, 'Roughness', 0.5, 1.0, 0.0, '03 - Roughness')
    node_sp8 = me.create_material_expression_scalar_parameter(m_opaque, -128 * 11 + 16, 128 * 7 + 48, 'Normal Strength', 1.0, 10.0, 0.0, '04 - Normal')
    node_t2dp1 = me.create_material_expression_texture_sample_parameter_2d(m_opaque, -128 * 15, -128 * 5, 'Albedo Map', unreal.EditorAssetLibrary.load_asset('/Material_Manager/Placeholder_Albedo'), unreal.MaterialSamplerType.SAMPLERTYPE_COLOR, '01 - Albedo', 0)
    node_t2dp2 = me.create_material_expression_texture_sample_parameter_2d(m_opaque, -128 * 15, 16, 'Metallic Map', unreal.EditorAssetLibrary.load_asset('/Material_Manager/Placeholder_Black'), unreal.MaterialSamplerType.SAMPLERTYPE_LINEAR_COLOR, '02 - Metallic', 0)
    node_t2dp3 = me.create_material_expression_texture_sample_parameter_2d(m_opaque, -128 * 15, 128 * 3 + 16, 'Roughness Map', unreal.EditorAssetLibrary.load_asset('/Material_Manager/Placeholder_White'), unreal.MaterialSamplerType.SAMPLERTYPE_LINEAR_COLOR, '03 - Roughness', 0)
    node_t2dp4 = me.create_material_expression_texture_sample_parameter_2d(m_opaque, -128 * 15, 128 * 6 + 16, 'Normal Map', unreal.EditorAssetLibrary.load_asset('/Material_Manager/Placeholder_Normal'), unreal.MaterialSamplerType.SAMPLERTYPE_NORMAL, '04 - Normal', 0)

    # create general nodes
    node_ds = me.create_material_expression_desaturation(m_opaque, -128 * 10, -128 * 5 + 16)
    node_m1 = me.create_material_expression_multiply(m_opaque, -128 * 8, -128 * 5 + 16)
    node_m2 = me.create_material_expression_multiply(m_opaque, -128 * 6 - 32, -128 * 5 + 16)
    node_p = me.create_material_expression_power(m_opaque, -128 * 5 + 64, -128 * 5 + 16)
    node_om1 = me.create_material_expression_one_minus(m_opaque, -128 * 11, -128 * 5 + 48)
    node_om2 = me.create_material_expression_one_minus(m_opaque, -128 * 9, 128 * 6 + 64)
    node_l = me.create_material_expression_linear_interpolate(m_opaque, -128 * 6 - 32, 128 * 2 + 48)
    node_mask = me.create_material_expression_component_mask(m_opaque, -128 * 8 + 64, 128 * 3 + 32, True, False)
    node_fn = me.create_material_expression_flatten_normal(m_opaque, -128 * 8, 128 * 6 + 32)
    node_c3 = me.create_material_expression_constant_3_vector(m_opaque, -128 * 8, 128 * 7 + 48, (0, 0, 1, 0))

    # connect nodes
    unreal.MaterialEditingLibrary.connect_material_property(node_ssp1, '', unreal.MaterialProperty.MP_BASE_COLOR)
    unreal.MaterialEditingLibrary.connect_material_property(node_ssp2, '', unreal.MaterialProperty.MP_METALLIC)
    unreal.MaterialEditingLibrary.connect_material_property(node_ssp3, '', unreal.MaterialProperty.MP_ROUGHNESS)
    unreal.MaterialEditingLibrary.connect_material_property(node_ssp4, '', unreal.MaterialProperty.MP_NORMAL)
    unreal.MaterialEditingLibrary.connect_material_expressions(node_t2dp1, '', node_ds, '')
    unreal.MaterialEditingLibrary.connect_material_expressions(node_sp1, '', node_om1, '')
    unreal.MaterialEditingLibrary.connect_material_expressions(node_om1, '', node_ds, 'Fraction')
    unreal.MaterialEditingLibrary.connect_material_expressions(node_ds, '', node_m1, 'A')
    unreal.MaterialEditingLibrary.connect_material_expressions(node_sp2, '', node_m1, 'B')
    unreal.MaterialEditingLibrary.connect_material_expressions(node_m1, '', node_m2, 'A')
    unreal.MaterialEditingLibrary.connect_material_expressions(node_vp1, '', node_m2, 'B')
    unreal.MaterialEditingLibrary.connect_material_expressions(node_m2, '', node_p, 'Base')
    unreal.MaterialEditingLibrary.connect_material_expressions(node_sp3, '', node_p, 'Exp')
    unreal.MaterialEditingLibrary.connect_material_expressions(node_p, '', node_ssp1, 'True')
    unreal.MaterialEditingLibrary.connect_material_expressions(node_vp2, '', node_ssp1, 'False')
    unreal.MaterialEditingLibrary.connect_material_expressions(node_t2dp2, '', node_ssp2, 'True')
    unreal.MaterialEditingLibrary.connect_material_expressions(node_sp4, '', node_ssp2, 'False')
    unreal.MaterialEditingLibrary.connect_material_expressions(node_t2dp3, '', node_mask, '')
    unreal.MaterialEditingLibrary.connect_material_expressions(node_sp5, '', node_l, 'A')
    unreal.MaterialEditingLibrary.connect_material_expressions(node_sp6, '', node_l, 'B')
    unreal.MaterialEditingLibrary.connect_material_expressions(node_mask, '', node_l, 'Alpha')
    unreal.MaterialEditingLibrary.connect_material_expressions(node_l, '', node_ssp3, 'True')
    unreal.MaterialEditingLibrary.connect_material_expressions(node_sp7, '', node_ssp3, 'False')
    unreal.MaterialEditingLibrary.connect_material_expressions(node_t2dp4, '', node_fn, 'Normal')
    unreal.MaterialEditingLibrary.connect_material_expressions(node_sp8, '', node_om2, '')
    unreal.MaterialEditingLibrary.connect_material_expressions(node_om2, '', node_fn, 'Flatness')
    unreal.MaterialEditingLibrary.connect_material_expressions(node_fn, '', node_ssp4, 'True')
    unreal.MaterialEditingLibrary.connect_material_expressions(node_c3, '', node_ssp4, 'False')

    # finish creating
    unreal.MaterialEditingLibrary.recompile_material(m_opaque)
    asset_path = m_opaque.get_path_name().split('.')[0]
    unreal.EditorAssetLibrary.save_asset(asset_path, True)


def create_material_glass_master():
    m_glass = create_material('M_Glass_Master')
    mf = create_material_function_reflectance()

    # create parameter nodes
    node_vp1 = me.create_material_expression_vector_parameter(m_glass, -128 * 3, -128 * 2 + 32, 'Glass Color', (0.05, 0.05, 0.05, 1), '01 - Glass', 0)
    node_vp2 = me.create_material_expression_vector_parameter(m_glass, -128 * 3, -128 * 4, 'Transmission Color', (1, 1, 1, 1), '01 - Glass', 1)
    node_sp1 = me.create_material_expression_scalar_parameter(m_glass, -128 * 5, 128 * 1, 'Specular Adjust', 0.0, 1.0, 0.0, '01 - Glass', 8)
    node_sp2 = me.create_material_expression_scalar_parameter(m_glass, -128 * 5, 128 * 2, 'Roughness', 0.02, 1.0, 0.0, '01 - Glass', 2)
    node_sp3 = me.create_material_expression_scalar_parameter(m_glass, -128 * 5, 128 * 4 - 32, 'Opacity', 0.2, 1.0, 0.0, '01 - Glass', 3)
    node_sp4 = me.create_material_expression_scalar_parameter(m_glass, -128 * 5, 128 * 7 + 32, 'Refraction', 1.0, 1.0, -1.0, '01 - Glass', 5)

    # create general nodes
    node_l1 = me.create_material_expression_linear_interpolate(m_glass, -128 * 3, 64)
    node_l2 = me.create_material_expression_linear_interpolate(m_glass, -128 * 3, 128 * 3 + 32)
    node_m1 = me.create_material_expression_multiply(m_glass, -128 * 5, 128 * 6)
    node_m2 = me.create_material_expression_multiply(m_glass, -128 * 4, 128 * 6)
    node_c = me.create_material_expression_constant(m_glass, -128 * 5, 128 * 5, 1.0)
    node_a = me.create_material_expression_add(m_glass, -128 * 3, 128 * 5)
    node_mf1 = me.create_material_expression_material_function_call(m_glass, mf, -128 * 10, 64)
    node_mf2 = me.create_material_expression_material_function_call(m_glass, mf, -128 * 10, 128 * 6)
    node_thin = unreal.MaterialEditingLibrary.create_material_expression(m_glass, unreal.MaterialExpressionThinTranslucentMaterialOutput, 0, -128 * 4 + 16)

    # connect nodes
    unreal.MaterialEditingLibrary.connect_material_property(node_vp1, '', unreal.MaterialProperty.MP_BASE_COLOR)
    unreal.MaterialEditingLibrary.connect_material_property(node_l1, '', unreal.MaterialProperty.MP_SPECULAR)
    unreal.MaterialEditingLibrary.connect_material_property(node_sp2, '', unreal.MaterialProperty.MP_ROUGHNESS)
    unreal.MaterialEditingLibrary.connect_material_property(node_l2, '', unreal.MaterialProperty.MP_OPACITY)
    unreal.MaterialEditingLibrary.connect_material_property(node_a, '', unreal.MaterialProperty.MP_REFRACTION)
    unreal.MaterialEditingLibrary.connect_material_expressions(node_sp1, '', node_l1, 'Alpha')
    unreal.MaterialEditingLibrary.connect_material_expressions(node_sp3, '', node_l2, 'Alpha')
    unreal.MaterialEditingLibrary.connect_material_expressions(node_c, '', node_a, 'A')
    unreal.MaterialEditingLibrary.connect_material_expressions(node_m1, '', node_m2, 'A')
    unreal.MaterialEditingLibrary.connect_material_expressions(node_sp4, '', node_m2, 'B')
    unreal.MaterialEditingLibrary.connect_material_expressions(node_m2, '', node_a, 'B')
    unreal.MaterialEditingLibrary.connect_material_expressions(node_mf1, 'Specular', node_l1, 'A')
    unreal.MaterialEditingLibrary.connect_material_expressions(node_mf1, 'Schlick Fresnel', node_l2, 'A')
    unreal.MaterialEditingLibrary.connect_material_expressions(node_mf2, 'Specular', node_m1, 'A')
    unreal.MaterialEditingLibrary.connect_material_expressions(node_mf2, 'Schlick Fresnel', node_m1, 'B')
    unreal.MaterialEditingLibrary.connect_material_expressions(node_vp2, '', node_thin, '')

    # finish creating
    m_glass.set_editor_property('blend_mode', unreal.BlendMode.BLEND_TRANSLUCENT)  # change blend mode
    m_glass.set_editor_property('translucency_lighting_mode', unreal.TranslucencyLightingMode.TLM_SURFACE_PER_PIXEL_LIGHTING)  # change translucency lighting mode
    m_glass.set_editor_property('shading_model', unreal.MaterialShadingModel.MSM_THIN_TRANSLUCENT)  # change shading model
    unreal.MaterialEditingLibrary.recompile_material(m_glass)
    asset_path = m_glass.get_path_name().split('.')[0]
    unreal.EditorAssetLibrary.save_asset(asset_path, True)


def create_material_emissive_master():
    m_emissive = create_material('M_Emissive_Master')

    # create parameter nodes
    node_vp = me.create_material_expression_vector_parameter(m_emissive, -128 * 11, 128 * 1 + 32, 'Emissive Color', (1, 1, 1, 0), '01 - Emission', 0)
    node_sp1 = me.create_material_expression_scalar_parameter(m_emissive, -128 * 7, 32, 'Facing Intensity (cd/m2)', 1.0, 10.0, 0.0, '01 - Emission', 1)
    node_sp2 = me.create_material_expression_scalar_parameter(m_emissive, -128 * 7, 128 * 2 + 16, 'Edge Intensity (cd/m2)', 0.5, 10.0, 0.0, '01 - Emission')
    node_sp3 = me.create_material_expression_scalar_parameter(m_emissive, -128 * 7, 128 * 4, 'Fresnel Power', 1.0, 10.0, 0.0, '01 - Emission')

    # create general nodes
    node_m1 = me.create_material_expression_multiply(m_emissive, -128 * 5, -64)
    node_m2 = me.create_material_expression_multiply(m_emissive, -128 * 5, 128 * 1 + 48)
    node_l = me.create_material_expression_linear_interpolate(m_emissive, -128 * 2, 128 * 1 + 16)
    node_fresnel = me.create_material_expression_fresnel(m_emissive, -128 * 5, 128 * 3 + 64)
    node_reroute = me.create_material_expression_reroute(m_emissive, -128 * 7 - 48, -32)

    # connect nodes
    unreal.MaterialEditingLibrary.connect_material_property(node_l, '', unreal.MaterialProperty.MP_EMISSIVE_COLOR)
    unreal.MaterialEditingLibrary.connect_material_expressions(node_vp, '', node_reroute, '')
    unreal.MaterialEditingLibrary.connect_material_expressions(node_reroute, '', node_m1, 'A')
    unreal.MaterialEditingLibrary.connect_material_expressions(node_sp1, '', node_m1, 'B')
    unreal.MaterialEditingLibrary.connect_material_expressions(node_vp, '', node_m2, 'A')
    unreal.MaterialEditingLibrary.connect_material_expressions(node_sp2, '', node_m2, 'B')
    unreal.MaterialEditingLibrary.connect_material_expressions(node_m1, '', node_l, 'A')
    unreal.MaterialEditingLibrary.connect_material_expressions(node_m2, '', node_l, 'B')
    unreal.MaterialEditingLibrary.connect_material_expressions(node_sp3, '', node_fresnel, 'ExponentIn')
    unreal.MaterialEditingLibrary.connect_material_expressions(node_fresnel, '', node_l, 'Alpha')

    # finish creating
    m_emissive.set_editor_property('shading_model', unreal.MaterialShadingModel.MSM_UNLIT)  # change shading model
    unreal.MaterialEditingLibrary.recompile_material(m_emissive)
    asset_path = m_emissive.get_path_name().split('.')[0]
    unreal.EditorAssetLibrary.save_asset(asset_path, True)


def create_material_debug():
    m_debug = create_material('M_Debug')

    # create parameter nodes
    node_vp = me.create_material_expression_vector_parameter(m_debug, -128 * 3, -16, 'Base Color', (1, 0, 0, 0), '01 - Debug')
    node_sp1 = me.create_material_expression_scalar_parameter(m_debug, -128 * 3, 128 * 2 - 16, 'Metallic', 0.0, 1.0, 0.0, '01 - Debug')
    node_sp2 = me.create_material_expression_scalar_parameter(m_debug, -128 * 3, 128 * 3 - 16, 'Roughness', 0.5, 1.0, 0.0, '01 - Debug')

    # connect nodes
    unreal.MaterialEditingLibrary.connect_material_property(node_vp, '', unreal.MaterialProperty.MP_BASE_COLOR)
    unreal.MaterialEditingLibrary.connect_material_property(node_sp1, '', unreal.MaterialProperty.MP_METALLIC)
    unreal.MaterialEditingLibrary.connect_material_property(node_sp2, '', unreal.MaterialProperty.MP_ROUGHNESS)

    # finish creating
    unreal.MaterialEditingLibrary.recompile_material(m_debug)
    asset_path = m_debug.get_path_name().split('.')[0]
    unreal.EditorAssetLibrary.save_asset(asset_path, True)


# ------------------------------------------------------------------------


def test():
    pass










