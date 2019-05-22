
# You may wish to change this script to use some network tool other
# than GIT.

# Or you can modify the current usage. This script will be used by
# the messenger whenever you send a message.
git pull
git add messages.txt
git add messages-tester.txt
git commit -m "."
git push -f
