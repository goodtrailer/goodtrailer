---
layout: page
title: projects
assets: /assets/projects/
---

{::options parse_block_html="true" /}

## 2024

{:.project}
<div>
![]({{page.assets}}path-tracer.png)
<div>
### physically based path tracer
Monte-Carlo path tracer that is physically based. Implements the GGX microfacet model for specular reflection and transmission based on [[Walter et al. 2007]](https://www.cs.cornell.edu/~srm/publications/EGSR07-btdf.html). Uses multiple importance sampling of the BSDF and next event estimation. Final project for CSE 168: Computer Graphics II at UCSD.
<br><br>
source unavailable (schoolwork) // [partial writeup](https://www.aldw.net/work/2024/06/11/cse168-hw5/)
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
![]({{page.assets}}paper.png)
<div>
### *paper*. online turn-based game
PvP multiplayer video game running on Unreal Engine 4. Full support for online (and local) play with up to 6 players at once. Based off of little board games I used to make in elementary school out of paper. 😄
<br><br>
[source](https://github.com/goodtrailer/Paper) // [screenshots](https://github.com/goodtrailer/paper?tab=readme-ov-file#screenshots) // [releases](https://github.com/goodtrailer/Paper/releases)
</div>
</div>
