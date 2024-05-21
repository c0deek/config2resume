from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML

import os

def generate(config, template_path, output_path):
    env = Environment(loader=FileSystemLoader(os.path.dirname(template_path)))
    template = env.get_template(os.path.basename(template_path))
    resume_html = template.render(config);

    HTML(string=resume_html).write_pdf(output_path);
