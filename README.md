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
download and install from [Here](https://lilypond.org/download.html)

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

## TextX Grammar Overview

WaveScript is defined using a TextX grammar (`grammar/wavescript.tx`) that describes the structure of valid programs. The grammar gives the language its “music-shaped” syntax, where each statement combines a note, a duration, and an instruction.

### Core Structure

A WaveScript program consists of a sequence of statements:

- tempo declarations
- note-based instructions
- control flow (loops and conditionals)
- program termination

Each statement follows a consistent pattern, making the language predictable and easy to parse.

---

### Musical Statements

The fundamental building block of the language is the **note instruction**:

```wavescript
C4 q -> print "Hello"
```
This statement includes:
- a pitch (e.g., C4, E4, G4)
- a duration (e.g., q for quarter, h for half, e for eigth)
- an action (print, let, if, for, end, etc)

These statements are interpreted in two ways
- logical instructions (e.g., printing text)
- sound events (e.g., note + duration = audio)

### Tempo Declaration
Programs begin with a tempo setting:
```wavescript
tempo 120
```
This defines how durations map to real time in seconds and affect audio playback.

### Variables
Variables are introduced using a musical trigger:
```wavescript
A3 q -> let
x = 10
```
This allows WaveScript to store and reuse values such as numbers or strings.

### Control Flow
WaveScript supports basic control structures using musical syntax.

#### Loops

```wavescript
D4 q -> for
i in 1..4
C4 q -> print "Looping"
G4 h -> end
```

#### Conditionals

```wavescript
E4 q -> if
x > 5
C4 q -> print "Big"
F4 q -> else
C4 q -> print "Small"
G4 h -> end
```
These behave like regular programming logic but are triggers by note based statements.

### Program Termination
Programs end with:
```wavescript
G4 h -> end
```
This marks the end of a control structure or the entire program.

### Dual Interpretation
A key feature of the grammar is dual interpretation:
- logical meaning: executes code (prints, loops, conditions)
- sonic meaning: generates timed sound events based on notes and durations
```wavescript
C4 q -> print "Hello"
```
This prints "Hello" to the console and produces a sound event (C4, quarter note).

