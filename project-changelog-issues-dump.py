import click
from jira import JIRA, JIRAError
from contextManagerRequests import no_ssl_verification
import json

@click.command()
@click.option('--source', prompt='Source Project', help='Origin of the data, jira project XXX')
@click.option('--target', prompt='Target File', help='File containing issues fetched')
def rename(source, target):
    with no_ssl_verification():
        # Connection to JIRA is created
        jira = JIRA('https://your.jira.server.com/jira')

        try:
            # Issues are retrieve for a given source
            issues = jira.search_issues('project='+source, expand='changelog')
            
            results = []
            for issue in issues:
                result = {'self' : issue.self}
                result['url'] = jira.client_info() + '/browse/' + issue.key
                result['key'] = issue.key
                
                changelog = [] 
                for history in issue.changelog.histories:
                    for item in history.items:
                        if hasattr(item, 'fieldId') and item.fieldId == 'status':
                            status = {'created' : history.created}
                            status['fromString'] = item.fromString
                            status['toString:'] = item.toString
                            changelog.append(status)
                result['changelog'] = changelog
                results.append(result)
                click.echo('%s dumped' % (result.get('url')))
            
            with open(target, 'w') as f:
                json.dump(results, f, ensure_ascii=False)
        
        except JIRAError as err:
            click.echo('JIRA Error ocurred: %s' % (err.text))


if __name__ == '__main__':
    rename()
