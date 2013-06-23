def user_confirm(prompt='Are you sure?'):
    while True:
        user_input = raw_input('%s [y/N] ' % prompt).lower()
        if user_input not in ('y', 'n'):
            print 'Unable to recognize input.'
            continue
        else:
            return user_input == 'y'


def list_changes(service, args):
    for change in service.list_changes():
        print 'ID:       %s' % change.id
        print 'Name:     %s' % getattr(change, 'name', '...')
        print 'Desc:     %s' % getattr(change, 'description', '...')
        print 'Tags:     %s' % (', '.join(change.tags) or '...',)
        print 'WIP:      %s' % ('Yes' if change.wip else 'No',)
        print 'Approved: %s' % ('Yes' if change.wip else 'No',)
        print


def delete_change(service, args):
    prompt = 'Are you sure you want to delete change %s?' % args.change_id
    if user_confirm(prompt):
        change = service.get_change(args.change_id)
        service.delete_change(change)
        print 'Deleted change change %s' % args.change_id
    else:
        print 'Ignoring request to delete change %s' % args.change_id


def register(subparsers):
    subparser = subparsers.add_parser('list')
    subparser.set_defaults(func=list_changes)

    subparser = subparsers.add_parser('delete')
    subparser.set_defaults(func=delete_change)
    subparser.add_argument('change_id')
