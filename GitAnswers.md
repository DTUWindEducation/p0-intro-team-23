## Git & GitLab Basics

### 1. What is the difference between git and GitLab?  
Git is a version control system, while GitLab is a platform for hosting Git repositories.  

### 2. What is the difference between GitLab, GitHub, and BitBucket?  
GitLab is open-source and supports self-hosting, GitHub is popular for open-source projects, and BitBucket integrates well with Atlassian tools.  

### 3. Why would I ever want to use git, but not GitLab?  
You can use Git locally for version control without needing a remote repository.  

### 4. What are the steps to update the GitLab server with some changes I made on my computer?  
Run:  
```sh
git add .
git commit -m "message"
git pull origin main
git push origin main
```

### 5. What is a branch and why would I use one?
A branch is a separate version of your code used for features or bug fixes without affecting the main code. This is very useful when multiple people work on the same project

### 6. How could you visualize a branch with 3 commits, and then another branch that breaks off after the second commit and has a single commit?

### 7. Give an example of a set of git commands that would result in a merge conflict.

### 8. Is Git suitable for LaTeX documents?
Yes, since LaTeX files are plain text, making version control and collaboration easy.

### 9. Should I from now on version my Word and PowerPoint slides using git? Why/why not?
No, because they are binary files, making tracking changes difficult.

### 10. What could happen when I push my latest commit to the remote repository without pulling first?
Your push might be rejected if new changes exist on the remote, requiring a pull first.

### 11. What happens when I pull without committing my local changes first?
Git tries to merge but may require conflict resolution if local changes conflict.

### 12. What is the difference between branching and forking?
Branching is within the same repo, while forking creates a separate copy in a different account.


