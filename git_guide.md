# Git Guide for Managing Elodin Chatbot Branches and Workflow

## 📁 Repository Setup (One-Time)

### Initialize Git

```bash
git init
```

Initializes a Git repository in your current folder.

### Set Remote Origin

```bash
git remote add origin https://github.com/yourname/yourrepo.git
```

Connects your local repo to GitHub.

### Rename Default Branch to `main`

```bash
git branch -M main
```

Recommended for compatibility with GitHub conventions.

---

## 🌱 Creating and Working with Branches

### Create and Switch to a New Branch

```bash
git checkout -b gui-mode
```

Use when building new features. Keeps your work separate from `main`.

### Switch Between Branches

```bash
git checkout main
```

Switches to the specified branch.

### Check Current Branch

```bash
git branch
```

Lists all local branches. The one with `*` is active.

---

## 📝 Editing and Tracking Changes

### Save in VS Code

- Pressing `Save` updates your **local disk**, but not Git.
- Does **not** change anything on GitHub until committed and pushed.

### Add and Commit Changes

```bash
git add elodin_langchain_chatbot.py
git commit -m "Add GUI logic"
```

Stages and snapshots the changes.

### Push to GitHub

```bash
git push
```

Uploads your commit to the current branch on GitHub.

---

## 🔁 Staying Synced

### Pull Remote Changes Safely

```bash
git pull --rebase origin main
```

- Fetches and reapplies your local commits on top.
- Prevents clutter from merge commits.

### Check Sync Status

```bash
git status
```

Tells you if you're ahead, behind, or uncommitted.

---

## 🧠 Switching Between Branches in VS Code

### What Happens When You `git checkout` a Branch

- Git swaps the working files to match that branch.
- Files in VS Code may not reflect the change immediately.

### To Ensure You See the Correct Version:

1. Close the file tab (`elodin_langchain_chatbot.py`).
2. Reopen it from the file explorer in VS Code.
3. If prompted to save unsaved changes, choose **Don't Save** to load the version from the branch.

---

## 🧪 Tips and Troubleshooting

### Undo Last Commit

```bash
git reset --hard HEAD~1
```

⚠️ Only if you know what you're doing. This erases changes.

### Check Remote URL

```bash
git remote -v
```

Confirms where your GitHub repo is linked.

### See File Differences

```bash
git diff
```

Compares your changes to the last commit.

---

## ✅ Daily Workflow Summary

1. `git pull --rebase origin <branch>` (sync with GitHub)
2. Edit files
3. `git status` (see what changed)
4. `git add <file>`
5. `git commit -m "message"`
6. `git push`
7. Switch branches with `git checkout <branch>` when needed
8. Always reopen files in VS Code after branch switches to avoid cached views

---

Keep this guide inside your project root as `GIT_GUIDE.md` for reference!

