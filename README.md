<a id="readme-top"></a>

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![License][license-shield]][license-url]

<h3 align="center">SSH Connector</h3>

<p align="center">
    An interactive terminal launcher for connecting to hosts defined in your SSH config, with support for one-off manual targets.
    <br />
    <br />
    <a href="https://github.com/MarcyVibin/ssh_wrapper/issues">Report Bug</a>
    &middot;
    <a href="https://github.com/MarcyVibin/ssh_wrapper/issues">Request Feature</a>
</p>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#requirements">Requirements</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>

---

## About The Project

**SSH Connector** is a lightweight, interactive terminal launcher for SSH connections. Instead of memorizing hostnames or hunting through your `~/.ssh/config`, it parses your existing config and presents all defined hosts in a searchable, arrow-key-navigable menu.

Key features:

- Automatically discovers hosts from `~/.ssh/config`
- Skips wildcard host patterns (`*`, `?`, `!`)
- Supports connecting to a manual target not yet in your config
- Offers to save manual targets to your SSH config for future reuse
- Automatically retries failed connections
- Clears the screen between attempts for a clean interface

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Built With

* [![Python][Python.org]][Python-url]
* [![InquirerPy][InquirerPy-badge]][InquirerPy-url]
* OpenSSH client (system `ssh` binary)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

## Getting Started

### Requirements

- Linux / macOS / WSL / Windows
- Python 3.8+
- OpenSSH client installed and available on `PATH`
- `InquirerPy` Python package

### Installation

Install the required dependency:

```sh
pip install InquirerPy
```

Then clone the repository:

```sh
git clone https://github.com/MarcyVibin/ssh_wrapper.git
cd ssh-connector
```

---

## Usage

Run the launcher directly:

```sh
python ssh_connector.py
```

You'll be shown a list of hosts pulled from your `~/.ssh/config`, plus a **Manual host...** option at the bottom. Selecting a manual entry prompts you for a target (e.g. `user@192.168.1.10`) and optionally saves it to your SSH config under a name you choose.

If a connection fails, you'll be asked whether to retry before returning to the host selection menu.

---

## License

Distributed under the GNU General Public License v3.0 (GPL-3.0). See `LICENSE` for more information.

---

## Contact

Marc Steger - marc.steger06@gmail.com

Project Link: https://github.com/MarcyVibin/ssh_wrapper

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- Badge Links -->

[Python.org]: https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white
[Python-url]: https://www.python.org/

[InquirerPy-badge]: https://img.shields.io/badge/InquirerPy-Interactive%20CLI-blueviolet?style=for-the-badge
[InquirerPy-url]: https://github.com/kazhala/InquirerPy

[contributors-shield]: https://img.shields.io/github/contributors/MarcyVibin/ssh_wrapper.svg?style=for-the-badge
[contributors-url]: https://github.com/YourUsername/ssh-connector/graphs/contributors

[forks-shield]: https://img.shields.io/github/forks/MarcyVibin/ssh_wrapper.svg?style=for-the-badge
[forks-url]: https://github.com/MarcyVibin/ssh_wrapper/network/members

[stars-shield]: https://img.shields.io/github/stars/MarcyVibin/ssh_wrapper.svg?style=for-the-badge
[stars-url]: https://github.com/MarcyVibin/ssh_wrapper/stargazers

[issues-shield]: https://img.shields.io/github/issues/MarcyVibin/ssh_wrapper.svg?style=for-the-badge
[issues-url]: https://github.com/MarcyVibin/ssh_wrapper/issues

[license-shield]: https://img.shields.io/github/license/MarcyVibin/ssh_wrapper.svg?style=for-the-badge
[license-url]: https://github.com/MarcyVibin/ssh_wrapper/blob/main/LICENSE
