from plone import api


TO_DELETE = ["news", "events", "Members"]


def post_install(context):
    """Post install script"""
    # Do something at the end of the installation of this package.
    portal = context.aq_parent
    for cid in TO_DELETE:
        if cid in portal:
            api.content.delete(obj=portal[cid])
