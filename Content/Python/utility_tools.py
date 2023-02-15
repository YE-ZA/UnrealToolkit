import unreal
import editor_basic as eb
import math


def test():
    actors = eb.get_selected_assets_from_outliner()
    if len(actors) > 2:
        unreal.log_warning('Measure only the distance between the first two selected objects')
    world = unreal.LevelEditorSubsystem().get_current_level()

    start = actors[0].get_actor_location()
    end = actors[1].get_actor_location()
    mid = (start + end)/2
    length = math.sqrt((start.x-end.x)**2 + (start.y-end.y)**2 + (start.z-end.z)**2)
    unreal.SystemLibrary.draw_debug_arrow(world, start, end, 500.0, unreal.LinearColor.RED, 10.0, 8.0)
    # unreal.SystemLibrary.draw_debug_sphere(world, mid, duration=10.0)
    HUD = unreal.HUD()
    HUD.draw_text('testhud', unreal.LinearColor.RED, 720, 440)
    unreal.SystemLibrary.draw_debug_string(world, mid, 'test', duration=10.0)
    unreal.SystemLibrary.draw_debug_string(world, {0,0,10}, str(start), actors[0], unreal.LinearColor.BLUE, 10.0)