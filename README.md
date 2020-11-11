# Collection of utils for Jira project migrations

This project is just a collection of python scripts to:

* [Copy all the components](component-bulk-copy.py) from one Jira project to another (in the same Jira instance)
* [Copy all the release versions](release-version-bulk-copy.py) from one Jira project to another (in the same Jira instance)
* [Rename release versions](release-version-bulk-rename.py) in one project.
    * Useful when you are merging projects into one. For instance: new project structure (destination) and a few other projects to be moved in (sources).
    * In cases like this one, I rename the release versions in the source with a prefix (to not crash with components defined in the destination project).
    * After renaming them, run the bulk copy to the final destination safely.
* [Dump the changelog of the issues](project-changelog-issues-dump.py) from a given Jira project
    * Useful to understand the evolution of the issues and doing lead time related calculations
> By the way, the code uses a wrapper to avoid problems with Jira servers with SSL certificates configured incorrectly (something very common in my experience).

Thanks for reading!
