import unreal


def get_selected_assets_from_content_browser():
    EUL = unreal.EditorUtilityLibrary
    assets = EUL.get_selected_assets()  # class method
    return assets


def get_selected_asset_data_from_content_browser():
    EUL = unreal.EditorUtilityLibrary
    asset_data = EUL.get_selected_asset_data()
    # asset_data.asset_name is the actual name of the asset
    # asset_data.asset_class_path.asset_name is the type of the asset
    return asset_data


def get_selected_assets_from_outliner():
    EAS = unreal.EditorActorSubsystem()
    assets = EAS.get_selected_level_actors()
    return assets
