"""Sherlock Notify Module

This module defines the objects for notifying the caller about the
results of queries.
"""

from app.core.modules.sherlock.result import QueryStatus
from app.core.tasks.task import SharedContent
from app.models import SocialUserFound


class QueryNotify():
    """Query Notify Object.

    Base class that describes methods available to notify the results of
    a query.
    It is intended that other classes inherit from this base class and
    override the methods to implement specific functionality.
    """

    def __init__(self, result=None):
        """Create Query Notify Object.

        Contains information about a specific method of notifying the results
        of a query.

        Keyword Arguments:
        self                   -- This object.
        result                 -- Object of type QueryResult() containing
                                  results for this query.

        Return Value:
        Nothing.
        """

        self.result = result

        return

    def start(self, message=None):
        """Notify Start.

        Notify method for start of query.  This method will be called before
        any queries are performed.  This method will typically be
        overridden by higher level classes that will inherit from it.

        Keyword Arguments:
        self                   -- This object.
        message                -- Object that is used to give context to start
                                  of query.
                                  Default is None.

        Return Value:
        Nothing.
        """

        return

    def update(self, result):
        """Notify Update.

        Notify method for query result.  This method will typically be
        overridden by higher level classes that will inherit from it.

        Keyword Arguments:
        self                   -- This object.
        result                 -- Object of type QueryResult() containing
                                  results for this query.

        Return Value:
        Nothing.
        """

        self.result = result

        return

    def finish(self, message=None):
        """Notify Finish.

        Notify method for finish of query.  This method will be called after
        all queries have been performed.  This method will typically be
        overridden by higher level classes that will inherit from it.

        Keyword Arguments:
        self                   -- This object.
        message                -- Object that is used to give context to start
                                  of query.
                                  Default is None.

        Return Value:
        Nothing.
        """

        return

    def __str__(self):
        """Convert Object To String.

        Keyword Arguments:
        self                   -- This object.

        Return Value:
        Nicely formatted string to get information about this object.
        """
        result = str(self.result)

        return result


class QueryNotifyPrint(QueryNotify):
    """Query Notify Print Object.

    Query notify class that prints results.
    """

    def __init__(self, result=None, verbose=False, print_found_only=False,
                 color=True):
        """Create Query Notify Print Object.

        Contains information about a specific method of notifying the results
        of a query.

        Keyword Arguments:
        self                   -- This object.
        result                 -- Object of type QueryResult() containing
                                  results for this query.
        verbose                -- Boolean indicating whether to give verbose output.
        print_found_only       -- Boolean indicating whether to only print found sites.
        color                  -- Boolean indicating whether to color terminal output

        Return Value:
        Nothing.
        """

        super().__init__(result)
        self.verbose = verbose
        self.print_found_only = print_found_only
        self.color = color

        return

    def update(self, result):
        self.result = result
        print(result)
        if result.status == QueryStatus.CLAIMED:
            print(SharedContent.USER_REF,
                  self.result.site_name,
                  self.result.site_url_user)
            SocialUserFound.objects.create(
                username=SharedContent.USER_REF,
                website_name=self.result.site_name,
                website_url=self.result.site_url_user
            )
        return

    def __str__(self):
        """Convert Object To String.

        Keyword Arguments:
        self                   -- This object.

        Return Value:
        Nicely formatted string to get information about this object.
        """
        result = str(self.result)

        return result
