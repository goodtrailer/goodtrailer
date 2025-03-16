---
layout: page
title: projects
assets: /assets/projects/
carousels:
  - images:
    - /assets/projects/path-tracer-0.png
    - /assets/projects/path-tracer-1.png
    - /assets/projects/path-tracer-2.png
    dimensions:
    - width: 1440.0
      height: 1080.0
    - width: 1280.0
      height: 280.0
    - width: 480.0
      height: 480.0
  - images:
    - /assets/projects/paper-0.png
    - /assets/projects/paper-1.png
    - /assets/projects/paper-2.png
    dimensions:
    - width: 960.0
      height: 720.0
    - width: 1280.0
      height: 960.0
    - width: 1040.0
      height: 780.0
---

{::options parse_block_html="true" /}

## 2024

{:.project-vertical}
<div>
{% include carousel.html max-height="300" number="1" %}
<div>
### physically based path tracer
Physically based rendering (PBR) using path tracing and Monte Carlo methods. Implements the Smith-GGX microfacet model for specular reflection and transmission based on [[Walter et al. 2007]](https://www.cs.cornell.edu/~srm/publications/EGSR07-btdf.html). Uses classical multiple importance sampling of the BSDF and next event estimation. Final project for CSE 168: Computer Graphics II at UC San Diego.
<br><br>
source unavailable (schoolwork) // [partial writeup](/work/2024/06/11/cse168-hw5/)
</div>
</div>

## 2023

{:.project}
<div>
<div>
### *rote*. flashcards study website
Full-stack web application written in HTML and TypeScript. Uses React and Joy UI for the frontend. Uses Node.js + Express.js for the backend, with Passport for authentication and PostgreSQL for storing flashcard data.
<br><br>
[source](https://github.com/goodtrailer/rote) // [website](https://rote.aldw.net)
</div>
![]({{page.assets}}rote.png)
</div>

## 2021

{:.project}
<div>
<div>
### *win-pipe*. header-only Windows IPC library
Lightweight library for facilitating Windows IPC via named pipes. Full C++ wrapping with copy and move semantics, RAII, etc. Decently low latency, roughly 50µs.
<br><br>
[source](https://github.com/goodtrailer/win-pipe) // [examples](https://github.com/goodtrailer/win-pipe?tab=readme-ov-file#examples)
</div>
</div>

{:.project}
<div>
![]({{page.assets}}daily-desktop.png)
<div>
### *daily desktop*. automatic wallpapers
Automatic wallpaper updater. Windows GUI app written in C# with extensibility in mind. Has provider modules implemented for 10+ different websites, including [pixiv's illustration rankings](https://www.pixiv.net/ranking.php), [Wikimedia Commons's Picture of the Day](https://commons.wikimedia.org/wiki/Commons:Picture_of_the_day), and [today's Calvin and Hobbes comic](https://www.gocomics.com/calvinandhobbes/).
<br><br>
[source](https://github.com/goodtrailer/daily-desktop) // [releases](https://github.com/goodtrailer/daily-desktop/releases)
</div>
</div>

## 2020

{:.project}
<div>
{% include carousel.html max-height="213" number="2" %}
<div>
### *paper*. online turn-based game
PvP multiplayer video game running on Unreal Engine 4. Full support for online (and local) play with up to 6 players at once. Based off of little board games I used to make in elementary school out of paper. 😄
<br><br>
[source](https://github.com/goodtrailer/Paper) // [screenshots](https://github.com/goodtrailer/paper?tab=readme-ov-file#screenshots) // [releases](https://github.com/goodtrailer/Paper/releases)
</div>
</div>
