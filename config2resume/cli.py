import click
from util.parser import parse_config
from util.resume_generator import generate

@click.command()
@click.option('--config', required=True, help='Path to config file')
@click.option('--template', default='templates/sample_template.yaml', help='Path to config file')
@click.option('--output', default='./resume.pdf', help='Path where resume needs to be stored')
def generate_resume(config, template, output):
    """CLI command to generate resume"""
    config_data = parse_config(config)
    generate(config, template, output)
    click.echo(f"Resume generated successfully at {output}")

if __name__ == "__main__":
    generate_resume()
