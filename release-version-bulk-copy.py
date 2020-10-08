import click
from jira import JIRA
from contextManagerRequests import no_ssl_verification


@click.command()
@click.option('--source', prompt='Source Project', help='Origin of the data, jira project XXX')
@click.option('--destination', prompt='Destination Project', help='Destination for the data, jira project XXX')
def rename(source, destination):
    with no_ssl_verification():
        jira = JIRA('https://your.jira.server.com/jira')
        versions = jira.project_versions(source)

        for version in versions:
            release_date = version.releaseDate if hasattr(version, 'releaseDate') else None
            start_date = version.startDate if hasattr(version, 'startDate') else None
            description = version.description if hasattr(version, 'description') else None
            archived = version.archived if hasattr(version, 'archived') else None
            released = version.released if hasattr(version, 'released') else None
            new_version = jira.create_version(version.name, destination, description, release_date, start_date,
                                              archived, released)
            click.echo('%s - %s copied to %s - %s.' % (source, version.name, destination, new_version.name))


if __name__ == '__main__':
    rename()
