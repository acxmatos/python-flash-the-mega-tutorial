import os
import click


def register(app):
    @app.cli.group()
    def translate():
        """Translation and localization commands."""
        pass

    @app.cli.group()
    def mailserver():
        """Development smtp mail server commands."""
        pass

    @app.cli.group()
    def elasticsearch():
        """Elastic Search on Docker."""
        pass

    @translate.command()
    @click.argument('lang')
    def init(lang):
        """Initialize a new language."""
        if os.system('pybabel extract -F babel.cfg -k _l -o messages.pot .'):
            raise RuntimeError('extract command failed')
        if os.system(
                'pybabel init -i messages.pot -d app/translations -l ' + lang):
            raise RuntimeError('init command failed')
        os.remove('messages.pot')

    @translate.command()
    def update():
        """Update all languages."""
        if os.system('pybabel extract -F babel.cfg -k _l -o messages.pot .'):
            raise RuntimeError('extract command failed')
        if os.system('pybabel update -i messages.pot -d app/translations'):
            raise RuntimeError('update command failed')
        os.remove('messages.pot')

    @translate.command()
    def compile():
        """Compile all languages."""
        if os.system('pybabel compile -d app/translations'):
            raise RuntimeError('compile command failed')

    @mailserver.command()
    def run():
        """Run development smtp mail server."""
        if os.system('python -m smtpd -n -c DebuggingServer localhost:8025'):
            raise RuntimeError('run command failed')

    @elasticsearch.command()
    def run():
        """Run Elastic Search on containers (needs local docker)."""
        if os.system('docker run -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" docker.elastic.co/elasticsearch/elasticsearch:7.8.1'):
            raise RuntimeError('run command failed')
