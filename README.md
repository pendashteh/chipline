# chipline
Console for ChatGPT

## Using Docker
If you are using Dox, simply:
1. Clone the repo
2. Place the key inside ./key directory
3. dox build && dox run

Otherwise, you may pass OPENAI_API_KEY or OPENAI_API_KEY_PATH to `docker run`
e.g. `docker run -e OPENAI_API_KEY=s-267e2...287 IMAGE_NAME`

## Installation
1. Install python requirements (and obviousely python3!)
```bash
$ pip install -r requirements.txt
```

2. Install `rlwrap` (used to enable navigation in prompt history)
```bash
$ sudo apt-get install rlwrap # Debian, Ubuntu

# sudo dnf install rlwrap # CentOS, Fedora

$ sudo pacman -S rlwrap # Arch Linux

$ brew install rlwrap # macOS

> choco install rlwrap # Windows
```

3. Rename your API key to `openai.api_key` and place it under `key` directory:
```bash
$ cat ./key/openai.api_key
sk-I0j2C2Co...SjCz45
```

4. Make sure `console` is executable.
```bash
$ chmod +x ./console
```

## Run
### Console
```
$ cd /path/to/chipline
$ ./console
> 
```
Now you can prompt via the console.

### Direct python call
```
$ python chipline_openai.py [module] [prompt]
```
Available modules:
- chat
- grammar

**Example**:
```
$ python chipline_openai.py chat What is the oldest Empire?
```
