import unreal


def create_menu():
    menus = unreal.ToolMenus.get()  # find all registered menus
    main_menu = menus.find_menu('LevelEditor.MainMenu')
    user = menus.find_menu('LevelEditor.LevelEditorToolBar.User')

    # parameter is owner, section_name, name, label, tool_tip=''
    # owner's name is important when unregister
    # name is the only id, can't register two menus in one section with the same name, but can have the same label
    my_menu = main_menu.add_sub_menu('LevelEditor.MainMenu', "MySection", "MyMenu", "Level Up Toolkit", "Open the Level Up Toolkit")

    menu_entry1 = unreal.ToolMenuEntry('MaterialManager', type=unreal.MultiBlockType.MENU_ENTRY)
    menu_entry1.set_label('Material Manager')
    menu_entry1.set_string_command(unreal.ToolMenuStringCommandType.PYTHON, "", 'unreal.EditorUtilitySubsystem().spawn_and_register_tab(unreal.EditorAssetLibrary.load_asset("/Material_Manager/MaterialManager"))')

    menu_entry2 = unreal.ToolMenuEntry('ModelsLibrary', type=unreal.MultiBlockType.MENU_ENTRY)
    menu_entry2.set_label('Models Library')
    menu_entry2.set_string_command(unreal.ToolMenuStringCommandType.PYTHON, "", 'unreal.EditorUtilitySubsystem().spawn_and_register_tab(unreal.EditorAssetLibrary.load_asset("/Material_Manager/ModelsLibrary"))')

    my_menu.add_menu_entry('Sec1', menu_entry1)
    my_menu.add_menu_entry('Sec2', menu_entry2)

    tool_entry1 = unreal.ToolMenuEntry('MaterialManager', type=unreal.MultiBlockType.TOOL_BAR_BUTTON)
    tool_entry1.set_label('Material Manager')
    tool_entry1.set_tool_tip('Open the Material Manager')
    tool_entry1.set_editor_property('style_name_override', 'CalloutToolbar')
    tool_entry1.set_string_command(unreal.ToolMenuStringCommandType.PYTHON, "", 'unreal.EditorUtilitySubsystem().spawn_and_register_tab(unreal.EditorAssetLibrary.load_asset("/Material_Manager/MaterialManager"))')

    tool_entry2 = unreal.ToolMenuEntry('ModelsLibrary', type=unreal.MultiBlockType.TOOL_BAR_BUTTON)
    tool_entry2.set_label('Models Library')
    tool_entry2.set_tool_tip('Open the Models Library')
    tool_entry2.set_editor_property('style_name_override', 'CalloutToolbar')
    tool_entry2.set_string_command(unreal.ToolMenuStringCommandType.PYTHON, "", 'unreal.EditorUtilitySubsystem().spawn_and_register_tab(unreal.EditorAssetLibrary.load_asset("/Material_Manager/ModelsLibrary"))')

    user.add_menu_entry('MyTool', tool_entry1)
    user.add_menu_entry('MyTool', tool_entry2)

    menus.refresh_all_widgets()


create_menu()