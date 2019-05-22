
# Note about nicknames:
# As mentioned a couple times below, there is no reason for nicknames
# to be synced up over the network. In this application anyone can set
# anyone's local nick. The main reason for this is so users can choose
# to opt for single letter names, first names, last names, whatever.
# Just do whatever looks best on your terminal settings :).

# Although I am confident this application can be used in a way that is
# highly anonymous I offer no such disclaimer. Furthermore, anonymity
# does not imply privacy. All messages are hosted on Github. They offer
# a private repo setting to university students, but, again, I yield
# no disclaimer.


# Create a new github repo and clone it to an out of the way location.
# For example in macOS ~/Library/CLI-Messenger/ might be a good place.
# Please put the path to the repository root here.
myMessagesLog="./messages.txt"

# This will be shown in front of your messages. Only you will see this.
# Your friends will set their own custom nickname for you.
myNick="S"

# This is a dictionary containing all of your friends.
# The key is the nick for a friend, and the value is their msg log url.
# Your friends do not see what you set as their nick. They will set
# their own custom nick.
friends = {
            "T": "./messages-tester.txt"
          }

# Note about friends.
# You and all of your friends are simply dropped in one big room.
# If your friendship graph is not connected, people will simply
# not receive the messages of those who are not in their friends list.

# It is up to you to manage your network!

# If you wish to create different "groups" it would be most sensible to
# create seperate repositories and instances of this program with diff-
# erent config files. If you want to see this as a more reasonable
# feature of the program send an angry email to samy@programmer.net .

# A groups feature would likely be a breaking change, so email with
# discretion.

# This number times 100ms is the delay between refreshes. Must be > 0.
refreshRate = 20

# Happy Messenging!


# Interface Settings (Not Implemented Yet)

# Character that encases dialog boxes
blockChar = "*"



