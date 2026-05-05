# WaveScript 🎵

WaveScript is a small programming language built with **TextX** where code is written using music-shaped syntax. A WaveScript program can be interpreted as both:

1. a normal program with execution behavior  
2. a musical/audio score that can be converted into sound, waveform images, and sheet music  

---

## Project Goal

WaveScript connects programming, music, and visualization. A single `.wave` file can:

- execute logic such as `print`, `if`, `for`, and `let`
- generate sound events from notes and durations
- synthesize audio as a `.wav` file
- create a waveform image
- export sheet music using LilyPond

---

## Example WaveScript Program

```wavescript
tempo 120

C4 q -> print "Hello, WaveScript!"
E4 q -> print "This program creates sound events."
G4 h -> end
```

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/starremi/WaveScript.git
cd WaveScript
```
### 2. Install Python dependencies

Make sure you have Python installed, then run:
```bash
pip install -r requirements.txt
```
This will install:
- textx
- numpy
- matplotlib
- scipy

### 3. Install LilyPond for sheet music

LilyPond is needed in order to generate the sheet music PDF's from the .ly files

macOS (with homebrew)
```bash
brew install lilypond
```

Windows
download and install from [Here]((https://lilypond.org/download.html))

Linux (Ubuntu)
```bash
sudo apt update
sudo apt install lilypond
```

### 4. Verify the installation

Run:
```bash
lilypond --version
```
If version number appears than it is correctly installed

### 5. Run programs

In terminal, to run a program, type:
```bash
python main.py examples/[fileName].wave
```
Be sure that any program you want to run is in a .wave file in the examples directory of WaveScript. 

  

