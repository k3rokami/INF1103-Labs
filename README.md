# Docker Cheatsheet - INF1103

## Docker Setup & Verification

| Command | Description | Purpose |
|---------|-------------|---------|
| `docker --version` | Check Docker version installed | Verify Docker installation |
| `docker ps` | List all running containers | Check active containers |
| `docker images` | List all local images | View available images |

---

## Docker Volume Mount & Run

| Command | Description | Example |
|---------|-------------|---------|
| `docker run --rm -it -v ${PWD}:/usr/src/app -w /usr/src/app python:3.11-slim python auditor.py` | Run Python script with local directory mounted | Mount current folder to container |

**Flag Breakdown:**
- `--rm` - Automatically remove container after execution
- `-it` - Interactive terminal (allows input)
- `-v ${PWD}:/usr/src/app` - Volume mount (maps local directory to container)
- `-w /usr/src/app` - Set working directory inside container
- `python:3.11-slim` - Base image
- `python auditor.py` - Command to run

---

## Dockerfile Instructions (For Lab)

| Instruction | Description | Lab Example |
|------------|-------------|------------|
| `FROM python:3.11-slim` | Set base image | Use official Python runtime |
| `WORKDIR /app` | Set working directory | All commands run in `/app` |
| `COPY auditor.py .` | Copy local file to container | Copy Python script into image |
| `CMD ["python", "auditor.py"]` | Default execution command | Run script when container starts |

**Sample Dockerfile for Lab:**
```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY auditor.py .
CMD ["python", "auditor.py"]
```

---

## Building & Running Custom Docker Image

| Task | Command | Explanation |
|------|---------|-------------|
| Build image | `docker build -t inf1003-labs-smart-auditor .` | Compile Dockerfile into reusable image |
| Run image | `docker run --rm -it inf1003-labs-smart-auditor` | Execute container with interactive terminal |
| View built images | `docker images` | Confirm image was successfully built |

**What Each Part Means:**
- `docker build` - Read Dockerfile and compile
- `-t inf1003-labs-smart-auditor` - Tag name for your image
- `.` - Look for Dockerfile in current directory
- `-rm -it` - Remove container after exit, keep input open for interaction

---

## Git Commands for Version Control

| Command | Purpose | Example |
|---------|---------|---------|
| `git init` | Initialize local repository | Create `.git` folder |
| `git remote add origin <url>` | Link to remote repository | `git remote add origin https://github.com/<user>/<repo>.git` |
| `git add .` | Stage all changes | Prepare files for commit |
| `git commit -m "message"` | Save changes locally | `git commit -m "Add auditor.py"` |
| `git push -u origin master` | Push to remote (first time) | Upload commits to GitHub |
| `git push` | Push subsequent updates | Upload new commits |
| `git log > log.txt` | Export commit history | Save logs for submission |
| `git remote -v` | Verify remote connection | Check linked repository |

---

## Lab Workflow Summary

| Step | Command | Result |
|------|---------|--------|
| 1. Create Python script | Create `auditor.py` | Application logic ready |
| 2. Test locally | `python auditor.py` | Verify code works |
| 3. Initialize git | `git init` | Start version control |
| 4. First commit | `git add . && git commit -m "Initial auditor"` | Save starting point |
| 5. Link to GitHub | `git remote add origin <url>` | Connect to remote |
| 6. Create Dockerfile | Create `Dockerfile` (no extension) | Package application |
| 7. Build image | `docker build -t inf1003-labs-smart-auditor .` | Compile container image |
| 8. Run container | `docker run -rm -it inf1003-labs-smart-auditor` | Execute application |
| 9. Push to GitHub | `git push` | Upload to repository |
| 10. Export logs | `git log > log.txt` | Prepare submission |

---

## Dockerfile Creation Checklist

Create a file named `Dockerfile` (no extension) with:
```dockerfile
FROM python:3.11-slim                 # Base image
WORKDIR /app                          # Working directory
COPY auditor.py .                     # Copy script
CMD ["python", "auditor.py"]          # Run command
```

**Critical Notes:**
- File must be named `Dockerfile` (not `Dockerfile.txt`)
- No file extension
- Save in project root directory
- Docker reads this to build your image

---

## Expected Workflow Output

| Action | Expected Result |
|--------|-----------------|
| `docker build` output | Shows layers being built, ends with "naming to docker.io/library/..." |
| `docker images` | Shows your image in the list with tag `inf1003-labs-smart-auditor:latest` |
| `docker run` execution | Shows program accepting input and displaying results |
| `git log > log.txt` | Creates text file with all commit history |

---
