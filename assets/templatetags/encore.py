import json

from django import template
from django.conf import settings
from django.template import Template

register = template.Library()


def _get_files_for_entrypoint(entrypoint, file_type):

    entrypoints_file_path = (
        str(
            settings.WEBPACK_ENCORE.get(
                "output_path", settings.BASE_DIR / "assets/static"
            )
        )
        + "/entrypoints.json"
    )

    try:
        with open(entrypoints_file_path, "r") as f:
            entrypoints = json.load(f)["entrypoints"]
            try:
                entrypoint_data = entrypoints[entrypoint]
                return entrypoint_data.get(file_type, [])
            except KeyError:
                raise Exception(f"Entrypoint `{entrypoint}` doesn't exist.")
    except FileNotFoundError:
        raise Exception(
            f"""entrypoints.json file doesn't exist at {entrypoints_file_path}.
            Did you run `yarn dev` or  `yarn dev --watch`?"
            """
        )


@register.simple_tag(takes_context=True)
def encore_entry_link_tags(context, entrypoint):
    entrypoints = _get_files_for_entrypoint(entrypoint, "css")

    # make sure the runtime.js and vendors-*.js files are already rendered
    # if not include them
    existing_entries = context.get("encore_styles", [])

    entries_to_render = []

    for entry in entrypoints:
        if entry not in existing_entries:
            entries_to_render.append(entry)
            existing_entries.append(entry)

    context['encore_styles'] = existing_entries
    context['entries'] = entries_to_render
    return Template(
        '{% for entry in entries %}'
        '<link rel="stylesheet" href="{{entry}}"/>'
        '{% endfor %}'
    ).render(context)

@register.simple_tag(takes_context=True)
def encore_entry_script_tags(context, entrypoint):
    entrypoints = _get_files_for_entrypoint(entrypoint, "js")

    # make sure the runtime.js and vendors-*.js files are already rendered
    # if not include them
    existing_entries = context.get("encore_scripts", [])

    entries_to_render = []

    for entry in entrypoints:
        if entry not in existing_entries:
            entries_to_render.append(entry)
            existing_entries.append(entry)

    context['encore_scripts'] = existing_entries
    context['entries'] = entries_to_render
    return Template(
        '{% for entry in entries %}'
        '<script defer src="{{entry}}"></script>'
        '{% endfor %}'
    ).render(context)
