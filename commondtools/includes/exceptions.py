"""
Custom Exceptions defined here
"""


class NotImplementedYet(Exception):
    """
    Better than just inserting a comment
    """

    def __init__(self, message: str = "This feature is not implemented yet. But you can raise a ticket at: "
                                      "https://github.com/M0Rph3U56031769/commondtools"):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return self.message
