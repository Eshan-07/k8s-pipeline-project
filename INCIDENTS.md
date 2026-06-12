# Incident Log — k8s-pipeline-project

## Phase 1: Containerize the app

### Image size (multi-stage build)
- Final image: 230MB disk usage / 55MB content size
- Built with multi-stage Dockerfile (builder stage installs deps, runtime stage copies only installed packages)

### Incident 1: docker build — daemon not running
- Error: "cannot find the file specified" at docker API pipe (npipe://...)
- Cause: Docker Desktop wasn't running, so the daemon wasn't listening
- Fix: started Docker Desktop, waited for engine, verified with `docker run hello-world`
- Lesson: "installed" ≠ "running"; the daemon is a separate background service

### Incident 2: COPY failed — wrong path
- Error: "/requirements.txt": not found
- Cause: COPY pointed at root, but file was in app/ subfolder
- Fix: corrected to `COPY app/requirements.txt .`
- Lesson: COPY paths are relative to the build context root, not the Dockerfile location

### Incident 3: COPY failed — misspelled filename
- Error: "/app/requirements.txt": not found (path was correct this time)
- Cause: file was named `requirments.txt` (missing an 'e')
- Fix: renamed to `requirements.txt`
- Lesson: read the error literally; verify files on disk with `dir` before blaming the Dockerfile