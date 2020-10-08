import click
from jira import JIRA
from contextManagerRequests import no_ssl_verification


@click.command()
@click.option('--source', prompt='Source Project', help='Origin of the data, jira project XXX')
@click.option('--destination', prompt='Destination Project', help='Destination for the data, jira project XXX')
def rename(source, destination):
    with no_ssl_verification():
        jira = JIRA('https://your.jira.server.com/jira')
        components = jira.project_components(source)

        for component in components:
            description = component.description if hasattr(component, 'description') else None
            lead_username = component.leadUserName if hasattr(component, 'leadUserName') else None
            assignee_type = component.assigneeType if hasattr(component, 'assigneeType') else None
            is_assignee_type_valid = component.isAssigneeTypeValid if hasattr(component,
                                                                              'isAssigneeTypeValid') else False
            new_component = jira.create_component(component.name, destination, description, lead_username,
                                                  assignee_type, is_assignee_type_valid)
            click.echo('%s - %s copied to %s - %s.' % (source, component.name, destination, new_component.name))


if __name__ == '__main__':
    rename()
