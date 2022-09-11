from django import template

register = template.Library()

def _to_controller_name(name):
    controller_name = name.replace('/', '--')
    return controller_name

@register.simple_tag
def stimulus_controller(name):
    return f'data-controller="{_to_controller_name(name)}"'

@register.simple_tag
def stimulus_action(controller, action, event='click'):
    return f'data-action="{event}->{_to_controller_name(controller)}#{action}"'

@register.simple_tag
def stimulus_target(controller, name):
    return f'data-{_to_controller_name(controller)}-target="{name}"'

@register.simple_tag
def stimulus_class(controller, class_name):
    return f'data-{_to_controller_name(controller)}-class={class_name}'

@register.simple_tag
def stimulus_value():
    return f'data-{_to_controller_name(controller)}-value="{}"'
