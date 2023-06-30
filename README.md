GIFT is a Graphical User Interface Functional Tester

Git Cheat Sheet

Configuring user information used across all local repositories

12


TLDR; No || Explanation: To communicate with the remote git repo you need to link it with a folder in your local machine (git init). After this, add the remote repo link (git remote add origin <URL>) and pull it (git pull origin master). Now, once your local folder is synchronized with the remote repo you're free to add any new files (git add <file>, git commit -m <message> and git push origin master). This would be the simplest way to do it. Remember, git stores all the information in your that local folder (in .git/ folder) which you just linked with the remote repo and its responsibility is to maintain all git metadata (credentials, git history...). Without this process in place, it would be difficult for git to track historical information about the project. I hope you understand the reason behind this.
	
	

1. Get GIT Version
	git --version
	
3. set a name that is identifiable for credit when review version history

	git config --global user.name "Vinodh Francis"

2. set an email address that will be associated with each history marker
	
	git config --global user.email "f.vinodhfranklin@gmail.com"

3. set automatic command line coloring for Git for easy reviewing

	git config --global color.ui auto

4. Configuring user information, initializing and cloning repositories, initialize an existing directory as a Git repository

	git init

5. Create Remoe Repository

   	 git remote add SpringBoot https://github.com/fvinodh1978/SpringBoot.git
   
7. Push to a Remote Repo first time

	git push --set-upstream name branch

8. retrieve an entire repository from a hosted location via URL

	git clone [url]

9. BRANCH & MERGE Isolating work in branches, changing context, and integrating changes
	
	git branch
list your branches. a * will appear next to the currently active branch
git branch [branch-name]
create a new branch at the current commit
git checkout
switch to another branch and check it out into your working directory
git merge [branch]
merge the specified branch’s history into the current one
git log
show all commits in the current branch’s history
Git is the free and open source distributed version control system that's responsible for everything GitHub
related that happens locally on your computer. This cheat sheet features the most important and commonly
used Git commands for easy reference.
INSTALLATION & GUIS
With platform specific installers for Git, GitHub also provides the
ease of staying up-to-date with the latest releases of the command
line tool while providing a graphical user interface for day-to-day
interaction, review, and repository synchronization.
GitHub for Windows
htps://windows.github.com
GitHub for Mac
htps://mac.github.com
For Linux and Solaris platforms, the latest release is available on
the official Git web site.
Git for All Platforms
htp://git-scm.com
education@github.com
education.github.com
Education
Teach and learn beter, together. GitHub is free for students and teachers. Discounts available for other educational uses.
SHARE & UPDATE
Retrieving updates from another repository and updating local repos
git remote add [alias] [url]
add a git URL as an alias
git fetch [alias]
fetch down all the branches from that Git remote
git merge [alias]/[branch]
merge a remote branch into your current branch to bring it up to date
git push [alias] [branch]
Transmit local branch commits to the remote repository branch
git pull
fetch and merge any commits from the tracking remote branch
TRACKING PATH CHANGES
Versioning file removes and path changes
git rm [file]
delete the file from project and stage the removal for commit
git mv [existing-path] [new-path]
change an existing file path and stage the move
git log --stat -M
show all commit logs with indication of any paths that moved TEMPORARY COMMITS
Temporarily store modified, tracked files in order to change branches
git stash
Save modified and staged changes
git stash list
list stack-order of stashed file changes
git stash pop
write working from top of stash stack
git stash drop
discard the changes from top of stash stack

Checkout a branch and Create if it doesnt exists
	
	git checkout -b <branch>

To push the current branch and set the remote as upstream, use

    git push --set-upstream origin <branch>


