# chipline
Console for ChatGPT

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
