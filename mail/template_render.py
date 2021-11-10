import os


def render_template(template, **kwargs):
    import jinja2

    path = os.path.join(os.path.dirname(__file__))
    templateLoader = jinja2.FileSystemLoader(path)
    templateEnv = jinja2.Environment(loader=templateLoader)
    templ = templateEnv.get_template(template)
    return templ.render(**kwargs)
