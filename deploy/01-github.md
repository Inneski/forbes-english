# Step 1 — Push this repo to GitHub

The code is already committed locally (`git log` shows one commit). This step gets it onto GitHub so Cloudflare Pages can deploy from it.

## Create the repo

1. Go to https://github.com/new
2. Repository name: `forbes-english` (or whatever you like)
3. Keep it **Private** unless you want the lesson content public
4. **Do not** check "Add a README" or any other init option — this repo already has commits, and GitHub will refuse to let you push if the new repo isn't empty
5. Click **Create repository**

## Push your existing code

GitHub will show you a page with commands. Since this repo already has a commit, use the **"…or push an existing repository from the command line"** section — it looks like this (GitHub will show your actual username):

```bash
git remote add origin https://github.com/YOUR_USERNAME/forbes-english.git
git branch -M main
git push -u origin main
```

Run those three lines in your terminal, inside the project folder:

```bash
cd "C:\Users\black\Documents\Teaching Materials\FORBES ENGLISH"
```

The first `git push` will ask you to authenticate — a browser window should pop up asking you to log into GitHub and authorize. Follow that through.

## Verify

Refresh the GitHub repo page in your browser — you should see all the lesson files listed.

Once this is done, tell me and we'll move to Step 2 (Cloudflare Pages).
