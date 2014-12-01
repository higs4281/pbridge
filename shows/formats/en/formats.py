from __future__ import unicode_literals

# Moved [2] to [0] from the default to set the default date display format.
DATE_INPUT_FORMATS = (
    '%m/%d/%y', '%Y-%m-%d', '%m/%d/%Y',  # '10/25/06', '2006-10-25', '10/25/2006'
    # '%b %d %Y', '%b %d, %Y',  # 'Oct 25 2006', 'Oct 25, 2006'
    # '%d %b %Y', '%d %b, %Y',  # '25 Oct 2006', '25 Oct, 2006'
    # '%B %d %Y', '%B %d, %Y',  # 'October 25 2006', 'October 25, 2006'
    # '%d %B %Y', '%d %B, %Y',  # '25 October 2006', '25 October, 2006'
)