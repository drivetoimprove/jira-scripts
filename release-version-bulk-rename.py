import click
from jira import JIRA
from contextManagerRequests import no_ssl_verification


@click.command()
@click.option('--source', prompt='Source Project', help='Origin of the data, jira project XXX')
@click.option('--prefix', prompt='Prefix', help='Prefix for the release names')
def rename(source, prefix):
    with no_ssl_verification():
        jira = JIRA('https://your.jira.server.com/jira')
        versions = jira.project_versions(source)

        for version in versions:
            new_version_name = prefix + '_' + version.name
            jira.rename_version(source, version.name, new_version_name)
            click.echo('%s version renamed to %s.' % (version.name, new_version_name))


if __name__ == '__main__':
    rename()
