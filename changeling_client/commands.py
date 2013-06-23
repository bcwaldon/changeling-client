def list_changes(service):
    for change in service.list_changes():
        print 'ID:       %s' % change.id
        print 'Name:     %s' % getattr(change, 'name', '...')
        print 'Desc:     %s' % getattr(change, 'description', '...')
        print 'Tags:     %s' % (', '.join(change.tags) or '...',)
        print 'WIP:      %s' % ('Yes' if change.wip else 'No',)
        print 'Approved: %s' % ('Yes' if change.wip else 'No',)
        print


def register(subparsers):
    subparser = subparsers.add_parser('list')
    subparser.set_defaults(func=list_changes)
